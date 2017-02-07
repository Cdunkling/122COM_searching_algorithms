import sys

def duplicates( values ):
    for i in values:
        count=0
        for j in values:
            if(i==j):
                count+=1
        if(count>1):
            return True

    return False

def main():
    # === print user instructions ======
    print( "Enter a series of numbers, one at a time." )

    # === get user input ======
    inputs = []
    for i in range(0,5):
        num=input("")
        inputs.append(num)

    # === confirm to the user what they entered ======
    print( "You entered :", ', '.join( inputs ) )
    if(duplicates(inputs)==True):
        print("There are duplicates")
    else:
        print("There are no duplicates")

if __name__ == '__main__':
    sys.exit(main())
