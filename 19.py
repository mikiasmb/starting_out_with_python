# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600     # Screen width
SCREEN_HEIGHT = 600    # Screen height
TARGET_L_LEFT_X = 100  # Target's lower-left X
TARGET_L_LEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25      # Width of the target
FORCE_FACTOR = 30      # Arbitrary force factor
PROJECTILE_SPEED = 1   # Projectile's animation speed
NORTH = 90             # Angle of north direction
SOUTH = 270            # Angle of south direction
EAST = 0               # Angle of east direction
WEST = 180             # Angle of west direction

# Set up the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_L_LEFT_X, TARGET_L_LEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = turtle.numinput("angle", "Enter the projectile's angle:")
force = turtle.numinput("force", "Enter the launch force: ", minval=1, maxval=10)

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if ((turtle.xcor() >= TARGET_L_LEFT_X) and (turtle.xcor() <= (TARGET_L_LEFT_X + TARGET_WIDTH)) and
        (turtle.ycor() >= TARGET_L_LEFT_Y) and (turtle.ycor() <= (TARGET_L_LEFT_Y + TARGET_WIDTH))):
    print('Target hit!')
else:
    print('You missed the target.')
