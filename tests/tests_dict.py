from utils import dict
import pytest


def test_get_val():
    assert dict.get_val({"window": "окно", "table": "стол"}, "table", "git") == "стол"
    assert dict.get_val({"window": "окно"}, "window") == "окно"
    assert dict.get_val({"window": "окно"}, "table", "git") == "git"
