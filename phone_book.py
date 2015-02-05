
phone_book = {'Clark': {'Name': 'Clark','Number': '555-555-1234'}, 'Barry': {'Name': 'Barry', 'Number': '555-555-1235'}}

print "-"*75
print "1. Look someone up"
print "2. Add new entry"
print "3. Modify entry"
print "4. Remove an entry"
print "5. View directory"
print "-"*75

choice = raw_input("What do you want to do?: ")

if (choice == "1"):
	Who = raw_input("Who do you want to look up?: ")
	print "You wanted to look up:"
	print phone_book[Who]['Name']
	print "Their number is:"
	print phone_book[Who]['Number']

if (choice == "2"):
    print "You've chosen to add an entry..."
    AddUserName = raw_input("What is the name of your new entry?: ")
    AddUserNumber = raw_input("What is the Number of your new entry?: ")
    phone_book.update({AddUserName: {'Name': AddUserName, 'Number': AddUserNumber}})
    print phone_book

if (choice == "3"):
    #print " Which entry do you want to modify?"
    NameModify = raw_input("Who do you wanna modify?: ")
    ChangeWhat = raw_input("Type 1 to change the name or 2 to change the number.: ")

    if (ChangeWhat == "1") :
        print "You've chosen change a name."
        ChangeName = raw_input("What is the new name?:" )
        phone_book[NameModify]['Name'] = ChangeName
        print phone_book
    else:
        print "You've chosen change the number."
        ChangeNum = raw_input("What is the new number?:" )
        phone_book[NameModify]['Number'] = ChangeNum
        print phone_book



