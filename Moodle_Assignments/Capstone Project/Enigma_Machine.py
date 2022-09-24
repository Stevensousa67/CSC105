""" This program simulates the Enigma Machine used by the Wehrmacht during World War 2.
Credit: https://github.com/omnitrogen/enigma for aiding in the creation of this program (mainly the UI) and giving a
north direction to me while developing the main Enigma algorithm.
Steven Sousa - Enigma Machine - 12/04/2020 """

# Import libraries
from tkinter import *

# Create Window
window = Tk()
window.title("Enigma Machine")  # Give window a name (upper left corner of window)
window.config(background='white')  # Change background of master window

# Place Wehrmacht image in window
logo = PhotoImage(file='Wehrmacht.png')  # Create variable that will have the Wehrmacht image
Label(window, image=logo, background='white').pack(padx=10, pady=10, side=TOP)

# Create new window for rotor wiring selection
rotor_window = Frame(window, background='white')

# There can be 3 different choices of rotor wiring. The reflector has only 1 value.
# Selection for rotor 1
rotor1_wiring = StringVar()
selection = Spinbox(rotor_window, values=('P,E,Z,U,O,H,X,S,C,V,F,M,T,B,G,L,R,I,N,Q,J,W,A,Y,D,K',
                                          'Z,O,U,E,S,Y,D,K,F,W,P,C,I,Q,X,H,M,V,B,L,G,N,J,R,A,T',
                                          'E,H,R,V,X,G,A,O,B,Q,U,S,I,M,Z,F,L,Y,N,W,K,T,P,D,J,C'),
                    textvariable=rotor1_wiring, width=55)
rotor1_wiring.set('P,E,Z,U,O,H,X,S,C,V,F,M,T,B,G,L,R,I,N,Q,J,W,A,Y,D,K')    # Default wiring selection
selection.grid(row=0, column=1)

# Selection for rotor 2
rotor2_wiring = StringVar()
selection = Spinbox(rotor_window, values=('P,E,Z,U,O,H,X,S,C,V,F,M,T,B,G,L,R,I,N,Q,J,W,A,Y,D,K',
                                          'Z,O,U,E,S,Y,D,K,F,W,P,C,I,Q,X,H,M,V,B,L,G,N,J,R,A,T',
                                          'E,H,R,V,X,G,A,O,B,Q,U,S,I,M,Z,F,L,Y,N,W,K,T,P,D,J,C'),
                    textvariable=rotor2_wiring, width=55)
rotor2_wiring.set('Z,O,U,E,S,Y,D,K,F,W,P,C,I,Q,X,H,M,V,B,L,G,N,J,R,A,T')    # Default wiring selection
selection.grid(row=1, column=1)

# Selection for rotor 3
rotor3_wiring = StringVar()
selection = Spinbox(rotor_window, values=('P,E,Z,U,O,H,X,S,C,V,F,M,T,B,G,L,R,I,N,Q,J,W,A,Y,D,K',
                                          'Z,O,U,E,S,Y,D,K,F,W,P,C,I,Q,X,H,M,V,B,L,G,N,J,R,A,T',
                                          'E,H,R,V,X,G,A,O,B,Q,U,S,I,M,Z,F,L,Y,N,W,K,T,P,D,J,C'),
                    textvariable=rotor3_wiring, width=55)
rotor3_wiring.set('E,H,R,V,X,G,A,O,B,Q,U,S,I,M,Z,F,L,Y,N,W,K,T,P,D,J,C')    # Default wiring selection
selection.grid(row=2, column=1)

# Display Reflector wiring
reflector_wiring = StringVar()
selection = Label(rotor_window, textvariable=reflector_wiring, width=55, relief=FLAT, background='white')
reflector_wiring.set("Y,R,U,H,Q,S,L,D,P,X,N,G,O,K,M,I,E,B,F,Z,C,W,V,J,A,T")  # Reflector's only wiring selection
selection.grid(row=3, column=1)

