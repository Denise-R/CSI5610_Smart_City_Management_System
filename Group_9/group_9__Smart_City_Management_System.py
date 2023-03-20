import food_Consumption_Management as food
import task_Scheduler as tasks
import resource_Allocation as resources
import transportation_Management as transportation
import resource_Booking_Management as rBooking

class SmartCity:
    # Defines the following public class variables: initialFood, instructor
    def __init__(self, initialFood):
        self._initialFood = initialFood
        self._daysTillStarvation = None

    # Contains a public get function for both of the protected class variables listed above
    def get_initialFood(self):
        return self._initialFood
    def find_daysToStarvation(self):
        self._daysTillStarvation = food.foodConsumptionManagement(self._initialFood)
        return self._daysTillStarvation

    # print function
    def __repr__(self):
        self._daysTillStarvation = food.foodConsumptionManagement(self._initialFood)
        return (f"The initial about of food available is equivalent to {self._initialFood} meals and it will be"
                f" gone in {self._daysTillStarvation} days.")

