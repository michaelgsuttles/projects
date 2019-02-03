import requests, json
from pprint import pprint
from datetime import datetime

f = open('av_api.key', 'r')
key = f.readline().strip('\n')
pprint(key)
f.close()
parameters = {'function':'TIME_SERIES_INTRADAY',
              'symbol':'MJ',
              'interval':'60min',
             'apikey': key}
category='Time Series (60min)'

# Make a get request with the parameters.
response = requests.get("https://www.alphavantage.co/query?", params=parameters)

# Print the content of the response (the data the server returned)
data = json.loads(response.text)
pprint(data)

# Wrangle the data and format it correctly
extracted=data[category]
new = newnew = {}
pprint(extracted.values())