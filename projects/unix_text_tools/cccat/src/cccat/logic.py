import sys
from collections.abc import Generator
from contextlib import nullcontext


def stream_lines(file_path: str | None = None) -> Generator[bytes]:
    context = open(file_path, "rb") if file_path else nullcontext(sys.stdin.buffer)
    with context as file:
        yield from file

    # consider shutil.copyfileobj when not enumerating line numbers
