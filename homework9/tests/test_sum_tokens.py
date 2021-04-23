from homework9.task3.sum_tokens import universal_file_counter


def test_universal_file_counter_test_file_txt_6():
    assert universal_file_counter("homework9/tests/test_file", "txt") == 6


def test_universal_file_counter_test_file_txt_3():
    assert universal_file_counter("homework9/tests/test_file1", "txt", str.split) == 3