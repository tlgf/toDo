#!/usr/bin/python

'''
 filename: toDo
   author: t flynn
     date: 23.04.2016
     desc: generates 'to do' lists for a day\
     	   by prompting the user at login to fill\
	   in a list.
'''

from plumbum import cli
import subprocess
from subprocess import call
import time
import quote.quote as QF

LIST_LOCATION = "~/Documents/toDo/list.xml"
QUOTE_LOCATION = "~/Documents/toDo/quote/quotes.xml"

class toDo(cli.Application):
    # start up
    PROGNAME = "toDo"
    VERSION  = "0.1"

    # FLAGS
    verbose  = cli.Flag(["v"], help = "extended output")
    edit     = cli.Flag(["e"], help = "Edit the lists or quote files via text editor")

    def EditMode(self):
         if self.edit:
            select = raw_input("Edit (L)ist or (Q)uote? \n")
            if (select == "L") or (select == "l"):
                 call(["emacs", "-nw", LIST_LOCATION])
            elif (select == "Q") or (select == "q"):
                  call(["emacs", "-nw", QUOTE_LOCATION])
            exit()

            return

    def KickOff(self):
        # get the terminal properties
        termRows, termColumns = subprocess.check_output(['stty', 'size']).split()
        dateToPrint = str(time.strftime("%Y/%m/%d"))
        timeToPrint = str(time.strftime("%H:%M:%S"))

        call(["clear"])
        
        padding = " "
        print(padding.center(int(termRows) * 10, ' '))
        print(dateToPrint.center(int(termColumns) / 2, ' '))
        print(timeToPrint.center(int(termColumns) / 2, ' '))
        print(padding.center(int(termRows) * 10, ' '))

        return

    def InspirationalQuote(self):
        quoteEngine = QF.QuoteFinder('./quote/quotes.xml', "on")
        quoteEngine.printRandomQuote()
        return
        
            
    def main(self):
        self.EditMode() # exits if edit flag is used
        self.KickOff()  # get the ball rolling!
        self.InspirationalQuote() # be inspired
                
        ###
        # do more here
        ###

        # wrap it up
        if self.verbose:
            if raw_input("Review list in editor?") == 'y':
                call(["emacs", "-nw", "LIST_LOCATION"])
            print "toDo finished. Exit."       
        exit()
               
if __name__=="__main__":
    toDo.run()
