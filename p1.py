#even or odd
print('welcome in even_odd_game^-^')
print('if you want end game enter x')
while True:
    number=input('enter THE number:')
    if number=='x' :
        print('colsing game')
        print('thanks...')
        break
    try:
        number=int(number)
        if number%2==0 :
            print("the number is even")
        else:
            print('the number is odd')
    except ValueError:
        print('enter a valid number')
    print('------------------------------------------------------------')