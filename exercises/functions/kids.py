# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

# For example, Jay ran like a fool! or Chantelle slid down the slide!.

# The following lists of children should be iterated, and the names sent to the appropriate functions.


running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run (name):
    print(f'{name} ran like a fool')

def swing (name):
    print(f'{name} swung on the swing')

def slide (name):
    print(f'{name} slid down the slide')

def hide (name):
    print(f'{name} hid from the kids')

for value in running_kids:
    run(value)

for value in swinging_kids:
    swing(value)

for value in sliding_kids:
    slide(value)

for value in hiding_kids:
    hide(value)
