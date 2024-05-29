def print_hi(name):
    print(f'Task {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def mean_list(list_test):
    '1. Нахождение индексов максимального и минимального элемента массива'
    size = len(list_test)
    sum = 0
    avg = 0
    index = 0

    while index < size:
        sum = sum + list_test[index]
        index += 1
    avg = sum / size

    return print(avg)

if __name__ == '__main__':

    print_hi('1. Среднее арифметич элементов массива')
    list_test = [2,5,13,7,6,4]
    mean_list(list_test)






