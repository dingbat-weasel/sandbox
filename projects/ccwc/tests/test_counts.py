import pytest

from ccwc.counts import count_bytes, count_chars, count_lines, count_words


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (b"", 0),
        (b"abc", 0),
        (b"abc\n", 1),
        (b"\nabc\ndef", 2),
        (b"a\rb\n", 1),
        (b"a\r\nb\r\n", 2),
        (b"\n\n\n", 3),
    ],
)
def test_count_lines(data: bytes, expected: int) -> None:
    assert count_lines(data) == expected


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (b"", 0),
        (b"abc", 1),
        (b"abc def", 2),
        (b"abc\ndef", 2),
        (b"  abc  ", 1),
        (b"a   b", 2),
        (b"     ", 0),
        (b"\r\n\v\f", 0),
        (b" \n\t", 0),
        (b"a,b", 1),
        (b"a\xc2\xa0b", 1),
    ],
)
def test_count_words(data: bytes, expected: int) -> None:
    assert count_words(data) == expected


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (b"", 0),
        (b"abc\r\n", 5),
        ("é".encode(), 1),
        ("😀".encode(), 1),
    ],
)
def test_count_chars(data: bytes, expected: int) -> None:
    assert count_chars(data) == expected


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (b"", 0),
        (b"abc", 3),
        (b"abc\r\n", 5),
        ("é".encode(), 2),
        ("😀".encode(), 4),
    ],
)
def test_count_bytes(data: bytes, expected: int) -> None:
    assert count_bytes(data) == expected
