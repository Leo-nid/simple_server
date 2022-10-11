#!/usr/bin/env python
import time, os, subprocess, sys
import requests
process = subprocess.Popen(['python3', 'server.py'], stdout=sys.stdout, stderr=sys.stderr)
response = requests.post('http://localhost:8888/sort', bytes('0 4 1 5 1 5 3', 'utf-8'))
assert response.content == bytes('0 1 1 3 4 5 5', 'utf-8')
process.terminate()