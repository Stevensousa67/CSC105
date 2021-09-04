# Steven Sousa - 11/3/2020
from tkinter import *
import random


def yes_click():
    """This function will execute the next widgets after user clicks 'Yes!'."""
    excellent = Label(window, text="Excellent! Choose a distance between -4 and 4.")
    # excellent will appear after user clicks Yes! button and tell user to choose a value
    excellent.pack()
    dis = Entry(window)     # Entry box for user to type the distance
    dis.pack()
    dis.insert(0, "Type distance here.")
    click = Button(window, text="Lets get that value!", command=start_algorithm)
    # click is a button that I intended to send the value entered by the user to the start_algorithm function
    # I tried using dis.get() and dis.getint(), but none of those work. I couldn't figure out how to make
    # my program actually get the value entered and use it.
    click.pack()


def start_algorithm() :
    """This function will execute after user clicks "Lets get that value!" button."""
    global cycle_counter    # i intended to ready this variable so that I could send it to my simulation function
    got_it = Label(window, text="Got it! Lets see how many cycles Robot will take for...")
    # got_it label will appear after user types a value and clicks "Lets get that value!" button
    got_it.pack()
    calculating = Label(window, text="Simulating the challenge... just a sec...")
    # calculating label is a follow up from got_it just to make program look interactive
    calculating.pack()
    # Professor, I wanted to call the simulation function, but i can't send any parameters to it.
    # Im at a complete loss, so I'm going to try to explain my thinking in english beyond this points.
    # everything that I tried always gives me a NameError saying that simulation doesn't exit. I quadruple
    # checked and there weren't any typos. I found Tkinter very difficult to grasp, especially because I
    # can't even draw stickmen...


# Create application window
window = Tk()
window.title("Robot GUI Simulator")     # Name my window
window.geometry("1000x800")             # Set a height x width setting for the window

# Create intro texts inside window
greeting = Label(window, text="Welcome to the Robot Simulator!").pack()  # Create greeting line

intro1 = Label(window, text="Robot only move 5 steps per cycle. After 5 steps, he falls and starts over."
                            " Each steps is 1m in length.")  # Create line that explains how Robot works

intro2 = Label(window, text="The challenge: See how many cycles it takes for Robot to walk a net forward distance.")
# intro2 explains the challenge to user

intro3 = Label(window, text="Ready?")   # Ask user if they're ready.
intro1.pack(), intro2.pack(), intro3.pack()

# Create a ready button when user is ready
yes_button = Button(window, text="Yes!", bg="lightblue", command=yes_click).pack()  # If yes, call yes_click()
no_button = Button(window, text="No!", bg="lightblue", command=window.quit).pack()  # If no, quit UI

window.mainloop()

# Algorithm --------------------------------------------------------------
# This algorithm works perfectly fine without using UI. I tested it to make sure.
# My issue, other than not being cut out for front end development, starts when
# I try to implement this function into my UI. I just couldn't get my UI to call it.

cycle_counter = 0   # Robot cycle counter


def simulation(x, y):
    """This function will perform the cycle of the Robot."""
    global dis, cycle_counter   # my intention was to user the dis that user chooses
    fwd_direction = 0

    for step_counter in range(5):
        x = random.randint(0, 3)

        if x == 0:  # 0 is forward
            fwd_direction += 1  # forward += 1
            step_counter += 1
        elif x == 1:  # 1 is backwards
            fwd_direction -= 1  # Subtract 1 from forward direction
            step_counter += 1
        elif x == 2:  # 2 is left direction. No need to add/subtract from forward direction
            step_counter += 1
        elif x == 3:  # 3 is right direction. No need to add/subtract from forward direction.
            step_counter += 1

        # If forward direction = move from user, end cycle.
        if fwd_direction == dis:
            success = Label(window, text="Success! The net forward distance is: " + dis +
                                         "meters and was achieved in cycle " + cycle_counter)
            # success label will display when Robot's net forward distance == user dis input
            success.pack()
            return  # end function
        else:
            if step_counter == 4:
                progress = Label(window, text="In cycle " + cycle_counter + ", the net forward distance is: "
                                              + fwd_direction + "m")
                # progress label will display where the robot ended in each cycle.
                # I don't know why python is saying that cycle_counter and fwd_direction in this if statement are ints
                # and it expected a str. This issue did not happen in the success label.
                progress.pack()
                cycle_counter += 1              # Add 1 to cycle counter
                simulation(dis, cycle_counter)  # Call function again using same user dis, but w/ updated cycle counter


# Final notes: I understand that I haven't made a creative UI nor have a submitted a UI design.
# I really did try my best with the creation of this UI, but I just couldn't find any materials that
# would show me how to send parameters to my simulation function. I feel like a completely failed this
# midterm, professor. For that I'm sorry and I promise I'll make a comeback with Exam 2 and the final project.
# Could you please help me make this code work, professor? I would really like to see the end result of it.
