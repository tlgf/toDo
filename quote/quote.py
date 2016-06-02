#!/usr/bin/python

'''
 title: quote.py
  date: 31.05.2016
author: t flynn
  desc: parses or *automatically adds* quotes from/to the quote.xml store -*not yet implemented
'''

import xml.etree.ElementTree as etree
from random import randint
from termcolor import colored, cprint
#import os

class QuoteFinder:
    def __init__(self, theQuotes, colorMode):
        if colorMode != ("on" or "off"):
            print "color Mode not initialised. exit"
            exit()
        self.colorMode = colorMode
        self.outputQuote = []
        self.quoteStoreLocation = theQuotes
        self.quoteFile = etree.parse(self.quoteStoreLocation)
        self.theQuotes = self.quoteFile.getroot()
        self.numberOfQuotes = len(self.theQuotes)
        self.randomQuoteID = randint(0, self.numberOfQuotes)
        

    def colorModeOn(self):
        if self.colorMode == "on":
            return True

        return False
    
    def printGivenQuote(self, quoteID):
        for row in range(0,3):
            self.outputQuote.append(self.theQuotes[quoteID][row].text)

        for row in self.outputQuote:
            if self.colorModeOn():
                print(colored(row, 'red', attrs=['bold', 'blink']))
            else:
                print(row)
        return
            
        
    def getQuote(self, aQuoteID):
        #aQuoteID = self.randomQuoteID
        for row in range(0,3):
            self.outputQuote.append(self.theQuotes[aQuoteID][row].text)
        return self.outputQuote

    def printRandomQuote(self):
        randomQuote = self.getQuote(self.randomQuoteID)
       # for row in randomQuote:
        #    print(row)
        for row in self.outputQuote:
            if self.colorModeOn():
                print(colored(row, 'red', attrs=['bold', 'blink']))
            else:
                print(row)
        return

    def printAllQuotes(self):
        print "Number of Quotes:", self.numberOfQuotes

        for quoteID in range(0, self.numberOfQuotes):
            for quotePiece in range(0,3):
                print(colored(self.theQuotes[quoteID][quotePiece].text,'red', attrs=['bold', 'blink']))
        return
        
    def addNewQuote(self, theQuote, theAuthor, theYear):
        ID = len(self.theQuotes) + 1
        '''
        add the xml magic here
        '''

def main():

    selection = int(raw_input("Enter 1 for a random quote, 2 to print all quotes \n"))

    quotes = QuoteFinder('./quotes.xml', "on")

    if selection == 1:
        quotes.printRandomQuote()
        exit()
    
    elif selection == 2:
        quotes.printAllQuotes()
        exit()
        
    elif selection == 3:
        quote = raw_input('Enter a quote \n')
        author = raw_input('Enter the author \n')
        year = raw_input('Enter the year \n')
        print('The following will be added to the list: \n')
        print (quote, author, year)
        quotes.addNewQuote(quote, author, year)
        exit()
        
    else:
        main()
        #print("Enter 1 or 2.")
        #break

if __name__ == '__main__':
    main()            
        
