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
    pass



# 
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething(prompt):
    pass



# 
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def saveChanges(dataList):
    pass




# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.




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
        pass


    
    elif choice == 'l':
        # List the current quotes.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "abbreviated" format when listing.
        pass



    elif choice == 's':
        # Search the current quotes.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "abbreviated" format when searching.
        pass



    elif choice == 'v':
        # View a quote.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        # Quotes should be displayed in the "full" format when viewing.
        pass

        

    elif choice == 'd':
        # Delete a quote.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        pass

        

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
