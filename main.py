import matplotlib.pyplot as plt

start = False

while start == False:
    try:
        number = int(input("enter a number "))
        start = True
    except:
        print("Please enter a valid number")



number_list = []

number_list.append(number)

while number != 1:
    if number % 2 == 0:
        number = (number // 2)
        number_list.append(number)
    else:
        number = (number * 3 + 1)
        number_list.append(number)


print(len(number_list),number_list)


plt.scatter(range(len(number_list)),number_list)
plt.plot(range(len(number_list)),number_list)
plt.xlabel("Steps before reaching infinite loop")
plt.ylabel('Number')
plt.title("Collatz Conjecture")
plt.show()