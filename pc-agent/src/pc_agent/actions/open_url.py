import re

SAFE_URL_PATTERN = r"^https://"

def open_safe_url(url: str)-> str:
    checker = re.compile(pattern=SAFE_URL_PATTERN)
    flag = checker.match(url)
    if not flag:
        return {
            "recieved": url,
            "flag": flag,
            "verdict": "unsafe url"
        }

    return {
            "recieved": url,
            "flag": flag,
            "verdict": "safe url"
        }