# DESCRIPTION:
# Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

# Examples (input --> output):
# "hello case" --> "HelloCase"
# "camel case word" --> "CamelCaseWord"
# Don't forget to rate this kata! Thanks :)

# SOLUTION:
def camel_case(s):
    s = s.title()
    s = s.replace(' ', '')
    return s
