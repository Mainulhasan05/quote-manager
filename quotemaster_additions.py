# Name:
# Student Number:

# This file is provided to you as a starting point for the "quotemaster.py" program of Project
# of CSI6208 in Semester 1, 2025.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json
import random
import time

class ProgramGUI:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('500x500')
        self.root.title('QuoteMaster')
        self.root.iconbitmap('icon.ico')
        try: 
            with open('data.txt', 'r') as file:
                self.data = json.load(file)
        except:
            tkinter.messagebox.showerror("Something Went Wrong", "The data file is missing or corrupted.\nPlease contact the administrator.")
            self.root.destroy()
            return
        # adding authors to authors list
        self.authors = []
        for quote in self.data:
            if quote['author'] not in self.authors:
                self.authors.append(quote['author'])
        # checking if authors are at least 3
        if len(self.authors) < 3:
            tkinter.messagebox.showerror("Something Went Wrong", "Insufficient number of authors.")
            self.root.destroy()
            return

        # creating attributes
        self.score = 0
        self.questionCount = 0
        self.timer=10
        self.timerId = None
        
        
        self.root.configure(bg='#f5f5f5')
        
        
        
        self.frame = tkinter.Frame(self.root)
        self.frame.pack(pady=20)
        self.frame.pack_propagate(0)
        self.frame.config(width=500, height=500)
        

        
        # loading the quote
        self.loadQuote()
        self.root.mainloop()



    def loadQuote(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.headingLabel = tkinter.Label(self.frame, width=500, fg='#ecf0f1', text="QuoteMaster",font=('Arial', 20, 'bold'), bg='#2c3e50')
        self.headingLabel.pack(pady=10)
        self.timerLabel = tkinter.Label(self.frame, text=f'Time Left: {self.timer}', bg='lightblue')
        self.timerLabel.pack(pady=10)
        #
        # See Point 1 of the "Methods in the GUI Class of quotemaster.py" section of the assignment brief.

        if self.timerId:
            self.root.after_cancel(self.timerId)
        self.startTimer()
        
        
        self.questionCount += 1 
        self.selectedQuote = random.choice(self.data)
        print("Picked quote:", self.selectedQuote)
        quoteText = self.selectedQuote['quote']
        quoteAuthor = self.selectedQuote['author']
        quoteYear = self.selectedQuote['year']
        # creating a label for the quote
        quoteLabel = tkinter.Label(self.frame, text=f'"{quoteText}"', bg='lightblue', wraplength=400, justify='center', font=('Italic', 16,"italic"))
        quoteLabel.pack(pady=10)

        tkinter.Label(self.frame, text="Who said this ?",  wraplength=400, justify='center', font=('Arial', 10)).pack(pady=10)
        # choose 3 random authors from the authors list including the correct author
        randomAuthors = []
        randomAuthors.append(quoteAuthor)
        while len(randomAuthors) < 3:
            randomAuthor = random.choice(self.authors)
            if randomAuthor not in randomAuthors:
                randomAuthors.append(randomAuthor)
        # shuffling the authors list
        random.shuffle(randomAuthors)
        # creating button for each author options
        for author in randomAuthors:
            button = tkinter.Button(self.frame,font=('Arial', 10, 'bold'), width=20, text=author, fg='#2c3e50', bg='#dfe6e9', command=lambda author=author: self.checkAnswer(author))
            button.pack(pady=5)

        # creating a label for the score
        self.scoreLabel = tkinter.Label(self.frame, text=f'Score: {self.score}', bg='lightblue')
        self.scoreLabel.pack(pady=10)

        # creating a label for the question count
        self.questionCountLabel = tkinter.Label(self.frame, text=f'Question: {self.questionCount}', bg='lightblue')
        self.questionCountLabel.pack(pady=10)
        
        
        # creating a button to quit the game
        quitButton = tkinter.Button(self.frame, text='Quit', bg='lightgrey', command=self.root.quit)
        quitButton.pack(pady=10)
        
        pass

    
    def checkAnswer(self, chosenName):
        #
        # See Point 2 of the "Methods in the GUI Class of quotemaster.py" section of the assignment brief.
        # This method should check if the chosen name is the correct author of the quote.
        percentage = 0
        if chosenName == self.selectedQuote['author']:
            year = self.selectedQuote['year']
            
            self.score += 1
            percentage = round(self.score / self.questionCount * 100)
            if tkinter.messagebox.askyesno("Correct!", f"You are correct!\n {"It was said in "+year+".\n" if year!='u' else "" } Your score is {self.score}/{self.questionCount}. \n You got {percentage}% of the questions correct.\n\n Continue ?"):
                self.loadQuote()
            else:
                self.root.destroy()
            
        else:
            # self.score -= 1
            percentage = round(self.score / self.questionCount * 100)
            if tkinter.messagebox.askyesno("Incorrect!", f"Incorrect! The correct answer is {self.selectedQuote['author']}.\n Your score is {self.score}/{self.questionCount}. \n You got {percentage}% of the questions correct.\n\n Continue ?"):
                self.loadQuote()
            else:
                self.root.destroy()
            
        
        self.scoreLabel.config(text=f'Score: {self.score}')
        

    def startTimer(self):
        self.timer = 10
        self.timerLabel.config(text=f'Time Left: {self.timer}')
        self.timerId = self.root.after(1000, self.updateTimer)

    def updateTimer(self):
        self.timer -= 1
        if self.timer <=3:
            # change color to red
            self.timerLabel.config(fg='red')
        self.timerLabel.config(text=f'Time Left: {self.timer}')
        if self.timer <= 0:
            self.root.after_cancel(self.timerId)
            self.loadQuote()
        else:
            self.timerId = self.root.after(1000, self.updateTimer)

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()


# testing code

# window = tkinter.Tk()
# window.title("QuoteMaster")
# label = tkinter.Label( text="Who Said...\n")
# label.pack()
# with open('data.txt', 'r') as file:
#     data = json.load(file)
# quote = random.choice(data)
# quote_text = quote['quote']
# quote_author = quote['author']
# quote_year = quote['year']
# quote_label = tkinter.Label(text=quote_text)
# quote_label.pack()
# author_label = tkinter.Label(text=quote_author)
# author_label.pack()
# author_year_label = tkinter.Label(text=quote_year)
# author_year_label.pack()
# answer_label = tkinter.Label(text="Enter the name of the author:")
# answer_label.pack()
# answer_entry = tkinter.Entry()
# answer_entry.pack()

# window.mainloop()