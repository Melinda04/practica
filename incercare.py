import PrettyTable

PrettyTable = r'C\C:\Users\Paul\Desktop\meli\mate an 2 sem 2\sabo\prettytable'

print(PrettyTable.image_to_string(r'C:\INFO MELINDA\python\10.jpg'))

print('--------------WELCOME TO XYZ Shop--------------\n')
table = PrettyTable(['Item Name', 'Item Price'])
total = 0

while (1):
    name = input('Enter Item name:')

    # 'q' pentru a iesi si a tipari tabelul
    if (name != 'q'):
        price = int(input('Enter the Price:'))

        # preturile se stocheaza in 'total'
        total += price
        table.add_row([name, price])
        continue

    elif (name == 'q'):
        break

table.add_row(['TOTAL', total])
print(table)
print('\nThanks for shopping with us :)')
print('Your total bill amount is ', total, '/-')