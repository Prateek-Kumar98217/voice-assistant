import re

SAFE_URL_PATTERN = r"^https://"

def open_safe_url(url: str)-> str:
    print(f"Recieved url: {url}")
    checker = re.compile(pattern=SAFE_URL_PATTERN)
    flag = checker.match(url)
    print(f"SAFE URL CHECK RESULT: {flag}")
    if not flag:
        return "Invalid URL"

    return f"Would open: {url}"