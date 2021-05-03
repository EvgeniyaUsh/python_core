import asyncio
import json
from datetime import datetime
from typing import Dict, List

import aiohttp
from bs4 import BeautifulSoup


async def fetch_response(session: aiohttp.ClientSession, url_link: str) -> str:
    async with session.get(url_link) as response:
        return await response.text()


async def get_current_dollar(session: aiohttp.ClientSession):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    date_now = datetime.now().strftime("%d/%m/%Y")
    url_new = url + date_now
    html_text = await fetch_response(session, url_new)
    soup = BeautifulSoup(html_text, "lxml")
    dollar_value = soup.find("valute", id="R01235").find("value").text.replace(",", ".")
    return float(dollar_value)


def get_pe(soup):
    P_E = soup.find_all("div", {"class": "snapshot__data-item"})[6].text.split()[0].replace(",", "")
    return float(P_E)


def get_potential_profit(soup):
    try:
        low52week = soup.find_all(class_='snapshot__highlow')[1].find(
            class_='snapshot__data-item snapshot__data-item--small').text.split()[0].replace(',', '')
        low52week = float(low52week)
    except IndexError:
        low52week = None
    try:
        high52week = soup.find_all(class_='snapshot__highlow')[1].find(
            class_='snapshot__data-item snapshot__data-item--small snapshot__data-item--right').text.split()[0].replace(
            ',',
            '')
        high52week = float(high52week)
    except IndexError:
        high52week = None

    return (
        round((high52week / low52week - 1) * 100, 2)
        if low52week and high52week
        else None
    )


async def get_company_name_href_growth(
        url: str, session: aiohttp.ClientSession
):
    company_name_href_growth = []
    data_companies = (
        BeautifulSoup(await fetch_response(session, url), "lxml")
            .find_all("table")[1]
            .find_all("tr")[1:]
    )
    for company_values in data_companies:
        name = company_values.find_all("a")[0].text
        href = company_values.find_all("a")[0].get("href")
        growth = float(
            company_values.find_all("td")[9]
                .find_all("span")[1]
                .text.replace("%", "")
                .replace("%", "")
        )
        company_name_href_growth.append({"name": name, "href": href, "growth": growth})
    return company_name_href_growth


async def get_company_info(
        session: aiohttp.ClientSession,
        company_name_href_growth: List[Dict],
        dollar_value: float,
) -> Dict:
    company_url = (
            "https://markets.businessinsider.com" + company_name_href_growth["href"]
    )
    soup = BeautifulSoup(await fetch_response(session, company_url), "lxml")
    price_in_dollars = soup.find(class_="price-section__current-value").text.replace(
        ",", ""
    )
    company_info = {
        "name": company_name_href_growth["name"],
        "code": soup.find(class_="price-section__category").find("span").text[2:],
        "price": round(float(price_in_dollars) * dollar_value, 2),
        "p_e": get_pe(soup),
        "growth": company_name_href_growth["growth"],
        "potential profit": get_potential_profit(soup),
    }
    return company_info


def save_json(sorted_data: List[Dict], description: str, key: str):
    data_to_json = [
        {"code": company["code"], "name": company["name"], f"{key}": company[key]}
        for company in sorted_data
    ]
    json_name = "top_10_" + description + "_" + key + ".json"
    with open(json_name, "w") as file:
        json.dump(data_to_json, file, indent=4)


def top_10_most_expensive(data: List):
    sorted_data = sorted(data, key=lambda x: x["price"], reverse=True)[:10]
    save_json(sorted_data, "largest", key="price")


def top_10_lowest_p_e(data: List):
    sorted_data = sorted(
        filter(lambda d: d["p_e"], data),
        key=lambda x: x["p_e"],
        reverse=False,
    )[:10]
    save_json(sorted_data, "lowest", key="p_e")


def top_10_largest_growth(data: List):
    sorted_data = sorted(data, key=lambda x: x["growth"], reverse=True)[:10]
    save_json(sorted_data, "largest", key="growth")


def top_10_largest_potential_profit(data: List):
    sorted_data = sorted(
        filter(lambda d: d["potential profit"], data),
        key=lambda x: x["potential profit"],
        reverse=True,
    )[:10]
    save_json(sorted_data, "largest", key="potential profit")


async def main():
    pages = [
        "https://markets.businessinsider.com/index/components/s&p_500?p=" + str(value)
        for value in range(1, 11)
    ]
    async with aiohttp.ClientSession() as session:
        tasks_1 = [
            asyncio.create_task(get_company_name_href_growth(url, session))
            for url in pages
        ]
        dollar_value = (
            await asyncio.gather(*tasks_1, get_current_dollar(session))
        )[10]
        data_pages = (
                         await asyncio.gather(*tasks_1, get_current_dollar(session))
                     )[:10]
        tasks_2 = [
            asyncio.create_task(get_company_info(session, company, dollar_value))
            for data_page in data_pages
            for company in data_page
        ]
        return await asyncio.gather(*tasks_2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop().run_until_complete(main())
    top_10_most_expensive(loop)
    top_10_lowest_p_e(loop)
    top_10_largest_growth(loop)
    top_10_largest_potential_profit(loop)
