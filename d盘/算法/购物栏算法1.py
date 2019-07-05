shopping_cart = []
shopping_goods = [['book', 20], ['cup', 30], ['pen', 38], ["laptop", 4000], ["phone", 3800], ['watch', 2800]]
salary = int(input('Please input your salary:'))
while True:
    for i in shopping_goods:
        print(shopping_goods.index(i),',',i[0],':',i[1])
        print('Please select your goods')
        command = input('Please input the command:')
        for i in shopping_goods:
            if command.isdigit():
                if int(command) == shopping_goods.index(i):
                    print('-------------')
                    if salary-i[1] >= 0:
                        shopping_cart.append(i)
                        salary = salary-i[1]
                        print("your balance is :",salary)
                    else:
                        print("your balacne is low please choose another good")

        if command == 'exit':
            print("your shopping cart is :",shopping_cart)
            print("your balance is :",salary)
            break