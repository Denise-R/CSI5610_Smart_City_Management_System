# Imports the Course and SECS classes
import group_9__Smart_City_Management_System as group9

# Creating SmartCity objects
city1 = group9.SmartCity(10)
city2 = group9.SmartCity(100)

# Calls the get functions
print(city1.get_initialFood())
print(city2.find_daysToStarvation())


# Call the get_description function twice using each of the class objects you created
print(city1)
print(city2)

