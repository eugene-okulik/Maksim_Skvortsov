# stroka = "результат операции: 565"
# list_from_stroka = stroka.split()
# print(int(list_from_stroka[-1]) + 10)

stroka = 'результат операции: 514'
new_index = stroka.index(':')
new_result = int(stroka[new_index + 1:])
print(new_result + 10)
