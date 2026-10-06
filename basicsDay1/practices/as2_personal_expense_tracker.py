
def load_expenses(filename):
    expenses = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 2:
                    print("Skipping bad line:", line)  # optional debug
                    continue

                category = parts[0].strip()
                amount = float(parts[1].strip())

                expenses.append((category, amount))

    except FileNotFoundError:
        return []

    return expenses

#add expense 
def  add_expense(filename, category, amount):
    if amount<=0:
        raise ValueError("Amount can't be negative ")
    
    with open(filename, "a") as file: 
        file.write(f'{category},{amount}\n')


def category_totals(expenses):
    totals = {}

    for category, amount in expenses:
        totals[category] = totals.get(category, 0) + amount

    print('\n ----Category Total----')
    print('Category        Total')

    grand_total = 0

    for category, amount in totals.items():
        print(f'{category:<15}:${amount:.2f}')
        grand_total += amount

    print("--------------------")
    print(f'Grand Total     : ${grand_total:.2f}')

    return totals
 

#list comprehension 
# n = [1,2,3]
# result=[]
# for i in n:
#     result.append(i**2)

# print(result)

# n= [1,2,3]
# result=[i**2 for i in n ]
# print(result)

# for c, a in expenses: 
#     if a> limit: 
#         return category, amount 

def  above_threshold(expenses, limit):  #def funName(argument1, argument2 )
    return [  (category,amount) for category,amount in expenses if amount > limit]  


filename = r'dlytica\expenses.txt'  #r'filepath' => raw string 

expenses = load_expenses(filename)    #load data from file 

category_totals(expenses)   #generate report 

limit = 100

print('\nExpenses above $100:')
for category, amount in above_threshold(expenses, limit):
    print(f'{category:<15}: $ {amount:.2f}')


