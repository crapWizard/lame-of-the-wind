# this a text adventure based upon the book 'the name of the wind' by patrick rothfuss
# by cecily and casey
# 2016

import random
from Tkinter import *


class Functions:

    def __init__(self):
        self.fnSetBaseStats()


        # define faces to change depending on charisma
        self.happy = """|||||
{. @ @ .}
|  o  |
\_U_/
"""
        self.ok = """|||||
{. @ @ .}
|  o  |
\_-_/
"""
        self.sad = """|||||
{. @ @ .}
|  o  |
\_^_/"""

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
                                        'Lute Skill:  ' + str(functions.luteSkill) + "\n" + "\n" +
                                        'Charisma:  ' + str(functions.charisma) + "\n" + "\n" +
                                        'Appearance:  ' + str(functions.appearance) + "\n" + "\n" +
                                        'Rank:  ' + str(functions.rank)+ "\n" + "\n" +
                                        "Money: " + str(functions.finalMoney) )
            # change face depending on charisma and appearance depending on appearance
            self.fnAppearanceCheck()

            # cardinal direction move

            # North (up)
            if playerInput == "w":
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
            elif playerInput == "d":
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
            elif playerInput == "a":
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

            # if in the mess hall, can eat food or chat
            elif self.location ==[2,1,0]:

               if playerInput == "eat":
                    appBasicGUI.txtFrame.insert(INSERT, "You ate a delicious sandwich and you feel replenished  \n")
                    self.energy +=10
                    break
               elif playerInput=="chat":
                    appBasicGUI.txtFrame.insert(INSERT, "You have a pleasant converation with your someone of your fellow students  \n")
                    self.charisma +=1
                    break


            else:
                appBasicGUI.txtFrame.insert(INSERT, "Sorry, that command was not recognised" + '\n')
                break





    def fnAppearanceCheck(self):
        if functions.charisma > 66:
            appBasicGUI.lblBaseStats.config(text="\n" + 'Energy:  ' + str(functions.energy) + "\n" + "\n" +
                                                 'Lute Skill:  ' + str(functions.luteSkill) + "\n" + "\n" +
                                                 'Charisma:  ' + str(functions.charisma) + "\n" + "\n" +
                                                 'Appearance:  ' + str(functions.appearance) + "\n" + "\n" +
                                                 'Rank:  ' + str(functions.rank) + "\n" + "\n" +
                                                 "Money: " + str(functions.finalMoney) + "\n" + "\n" + self.happy)
        elif functions.charisma > 33:
            appBasicGUI.lblBaseStats.config(text="\n" + 'Energy:  ' + str(functions.energy) + "\n" + "\n" +
                                                 'Lute Skill:  ' + str(functions.luteSkill) + "\n" + "\n" +
                                                 'Charisma:  ' + str(functions.charisma) + "\n" + "\n" +
                                                 'Appearance:  ' + str(functions.appearance) + "\n" + "\n" +
                                                 'Rank:  ' + str(functions.rank) + "\n" + "\n" +
                                                 "Money: " + str(functions.finalMoney) + "\n" + "\n" + self.ok)
        else:
            appBasicGUI.lblBaseStats.config(text="\n" + 'Energy:  ' + str(functions.energy) + "\n" + "\n" +
                                                 'Lute Skill:  ' + str(functions.luteSkill) + "\n" + "\n" +
                                                 'Charisma:  ' + str(functions.charisma) + "\n" + "\n" +
                                                 'Appearance:  ' + str(functions.appearance) + "\n" + "\n" +
                                                 'Rank:  ' + str(functions.rank) + "\n" + "\n" +
                                                 "Money: " + str(functions.finalMoney) + "\n" + "\n" + self.sad)

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

    def fnMoney(self, money):
        jonts = int(money)
        talons = 0
        marks = 0
        while jonts >= 10:
            talons = talons + 1
            jonts = jonts - 10
            if talons > 10:
                marks = marks + 1
                talons = talons - 10
        print str(jonts) + " jonts, " + str(talons) + " talons, and " + str(marks) + " marks"
        strFinalMoney = str(   "\n" + "\n" + str(marks) + " marks" +"\n" +  "\n" +  str(talons) + " talons" +"\n" + "\n" +str(jonts) + " jonts " )
        return strFinalMoney


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
        money = random.randrange(0, 200)
        print money
        self.finalMoney = self.fnMoney(money)

        # set initital rank
        self.rank = 'elir'

    def fnDormitory(self):
        appBasicGUI.txtFrame.insert(INSERT, "You are now in the dormitory.\n Rows of spacious single beds line the walls. A small desk is allocated for \n each bunk. Bed furnishings are modest, yet comfortable.\n")
        self.energy = 100
        appBasicGUI.txtFrame.insert(INSERT,"Energy fully restored, you may now exit the dormitory\n")
        # scrolls to newest entry in box
        appBasicGUI.txtFrame.see(END)

    def fnMessHall(self):
        appBasicGUI.txtFrame.insert(INSERT, "You are now in the mess hall. \n")
        appBasicGUI.txtFrame.insert(INSERT, 'Would you like to eat or chat? \n')
        appBasicGUI.txtFrame.see(END)


    def fnHall(self):
        appBasicGUI.txtFrame.insert(INSERT, "You're in the hall.\n")
        appBasicGUI.txtFrame.see(END)

    def fnHomeowrkRoom(self):
        appBasicGUI.txtFrame.insert(INSERT, "A row of recently polished oak deaks stands in one corner. Some music stands lay scattered around a large empty space in the centre of the room. You are now in the practice/homework room.\n")
        appBasicGUI.txtFrame.see(END)

    def fnLibrary(self):
        appBasicGUI.txtFrame.insert(INSERT, "You are now in the Library.\n")
        appBasicGUI.txtFrame.insert(INSERT, "You look around to see rows and rows of bookshelves full of books that can \n be used to study for your class.\n")
        appBasicGUI.txtFrame.see(END)

    def fnMastersRoom(self):
        appBasicGUI.txtFrame.insert(INSERT, "You are now in the Masters' Room.\n")
        appBasicGUI.txtFrame.insert(INSERT, "You are see the Master Artificer, Kilvin and Master Sympathist, Elxa Dal, \n having a debate about the intricacies of Sympathy." +"\n" +
                                            "However, you aren't knowledgeable enough in Sympathy to understand their \n  discussion. \n")
        appBasicGUI.txtFrame.insert(INSERT, "The masters don't seem to notice to your presence in the room" + "\n")
        appBasicGUI.txtFrame.see(END)

    def fnClassroom(self):
        appBasicGUI.txtFrame.insert(INSERT, "You are now in the Classroom.\n")
        appBasicGUI.txtFrame.insert(INSERT, "No classes are currently running, so there is no point for you to be in this \n room")
        appBasicGUI.txtFrame.see(END)




    def fnCheckLocation(self):
        if self.location == [0,0,0]:
            self.fnDormitory()

        elif self.location == [2,1,0]:
            self.fnMessHall()

        elif self.location == [1,1,0] or self.location == [1,0,0] or self.location == [1,2,0]:
            self.fnHall()

        elif self.location == [2,0,0]:
            self.fnHomeowrkRoom()

        elif self.location == [0,1,0]:
            self.fnClassroom()

        elif self.location ==[0,2,0]:
            self.fnMastersRoom()

        elif self.location ==[2,2,0]:
            self.fnLibrary()


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
        self.master.title("The University")
        self.master.minsize(700, 550)
        self.master.maxsize(900, 800)
        self.fnCreateWidgets()




    def fnCreateWidgets(self):
        self.strCmd = StringVar()


        self.frWindow = Frame(height=500, width=400)
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
        'Rank:  ' + str(functions.rank)+ "\n" + "\n" +
        "Money: " + str(functions.finalMoney))


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



