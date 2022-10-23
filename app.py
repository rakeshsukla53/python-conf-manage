import json
import pathlib
import requests


with open("tenant.json", "r") as f:
    config = json.load(f)


def get_users() -> dict:
    r = requests.get(config["api"]["url"])
    return r.text


if __name__ == "__main__":
    print(get_users())


