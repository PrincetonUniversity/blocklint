# check directly before and after ignored docstrings

# blocked word in a comment whitelist
"""single line docstring blacklist that is ignored"""      # blocklint: pragma
# blocked word on first line master


# blocked word slave before a multiline ignored docstring
""" a test multi line docstring
what happens if I put
things before and
after it
"""  #    blocklint:      pragma
# blocked word in a comment blacklist

"""
A weird example of a docstring
within a docstring
''' a docstring here
here in the middle of
another blacklist docstring
'''
Who would
even do this?
"""  # blocklint: I don't even own a cat pragma

'''
Nobody would ever do this
"""
but if they did
it would be a
masterful
piece of work
"""  # blocklint: pragma
and it would still be
properly caught
whitelisted
blaarg
'''
