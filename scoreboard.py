from turtle import Turtle

# Constant for the font style used in the scoreboard
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the level to 1
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Lift the pen to prevent drawing
        self.goto(-280, 280)  # Set the position of the scoreboard
        self.update_scoreboard()  # Display the initial level

    def update_scoreboard(self):
        self.clear()  # Clear the previous level
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level

    def increase_level(self):
        self.level += 1  # Increment the level
        self.update_scoreboard()  # Update the displayed level

    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align="center", font=FONT)  # Display the game over message
