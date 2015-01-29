
print "Get crazy! Pick a number between 1 and 2 and I will tell you what you picked!"

number = raw_input("What is your number?: ")
x = int(number)

# ABove was recast number cast as raw input to int 
#a = 2

if x == 1:
	print " You chose 1 . "  
# you can run above sans the other conditions 
elif x == 2:
	print " You chose 2 . "  

else: 
	print " You chose the wrong number. " 
