import hashlib
from pathlib import Path

import pytest

from tools.target_inventory import SCHEMA, inventory, sha256_file


def test_sha256_file(tmp_path: Path) -> None:
    target = tmp_path / "sample.bin"
    target.write_bytes(b"abc")
    assert sha256_file(target) == hashlib.sha256(b"abc").hexdigest()


def test_inventory_single_file(tmp_path: Path) -> None:
    target = tmp_path / "pokemon-x.3ds"
    target.write_bytes(b"test-data")

    result = inventory(target, "local-test")

    assert result["schema"] == SCHEMA
    assert result["target_label"] == "local-test"
    assert result["target_kind"] == "file"
    assert result["entry_count"] == 1
    assert result["total_bytes"] == len(b"test-data")
    assert result["entries"][0]["path"] == "pokemon-x.3ds"
    assert result["entries"][0]["sha256"] == hashlib.sha256(b"test-data").hexdigest()


def test_inventory_directory_is_sorted_and_skips_key_material(tmp_path: Path) -> None:
    root = tmp_path / "extract"
    (root / "romfs").mkdir(parents=True)
    (root / "exefs").mkdir(parents=True)
    (root / "romfs" / "b.bin").write_bytes(b"b")
    (root / "exefs" / "a.bin").write_bytes(b"a")
    (root / "prod.keys").write_text("do-not-record", encoding="utf-8")

    result = inventory(root)

    assert [entry["path"] for entry in result["entries"]] == [
        "exefs/a.bin",
        "romfs/b.bin",
    ]
    assert result["entry_count"] == 2


def test_inventory_rejects_key_file(tmp_path: Path) -> None:
    target = tmp_path / "title.keys"
    target.write_text("secret", encoding="utf-8")

    with pytest.raises(ValueError, match="key material"):
        inventory(target)
