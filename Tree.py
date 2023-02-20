import random
import time


# Define tree size 
tree_size = 12

# Define a list of colors for the tree
colors = ['\033[92m', '\033[91m', '\033[93m']

# Draw the star at top of the tree
star = '\033[93m' + '***'
print(' '*(tree_size-1) + star)
print ('')

# Draw the tree
for i in range(tree_size):
    stars = ''
    for j in range(2*i + 1):
        color = random.choice(colors)
        stars += color + '*'
    print(' '*(tree_size - i - 1) + stars)

# Draw the tree stand
stem = 3
for i in range(stem):
    stem = color + '\033[92m'
    print(((' ' * 9) + stem)+ (('#' * 3)+ stem) + ((''* 4) + stem))


# Wait for a moment before showing the message
time.sleep(2)

# Display the message
print('\033[91m\033[1m\nMerry Christmas!\n\033[0m')