b = "hello" in "hello world"
print(b)

# However, we need to know exact value with case sensitivity

# regular expression

# joon@helloworld.com

# phone number
# (123)123-1234
# r"(\d\d\d)-\d\d\d-\d\d\d\d"
# r"(\d(3))-\d(3)-\d(4)"

txt = "My phone number is 123-123-1234. please call me to this phone number"

import re

pattern = "number"
matched = re.search(pattern, txt)
print(matched)

print(matched.span())
print(matched.start())
print(matched.end())

matched = re.findall(pattern, txt)
print(matched)
print(len(matched))

for m in re.finditer(pattern, txt):
    print(m.span())

### Identifier ###
# \d = any number ## abc_\d\d -> abc_11
# \D = anything but a number ## \D\D\D -> ABC
# \s = space ## a\sb\sc -> a b c
# \w = any letter ##\w\w\w\w -> abcd
# \W = anything but a letter ## \W\W -> *_

import re

txt = "My phone number is 123-123-1234. please call me to this phone number"

# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', txt)
phone = re.search(r'\d{3}-\d{3}-\d{4}', txt)

print(phone)
print(phone.group())

### Quantifiers ###
# * Asterisk ## Match its preceding element zero or more times.
# + plus ## Match its preceding element one or more times.
# ? Questing Mark ## Match its preceding element zero or one time.
# { n } Curly Braces ## Match its preceding element exactly n times.
# {n , m} Curly Braces ## Match its preceding element from n to m times.

import re

txt = "My phone number is 123-123-1234. please call me to this phone number"

phone = re.search(r'\d{3}-\d*-\d{3,}', txt)

print(phone)
print(phone.group())

# detail with group
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
output = re.search(pattern, txt)

# index starts from 1
print(output.group(1))

# import re
r = re.search(r'cat|dog', 'cats and dogs')
print(r)

r = re.findall(r'.at', 'The person wearing the hat sat in the shade')
print(r)

r = re.findall(r'^\d', '1 person wearing the hat sat in the shade2')
print(r)

r = re.findall(r'[^!.?]+', 'Jesus! Hello World. Typical?')
print(r)

r = re.findall(r'[\w]+-[\w]+', "Here is hypen-string")
print(r)

r = re.findall(r' (cat|sat|hat)', 'person holding a cat sat wearing at hat')
print(r)