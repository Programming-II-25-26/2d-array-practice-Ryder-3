# Test Case:
# Input:
# Enter the number of bread types: 3
# Enter the number of days: 4
# Enter sales for bread type 1: 5 7 8 6
# Enter sales for bread type 2: 3 4 2 5
# Enter sales for bread type 3: 9 6 7 8 

# Note that the sales for bread type input comes in as a list of strings. 


# Expected Output:
# Total sales for each bread: [26, 14, 30]
# Average daily sales: [5.66, 5.66, 5.66, 6.33]

# If you feel overwhelmed by the problem, try writing down 1. the information you need, 2. a representation og the 2D array, and
# 3. the steps you need to take to solve the problem. 

def getInput():
    #gets the number of types of bread
    types = input('Enter the number of bread types: ')
    try: int(types)
    except ValueError:
        passable = False
    else:
        passable = True
    
    while not passable:
        types = input('Please enter the number of types of bread: ')
        try: int(types)
        except ValueError:
            passable = False
        else:
            passable = True

    #gets the number of days
    days = input('Enter the number of days: ')
    try: int(days)
    except ValueError:
        passable = False
    else:
        passable = True
    
    while not passable:
        days = input('Please enter the number of days the bakery was open: ')
        try: int(days)
        except ValueError:
            passable = False
        else:
            passable = True
    

    #gets the sales number for the week
    days = int(days)
    types = int(types)
    week = []
    for type_number in range(0, types):
        week.append([])
        for day_number in range(0, days):
            sale = input(f'how much of type {type_number+1} bread did you sell on day {day_number+1}? ')
            try: int(sale)
            except ValueError:
                passable = False
            else:
                passable = True
            
            while not passable:
                sale = input(f'how much of type {type_number+1} bread did you sell on day {day_number+1}? ')
                try: int(sale)
                except ValueError:
                    passable = False
                else:
                        passable = True
            week[type_number].append(int(sale))
    return week







def bakery(full_week):

    #total sales for each type
    total_sales = []
    for i in range(0, len(full_week)):
        total_sales.append(sum(full_week[i]))
    print(f'Total sales for each bread: {total_sales}')

    #average for sales for each day
    daily_sales = []
    for day in range(0, len(full_week[0])):
        day_average = 0
        for type in range(0,3):
            day_average += full_week[type][day]
        day_average = day_average/len(full_week)
        daily_sales.append(round(day_average, 2))
    print(f'Average daily sales: {daily_sales}')
        

    


    
if __name__ == '__main__':
    week = getInput()
    bakery(week)




  
