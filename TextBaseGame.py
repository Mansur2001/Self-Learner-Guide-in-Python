answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

def intro():

    print("""WELCOME TO THE ADVENTURE GAME!
    Let's start the action! ☆-🎬-☆
     
    Its a saturday night, you are just a kid at the age of 10.
    Once you get ready for bed, both your parents are ready to be at your side.
    A few moments later you wake up with an urge to pee, whilst walking around
    the house you notice....you find yourself to be all alone.
    What should you do?
    Choose your battle: (Type any version of YES/NO)
""")
    ans1 = input(" >>")
    if ans1 in answer_yes:
        print("Run out the house looking for help,(yes/no)\n")
        character = character()
        print(character)

        ans2 = input(">>")
        if ans2 in answer_no:
            print("There is nothing but mist and rain, you dont have a phone do you keep running (yes/no)\n")
        ans3 = input(">>")
        if ans3 in answer_yes:
           
            print("You end up near a forest, soon you will have no options will you scream for help(yes/no)\n")
            win = Win()
            print(win)
        else:
            lose = Lose()
            print(lose)
def character():
    print("""
     o
    /|\
    / \
    """)

def Win():
    print("""
      ---------------+---------------
          ___ /^^[___              _
         /|^+----+   |#___________//
       ( -+ |__\o/__|    ______-----+/
        ==______\_\__--'            \
          ~_|___|\__
    """)

def Lose():
    print("""
     O
    \|\
     /\/   .....WHAT HAPPENS NEXT!?
    /
    """)
