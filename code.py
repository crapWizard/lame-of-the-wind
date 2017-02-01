# this a text adventure based upon the book 'the name of the wind' by patrick rothfuss
# by cecily and casey
# 2016

import random
from Tkinter import *


class Functions:

    def __init__(self):
        self.fnSetBaseStats()

    def fnInput(self,i):
        playerInput = appBasicGUI.entCmd.get()

        # print whatever was typed onto the game screen
        appBasicGUI.txtFrame.insert(INSERT,playerInput + '\n')
        # scrolls to newest entry on box
        appBasicGUI.txtFrame.see(END)


        appBasicGUI.entCmd.delete(0, 'end') # clear entry box

        while True:
            # update base stats display
            appBasicGUI.lblBaseStats.config(text="\n" + 'Energy:  ' + str(functions.energy) + "\n" + "\n" +
                                          'Lute Skill:  ' + str(functions.luteSkill) + "\n" + "\n"
                                                                                              'Charisma:  ' + str(
                functions.charisma) + "\n" + "\n" +
                                          'Appearance:  ' + str(functions.appearance) + "\n" + "\n" +
                                          'Rank:  ' + str(functions.rank))
            # cardinal direction move

            # North (up)
            if playerInput == "n":
                if self.location[1] > 0 and self.location[0] == 1:
                    self.location[1] -= 1
                    self.energy -= 3
                    appBasicGUI.txtFrame.insert(INSERT, "You went North" + '\n')
                    self.fnCheckLocation()
                    break
                else:
                    appBasicGUI.txtFrame.insert(INSERT,"There is a barrier, you cannot go in this direction" + '\n')
                    break
            # South (down)
            elif playerInput == "s":
                if self.location[1] < 2  and self.location[0] == 1 and self.location[0] == 1:
                    self.location[1] += 1
                    self.energy -= 3
                    self.fnCheckLocation()
                    appBasicGUI.txtFrame.insert(INSERT, "You went South" + '\n')
                    break
                # staircase exception
                elif self.location == [1,2,0]:
                    # if self.location[0] == 1, then they are on the staircase and need to be taken to the next level
                    if self.rank == 'relar':
                        self.fnRankRelar
                    elif self.rank == 'elthe':
                        self.fnRnakElthe
                        break
                    else:
                        appBasicGUI.txtFrame.insert(INSERT, "You enter the staircase but encouter a barrier in form of a chain over the bottom most step. "
                                                            "Try coming back when you reach a better rank" + '\n')
                        break

                else:
                    appBasicGUI.txtFrame.insert(INSERT, "There is a barrier, you cannot go in this direction" + '\n')
                    break
            # East (right)
            elif playerInput == "e":
                if self.location[0] < 2:
                    self.location[0] += 1
                    self.energy -= 3
                    self.fnCheckLocation()
                    appBasicGUI.txtFrame.insert(INSERT, "You went East" + '\n')
                    break
                else:
                    appBasicGUI.txtFrame.insert(INSERT, "There is a barrier, you cannot go in this direction" + '\n')
                    break
            # West (left)
            elif playerInput == "w":
                if self.location[0] > 0:
                    self.location[0] -= 1
                    self.energy -= 3
                    self.fnCheckLocation()
                    appBasicGUI.txtFrame.insert(INSERT, "You went West" + '\n')
                    break
                else:
                    appBasicGUI.txtFrame.insert(INSERT, "There is a barrier, you cannot go in this direction" + '\n')
                    break


            # a map is displayed
            elif playerInput == "map":
                self.fnMaps()
                break

            else:
                appBasicGUI.txtFrame.insert(INSERT, "Sorry, that command was not recognised" + '\n')
                break







    def fnMaps(self):

        self.uni100 = """
        the * represents where you are


                    to town
                      /\\
                      |
        _____________    ____________________
        | dormitory|| * || practise/homework|
        |          ||   ||      room        |
        -----------||   ||-------------------
        | classroom||   || mess hall        |
        |          ||   ||                  |
        -----------||   ||-------------------
        | masters  ||   || library          |
        | room     ||   ||                  |
        -----------||   ||-------------------
               | stairwell |
               |           |
               -------------

            N
        W --|-- E
            S"""

        self.uni110 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |          ||   ||      room        |
                -----------||   ||-------------------
                | classroom|| * || mess hall        |
                |          ||   ||                  |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room     ||   ||                  |
                -----------||   ||-------------------
                       | stairwell |
                       |           |
                       -------------

                    N
                W --|-- E
                    S"""

        self.uni120 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |          ||   ||      room        |
                -----------||   ||-------------------
                | classroom||   || mess hall        |
                |          ||   ||                  |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room     || * ||                  |
                -----------||   ||-------------------
                       | stairwell |
                       |           |
                       -------------

                    N
                W --|-- E
                    S"""
        self.uni000 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |    *     ||   ||      room        |
                -----------||   ||-------------------
                | classroom||   || mess hall        |
                |          ||   ||                  |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room     ||   ||                  |
                -----------||   ||-------------------
                       | stairwell |
                       |           |
                       -------------

                    N
                W --|-- E
                    S"""
        self.uni200 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |          ||   ||   *  room        |
                -----------||   ||-------------------
                | classroom||   || mess hall        |
                |          ||   ||                  |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room     ||   ||                  |
                -----------||   ||-------------------
                       | stairwell |0
                       |           |
                       -------------

                    N
                W --|-- E
                    S"""
        self.uni210 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |          ||   ||      room        |
                -----------||   ||-------------------
                | classroom||   || mess hall        |
                |          ||   ||   *              |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room     ||   ||                  |
                -----------||   ||-------------------
                       | stairwell |
                       |           |
                       -------------

                    N
                W --|-- E
                    S"""
        self.uni220 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |          ||   ||      room        |
                -----------||   ||-------------------
                | classroom||   || mess hall        |
                |          ||   ||                  |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room     ||   ||    *             |
                -----------||   ||-------------------
                       | stairwell |
                       |           |
                       -------------

                    N
                W --|-- E
                    S"""
        self.uni130 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |          ||   ||      room        |
                -----------||   ||-------------------
                | classroom||   || mess hall        |
                |          ||   ||                  |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room     ||   ||                  |
                -----------||   ||-------------------
                       | stairwell |
                       |      *    |
                       -------------

                    N
                W --|-- E
                    S"""
        self.uni020 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |          ||   ||      room        |
                -----------||   ||-------------------
                | classroom||   || mess hall        |
                |          ||   ||                  |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room *   ||   ||                  |
                -----------||   ||-------------------
                       | stairwell |
                       |           |
                       -------------

                    N
                W --|-- E
                    S"""
        self.uni010 = """
                the * represents where you are


                            to town
                              /\\
                              |
                _____________    ____________________
                | dormitory||   || practise/homework|
                |          ||   ||      room        |
                -----------||   ||-------------------
                | classroom||   || mess hall        |
                |    *     ||   ||                  |
                -----------||   ||-------------------
                | masters  ||   || library          |
                | room     ||   ||                  |
                -----------||   ||-------------------
                       | stairwell |
                       |           |
                       -------------

                    N
                W --|-- E
                    S"""
        if self.location == [0,0,0]:
            appBasicGUI.txtFrame.insert(INSERT, self.uni000 + '\n')
        elif self.location == [0,1,0]:
            appBasicGUI.txtFrame.insert(INSERT,self.uni010+ '\n')
        elif self.location == [2,0,0]:
            appBasicGUI.txtFrame.insert(INSERT,self.uni200+ '\n')
        elif self.location == [0,2,0]:
            appBasicGUI.txtFrame.insert(INSERT,self.uni020+ '\n')
        elif self.location == [1,0,0]:
            appBasicGUI.txtFrame.insert(INSERT,self.uni100+ '\n')
        elif self.location == [1,1,0]:
            appBasicGUI.txtFrame.insert(INSERT,self.uni110+ '\n')
        elif self.location == [1,2,0]:
            appBasicGUI.txtFrame.insert(INSERT,self.uni120+ '\n')
        elif self.location == [2,2,0]:
            appBasicGUI.txtFrame.insert(INSERT,self.uni220+ '\n')
        elif self.location == [2,1,0]:
            appBasicGUI.txtFrame.insert(INSERT,self.uni210+ '\n')
        # scrolls to newest entry in box
        appBasicGUI.txtFrame.see(END)




    def fnSetBaseStats(self):

        # chat dialogue for convos throughout the game

        self.chatResponse = []

    # set initial location
        self.location = [0,0,0]

        """ these are the following base stats initially generated at the start of the game and
        displayed on the gui
        energy | /100
        skill level (lute) | /100
        charisma | /100
        appearance | /100"""

        # set the inital values for the start of the game
        self.energy = 100
        self.luteSkill = 0
        self.charisma = random.randrange(0,50)
        self.appearance = random.randrange(0,25)

        # set initital rank
        self.rank = 'elir'

    def fnDormitory(self):
        appBasicGUI.txtFrame.insert(INSERT, "You are now in the dormitory.\n")
        appBasicGUI.txtFrame.insert(INSERT, "Rows of spacious single beds line the walls. A small desk is allocated for each bunk. Bed furnishings are modest, yet comfortable.\n")
        self.energy = 100
        appBasicGUI.txtFrame.insert(INSERT,"Energy fully restored, you may now exit the dormitory\n")
        # scrolls to newest entry in box
        appBasicGUI.txtFrame.see(END)

    def fnMessHall(self):
        print "You are now in the mess hall"
        response = input('Would you like to eat or chat?')
        if response == 'eat':
            self.energy += 10
        elif response == 'chat':
            print random.choice(self.chatDialogue)
            self.charisma += 1
            input = input("What do you think?")
            print random.choice(self.chatResponse)



    def fnCheckLocation(self):
        if self.location == [0,0,0]:
            self.fnDormitory()
        elif self.location == [2,2,0]:
            self.fnMessHall()


    def fnSetSubjectStats(self):

        # set subjects for each rank
        self.elirSubjects = {'Sympathy': 0, 'Alchemy': 0, 'Geometry': 0, 'Rhetoric': 0, 'Physiognomy': 0, 'Metallurgy': 0}
        self.relarSubjects = {'Naming': 0, 'Chemistry': 0, 'History': 0, 'Artifying': 0, 'Languages': 0, 'Herbology': 0}
        self.eltheSubjects = {'History': 0, 'Mathematics': 0, 'Artifying': 0, 'Poetry': 0, 'Philosophy': 0, 'Anatomy': 0}

        if self.rank == 'elir':
            for eachSubject in self.elirSubjects:
                self.elirSubjects[eachSubject] = random.randrange(0,40)
        elif self.rank == 'relar':
            for eachSubject in self.relarSubjects:
                self.relarSubjects[eachSubject] = random.randrange(0,40)
        if self.rank == 'elthe':
            for eachSubject in self.eltheSubjects:
                self.eltheSubjects[eachSubject] = random.randrange(0,40)
        print self.elirSubjects



