#Creating a Dictionary
dict_name={
    'name':'Himal',
    'age':22,
    'place':{'city':'biratnagar',
             'local':'futsal'}
}
print(dict_name['place']['local'])

# Printing Key, Value, And Key-value
'''
for x in dict_name.keys():
    print(x)

for y in dict_name.values():
    print(y)

for x,y in dict_name.items():
    print(x,y)

'''
'''
#searching For a Key

if 'name' in dict_name.keys():
    print("Key exists")

#searching For the value

for x in dict_name.values():
    if x=='Himal':
        print("Exists")
'''

new_dict=dict(name='Himal', age=22)
print(new_dict)

