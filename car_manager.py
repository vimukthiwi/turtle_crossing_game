import random
from turtle import Turtle

# Constants for car attributes and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

    def create_car(self):
        # Random chance to create a new car
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")  # Create a new car as a square turtle
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the shape to look like a car
            new_car.penup()  # Lift the pen to prevent drawing
            new_car.color(random.choice(COLORS))  # Assign a random color to the car
            random_y = random.randint(-250, 250)  # Randomly position the car along the y-axis
            new_car.goto(300, random_y)  # Start the car at the right edge of the screen
            self.all_cars.append(new_car)  # Add the new car to the list of cars

    def move_cars(self):
        # Move each car in the list backward (to the left)
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # Increase the speed of the cars for the next level
        self.car_speed += MOVE_INCREMENT
