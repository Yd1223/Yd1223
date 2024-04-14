num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

print("choose calculation: /n",
     "Add /n", 
     "Subtract /n", 
     "Multiply /n", 
     "Divide /n")

calc = input('Add, Subtract, Multiply and Divide')

if calc == 'Add':
    ans = num1 + num2
    
elif calc == 'Subtract':
    ans = num1 - num2
    
elif calc == 'Multiply':
    ans = num1 * num2
    
elif calc == 'Divide':
    ans = num1 / num2
    
print(ans)
