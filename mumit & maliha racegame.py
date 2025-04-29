from turtle import *
import random

# Screen setup
screen = Screen()
screen.bgcolor("lightblue")
screen.title("Mumit Vs Maliha Race")

# Register image shapes
screen.register_shape("maliha_turtle.gif")
screen.register_shape("mumit_turtle.gif")

# Create turtles
Maliha = Turtle()
Mumit = Turtle()

# Set image shapes
Maliha.shape("maliha_turtle.gif")
Mumit.shape("mumit_turtle.gif")

# Move Maliha & Mumit to start line
Maliha.penup()
Mumit.penup()
Maliha.goto(-200, 100)
Mumit.goto(-200, -100)

# Race track
finish_line = 200

# Start race
while Maliha.xcor() < finish_line and Mumit.xcor() < finish_line:
    Maliha.forward(random.randint(1, 10))
    Mumit.forward(random.randint(1, 10))

# Declare winner and display on screen
winner = ""
if Maliha.xcor() > Mumit.xcor():
    winner = "Maliha Wins!"
else:
    winner = "Mumit Wins!"

# Display winner
pen = Turtle()
pen.hideturtle()  # Hide the turtle
pen.penup()
pen.goto(0, 0)  # Place at center
pen.color("black")
pen.write(winner, align="center", font=("Arial", 24, "bold"))

screen.mainloop()