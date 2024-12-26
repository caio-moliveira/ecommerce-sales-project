import requests
import json
from datetime import datetime
from pprint import pprint


# Structure payload.
payload = {
   'source': 'amazon',
   'url': 'https://www.amazon.com.br/gp/bestsellers/books'
   
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('caiomo_csXye', 'Trakinas123_'), #Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())