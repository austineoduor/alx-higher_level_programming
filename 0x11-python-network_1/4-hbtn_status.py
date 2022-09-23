#!/usr/bin/python3

"""
scriptthat fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    """
        Using the package requests
    """
    response = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
