class DataHandler:
    def __init__(self):
        self.data = None
        self.flight_index = 0
        self.flights = []
        self.max_price = None
        self.message_body = ""
        self.message = ""

    def get_data(self, data):
        self.data = data

    def sort_sutiable_flights(self, max_price):
        self.max_price = max_price
        flight = self.data[self.flight_index]
        print(flight)
        if flight['price'] < max_price:
            departure = flight['route'][0]['local_departure']
            returning = flight['route'][1]['local_departure']
            info = {'price': flight['price'],
                    'bags_price': flight['bags_price'],
                    'fly from': flight['flyFrom'],
                    'city from': flight['cityFrom'],
                    'departure date': f"{departure[8:10]}{departure[4:8]}{departure[:4]}",
                    'departure time': departure[11:16],
                    'fly to': flight['flyTo'],
                    'city to': flight['cityTo'],
                    'return date': f"{returning[8:10]}{returning[4:8]}{returning[:4]}",
                    'return time': returning[11:16],
                    'link': flight['deep_link']}
            self.flights.append(info)
            self.create_message(info)
        return self.next_flight()

    def next_flight(self):
        self.flight_index += 1
        if self.flight_index <= len(self.data) - 1:
            return self.sort_sutiable_flights(self.max_price)
        else:
            return self.flights

    def create_message(self, info):
        subject = f"Subject: Flights from {info['city from']} to {info['city to']}"
        message = f"\n\nPrice: {info['price']}\nDeparts:{info['fly from']}  {info['departure date']}  {info['departure time']}\nReturns:{info['fly to']}  {info['return date']}  {info['return time']}\n{info['link']}"
        self.message_body = self.message_body + message
        self.message = f"""{subject}
                        {self.message_body}"""
