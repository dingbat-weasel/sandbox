# Problem

# You are given a published Google Doc like this one that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

#     The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.

#     The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.

#     Any positions in the grid that do not have a specified character should be filled with a space character.

#     You can assume the document will always have the same format as the example document linked above.

# For example, the simplified example document linked above draws out the letter 'F':

# █▀▀▀
# █▀▀
# █

# Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

# Specifications

#     Your code must be written in Python (preferred), JavaScript, TypeScript, Java, Kotlin, C#, C++, Go, Rust, Swift or Ruby.

#     You may use external libraries.

#     You may write helper functions, but there should be one function that:

#     1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND

#     2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.
import requests
from bs4 import BeautifulSoup


def get_secret_letter(url: str) -> None:
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")
        table_elements = {}

        for row in soup.find_all("tr"):
            spans = row.find_all("span")

            if spans[0].get_text(strip=True).isdigit() == False:
                continue

            x = int(spans[0].get_text(strip=True))
            char = spans[1].get_text(strip=True)
            y = int(spans[2].get_text(strip=True))

            table_elements[(x, y)] = char

        max_x = max(x for x, y in table_elements.keys())
        max_y = max(y for x, y in table_elements.keys())

        for y in range(max_y, -1, -1):
            for x in range(max_x + 1):
                char = table_elements.get((x, y), " ")

                print(char, end="")

            print()

    except Exception as e:
        print(f"An error has occurred: {e}")


get_secret_letter(
    "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
)

get_secret_letter(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)
