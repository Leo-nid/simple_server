#!/usr/bin/env python
import time, os, subprocess, sys
import requests
process = subprocess.Popen(['python3', 'server.py'])
time.sleep(0.2)
response = requests.post('http://localhost:8888/sort', data=bytes('0 4 1 5 1 5 3', 'utf-8'))
assert response.content == bytes('0 1 1 3 4 5 5\n', 'utf-8')
response = requests.post('http://localhost:8888/sort', data=bytes('tasty and dot', 'utf-8'))
assert response.status_code == 400
response = requests.get('http://localhost:8888/any_other_request')
assert response.status_code == 404
process.terminate()