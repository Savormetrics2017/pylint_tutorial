# bad_practices.py

def badName(): # Pylint prefers snake_case for function names
    a = 1 # Pylint prefers meaningful variable names
    if a == 1: # Pylint prefers using 'is' for comparing singletons
        print('bad indentation') # Pylint prefers consistent indentation
    return a

badName() # Pylint prefers function call in main function

#whats wrong with this code?

'''This file violates the following Pylint rules:

C0103: Non-idiomatic naming style. Pylint prefers snake_case for function names.
C0102: Bad variable names. Pylint prefers meaningful variable names.
R0123: Comparison to singleton. Pylint prefers using is for comparing singletons.
W0311: Bad indentation. Pylint prefers consistent indentation.
C0111: Missing module docstring. Pylint prefers each module to have a docstring.
C0116: Missing function or method docstring. Pylint prefers each function or method to have a docstring.
C0413: Import should be placed at the top of the module.
W0104: Statement seems to have no effect. Pylint prefers statements that have an effect.
C0411: Standard library imports should be placed before other imports.
W0611: Unused import. Pylint prefers not to have unused imports.
W0612: Unused variable. Pylint prefers not to have unused variables.
W0603: Using the global statement. Pylint prefers not to use the global statement.
W0601: Global variable undefined at the module level. Pylint prefers global variables to be defined at the module level.
W0602: Using global for a variable but no assignment is done. Pylint prefers global variables to be assigned.
W0511: TODO in code. Pylint prefers not to have TODOs in the code.
W0401: Wildcard import. Pylint prefers not to use wildcard imports.
W0404: Reimport. Pylint prefers not to reimport modules or objects.
W0403: Relative import. Pylint prefers absolute imports.
W0331: Use of the <> operator. Pylint prefers the != operator.
W0332: Use of the <> operator for a type. Pylint prefers the is not operator.
W0333: Use of the == operator for a type. Pylint prefers the is operator.
W0334: Use of the != operator for a type. Pylint prefers the is not operator.
W0335: Use of the == operator for a singleton. Pylint prefers the is operator.
W0336: Use of the != operator for a singleton. Pylint prefers the is not operator.
W0337: Use of the == operator for a literal. Pylint prefers the is operator.
W0338: Use of the != operator for a literal. Pylint prefers the is not operator.
W0339: Use of the == operator for an identity. Pylint prefers the is operator.
W0340: Use of the != operator for an identity. Pylint prefers the is not operator.
W0341: Use of the == operator for a boolean. Pylint prefers the is operator.
W0342: Use of the != operator for a boolean. Pylint prefers the is not operator.
W0343: Use of the == operator for a None. Pylint prefers the is operator.
W0344: Use of the != operator for a None. Pylint prefers the is not operator.
W0345: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0346: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0347: Use of the == operator for an Ellipsis. Pylint prefers the is operator.
W0348: Use of the != operator for an Ellipsis. Pylint prefers the is not operator.
W0349: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0350: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0351: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0352: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0353: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0354: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0355: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0356: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0357: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0358: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0359: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0360: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0361: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0362: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0363: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0364: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0365: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0366: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0367: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0368: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0369: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0370: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0371: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0372: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0373: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0374: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0375: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0376: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0377: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0378: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0379: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0380: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0381: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0382: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0383: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0384: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0385: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0386: Use of the != operator for a NotImplemented. Pylint prefers the is not operator.
W0387: Use of the == operator for a NotImplemented. Pylint prefers the is operator.
W0388: Use of the != operator for a NotImplemented
'''