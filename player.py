from turtle import Turtle

# Constants for player's starting position, movement distance, and finish line position
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")  # Set the color of the player
        self.shape("turtle")  # Set the shape of the player
        self.penup()  # Lift the pen to prevent drawing
        self.setheading(90)  # Set the initial heading to north (up)
        self.go_to_start()  # Move the player to the starting position

    def up(self):
        self.forward(MOVE_DISTANCE)  # Move the player forward by the defined distance

    def go_to_start(self):
        self.goto(STARTING_POSITION)  # Move the player to the starting position

    def is_at_finish_line(self):
        # Check if the player has crossed the finish line
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
