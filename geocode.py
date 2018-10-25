import json
import requests


url = 'https://api.foursquare.com/v2/venues/explore'


def getGeocodeLocation(inputString):
    params = dict(
            client_id='Z4E2HRATM1ULL31TE1WT3HORJQ1EG03ECRNUGT45R1N523QX',
            client_secret='N2YOBJPIZW1RCRCCVLJKPZRRUMUH2CLWUUP3C13WQKFCOTOA',
            v='20180323',
            ll='47.0105, 28.8638',
            query=inputString,
            limit=1
        )
    response = requests.get(url=url, params=params)
    data = json.loads(response.text)
    print data
    return data
