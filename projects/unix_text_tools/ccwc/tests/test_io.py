import io
import sys
from pathlib import Path

import pytest

from ccwc.cli import main

TEST_FILE = Path(__file__).parent / "test.txt"


def test_matches_wc_on_sample(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([str(TEST_FILE)]) == 0
    assert capsys.readouterr().out == f"    7145   58164  342190 {TEST_FILE}\n"


def test_stdin_has_no_name(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "stdin", io.TextIOWrapper(io.BytesIO(b"hi\n")))

    assert main([]) == 0
    assert capsys.readouterr().out == "       1       1       3\n"
