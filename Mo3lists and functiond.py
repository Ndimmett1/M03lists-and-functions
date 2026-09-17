#7.4
things = ["mozzarella", "cinderella", "salmonella"]
things

#7.5
things[1] = things[1].capitalize()
print(things)

#7.6
things[0] = things[0].upper()
print(things)

#7.7
del things[2]
print(things)

#9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

good()

#9.2
def get_odds():
    for num in range(10):
        if num % 2 == 1:
            yield num

count = 0
for odd in get_odds():
    count += 1
    if count == 3:
        print(odd)
        break
