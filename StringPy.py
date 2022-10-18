
year = input('Type the year: ')
print('You have ' + str((2022 - int(year))) + ' years.')
name = input('Type your name: ')

fullName = (f'The full name is {name}')
print(fullName)
print('Your second name is ' + name[6:13])

print(name.upper())
print(name.replace('Marco','MARCO'))

nam = len(name)
print(f'The name {name} has {str(nam)} caracters')

print (name.casefold())

print(name.endswith('rta')) # Return true or false if the last string is rta

print("First space position is " + str(name.find(" ")))


namesub = name[0 : name.find(' ')]
print(f'Length of namesub is {len(namesub)}')
print (namesub, "The last caracter is", namesub[len(namesub) - 1])

names = f' Carr{namesub[len(namesub) - 1]}'
print (names)

