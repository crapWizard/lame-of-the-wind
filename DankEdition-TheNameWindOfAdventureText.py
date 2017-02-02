# This is a text Adeventure by Cecily and Casey
# dedicated to misha and harambe, may he live on in peace
# 2016-09-17 22:09:12.885000
import time
class Adventure():

    def fnStartQuiz(self):
        self.SweetSweetCashMoney = 0

        print "yo yo yo!! dis be the quiz for your tuition bro. you wanna pass or else you diez! #eddggyyyy"
        raw_input()
        self.playerName = raw_input( "whats yo name dawg")
        print "mym mymy my mannnnnn " + self.playerName + " you gotta answer dem 10 questions. this will determine your sweet sweet cash money for the turition so better get googling"
        self.DemeMankness = raw_input(" Dis be question 1: Rate on a scale of 1 to 5, how mank are your demes????")
        self.Eyeness = raw_input("Dis be queastion too: what is the square root of negative 1??")
        self.ReferenceTest = raw_input("Dis be the tird question: What is answer to life, the universe, and everyting?")
        self.SanityCheck = raw_input("who is better, faramir or boromir?")
        self.Graphzzzzzzzz = raw_input("wahts the gradient of a vertical line")
        self.GeographyCheck = raw_input("Where is Barad-dur located")
        self.movie = raw_input("What is the best movie?")
        self.CoolnessCheck = raw_input("Name the greatest formula :)")
        print "  The professors are staring at you wiher because of stupidity (most likely) or because of great dankness. You will now find out which."
        raw_input()

        print " Calculating tuition..."
        time.sleep(1)

        # score is calculated
        if self.DemeMankness == "1":
            pass
        else:
            self.SweetSweetCashMoney += 10
        if self.Eyeness == "i":
            pass
        else:
            self.SweetSweetCashMoney += 10
        if self.ReferenceTest == "42":
            pass
        else:
            self.SweetSweetCashMoney += 10
        if self.SanityCheck  == 'faramir':
            pass
        else:
            self.SweetSweetCashMoney += 10
        if self.Graphzzzzzzzz == "undefined":
            pass
        else:
            self.SweetSweetCashMoney += 10
        if self.GeographyCheck == "mordor":
            pass
        else:
            self.SweetSweetCashMoney += 10
        if self.movie == "bee movie" or "gnomeo and juliet" or "shrek" or "shrek 2":
            pass
        else:
            self.SweetSweetCashMoney += 10
        if self.CoolnessCheck == "time of pendulum swing":
            pass
        else:
            self.SweetSweetCashMoney += 10
        print self.playerName + " yous sweet sweet cash munny is equal to " + str(self.SweetSweetCashMoney)

    def __init__(self):
        self.fnStartQuiz()


Adventure()
