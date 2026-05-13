my_dict = {
    'tuple': (41, 6, 8, None, 'Maksim', False, 0.9),
    'list': [100, 33, 4, 5, None, 'test', True, 5.99, 'last'],
    'dict': {'name': 'Maksim', 'age': 32, 'lastname': 'Skvrtsv', 'work': 'tester', 'phone': 12345},
    'set': {1, 3, 6, 7, None, 'text', False, 2.42, 3, 7}
}

print(my_dict['tuple'][-1])
my_dict['list'].append('последний')
my_dict['list'].pop(1)
# print(my_dict['list'])
my_dict['dict']['i am a tuple'] = 'test'
my_dict['dict'].pop('lastname')
# print(my_dict['dict'])
my_dict['set'].add(1000)
my_dict['set'].remove(False)
# print(my_dict['set'])
print(my_dict.items())
