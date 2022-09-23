#!/usr/bin/python3

"""
    Python script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
"""
if __name__ == "__main__":

import urllib.request
import sys

    """
        Displaying the body response
    """
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print(html.decode(encoding="utf-8"))
