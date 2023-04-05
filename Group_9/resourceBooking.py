import sys
from PyQt5 import QtWidgets, uic
from datetime import datetime

"""
We first define the Resource class that has a name, capacity, and a 
dictionary of bookings. The add_booking method checks if the resource 
is available at the specified time and adds the booking to the 
dictionary if it is available. The check_availability method checks 
if the resource is available at the specified time.

Next, we define the Booking class that has an id, start time, end time, 
and resource.

This code uses QT Designer to create a simple UI with two list widgets 
(list_resources and list_bookings), two line edit widgets (txt_start_time 
and txt_end_time), and a push button widget (btn_book_resource).

The MainWindow class initializes the UI by loading the resource_booking.ui 
file, creating a list of resources, and populating the resource list widget 
with the available resources. When the user clicks on the btn_book_resource 
button, the book_resource method is called, which extracts the selected 
resource, start time, and end time from the UI and checks if the resource 
is available during that time. If the resource is available, a new booking 
is created
"""

MAX_CAPACITY = 100

class Resource:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.bookings = {}

    def add_booking(self, booking):
        if self.check_availability(booking.start_time, booking.end_time):
            self.bookings[booking.id] = booking
            return True
        else:
            return False

    def check_availability(self, start_time, end_time):
        for booking in self.bookings.values():
            if (booking.start_time < end_time) and (start_time < booking.end_time):
                return False
        return True

class Booking:
    def __init__(self, id, start_time, end_time, resource):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.resource = resource

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('resource_booking.ui', self)
        self.resources = [Resource("Public Bus", MAX_CAPACITY),
                          Resource("Vehicles", MAX_CAPACITY),
                          Resource("Conference Rooms", MAX_CAPACITY),
                          Resource("Books in Library", MAX_CAPACITY)]
        self.bookings = []
        self.populate_resource_list()
        self.btn_book_resource.clicked.connect(self.book_resource)

    def populate_resource_list(self):
        for resource in self.resources:
            self.list_resources.addItem(resource.name)

    def book_resource(self):
        resource = self.resources[self.list_resources.currentRow()]
        start_time = datetime.strptime(self.txt_start_time.text(), '%Y-%m-%d %H:%M')
        end_time = datetime.strptime(self.txt_end_time.text(), '%Y-%m-%d %H:%M')
        if resource.check_availability(start_time, end_time):
            booking_id = len(self.bookings) + 1
            booking = Booking(booking_id, start_time, end_time, resource)
            if resource.add_booking(booking):
                self.bookings.append(booking)
                self.populate_bookings_list()
                QtWidgets.QMessageBox.information(self, 'Booking', f'{booking.resource.name} booked successfully')
            else:
                QtWidgets.QMessageBox.warning(self, 'Booking', f'{booking.resource.name} is already booked at this time')
        else:
            QtWidgets.QMessageBox.warning(self, 'Booking', f'{booking.resource.name} is not available at this time')

    def populate_bookings_list(self):
        self.list_bookings.clear()
        for booking in self.bookings:
            self.list_bookings.addItem(f'Booking {booking.id}: {booking.resource.name} from {booking.start_time} to {booking.end_time}')

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