class GUI:

    # set inital gui stuff
    def __init__(self, master):
        self.master = master
        self.master.title("The Academy")
        self.master.minsize(700, 550)
        self.master.maxsize(700, 550)
        self.fnCreateWidgets()




    def fnCreateWidgets(self):
        self.strCmd = StringVar()


        self.frWindow = Frame(height=400, width=500)
        self.frWindow.pack(fill=BOTH, expand=1)

        self.txtFrame = Text(self.frWindow, relief = SUNKEN, height = 30, width = 80)
        self.txtFrame.grid(row = 0, column = 0)
        self.txtFrame.insert(INSERT, "Welcome to the Academy!\n")

        # label to display all base stats
        self.lblBaseStats = Label(self.frWindow, relief = SUNKEN, anchor = N, height = 30, width =16, bg = 'light grey', font  ='MONACO 12 bold' )
        self.lblBaseStats.grid(row = 0, column = 2, padx = 5)


        # display stats
        self.lblBaseStats.config(text =  "\n" +'Energy:  ' + str(functions.energy) + "\n"+ "\n"+
        'Lute Skill:  '+ str(functions.luteSkill) + "\n" + "\n"
        'Charisma:  ' + str(functions.charisma) + "\n"+  "\n" +
        'Appearance:  ' + str(functions.appearance) + "\n" + "\n"+
        'Rank:  '+ str(functions.rank))

        # entry box for control of character
        self.entCmd = Entry(self.frWindow, relief = SUNKEN, width = 80)
        self.entCmd.grid(row = 1 , column = 0, pady = 10)

        # button, enters text in entry box- also binds return key to entry
        self.btnEntry = Button(self.frWindow,relief = RAISED,text = 'enter', width = 14, height = 1, command = lambda :functions.fnInput(0))
        self.btnEntry.grid(row = 1, column = 2, pady = 10)
        self.entCmd.bind('<Return>', functions.fnInput)






functions = Functions()

wdBaseWindow = Tk()
appBasicGUI = GUI(wdBaseWindow)
wdBaseWindow.mainloop()




