# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def yearLeapcheck(yearVar):
    if yearVar % 4 != 0:
        yearType = "common" 
    elif yearVar % 100 != 0:
        yearType = "leap" 
    elif yearVar % 400 != 0:
        yearType = "common" 
    else:
        yearType = "leap" 
    return yearType    



def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #test years    
    daysOutput = 0
    daysOfMonths1 = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfMonths2 = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year1 == year2:
        daysOutput = daysOutput
    else:    
        yearTest = year1 + 1 
        while yearTest < year2:
            if yearLeapcheck(yearTest) == "common":
               addDays = 365
            else:
                addDays = 366
            daysOutput = daysOutput + addDays
            yearTest = yearTest + 1
    #days***********************************************
    if yearLeapcheck(year1) == "common":
        daysofMonths = daysOfMonths1
    else:
        daysofMonths = daysOfMonths2
    if month1 == month2 and year1 == year2:
        daysOutput = day2 - day1
    else:    
        daysOutput =  daysOutput + (daysofMonths[month1-1] - day1)   
        daysOutput = daysOutput + day2
    
    #months********************************************
    if year1 == year2:
        daysOutput = daysOutput
    else:    
        if yearLeapcheck(year1) == "common":
            daysofMonths = daysOfMonths1
        else:
            daysofMonths = daysOfMonths2    
        testMonth = month1 + 1
        while testMonth <= 12:
            daysOutput = daysOutput + daysofMonths[testMonth-1]
            testMonth = testMonth + 1
   
   
    if yearLeapcheck(year2) == "common":
        daysofMonths = daysOfMonths1
    else:
        daysofMonths = daysOfMonths2    
   
    if year1 == year2:
  
        testMonth = month1 + 1
        while testMonth < month2:
            daysOutput = daysOutput + daysofMonths[testMonth-1]
            testMonth = testMonth + 1        
    else:
        testMonth = 1
        while testMonth < month2:
            daysOutput = daysOutput + daysofMonths[testMonth-1]
            testMonth = testMonth + 1 
            
    return daysOutput      
    
    #test       
          

print daysBetweenDates (2012,1,1,2012,1,2)
print daysBetweenDates (2012,1,1,2012,3,1)
print daysBetweenDates (2011,6,30,2012,6,30)
print daysBetweenDates (2011,1,1,2012,8,8)
print daysBetweenDates (1900,1,1,1999,12,31)  
        
        
        
#
## Test routine
#
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

