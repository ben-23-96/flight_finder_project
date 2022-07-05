from requests import get


class FlightSearch:
    def __init__(self):
        self.API_KEY = 'JZMGFnnggdy5A1IPNsjRG2r4Q4F6FWK0'
        self.headers = {'apikey': self.API_KEY}
        self.search_endpoint = 'https://tequila-api.kiwi.com/v2/search?'
        self.location_endpoint = 'http://tequila-api.kiwi.com/locations/query?'

    def get_city_code(self, city):
        params = {'term': city}
        response = get(self.location_endpoint,
                       params=params, headers=self.headers)
        data = response.json()

        city_code = data['locations'][0]['code']
        # print(response.text)
        return city_code

    def search_flights(self, search_from, search_to, departure_location, destination):

        params = {'fly_from': departure_location,
                  'fly_to': destination,
                  'date_from': search_from,
                  'date_to': search_to,
                  'fly_days': 5,
                  'return_fly_days': 0,
                  'dtime_from': '12:00',
                  'dtime_to': '18:00',
                  'nights_in_dst_from': 2,
                  'nights_in_dst_to': 2,
                  'curr': 'GBP',
                  'max_stopovers': 0}
        response = get(self.search_endpoint,
                       headers=self.headers, params=params)
        # print(response.text)
        data = response.json()['data']

        return data
