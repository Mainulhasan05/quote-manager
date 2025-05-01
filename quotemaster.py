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


class ProgramGUI:

    def __init__(self):
        try: 
            with open('data.txt', 'r') as file:
                self.data = json.load(file)
        except:
            tkinter.messagebox.showerror("Something Went Wrong", "The data file is missing or corrupted.\nPlease contact the administrator.")
            return
        # adding authors to authors list
        self.authors = []
        for quote in self.data:
            if quote['author'] not in self.authors:
                self.authors.append(quote['author'])
        # checking if authors are at least 3
        if len(self.authors) < 3:
            tkinter.messagebox.showerror("Something Went Wrong", "There are not enough authors to play the game.\nPlease contact the administrator.")
            return
        # creating attributes
        self.score = 0
        self.questionCount = 0
        self.root = tkinter.Tk()
        self.root.geometry('500x500')
        self.root.title('QuoteMaster')
        self.root.resizable(False, False)
        self.root.configure(bg='lightblue')
        
        
        
        self.frame = tkinter.Frame(self.root, bg='lightblue')
        self.frame.pack(pady=20)
        self.frame.pack_propagate(0)
        self.frame.config(width=500, height=500)
        
        # take the frame to the center of the screen

        
        # loading the quote
        self.loadQuote()
        self.root.mainloop()



    def loadQuote(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.headingLabel = tkinter.Label(self.frame, text="QuoteMaster",font=('Arial', 20, 'bold'), bg='lightblue')
        self.headingLabel.pack(pady=10)
        #
        # See Point 1 of the "Methods in the GUI Class of quotemaster.py" section of the assignment brief.
        
        self.questionCount += 1 
        self.selectedQuote = random.choice(self.data)
        print("Picked quote:", self.selectedQuote)
        quoteText = self.selectedQuote['quote']
        quoteAuthor = self.selectedQuote['author']
        quoteYear = self.selectedQuote['year']
        # creating a label for the quote
        quoteLabel = tkinter.Label(self.frame, text=f'"{quoteText}"', bg='lightblue', wraplength=400, justify='center', font=('Italic', 16))
        quoteLabel.pack(pady=10)

        tkinter.Label(self.frame, text="Who said this ?", bg='lightblue', wraplength=400, justify='center', font=('Arial', 12)).pack(pady=10)
        # choose 3 random authors from the authors list including the correct author
        randomAuthors = []
        randomAuthors.append(quoteAuthor)
        while len(randomAuthors) < 3:
            randomAuthor = random.choice(self.authors)
            if randomAuthor not in randomAuthors:
                randomAuthors.append(randomAuthor)
        # shuffling the authors list
        random.shuffle(randomAuthors)
        # creating a button for each author
        for author in randomAuthors:
            button = tkinter.Button(self.frame, text=author, bg='lightblue', command=lambda author=author: self.checkAnswer(author))
            button.pack(pady=5)
        # creating a label for the score
        self.scoreLabel = tkinter.Label(self.frame, text=f'Score: {self.score}', bg='lightblue')
        self.scoreLabel.pack(pady=10)
        # creating a label for the question count
        self.questionCountLabel = tkinter.Label(self.frame, text=f'Question: {self.questionCount}', bg='lightblue')
        self.questionCountLabel.pack(pady=10)
        # creating a button to load the next quote
        
        # creating a button to quit the game
        quitButton = tkinter.Button(self.frame, text='Quit', bg='lightblue', command=self.root.quit)
        quitButton.pack(pady=10)
        # creating a label for the author
        # authorLabel = tkinter.Label(self.frame, text=f'Author: {quoteAuthor}', bg='lightblue')
        # authorLabel.pack(pady=10)
        # creating a label for the year
        pass



    def checkAnswer(self, chosenName):
        #
        # See Point 2 of the "Methods in the GUI Class of quotemaster.py" section of the assignment brief.
        # This method should check if the chosen name is the correct author of the quote.
        # If the answer is correct, the score should be increased by 1 and a message box should be displayed
        # saying "Correct!" and the score.
        # If the answer is incorrect, the score should be decreased by 1 and a message box should be displayed

        # saying "Incorrect!" and the score.
        # The question count should be increased by 1.
        # The next quote should be loaded.

        if chosenName == self.selectedQuote['author']:
            self.score += 1
            tkinter.messagebox.showinfo("You are correct!", f"Your score is {self.score}/{self.questionCount}.")
        else:
            # self.score -= 1
            tkinter.messagebox.showerror("Incorrect!", f"Incorrect! Your score is {self.score}/{self.questionCount}.")
        
        self.scoreLabel.config(text=f'Score: {self.score}')
        self.questionCountLabel.config(text=f'Question: {self.questionCount}')
        self.loadQuote()
        pass



# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()


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