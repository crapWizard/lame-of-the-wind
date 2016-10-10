# this a text adventure based upon the book 'the name of the wind' by patrick rothfuss
# by Cecily and Casey
# 2016

import random

class Functions:

    def fnInput(self):

        self.fnSetBaseStats()

        while True:
            playerInput = raw_input(": ")


            # cardinal direction move

            # North (up)
            if playerInput == "n":
                if self.location[1] > 0:
                    self.location[1] -= 1
                else:
                    print "There is a barrier, you cannot go in this direction"
            # South (down)
            elif playerInput == "s":
                if self.location[1] < 2 or self.location[0] == 1:  # staircase exception
                    self.location[1] += 1
                    # if self.location[0] == 1, then they are on the staircase and need to be taken to the next level
                else:
                    print "There is a barrier, you cannot go in this direction"
            # East (right)
            elif playerInput == "e":
                if self.location[0] < 2:
                    self.location[0] += 1
                else:
                    print "There is a barrier, you cannot go in this direction"
            # West (left)
            elif playerInput == "w":
                if self.location[0] > 0:
                    self.location[0] -= 1
                else:
                    print "There is a barrier, you cannot go in this direction"


            # a map is displayed
            elif playerInput == "map":
                self.fnMaps()
            else:
                print "Sorry, that command was not recognised"
            print self.location



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
                       | stairwell |
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
            print self.uni000
        elif self.location == [0,1,0]:
            print self.uni010
        elif self.location == [2,0,0]:
            print self.uni200
        elif self.location == [0,2,0]:
            print self.uni020
        elif self.location == [1,0,0]:
            print self.uni100
        elif self.location == [1,1,0]:
            print self.uni110
        elif self.location == [1,2,0]:
            print self.uni120
        elif self.location == [2,2,0]:
            print self.uni220
        elif self.location == [2,1,0]:
            print self.uni210




    def fnSetBaseStats(self):

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

        print 'energy', self.energy
        print 'Lute Skill', self.luteSkill
        print 'Charisma', self.charisma
        print 'Appearance', self.appearance
        print 'Rank', self.rank

    def fnSetSubjectStats(self):

        # set subjects for each rank
        self.elirSubjects = {'Sympathy': 0, 'Alchemy': 0, 'Geometry': 0, 'Rhetoric': 0, 'Physiognomy': 0, 'Metallurgy': 0}
        self.relarSubjects = {'Naming': 0, 'Chemistry': 0, 'History': 0, 'Artifying': 0, 'Languages': 0, 'Herbology': 0}
        self.eltheSubjects = {'History': 0, 'Mathematics': 0, 'Artifying': 0, 'Poetry': 0, 'Philosophy': 0, 'Anatomy': 0}

        if self.rank == 'elir':
            for eachSubject in self.elirSubjects:
                self.elirSubjects[eachSubject] = random.randrange(0,40)
        elif self.rank == 'relir':
            for eachSubject in self.relarSubjects:
                self.relarSubjects[eachSubject] = random.randrange(0,40)
        if self.rank == 'elthe':
            for eachSubject in self.eltheSubjects:
                self.eltheSubjects[eachSubject] = random.randrange(0,40)
        print self.elirSubjects
functions = Functions()
Functions.fnInput(functions)