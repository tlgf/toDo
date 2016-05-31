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
import os
import time

class toDo(cli.Application):
    # start up
    PROGNAME = "ToDo"
    VERSION  = "0.1"
    verbose = cli.Flag(["v"], help = "extended output")
    quoteNumber = random()
        
    def main(self):
        if self.verbose:
            verboseMode="on"
        else:
            verboseMode="off" 
            
        if verboseMode=="on":
                print "toDo finished. Exit."

        print randomQuote # randomQuote finshes on exit ->
                          # store these quotes in a text file 
        exit()
               
if __name__=="__main__":
    toDo.run()
