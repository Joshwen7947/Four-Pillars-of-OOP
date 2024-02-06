class TravelTicket:
    def __init__(self, source, destination, date, price):
        self._source = source  # Encapsulated source location
        self._destination = destination  # Encapsulated destination location
        self._date = date  # Encapsulated date of travel
        self._price = price  # Encapsulated price of the ticket

    def get_source(self):
        return self._source

    def set_source(self, source):
        self._source = source

    def get_destination(self):
        return self._destination

    def set_destination(self, destination):
        self._destination = destination

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price


# Creating an instance of the TravelTicket class
ticket1 = TravelTicket("New York", "Saigon", "2024-05-15", 1100)

# Accessing encapsulated attributes using getter methods
print("Origin:", ticket1.get_source())  # Output: New York
print("Destination:", ticket1.get_destination())  # Output: London
print("Date:", ticket1.get_date())  # Output: 2024-05-15
print("Price:", ticket1.get_price())  # Output: 500

# Modifying encapsulated attributes using setter methods
ticket1.set_price(800)
ticket1.set_destination("Hong Kong")

# Accessing encapsulated attributes after modification
print("Modified Destination:", ticket1.get_destination())  # Output: Paris
print("Modified Price:", ticket1.get_price())  # Output: 550


##############################################


class TravelTicket:
    def __init__(self, source, destination, date, price):
        self.source = source
        self.destination = destination
        self.date = date
        self.price = price

    def display_ticket_info(self):
        print("Origin:", self.source)
        print("Destination:", self.destination)
        print("Date:", self.date)
        print("Price:", self.price)


class FlightTicket(TravelTicket):
    def __init__(self, source, destination, date, price, airline):
        super().__init__(source, destination, date, price)
        self.airline = airline

    def display_ticket_info(self):
        super().display_ticket_info()
        print("Airline:", self.airline)


# Creating an instance of the FlightTicket class
flight_ticket = FlightTicket("Saigon", "Frankfurt", "2024-05-15", 950, "Vietnam Airlines")

# Accessing and displaying ticket information using the inherited method
flight_ticket.display_ticket_info()

##############################################

"""Despite the function being unaware of the specific ticket type, it dynamically invokes the correct display_ticket_info() method based on the object passed to it, showcasing polymorphic behavior."""

class TravelTicket:
    def __init__(self, source, destination, date, price):
        self.source = source
        self.destination = destination
        self.date = date
        self.price = price

    def display_ticket_info(self):
        print("Origin:", self.source)
        print("Destination:", self.destination)
        print("Date:", self.date)
        print("Price:", self.price)


class FlightTicket(TravelTicket):
    def __init__(self, source, destination, date, price, airline):
        super().__init__(source, destination, date, price)
        self.airline = airline

    def display_ticket_info(self):
        print("Flight Ticket Information:")
        super().display_ticket_info()
        print("Airline:", self.airline)


class TrainTicket(TravelTicket):
    def __init__(self, source, destination, date, price, train_name):
        super().__init__(source, destination, date, price)
        self.train_name = train_name

    def display_ticket_info(self):
        print("Train Ticket Information:")
        super().display_ticket_info()
        print("Train Name:", self.train_name)


# Function to display ticket information dynamically
def display_ticket_information(ticket):
    ticket.display_ticket_info()


# Creating instances of different ticket types
flight_ticket = FlightTicket("Seoul", "Athens", "2024-05-15", 700, "Korean Air")
train_ticket = TrainTicket("Paris", "Rome", "2024-06-20", 300, "Eurostar")

# Displaying ticket information dynamically using polymorphism
display_ticket_information(flight_ticket)
print()
display_ticket_information(train_ticket)

#################################################

"""By using abstraction, we define a common interface for all travel tickets through the abstract method display_ticket_info(), ensuring that subclasses provide their implementation for displaying ticket information."""


from abc import ABC, abstractmethod

class TravelTicket(ABC):
    def __init__(self, source, destination, date, price):
        self.source = source
        self.destination = destination
        self.date = date
        self.price = price

    @abstractmethod
    def display_ticket_info(self):
        pass

class FlightTicket(TravelTicket):
    def __init__(self, source, destination, date, price, airline):
        super().__init__(source, destination, date, price)
        self.airline = airline

    def display_ticket_info(self):
        print("Flight Ticket Information:")
        print("Origin:", self.source)
        print("Destination:", self.destination)
        print("Date:", self.date)
        print("Price:", self.price)
        print("Airline:", self.airline)

class TrainTicket(TravelTicket):
    def __init__(self, source, destination, date, price, train_name):
        super().__init__(source, destination, date, price)
        self.train_name = train_name

    def display_ticket_info(self):
        print("Train Ticket Information:")
        print("Origin:", self.source)
        print("Destination:", self.destination)
        print("Date:", self.date)
        print("Price:", self.price)
        print("Train Name:", self.train_name)

# Create instances of different ticket types
flight_ticket = FlightTicket("Madrid", "Amman", "2024-05-15", 500, "Iberia Airlines")
train_ticket = TrainTicket("Cairo", "Beijing", "2024-06-20", 300, "Air China")

# Display ticket information using abstraction
flight_ticket.display_ticket_info()
print()
train_ticket.display_ticket_info()

