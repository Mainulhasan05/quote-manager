# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "admin.py" program of Project
# of CSI6208 in Semester 1, 2025.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to "do nothing".
# It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.
# Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json
import textwrap
import random



# Add your comments
# 
# 
def inputInt(prompt):
    while True:
        try:
            int_value = int(input(prompt))
            if int_value <= 0:
                print('input must be greater than 0.')
                continue
            return int_value
        except:
            pass



# 
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething(prompt):
    while True:
        something = input(prompt)
        if something.strip() != "":
            return something



# 
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def saveChanges(dataList):
    with open('data.txt', 'w') as file:
        json.dump(dataList, file, indent=4)


# self define functions
def addQuote():
    quote = inputSomething('Enter the quote: ')
    author = inputSomething("Enter the author's name: ")
    year = inputSomething('Enter the year (enter "u" if unknown): ')
    data.append({'quote': quote, 'author': author, 'year': year})
    saveChanges(data)
    print('Quote added!', end='\n\n')

def abbreviateQuote(quote):
    # Abbreviate the quote to a maximum of 40 characters.
    return textwrap.shorten(quote, width=40, placeholder='...') 

def printList(quotes):
    for index, quote in enumerate(quotes):
        print(f'{index+1}) "{abbreviateQuote(quote["quote"])}" - {formatAuthor(quote)}')




def searchQuote(search_term):
    search_results = []
    for index, quote in enumerate(data):
        if search_term.lower() in quote['quote'].lower() or search_term.lower() in quote['author'].lower():
            search_results.append({'index': index,'quote': quote['quote'], 'author': quote['author'], 'year': quote['year']})
    if len(search_results) == 0:
        print('No results found.')
        return
    print("Search results:")
    for index, quote in enumerate(search_results):
        print(f'{quote["index"]+1}) "{abbreviateQuote(quote["quote"])}" - {formatAuthor(quote)}')

def viewQuote(index):
    if index < 0:
        print('Invalid index number.')
        return
    if index >= len(data):
        print('Does not exist.')
        return
    if len(data) == 0:
        print("No quotes saved")
    quote = data[index]
    print(f'"{quote['quote']}"')
    print(f' - {formatAuthor(quote)}')
    print('')


def deleteQuote(index):
    if index < 0 or index >= len(data):
        print('Invalid index number.')
        return
    if len(data) == 0:
        print("No quotes saved")
    del data[index]
    saveChanges(data)
    print('Quote deleted.', end='\n\n')

def formatAuthor(quote):
    if quote['year'] != 'u':
        return f"{quote['author']}, {quote['year']}"
    else:
        return quote['author']

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

# Reading the file
try:
    with open('data.txt', 'r') as file:
        data = json.load(file)
except:
    data = []


# 
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the QuoteMaster Admin Program.')

while True:
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [r]amdom, [i]nsert, [d]elete or [q]uit.')
    choice = input('> ')
        
    if choice == 'a':
        # Add a new quote.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        addQuote()


    
    elif choice == 'l':
        # List the current quotes.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "abbreviated" format when listing.
        if len(data) == 0:
            print('There are no quotes saved. ',end='\n\n')
            continue
        print("List of quotes:")
        printList(data)



    elif choice == 's':
        # Search the current quotes.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "abbreviated" format when searching.
        search_term = inputSomething('Enter a search term: ')
        searchQuote(search_term)
        

    elif choice == 'v':
        # View a quote.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "full" format when viewing.
        index = inputInt('Quote number to view: ')
        viewQuote(index-1)

        

    elif choice == 'd':
        # Delete a quote.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        index = inputInt('Quote number to delete: ')
        deleteQuote(index-1)

        

    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Goodbye!")
        break
    elif choice == 'r':
        # Random a quote.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        
        random_index = random.randint(0, len(data)-1)
        viewQuote(random_index)
    elif choice == 'i':
        # Insert a quote.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        try:
            quote_details = inputSomething('Enter the quote details in the format of: ("Brevity is the soul of wit." - William Shakespeare, 1602): ')
            quote =  quote_details.split('"')[1]
            print("quote", quote)
            total_possible_author = len(quote_details.split('-')[1].split(',')[0].strip())
            print("total_possible_author", total_possible_author)
            print(quote_details.split('-')[1].split(',')[0].strip())
            author = quote_details.split('-')[1].split(',')[total_possible_author-1].strip()
            print("author", author)
            year = quote_details.split(',')[1].strip()
            print("year", year)
        except:
            print("Invalid format")
            continue



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice")
        pass
