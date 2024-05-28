# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Task {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def max_min_index(list_test):
    '1. Нахождение индексов максимального и минимального элемента массива'
    max_i = list_test[0]
    min_i = list_test[0]
    max_index = list_test.index(max_i)
    min_index = list_test.index(min_i)
    for i in list_test:
        if i > max_i:
            max_i = i
            max_index = list_test.index(i)
        if i < min_i:
            min_i = i
            min_index = list_test.index(i)

    return list_test, max_index, min_index

def list_reverce(list_test):
    '2. Задание на «разворот» массива. Нужно перевернуть массив и записать его в обратном порядке.'
    new_list = []
    for i in reversed(list_test):
        new_list.append(i)


    return print(list_test, new_list )

def sum_delts_min_max(list_test):
    """3. **Задача повышенной сложности. Найти сумму элементов массива, лежащих между максимальным
    и минимальным по значению элементами"""
    max_ind = max_min_index(l_test)[1]
    min_ind = max_min_index(l_test)[2]
    result_sum = 0
    if max_ind > min_ind:
        for i in range(min_ind, max_ind + 1):
            result_sum = result_sum + l_test[i]
    else:
        for i in range(max_ind,min_ind + 1):
            result_sum = result_sum + l_test[i]

    return result_sum

def mean_of_list(list_test):
    """4. Найти среднее арифметическое среди всех элементов массива"""
    res_sum = 0
    for i in list_test:
        res_sum = res_sum + i
    mean = res_sum / (len(list_test))
    return mean


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('1. Нахождение индексов максимального и минимального элемента массива')
    l_test = [1,13,4,16,8]
    
    print(max_min_index(l_test))
    print_hi('2. Задание на «разворот» массива. Нужно перевернуть массив и записать его в обратном порядке')
    list_reverce(l_test)
    print_hi('3-Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами-')
    print(sum_delts_min_max(l_test))
    print_hi('4. *Найти среднее арифметическое среди всех элементов массива.')
    print(mean_of_list(l_test))




