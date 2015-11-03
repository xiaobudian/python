#!/usr/bin/env python
# encoding: utf-8

import re
import requests

baseUri = "http://apis.baidu.com/3023/weather/"
headers = {
    'apikey':'fb655c55aed101b68d2e1f3bf5534738',
}
url = baseUri + "weather?id=101010200"
response = requests.get(url, headers=headers)

times = re.findall(r'"time":([0-9]{10}),', response.text, re.S)

for t in times:
    print t

