import os
import pytest

from src.utils import financial_transactions



def test_financial_transactions_nofile():
    assert financial_transactions('nofile') == []


def test_financial_transactions_not_file(path_mistake_json):
    assert financial_transactions(path_mistake_json) == []

