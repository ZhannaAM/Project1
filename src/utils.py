import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

from src.external_api import convert_to_rub

load_dotenv()
api_key = os.getenv("API_KEY")


PATH_TO_PROJECT = Path(__file__).resolve().parent.parent
PATH_TO_FILE = PATH_TO_PROJECT / "data" / "operations.json"

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_PROJECT / "logs" / "utils.log", encoding="UTF-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# path = Path('C:\Users\user\PycharmProjects\Homeworkbank\data\operations.json')

def financial_transactions(path):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""
    try:
        logger.info("Открываем JSON файл")

        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            return data

    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


def transaction_amount(transactions, transaction_id):
    """Принимает транзакцию и возвращает сумму в рублях, если операция не в рублях, конвертирует"""
    logger.info("Получение суммы операции")
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                logger.info(f"Сумма операции в рублях:{rub_amount}")
                return rub_amount
            else:
                transaction_convert = dict()
                transaction_convert["amount"] = transaction["operationAmount"]["amount"]
                transaction_convert["currency"] = transaction["operationAmount"]["currency"]["code"]
                logger.info(f'Сумма операции в {transaction_convert["currency"]}:{transaction_convert["amount"]}')
                rub_amount = round(convert_to_rub(transaction_convert), 2)
                return rub_amount
    else:
        logger.error("Транзакция не найдена")
        return "Транзакция не найдена"


# if __name__ == "__main__":
#     print(financial_transactions(path))