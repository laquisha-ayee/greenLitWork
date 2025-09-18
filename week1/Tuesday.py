import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url):
    # Validate URL format
    if not doc_url.endswith("/pub"):
        raise ValueError("URL must end in /pub to access published content")

    # Fetch HTML content from published Google Doc
    response = requests.get(doc_url)
    if response.status_code != 200:
        raise Exception("Failed to retrieve document content")

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    cells = soup.find_all("td")

    # Skip header row (first 3 cells)
    cells = cells[3:]

    if len(cells) % 3 != 0:
        raise Exception("Unexpected table format: not divisible by 3")

    # Extract grid data
    grid_data = []
    max_x = max_y = 0
    for i in range(0, len(cells), 3):
        x = int(cells[i].text.strip())
        char = cells[i + 1].text.strip()
        y = int(cells[i + 2].text.strip())
        grid_data.append((x, char, y))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Initialize grid with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters in the grid
    for x, char, y in grid_data:
        grid[y][x] = char

    # Print the grid
    for row in grid:
        print("".join(row))

    # Extract secret message: read non-space characters row by row
    message = ""
    for row in grid:
        for char in row:
            if char.isupper():
                message += char
print("Secret message:", decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"))
    return message