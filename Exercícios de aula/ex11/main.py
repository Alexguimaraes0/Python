name = input(("what's your name?:"))
if name == 'leonardo':
    print('what a beautiful name you have!')
else:
    print('you name is boring!')
print(f'Good morning {name}!')

print('=' * 30)

n1 = float(input('Enter the first scholl grade:'))
n2 = float(input('Enter the second scholl grade:'))
m = (n1 + n2) / 2
print(f'your avarage was{m}')   
if m >= 6.0:
    print('your avarage was good! congratulations!')
else:
    print('your avarage was bad! study more!')