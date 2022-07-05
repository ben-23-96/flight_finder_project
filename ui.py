from tkinter import Button, Label, Canvas, PhotoImage, Entry, messagebox
from datetime import date
from dateutil.relativedelta import relativedelta


class UI:
    def __init__(self, window, flight_function):
        self.flight_function = flight_function
        self.title_label = Label(text='Flight Finder',
                                 font=('ariel', 40, 'bold'))
        self.email_label = Label(text='Email:', pady=5, anchor='e', width=15)
        self.search_from_label = Label(
            text='Search From:', anchor='e', width=15)
        self.search_to_label = Label(
            text='Search To:', pady=5, anchor='e', width=15)
        self.departure_label = Label(
            text='Departure Location:', anchor='e', width=15)
        self.destination_label = Label(
            text='Destination:', pady=5, anchor='e', width=15)
        self.max_price_label = Label(
            text='Max Flight Price', pady=5, anchor='e', width=15)
        self.email_entry = Entry(width=50)
        self.search_from_entry = Entry(width=50)
        self.search_to_entry = Entry(width=50)
        self.departure_entry = Entry(width=50)
        self.destination_entry = Entry(width=50)
        self.max_price_entry = Entry(width=50)
        self.search_button = Button(text='Search', font=(
            'ariel', 14, 'bold'), command=self.get_information)

    def load_ui(self):
        self.title_label.grid(row=0, column=0, columnspan=3)
        self.email_label.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=1, columnspan=2)
        self.search_from_label.grid(row=2, column=0)
        self.search_from_entry.grid(row=2, column=1, columnspan=2)
        self.search_to_label.grid(row=3, column=0)
        self.search_to_entry.grid(row=3, column=1, columnspan=2)
        self.departure_label.grid(row=4, column=0)
        self.departure_entry.grid(row=4, column=1, columnspan=2)
        self.destination_label.grid(row=5, column=0)
        self.destination_entry.grid(row=5, column=1, columnspan=2)
        self.max_price_label.grid(row=6, column=0)
        self.max_price_entry.grid(row=6, column=1, columnspan=2)
        self.search_button.grid(row=7, column=2)
        self.insert_dates()

    def insert_dates(self):
        today = date.today().strftime('%d/%m/%Y')
        six_months = (date.today() + relativedelta(months=+6)
                      ).strftime('%d/%m/%Y')
        self.search_from_entry.delete(0, 'end')
        self.search_from_entry.insert(0, today)
        self.search_to_entry.delete(0, 'end')
        self.search_to_entry.insert(0, six_months)

    def get_information(self):
        user_email = self.email_entry.get()
        date_from = self.search_from_entry.get()
        date_to = self.search_to_entry.get()
        departure = self.departure_entry.get()
        destination = self.destination_entry.get()
        max_price = int(self.max_price_entry.get())

        flights = self.flight_function(user_email, departure, destination,
                                       date_from, date_to, max_price)

        if len(flights) > 0:
            messagebox.showinfo(
                "Hooray", f"{len(flights)} flights found, check your email")
        else:
            messagebox.showinfo(
                "Oops", "no flights found, try raising the max price or extending the range of time")
