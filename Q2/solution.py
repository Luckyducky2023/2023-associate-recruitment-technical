Read data from input file
allValid = true
errorCodes = []
for each record in input file:
    record.isValid =  allValid 
    if record.isValid is not true:
        errorCodes append error message

if allValid is true:
    print "Yes"
    print errorCodes
else:
    print "No"
    print errorCodes sepearated by space character
