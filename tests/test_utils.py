import os

import pytest

from src.utils import financial_transactions



@pytest.fixture
def path():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


@pytest.fixture
def path_mistake_json():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_1.json")
    return PATH_TO_FILE


def test_financial_transactions_nofile():
    assert financial_transactions('nofile') == []


def test_financial_transactions_not_file():
    assert financial_transactions("data/test.json") == []

