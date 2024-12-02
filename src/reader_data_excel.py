from pathlib import Path

import pandas as pd

PATH_TO_PROJECT = Path(__file__).resolve().parent.parent
PATH_TO_EXCEL = PATH_TO_PROJECT / "data" / "transactions_excel.xlsx"
path_xlsx = PATH_TO_EXCEL


def reader_file_transaction_excel(path):
    """Принимает путь до EXCEL-файла и возвращает список словарей с данными о финансовых транзакциях"""
    transaction_xlsx_list = []
    try:
        transactions_xlsx = pd.read_excel(path)
        len_, b = transactions_xlsx.shape
        for i in range(len_):
            if transactions_xlsx["id"][i]:
                transaction_xlsx_list.append(
                    {
                        "id": str(transactions_xlsx["id"][i]),
                        "state": transactions_xlsx["state"][i],
                        "date": transactions_xlsx["date"][i],
                        "operationAmount": {
                            "amount": str(transactions_xlsx["amount"][i]),
                            "currency": {
                                "name": transactions_xlsx["currency_name"][i],
                                "code": transactions_xlsx["currency_code"][i],
                            },
                        },
                        "description": transactions_xlsx["description"][i],
                        "from": transactions_xlsx["from"][i],
                        "to": transactions_xlsx["to"][i],
                    }
                )
    except Exception:
        return []
    return transaction_xlsx_list


#if __name__ == "__main__":
     #print(reader_file_transaction_excel(path_xlsx))