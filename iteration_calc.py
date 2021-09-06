import main
from main import random_gen
from main import statistics_gen
import random

new_iteration = main.iteration_number


def correct_gen(lst_gen, lst_not_gen):
    if len(lst_not_gen) > 0:
        return False
    else:
        num_rep = lst_gen[0][1]
        print("nr" + str(num_rep))
        for x in lst_gen:
            print (str(x[0]) + " "+str(x[1]))
            if x[1] != num_rep:
                return False

        return True


numbers_gen = []
numbers_not_gen = main.numbers_interval


def add(num):

    for i in range(len(numbers_gen)):
        if numbers_gen[i][0] == num:
            numbers_gen[i][1] = numbers_gen[i][1] + 1
            return 0
    numbers_gen.append([num, 1])
    print(len(numbers_gen))
    numbers_not_gen.remove(num)
    return 0


lst_rand = []


it = 0

while not correct_gen(numbers_gen, numbers_not_gen):
    it += 1
    add(random.randint(0, 50) + 20)

print("-----------------------------------------------------------------------------")
print("Cant iteraciones:" + str(it))
