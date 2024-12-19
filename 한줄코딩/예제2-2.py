text = '''

Call me Ishmael. Some years ago - never mind how long precisely - having little
or no money in my purse, and nothing particular to interest me on shore, I
thought would sail about a little and see the watery part of the world. It is
a wat I have of driving off the spleen, and regulating the circulation. - Moby
Dick'''

w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

print(w)

h = [[x for x in line.split() if len(x)<=5]for line in text.split('\n')]
print(h)

s = [[x for x in line.split() if len(x)==2]for line in text.split('\n')]
print(s)
