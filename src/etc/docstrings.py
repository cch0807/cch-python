# docstrings


def get_name(first_name, last_name):
    """take first name and last name then return combine two"""
    if first_name == "":
        return "Your first name is missing ..."
    if last_name == "":
        return "Your last name is missing ..."
    return f"{first_name}, {last_name}"


# print(get_name.__doc__)
# print(help(get_name))

# # WARNING ...
# a = """
# Hello World
# """
# print(a)

# - Epytext
"""
This is a javadoc style.

@param param1: this is a first param
@param param2: this is a second param
@return: this is a description of what is returned
@raise keyError: raises an exception
"""

# - reST reStructuredText (reST) from Sphinx
"""
This is a reST style.

:param first_name: this is a first param
:param last_name: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""

# - Google
"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""

# - Numpydoc
"""
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""
