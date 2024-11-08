line = str(input())

if line .count(':-)') == 0 or line .count(':-(') == 0:
    print('none')
elif line.count(':-)') == line .count(':-('):
    print('unsure')
elif line.count(':-)') > line .count(':-('):
    print('happy')
else:
    print('sad')
