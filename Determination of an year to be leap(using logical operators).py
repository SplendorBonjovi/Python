a = int(input('Enter an year value:'))

if(a%100 !=0 and a%400 == 0) or (a%100 !=0 and a%4 == 0):
    print("Leap")
else:
    print('Not Leap')