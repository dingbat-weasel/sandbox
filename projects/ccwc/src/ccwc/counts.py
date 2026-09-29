def count_lines(data: bytes) -> int:
    return data.count(b"\n")


def count_words(data: bytes) -> int:
    return len(data.split())


def count_chars(data: bytes, encoding: str = "utf-8") -> int:
    return len(str(data, encoding))


def count_bytes(data: bytes) -> int:
    return len(data)
