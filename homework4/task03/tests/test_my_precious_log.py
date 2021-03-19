from homework4.task03.my_logger.my_precious_log import my_precious_logger


# # tests for my_logger/my_precious_log for funk my_precious_logger()
def test_logger_that_write_a_string_to_stderr(capsys):
    my_precious_logger("error: file not found")
    out, err = capsys.readouterr()
    assert err == "error: file not found\n"


def test_logger_that_write_a_string_to_stdout(capsys):
    my_precious_logger("OK")
    out, err = capsys.readouterr()
    assert out == "OK\n"
