import os

from typing import Any

import pandas as pd
import pytest


@pytest.fixture
def date() -> str:
    return '11.03.2024'


@pytest.fixture
def code():
    return "USD"


@pytest.fixture
def transaction_list() -> Any:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def usd_transaction():
    return [
        {
            'id': 939719570,
            'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572',
            'operationAmount':
                {
                    'amount': '9824.07',
                    'currency':
                        {
                            'name': 'USD',
                            'code': 'USD'
                        }
                },
            'description': 'Перевод организации',
            'from': 'Счет 75106830613657916952',
            'to': 'Счет 11776614605963066702'
        }, {
            'id': 142264268, 'state': 'EXECUTED',
            'date': '2019-04-04T23:20:05.206878',
            'operationAmount':
                {
                    'amount': '79114.93',
                    'currency':
                    {
                        'name': 'USD',
                        'code': 'USD'
                    }
                },
            'description': 'Перевод со счета на счет',
            'from': 'Счет 19708645243227258542',
            'to': 'Счет 75651667383060284188'
        }, {
            'id': 895315941,
            'state': 'EXECUTED',
            'date': '2018-08-19T04:27:37.904916',
            'operationAmount':
                {
                    'amount': '56883.54',
                    'currency': {'name': 'USD', 'code': 'USD'}
                }, 'description': 'Перевод с карты на карту',
            'from': 'Visa Classic 6831982476737658',
            'to': 'Visa Platinum 8990922113665229'
        }]


@pytest.fixture
def test_df() -> pd.DataFrame:
    """Фикстура, создающая тестовый DataFrame"""

    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"]
    }

    return pd.DataFrame(test_dict)


@pytest.fixture
def test_df_1() -> pd.DataFrame:
    """Фикстура, создающая тестовый DataFrame"""
    test_dict = {}
    return pd.DataFrame(test_dict)


@pytest.fixture
def test_df_2() -> pd.DataFrame:
    """Фикстура, создающая тестовый DataFrame"""
    test_dict = ['1, 2, 3']
    return pd.DataFrame(test_dict)


@pytest.fixture
def trans_1():
    return {"amount": 92688.46, "currency": "USD"}


@pytest.fixture
def trans_2():
    return {"amount": 92688.46, "currency": "EUR"}


@pytest.fixture
def trans_3():
    return {"amount": 0, "currency": "USD"}


@pytest.fixture
def dictionaries():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture
def dictionaries_1():
    return []


@pytest.fixture
def path():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


@pytest.fixture
def path_mistake_json():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_1.json")
    return PATH_TO_FILE