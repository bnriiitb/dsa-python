def prob1():
    # 1. Let us say your expense for every month are listed below,
    # 	1. January -  2200
    #  	2. February - 2350
    #     3. March - 2600
    #     4. April - 2130
    #     5. May - 2190
    #
    # Create a list to store these monthly expenses and using that find out,
    #
    #     1. In Feb, how many dollars you spent extra compare to January?
    #     2. Find out your total expense in first quarter (first three months) of the year.
    #     3. Find out if you spent exactly 2000 dollars in any month
    #     4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    #     5. You returned an item that you bought in a month of April and
    #     got a refund of 200$. Make a correction to your monthly expense list
    #     based on this

    expenses = [2200, 2350, 2600, 2600, 2130, 2190]
    print(expenses)
    print(f'1. In Feb, how many dollars you spent extra compare to January? --> {expenses[1]}')
    print(f'2. Find out your total expense in first quarter (first three months) of the year. --> {sum(expenses[:3])}')
    print(f'3. Find out if you spent exactly 2000 dollars in any month --> {2000 in expenses}')
    expenses.append(1980)
    print(
        f'4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list --> {expenses}')
    expenses.insert(3, expenses[3] - 200)
    print(
        f'5. You returned an item that you bought in a month of April and --> {expenses}')


def prob2():
    # You have a list of your favourite marvel super heros.
    # heros=['spider man','thor','hulk','iron man','captain america']
    # Using this find out,
    #
    # 1. Length of the list
    # 2. Add 'black panther' at the end of this list
    # 3. You realize that you need to add 'black panther' after 'hulk',
    #    so remove it from the list first and then add it after 'hulk'
    # 4. Now you don't like thor and hulk because they get angry easily :)
    #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
    #    Do that with one line of code.
    # 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
    heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
    print(f'1. Length of the list --> {len(heros)}')
    heros.append('black panther')
    print(f"2. Add 'black panther' at the end of this list --> {heros}")
    heros.remove('black panther')
    heros.append('hulk')
    heros.append('black panther')
    print(f"3. You realize that you need to add 'black panther' after 'hulk "
          f"so remove it from the list first and then add it after 'hulk' --> {heros}")
    heros.insert(1, 'doctor strange')
    heros.insert(6, 'doctor strange')
    print(f"4. Now you don't like thor and hulk because they get angry easily :) "
          f"So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool)."
          f"Do that with one line of code. --> {heros}")
    print(
        f"5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list) --> {heros.sort()}")


def prob3(max_number):
    # Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
    print([i for i in range(max_number) if i % 2 == 1])


if __name__ == '__main__':
    prob1()
    print("\n")
    prob2()
    max_number = input("Please enter the max number to generate odd numbers in that range \n")
    prob3(int(max_number))
