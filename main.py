from flight_searcher import FlightSearch
from flight_data import DataHandler
from email_sender import EmailSender
from ui import UI
from tkinter import Tk


def find_sutiable_flights(email, departure, destination, date_from, date_to, max_price):
    flight_search = FlightSearch()
    data_handler = DataHandler()
    email_sender = EmailSender()

    departure_iata = flight_search.get_city_code(departure)
    destination_iata = flight_search.get_city_code(destination)

    data = flight_search.search_flights(
        date_from, date_to, departure_iata, destination_iata)
    data_handler.get_data(data)

    flights = data_handler.sort_sutiable_flights(max_price)

    if len(flights) > 0:
        email_sender.send_email(
            email_message=data_handler.message, recipient=email)

    return flights


window = Tk()
window.title('Flight Finder')
window.config(padx=20, pady=20)

ui = UI(window, find_sutiable_flights)

ui.load_ui()

window.mainloop()
