'''this is a code to show bad linting'''

def bad_name(): # Pylint prefers snake_case for function names
    '''this is a badName'''
    a = 1 # Pylint prefers meaningful variable names
    if a == 1: # Pylint prefers using 'is' for comparing singletons
        print('bad indentation') # Pylint prefers consistent indentation
    return a

bad_name() # Pylint prefers function call in main function
