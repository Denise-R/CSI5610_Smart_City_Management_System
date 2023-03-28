import foodWindow as food
from tkinter import *

root = Tk()
root.title("Smart City Management System")
# root.configure(background='#123456')

task = Button(root, text="Task Scheduler", padx=29, pady=20)
resource = Button(root, text="Resource Allocation", padx=20, pady=20)
transport = Button(root, text="Transportation", padx=34, pady=20)
booking = Button(root, text="Resource Booking", padx=21, pady=20)
food = Button(root, text="Food Consumption", padx=20, pady=20, command=food.openFood)
emergency = Button(root, text="Emergency Services", padx=21, pady=20)

task.grid(row=0, column=0, padx=5, pady=5)
resource.grid(row=0, column=1, padx=5, pady=5)
transport.grid(row=0, column=2, padx=5, pady=5)
booking.grid(row=1, column=0, padx=5, pady=5)
food.grid(row=1, column=1, padx=5, pady=5)
emergency.grid(row=1, column=2, padx=5, pady=5)


root.mainloop()
