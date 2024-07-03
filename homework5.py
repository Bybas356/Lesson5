immutable_war = (0, 2, 'Бубас', False)
print('Immutable tuple:', immutable_war)
#immutable_war[1] = 'Кукусик'
#print(immutable_war) - так как переменной immutable_war присвоен кортеж - неизменяемый объект
#print(type(immutable_war)) <class 'tuple'>
mutable_list = [0, 2, 'Бубас', True]
print('Mutable list:', mutable_list)
mutable_list[0] = 'Пупырка'
print('Mutable list modified:', mutable_list)
mutable_list.append(False)
print('Mutable list modified:', mutable_list)
mutable_list.extend('apple')
print('Mutable list modified:', mutable_list)
mutable_list.remove('a')
print('Mutable list modified:', mutable_list)