#p1+p2+p3
class game:
    def __init__(self):
        print('welcom in the full game..^-^')
        print('choose your game from our collection')
        print('press [1]: play even_odd_game')
        print('press [2]: play sum_average_numbers')
        print('press [3]: play multipliction_table_game')
        self.choices()


    def choices(self):
        while True:
            user_choice=input('enter your choice:')
            try:
                user_choice=int(user_choice)
                if user_choice==1 :
                    self.even_odd_game()
                elif user_choice==2:
                    self.sum_average_numbers()
                elif user_choice== 3:
                    self.multipliction_table_game()
                else:
                     print('please choose between 1,2 or 3')
            except ValueError:
                print('please enter a valid number')



    def even_odd_game(self):
        print('welcome in even_odd_game^-^')
        print('if you want end game enter x')
        while True:
            number = input('enter THE number:')
            if number == 'x':
                print('colsing game')
                print('thanks...')
                break
            try:
                number = int(number)
                if number % 2 == 0:
                    print("the number is even")
                else:
                    print('the number is odd')
            except ValueError:
                print('enter a valid number')
            print('------------------------------------------------------------')


    def sum_average_numbers(self):
        print('welcome in sum_average_game ^-^')
        count = int(input('how many number :'))
        current_count = 0
        sum = 0
        while current_count < count:
            number = float(input('enter number:'))
            sum += number
            current_count += 1
        print('sum=', sum)
        print('average=', sum / count)
        print('------------------------------------------------------------')


    def multipliction_table_game(self):
        print('welcome in multipliction_game^-^ ')
        start = int(input('enter the start number:'))
        end = int(input('enter the end number:'))
        for x in range(start, end + 1):
            for y in range(1, 13):
                print(x, '*', y, '=', x * y)
            print('------------------------------------------------------------')

            
game1=game()
