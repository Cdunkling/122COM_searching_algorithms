#!/usr/bin/python3
import sys

def linear_search( sequence, value ):
    for i in sequence:
        if(i==value):
            return True
    return False



# this function is designed to test that your function produces 
# the correct outputs
def main():
    errflg = 0
    sequence = [ i for i in range(99,-1,-3) ]
    testing = [ (99,True), (33,True), (31,False), (76,False) ]

    for value, expected in testing:
        result = linear_search( sequence, value )

        print( "%s search for %d test, got %r expected %r" % \
            ("Passed" if result is expected else "Failed", value, result, expected) )

        if result is not expected: errflg += 1

    return errflg

if __name__ == '__main__':
    sys.exit( main() )
