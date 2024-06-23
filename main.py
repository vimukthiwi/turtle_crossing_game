import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Create the player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up key listener for player movement
screen.listen()
screen.onkey(player.up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Pause the loop for a short time
    screen.update()  # Update the screen

    car_manager.create_car()  # Create a new car at random intervals
    car_manager.move_cars()  # Move all cars forward

    # Check for collision with any car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If the car is too close to the player
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display game over message

    # Check if the player has reached the finish line
    if player.is_at_finish_line():
        player.go_to_start()  # Reset player position
        car_manager.level_up()  # Increase car speed
        scoreboard.increase_level()  # Update the level on the scoreboard

# Exit the game when the screen is clicked
screen.exitonclick()
