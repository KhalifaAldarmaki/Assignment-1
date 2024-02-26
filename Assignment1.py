class Passenger:
    def __init__(self, name, contactDetails):
        self.name = name
        self.contactDetails = contactDetails

    # Getter and setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and setter for contactdetails
    def get_contact_details(self):
        return self.contactDetails

    def set_contact_details(self, contactDetails):
        self.contactDetails = contactDetails

    def update_contact_details(self, new_details):
        self.set_contact_details(new_details)


class Flight:
    def __init__(self, flight_number, departure_time, arrival_time, to, From):
        self._flight_number = flight_number
        self._departure_time = departure_time
        self._arrival_time = arrival_time
        self._to = to
        self._From = From

    # Getter and setter for flight_number
    def get_flight_number(self):
        return self._flight_number

    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    # Getter and setter for departure_time
    def get_departure_time(self):
        return self._departure_time

    def set_departure_time(self, departure_time):
        self._departure_time = departure_time

    # Getter and setter for arrival_time
    def get_arrival_time(self):
        return self._arrival_time

    def set_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time

    # Getter and setter for to
    def get_to(self):
        return self._to

    def set_to(self, to):
        self._destination = to

    # Getter and setter for from
    def get_From(self):
        return self._From

    def set_from(self, From):
        self._from = From

    def update_flight_details(self, new_departure_time, new_arrival_time, new_to, new_From):
        self.set_departure_time(new_departure_time)
        self.set_arrival_time(new_arrival_time)
        self.set_destination(new_to)
        self.set_origin(new_From)


class BoardingPass:
    def __init__(self, passenger, flight, seat_number, gate_number, terminal):
        self._passenger = passenger
        self._flight = flight
        self._seat_number = seat_number
        self._gate_number = gate_number
        self.terminal = terminal

    # Getter and setter for passenger
    def get_passenger(self):
        return self._passenger

    def set_passenger(self, passenger):
        self._passenger = passenger

    # Getter and setter for flight
    def get_flight(self):
        return self._flight

    def set_flight(self, flight):
        self._flight = flight

    # Getter and setter for seat_number
    def get_seat_number(self):
        return self._seat_number

    def set_seat_number(self, seat_number):
        self._seat_number = seat_number

    # Getter and setter for gate_number
    def get_gate_number(self):
        return self._gate_number

    def set_gate_number(self, gate_number):
        self._gate_number = gate_number

    def get_terminal(self):
        return self.terminal

    def set_terminal(self, terminal):
        self.get_terminal = terminal

    def display(self):
        print("Passenger Name:", self.get_passenger().get_name())
        print("Contact Details:", self.get_passenger().get_contact_details())
        print("Flight Number: ", self.get_flight().get_flight_number())
        print("Departure Time:", self.get_flight().get_departure_time())
        print("Arrival Time:", self.get_flight().get_arrival_time())
        print("To: ", self.get_flight().get_to())
        print("From:", self.get_flight().get_From())
        print("Seat Number:", self.get_seat_number())
        print("Gate Number:", self.get_gate_number())
        print("Terminal: ", self.get_terminal())


class BoardingPassGenerator:
    def generate_boarding_pass(passenger, flight, seat_number, gate_number, terminal):
        return BoardingPass(passenger, flight, seat_number, gate_number, terminal)


class BoardingPassValidator:
    def validate_boarding_pass(boarding_pass):
        # Sample validation logic - this can be customized as per requirements
        if (boarding_pass.get_passenger().get_name() and boarding_pass.get_flight().get_flight_number()
                and boarding_pass.get_seat_number()):
            print("Boarding pass is valid.")
        else:
            print("Boarding pass is invalid.")


if __name__ == "__main__":
    # Create a passenger
    passenger1 = Passenger(name= "Khalifa Aldarmaki", contactDetails= "202208471@zu.ac.ae")

    # Create a flight
    flight1 = Flight(flight_number= "NA4321", departure_time= "2024-02-24 10:00", arrival_time= "2024-02-24 12:00", to= "New York", From= "Chicago")

    # Generate a boarding pass
    boarding_pass1 = BoardingPassGenerator.generate_boarding_pass(passenger1, flight1, seat_number= "A123", gate_number= "Gate 1", terminal= "2")

    # Display the boarding pass
    boarding_pass1.display()

