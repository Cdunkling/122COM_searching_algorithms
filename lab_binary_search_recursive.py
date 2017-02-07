#!/usr/bin/python3
import sys

def binary_search( sequence, value ):
    def recurse(first, last):
        mid = int((first + last) / 2 )
        if first > last:
            return False
        elif (sequence[mid] < value):
            return recurse(mid + 1, last)
        elif (sequence[mid] > value):
            return recurse(first, mid - 1)
        else:
            return True 

    return recurse(0, len(sequence)-1)


def binary_search2( sequence, value, low,high ):
            mid = int((low + high) / 2 )
            if low > high:
                return False
            elif (sequence[mid] < value):
                return binary_search2(sequence, value,mid + 1, high)
            elif (sequence[mid] > value):
                return binary_search2(sequence, value,low, mid - 1)
            else:
                return True 



def main():
    errflg = 0
    sequence = [ i for i in range(0,100,3) ]
    testing = [ (96,True), (33,True), (31,False), (76,False) ]

    for value, expected in testing:
        #result = binary_search( sequence, value )
        result = binary_search2( sequence, value ,0,len(sequence))

        print( "%s search for %d test, got %r expected %r" % \
            ("Passed" if result is expected else "Failed", value, result, expected) )

        if result is not expected:
            errflg += 1

    return errflg

if __name__ == '__main__':
    sys.exit( main() )
