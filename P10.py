#@author: Christian Bahamon


def main():
    thetext = '''
       \nPython was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.\n    
        '''
    print(thetext)

# ---------------------------------
    len1 = len(thetext)
    print('the number of characters: ',len1)
    print('\n' * 1)
    word1 = thetext.count('the')
    print('the number of times the word "the" is used: ',word1)
    print('\n' * 1)
    word2 = 'little'
    if word2 in thetext:
        print('little is found')
    else:
        print('little is not found')
    print('\n' *1)
    word3 = 'titan'
    if word3 in thetext:
        print('titan was found')
    else:
        print('titan was not found')
    print('\n' * 1)
    char1 = thetext.find('appl')
    print('Position of "appl" is->', char1)
    print('\n' * 2)
    thetext2 = thetext.replace('Python','PYTHON')
    print('new text is->', thetext2)
    print('\n' * 1)
# ---------------------------------
    return
main()
