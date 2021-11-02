import requests
import os
os.environ["http_proxy"] = "http://192.168.5.1:7890"
os.environ["https_proxy"] = "http://192.168.5.1:7890"

LOGIN_URL = 'http://example.python-scraping.com/user/login'
LOGIN_EMAIL = 'example@python-scraping.com'
LOGIN_PASSWORD = 'example'
data = {'email': LOGIN_EMAIL, 'password': LOGIN_PASSWORD}

response = requests.post(LOGIN_URL, data)
print(response.url)
