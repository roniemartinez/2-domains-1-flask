#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from flask import Flask

FIRST_DOMAIN = 'www.first.local'
SECOND_DOMAIN = 'www.second.local'

application = Flask(__name__, host_matching=True, static_host=FIRST_DOMAIN)


@application.route('/', host=FIRST_DOMAIN)
def first_index():
    return f"Hello from {FIRST_DOMAIN}!"


@application.route('/', host=SECOND_DOMAIN)
def second_index():
    return f"Hello from {SECOND_DOMAIN}!"


if __name__ == '__main__':
    r"""
    Add these to hosts (C:\Windows\System32\drivers\etc\hosts) file:
    127.0.0.1       www.first.local
    127.0.0.1       www.second.local
    """
    application.run(host=FIRST_DOMAIN, port=80, debug=True, threaded=True)
