# cccat

A small clone of the Unix `cat` tool, built following the [Coding Challenges cat challenge](https://codingchallenges.fyi/challenges/challenge-cat/)

From the man page:
The cat utility reads files sequentially, writing them to the standard output.
The file operands are processed in command-line order.  If file is a single
dash (‘-’) or absent, cat reads from the standard input.

## Installation

The project uses uv to establish the project:

```bash
cd projects/cccat && uv sync
```

It can be run and tested with the local test.txt or test2.txt files:

```bash
uv sync
uv run ccwc tests/test.txt
```

```console
$ uv run cccat tests/test.txt
    ... example output
```

## Usage


```bash
uv run cccat [filename]
```


## Differences from cat

## Design

## Reflection
