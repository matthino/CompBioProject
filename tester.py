#!/usr/bin/python

# Function used for testing code

# pass in an expected and actual value, and test returns the results
def test(expected, actual):
    if(expected == actual):
        return "Test passed."
    else:
        return "Test Failed. \n Expected: %s \n Actual: %s" % (expected, actual)
    
