#match statement

day = 4

match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday") 
    case 6:
        print("saturday")
    case 7:
        print("sunday")


#Defalut value

#use _ in last to behaves as a default value

match day:
    case 6:
        print("Today is saturday")
    case 7:
        print("Today is sunday")
    case _:
        print("Looking forwards to weekend") 


#combine

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends.")    

        