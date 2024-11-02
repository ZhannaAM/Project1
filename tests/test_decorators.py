import tempfile

from src.decorators import log


def test_log_ok(capsys):
    """Тестирует выполнение декорированной функции"""

    @log()
    def func(x, y):
        return x + y

    result = func(1, 2)
    assert result == 3


def test_log_ok_file_log(capsys):
    """Тестирует запись в файл после успешного выполнения"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y

    func(1, 2)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()