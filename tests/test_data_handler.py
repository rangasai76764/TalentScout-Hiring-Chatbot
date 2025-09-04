import json
import os
from data_handler import DataHandler
import tempfile

def test_save_and_persistence(tmp_path):
    path = tmp_path / "cand.json"
    dh = DataHandler(str(path))
    assert os.path.exists(str(path))
    dh.save({"full_name": "Alice", "email": "a@b.com"})
    with open(str(path), "r") as f:
        arr = json.load(f)
    assert isinstance(arr, list)
    assert arr[0]["full_name"] == "Alice"
