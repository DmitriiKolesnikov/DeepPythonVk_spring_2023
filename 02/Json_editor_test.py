from Json_editor import *
import json
from unittest.mock import Mock
import pytest


def test_process_json():
    mock_handler = Mock()

    test_json = create_test_json()

    process_json(test_json, ["fields"], ["name", "items", "value"], mock_handler)

    mock_handler.assert_called_once_with("value", "test_value")


def test_process_json_with_invalid_json():
    mock_handler = Mock()

    with pytest.raises(ValueError):
        process_json("invalid json", ["fields"], ["name", "items", "value"], mock_handler)

    mock_handler.assert_not_called()


def test_process_json_with_missing_fields():
    mock_handler = Mock()

    test_json = create_test_json()
    del test_json["fields"]

    process_json(json.dumps(test_json), ["fields"], ["name", "items", "value"], mock_handler)

    mock_handler.assert_not_called()


def test_process_json_with_missing_item_key():
    mock_handler = Mock()

    test_json = create_test_json()
    del test_json["fields"][0]["items"][0]["value"]

    process_json(json.dumps(test_json), ["fields"],  ["name", "items", "value"], mock_handler)