# Create label for rotor 1 wiring selection
rotor_1_selection = Label(rotor_window, text='Rotor 1 Wiring: ', padx=10, pady=10, background='white')
rotor_1_selection.grid(row=0, column=0)

# Create label for rotor 2 wiring selection
rotor_2_selection = Label(rotor_window, text='Rotor 2 Wiring: ', padx=10, pady=10, background='white')
rotor_2_selection.grid(row=1, column=0)

# Create label for rotor 3 wiring selection
rotor_3_selection = Label(rotor_window, text='Rotor 3 Wiring: ', padx=10, pady=10, background='white')
rotor_3_selection.grid(row=2, column=0)

# Create label for Reflector wiring
reflector_selection = Label(rotor_window, text="Reflector: ", padx=10, pady=10, background='white')
reflector_selection.grid(row=3, column=0)

rotor_window.pack()

# Create a third frame that will have the rotor position scale
scale = Frame(window, borderwidth=0, relief=FLAT, background='white')
scale.pack(side=TOP, padx=10, pady=10)

# Create label for Rotor 1 position selection
rotor1_text = Label(scale, text='Rotor 1', padx=10, pady=5, borderwidth=0, background='white')
rotor1_text.grid(row=0, column=0)

# Create label for Rotor 2 position selection
rotor2_text = Label(scale, text='Rotor 2', padx=10, pady=5, borderwidth=0, background='white')
rotor2_text.grid(row=0, column=1)

# Create label for Rotor 3 position selection
rotor3_text = Label(scale, text='Rotor 3', padx=10, pady=5, borderwidth=0, background='white')
rotor3_text.grid(row=0, column=2)


# Create function for rotor 1 position display
def rotor1(variable):
    """ This function will set rotor 1 to a specific letter and display it"""
    variable = int(variable)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    rotor1_label.configure(text='Position: {}'.format(alphabet[variable]))


# Create function for rotor 2 position display
def rotor2(variable):
    """ This function will set rotor 2 to a specific letter and display it"""
    variable = int(variable)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    rotor2_label.configure(text='Position: {}'.format(alphabet[variable]))


# Create function for rotor 3 position display
def rotor3(variable):
    """ This function will set rotor 3 to a specific letter and display it"""
    variable = int(variable)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    rotor3_label.configure(text='Position: {}'.format(alphabet[variable]))


# Create scale for Rotor 1
rotor1_scale = IntVar()
rotor_scale = Scale(scale, from_=0, to=25, variable=rotor1_scale, background='white', showvalue=0,
                    command=rotor1)
rotor_scale.grid(row=1, column=0, padx=60, pady=10)

# Create scale for Rotor 2
rotor2_scale = IntVar()
rotor_scale = Scale(scale, from_=0, to=25, variable=rotor2_scale, background='white', showvalue=0,
                    command=rotor2)
rotor_scale.grid(row=1, column=1, padx=60, pady=10)

# Create scale for Rotor 3
rotor3_scale = IntVar()
rotor_scale = Scale(scale, from_=0, to=25, variable=rotor3_scale, background='white', showvalue=0,
                    command=rotor3)
rotor_scale.grid(row=1, column=2, padx=60, pady=10)

# Create label that will tell user which position Rotor 1 is set to
rotor1_label = Label(scale, background='white')
rotor1_label.configure(text='Position: A')
rotor1_label.grid(row=2, column=0)

# Create label that will tell user which position Rotor 2 is set to
rotor2_label = Label(scale, background='white')
rotor2_label.configure(text='Position: A')
rotor2_label.grid(row=2, column=1)

# Create label that will tell user which position Rotor 3 is set to
rotor3_label = Label(scale, background='white')
rotor3_label.configure(text='Position: A')
rotor3_label.grid(row=2, column=2)

