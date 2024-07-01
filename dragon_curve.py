import turtle

# Possible rotations
right = 'r'
left = 'l'

# Sequences
old = right
new = old

iteration = int(input('Enter iteration:'))  
length = int(input('Enter length of each segment:'))
angle = int(input('Enter the angle of rotation (normal=90): '))

cycle = 1
while cycle < iteration:
    # Turn right
    new = old + right
    
    # Reverse the sequence of previous iteration
    old = old[::-1]
    
    # For the reversed sequence swap rotations (l -> r and r -> l)
    for rotation in range(len(old)):
        if old[rotation] == right:
            new += left
        elif old[rotation] == left:
            new += right
    
    # Prepare for next iteration
    old = new
    cycle += 1

# Set turtle
turtle.ht() 
turtle.speed("fastest")  
turtle.color("blue")  
turtle.bgcolor("white")  
turtle.forward(length)

# Draw the curve
for char in range(len(new)):
    if new[char] == right:
        # Make the angle to the right side
        turtle.right(angle)  
        turtle.forward(length)
        
    elif new[char] == left:
        # Make the angle to the left side
        turtle.left(angle)
        turtle.forward(length)
