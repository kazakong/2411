txt =['lambda functions are anonymous funtions.',
      'anonymous functions dont have a name.',
      'functions are objects in Python.']

mark = map(lambda s: (True,s) if 'anonymous' in s else (False,s), txt)




#if any("anonymous" in s for s in txt):
#    print(True)
#else:
#    print(False)

