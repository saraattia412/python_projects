#sum and average any number
print('welcome in sum_average_game ^-^')
count=int(input('how many number :'))
current_count=0
sum=0
while current_count<count :
    number=float(input('enter number:'))
    sum += number
    current_count += 1
print('sum=',sum)
print('average=',sum/count)