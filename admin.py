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



# Add your comments
# 
# 
def inputInt(prompt):
    while True:
        try:
            int_value = int(input(prompt))
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
    year = inputSomething('Enter the year: ')
    data.append({'quote': quote, 'author': author, 'year': year})
    saveChanges(data)
    print('Quote added!', end='\n\n')

def abbreviateQuote(quote):
    # Abbreviate the quote to a maximum of 50 characters.
    if len(quote) > 40:
        return quote[:40] + '...'
    else:
        return quote

def printList(quotes):
    for index, quote in enumerate(quotes):
        print(f'{index}) "{abbreviateQuote(quote['quote'])}" - {quote['author']}, {quote['year']}')
        

def searchQuote(search_term):
    search_results = []
    for index, quote in enumerate(data):
        if search_term.lower() in quote['quote'].lower() or search_term.lower() in quote['author'].lower():
            search_results.append({'index': index,'quote': quote['quote'], 'author': quote['author'], 'year': quote['year']})
    return search_results

def viewQuote(index):
    if index < 0 or index >= len(data):
        print('Invalid index.')
        return
    quote = data[index]
    print(f'"{quote['quote']}"')
    if quote['year'] != 'u':
        print(f" - {quote['author']}, {quote['year']}")
    else:
        print(f" - {quote['author']}")


def deleteQuote(index):
    if index < 0 or index >= len(data):
        print('Invalid index.')
        return
    del data[index]
    saveChanges(data)
    print('Quote deleted.', end='\n\n')
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
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ')
        
    if choice == 'a':
        # Add a new quote.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        addQuote()


    
    elif choice == 'l':
        # List the current quotes.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "abbreviated" format when listing.
        print("List of quotes:")
        printList(data)



    elif choice == 's':
        # Search the current quotes.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "abbreviated" format when searching.
        search_term = inputSomething('Enter a search term: ')
        search_results = searchQuote(search_term)
        if len(search_results) == 0:
            print('No results found.')
            continue
        print("Search results:")
        printList(search_results)



    elif choice == 'v':
        # View a quote.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "full" format when viewing.
        index = inputInt('Quote number to view: ')
        viewQuote(index)

        

    elif choice == 'd':
        # Delete a quote.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        index = inputInt('Quote number to delete: ')
        deleteQuote(index)

        

    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Goodbye!")
        break



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice")
        pass
