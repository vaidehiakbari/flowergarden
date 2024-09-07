import turtle
import random

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()

# Get user input
flower_type = input("Enter the type of flower you want (lily, sunflower, violet, bluebell, jasmine): ").lower()
num_flowers = int(input("Enter the number of flowers you want: "))

# Define a function to place flowers randomly
def place_flowers(flower_type, num_flowers):
  for _ in range(num_flowers):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    if flower_type == "lily":
      draw_lily(x, y, random.choice(["pink", "orange"]))
    elif flower_type == "sunflower":
      draw_sunflower(x, y, random.choice(["yellow"]))
    elif flower_type == "violet":
      draw_violet(x, y, random.choice(["purple"]))
    elif flower_type == "bluebell":
      draw_bluebell(x, y, random.choice(["blue", "lightblue"]))
    elif flower_type == "jasmine":
      draw_jasmine(x, y, random.choice(["lightpurple"]))

# Flower drawing functions
def draw_lily(x, y, color):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.color(color)
  t.begin_fill()
  def draw_petal():
      t.circle(100, 60)  # Draw a semicircle
      t.left(120)
      t.circle(100, 60)
      t.left(120)
  
    # Draw a flower with 6 petals
  for _ in range(6):
      draw_petal()
      t.right(60)  # Move to the next petal position
t.end_fill()

def draw_sunflower(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    def draw_petal():
        t.circle(100, 60)  # Draw a semicircle
        t.left(120)
        t.circle(100, 60)
        t.left(120)

      # Draw a flower with 6 petals
    for _ in range(6):
        draw_petal()
        t.right(60)  # Move to the next petal position
    t.end_fill()

def draw_violet(x, y, color):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.color(color)
  t.begin_fill()
  def draw_petal():
      t.circle(100, 60)  # Draw a semicircle
      t.left(120)
      t.circle(100, 60)
      t.left(120)

    # Draw a flower with 6 petals
  for _ in range(6):
      draw_petal()
      t.right(60)  # Move to the next petal position
  t.end_fill()

def draw_bluebell(x, y, color):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.color(color)
  t.begin_fill()
  def draw_petal():
      t.circle(100, 60)  # Draw a semicircle
      t.left(120)
      t.circle(100, 60)
      t.left(120)

    # Draw a flower with 6 petals
  for _ in range(6):
      draw_petal()
      t.right(60)  # Move to the next petal position
t.end_fill()

def draw_jasmine(x, y, color):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.color(color)
  t.begin_fill()
  def draw_petal():
      t.circle(100, 60)  # Draw a semicircle
      t.left(120)
      t.circle(100, 60)
      t.left(120)

    # Draw a flower with 6 petals
  for _ in range(6):
      draw_petal()
      t.right(60)  # Move to the next petal position
t.end_fill()

# Draw the flowers
place_flowers(flower_type, num_flowers)

turtle.done()
