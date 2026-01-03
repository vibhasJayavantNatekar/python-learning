
month_no = 4
month_name = ""
days = ""

match month_no:
    case 1:
       days = 31
    case 2:
        days = 28
    case 3:
       days = 31
    case 4:
        days =30
    case 5:
        days = 31
    case 6:
        days = 30
    case 7:
        days = 31
    case 8:
        days = 31
    case 9:
        days = 30
    case 10:
        days = 31
    case 11:
        days = 30
    case 12:
        days = 31
    
            

match month_no:
    case 1:
        month_name = "January"
    case 2:
        month_name = "February"
    case 3:
        month_name = "March"
    case 4:
        month_name = "April"
    case 5:
        month_name = "May"
    case 6:
        month_name = "June"
    case 7:
        month_name = "July"
    case 8:
        month_name = "August"
    case 9:
        month_name = "September"
    case 10:
        month_name = "October"
    case 11:
        month_name = "November"
    case 12:
        month_name = "December" 
       



print("Number of days in an month ", month_name ,  "is " , days)                            
