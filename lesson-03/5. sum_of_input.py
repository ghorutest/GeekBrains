global result, exit_code, exit_request
result = 0
exit_request = False
exit_code = 'quit'

def sum_f(list_to_sum):
    """Returns the sum of the list, if detects 'exit_code' sets 'exit_request' """
    global result, exit_code, exit_request
    for i in range(len(list_to_sum)):
        try:
            if list_to_sum[i] == exit_code: exit_request = True
            result += int(list_to_sum[i])
        except:
            pass
    return result

while not exit_request:
    list_to_sum = input("Введите числа, разделяя пробелом, 'quit' для выхода: ").split()
    print(sum_f(list_to_sum))
