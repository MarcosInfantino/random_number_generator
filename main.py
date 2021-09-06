import random

cota_inf_intervalo = 20
cota_sup_intervalo = 70

numbers_interval = []
for i in range(cota_sup_intervalo - cota_inf_intervalo + 1):
    num = cota_inf_intervalo + i
    numbers_interval.append(num)

iteration_number = 1000


def random_gen(it):
    lst = []
    for i in range(it + 1):
        lst.append(random.randint(0, 50) + 20)
    return lst


random_numbers = random_gen(iteration_number)


print("-------------------------------------------------------")
numbers_gen = []
numbers_not_gen = []


def statistics_gen(numb_lst, rand_lst):
    for n in numb_lst:
        if n in rand_lst:
            numbers_gen.append((n, rand_lst.count(n)))
        else:

            numbers_not_gen.append(n)


statistics_gen(numbers_interval, random_numbers)


def statistics_show():
    print(
        "-------------------------------------------------------NUMEROS GENERADOS---------------------------------------------------------------")
    for (x, y) in numbers_gen:
        print("Numero: " + str(x) + ". Cantidad de veces generado: " + str(y))

    print(
        "-------------------------------------------------------NUMEROS NO GENERADOS---------------------------------------------------------------")
    for n in numbers_not_gen:
        print(str(n))


statistics_show()
