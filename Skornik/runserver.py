"""
This script runs the Skornik application using a development server.
"""
# -*- coding: utf-8 -*-

from os import environ
from Skornik import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '127.0.0.1')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(host=HOST, port=PORT, debug=True)
