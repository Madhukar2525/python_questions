# Requirement: Make it able to handle if user enters invalid number.
#              If entered invalid number, it should print "Please enter valid number"

def numTriangle():
    a = input("Enter any number: ")
    for i in range(int(a)+1):
        print(i*str(i))
# numTriangle()



def starPattern():
    b = int(input("Enter any number: "))
    for i in range(b):
        print(i*'*')
# starPattern()
