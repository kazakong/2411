emotion = str(input())

if happy < 1 and sad < 1:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')