# Create a label that will instruct user to type message
instruction_label = Label(window, text='Enter message below after selecting desired rotor wiring. Hit "Encode/Decode" '
                                 'button after typing.', background='white')
instruction_label.pack()

# Create text field for user to type message
message = StringVar()
message = Entry(window, textvariable=message, background='white', width=80)
message.pack(padx=10, pady=10)


def code():
    """This function is the Enigma Machine's code"""

    # Transform rotor scale position into int
    rotor_1_position = int((rotor1_scale.get()))
    rotor_2_position = int((rotor2_scale.get()))
    rotor_3_position = int((rotor3_scale.get()))

    # Get user message's and make all letters caps locked.
    text = message.get()
    text = text.upper()

    # Make each rotor wiring a string and then a list
    rotor1_wiringstr = rotor1_wiring.get()
    rotor2_wiringstr = rotor2_wiring.get()
    rotor3_wiringstr = rotor3_wiring.get()

    rotor1_wiringlist = list(rotor1_wiringstr)
    rotor2_wiringlist = list(rotor2_wiringstr)
    rotor3_wiringlist = list(rotor3_wiringstr)

    # Create Enigma alphabet and alphabet dictionary
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

    alphabet_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                     'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                     'X': 24, 'Y': 25, 'Z': 26}

    def rotor_rotation(text_list):
        """This function will generate the rotor rotation"""
        text_list.append((text_list[0]))
        del text_list[0]
        return text_list

    def text_validity(text_list):
        """This function will test to see if text is valid"""
        if not text_list:
            print("Sorry, but the message is empty.")
            return False
        for character in text_list:
            if character == " ":
                pass
            elif alphabet.count(character.upper()) < 1:
                return False
        return True

    # Make rotor 1 wiring selection effective
    if rotor1_wiringlist[0] == 'P':
        rotor01 = ['P', 'E', 'Z', 'U', 'O', 'H', 'X', 'S', 'C', 'V', 'F', 'M', 'T', 'B', 'G', 'L', 'R', 'I', 'N', 'Q',
                   'J', 'W', 'A', 'Y', 'D', 'K']
    elif rotor1_wiringlist[0] == 'Z':
        rotor01 = ['Z', 'O', 'U', 'E', 'S', 'Y', 'D', 'K', 'F', 'W', 'P', 'C', 'I', 'Q', 'X', 'H', 'M', 'V', 'B', 'L',
                   'G', 'N', 'J', 'R', 'A', 'T']
    elif rotor1_wiringlist[0] == 'E':
        rotor01 = ['E', 'H', 'R', 'V', 'X', 'G', 'A', 'O', 'B', 'Q', 'U', 'S', 'I', 'M', 'Z', 'F', 'L', 'Y', 'N', 'W',
                   'K', 'T', 'P', 'D', 'J', 'C']

    # Make rotor 2 wiring selection effective
    if rotor2_wiringlist[0] == 'P':
        rotor02 = ['P', 'E', 'Z', 'U', 'O', 'H', 'X', 'S', 'C', 'V', 'F', 'M', 'T', 'B', 'G', 'L', 'R', 'I', 'N', 'Q',
                   'J', 'W', 'A', 'Y', 'D', 'K']
    elif rotor2_wiringlist[0] == 'Z':
        rotor02 = ['Z', 'O', 'U', 'E', 'S', 'Y', 'D', 'K', 'F', 'W', 'P', 'C', 'I', 'Q', 'X', 'H', 'M', 'V', 'B', 'L',
                   'G', 'N', 'J', 'R', 'A', 'T']
    elif rotor2_wiringlist[0] == 'E':
        rotor02 = ['E', 'H', 'R', 'V', 'X', 'G', 'A', 'O', 'B', 'Q', 'U', 'S', 'I', 'M', 'Z', 'F', 'L', 'Y', 'N', 'W',
                   'K', 'T', 'P', 'D', 'J', 'C']

    # Make rotor 3 wiring selection effective
    if rotor3_wiringlist[0] == 'P':
        rotor03 = ['P', 'E', 'Z', 'U', 'O', 'H', 'X', 'S', 'C', 'V', 'F', 'M', 'T', 'B', 'G', 'L', 'R', 'I', 'N', 'Q',
                   'J', 'W', 'A', 'Y', 'D', 'K']
    elif rotor3_wiringlist[0] == 'Z':
        rotor03 = ['Z', 'O', 'U', 'E', 'S', 'Y', 'D', 'K', 'F', 'W', 'P', 'C', 'I', 'Q', 'X', 'H', 'M', 'V', 'B', 'L',
                   'G', 'N', 'J', 'R', 'A', 'T']
    elif rotor3_wiringlist[0] == 'E':
        rotor03 = ['E', 'H', 'R', 'V', 'X', 'G', 'A', 'O', 'B', 'Q', 'U', 'S', 'I', 'M', 'Z', 'F', 'L', 'Y', 'N', 'W',
                   'K', 'T', 'P', 'D', 'J', 'C']

    # Make Reflector wiring effective
    reflector = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z',
                 'C', 'W', 'V', 'J', 'A', 'T']

    for loop1 in range(rotor_1_position):
        rotor_rotation(rotor01)
    for loop2 in range(rotor_2_position):
        rotor_rotation(rotor02)
    for loop3 in range(rotor_3_position):
        rotor_rotation(rotor03)

    text_list = list(text)
    text_list = [x for x in text_list if x != " "]

    # Check if text is valid (text only)
    if not text_validity(text_list):
        value = StringVar()
        value.set('You didnt type anything.')
        results.insert(END, value.get())
        results.see("end")

    # Check if rotor wiring is being used in different rotors
    elif (rotor1_wiringlist[0] == rotor2_wiringlist[0] == rotor3_wiringlist[0]) or \
            (rotor1_wiringlist[0] == rotor2_wiringlist[0]) or (rotor1_wiringlist[0] == rotor3_wiringlist[0]) or\
            (rotor2_wiringlist[0] == rotor3_wiringlist[0]):

        value = StringVar()
        value.set('Rotor wiring must be unique for each rotor.')
        results.insert(END, value.get())
        results.itemconfig(END)
        results.see("end")

    # If text is valid and rotor wiring are unique, proceed with encryption
    else:
        s = []

        # Iterate over each character of user's message
        for z in range(len(text_list)):
            a = alphabet_dict[text_list[z]]
            b = rotor01[a - 1]
            c = alphabet_dict[b]
            d = rotor02[c - 1]
            e = alphabet_dict[d]
            f = rotor03[e - 1]
            g = alphabet_dict[f]
            h = reflector[g - 1]
            j = rotor03.index(h)
            k = alphabet[j]
            l = rotor02.index(k)
            m = alphabet[l]
            n = rotor01.index(m)
            o = alphabet[n]
            s.append(o)

            # Generate rotor 1 rotation
            if (z + 1) % 1 == 0:
                rotor_rotation(rotor01)

            # Generate rotor 2 rotation
            if (z + 1) % 26 == 0:
                rotor_rotation(rotor02)

            # Generate rotor 3 rotation
            if (z + 1) % 676 == 0:
                rotor_rotation(rotor03)

        # Display encrypted results
        value = StringVar()
        value.set(''.join(s))
        results.insert(END, value.get())
        results.see("end")


# Create decode button
decode_button = Button(window, text='Encode/Decode', background='white', command=code)
decode_button.pack(padx=10, pady=10)

# Create a box area that will display converted strings.
results = Listbox(window, background='white', width=80)
results.pack(fill=Y, padx=5, pady=5)

# Create a quit button
quit_button = Button(window, text='Quit', background='white', command=window.quit, width=10)
quit_button.pack(padx=10, pady=10)

# Create mainloop event
mainloop()
