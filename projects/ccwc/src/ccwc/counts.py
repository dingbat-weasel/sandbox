def count_lines(data: bytes) -> int:
    return data.count(b"\n")


def count_words(data: bytes) -> int:
    return len(data.split())


def count_chars(data: bytes, encoding: str = "utf-8", errors: str = "replace") -> int:
    return len(str(data, encoding, errors))


def count_bytes(data: bytes) -> int:
    return len(data)
