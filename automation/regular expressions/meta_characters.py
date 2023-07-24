"""
LIST_OF_META_CHARACTERS
.        Matches any single character
\        Escapes one of the meta characters to treat it as a regular character
[...]    Matches a single character or a range that is contained within brackets. Order does not matter but without brackets order does matter
+        Matches the preeceding element one or more times
?        Matches the preeceding element zero or one time
*        Matches the preeceding element zero or more times
{m,n}    Matches the preeceding element at least m and not more than n times
^        Matches the beginning of a line or string
$        Matches the end of a line or string
[^...]   Matches a single character or a range that is not contained within the brackets
?:...|..."Or" operator
()       Matches an optional expression
"""

import re

filenames = ['nov-12.txt','november-14.txt','Oct-17.txt','Nov-22.txt']

text = "hi there you here exa_mple@example=com and @blabla and example@example.com some more text here and there another@example.de if another@example.de"

pattern = re.compile("[^ ]+@[^ ]+.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[^ ]+@[^ ]+\.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[another]+@[^ ]+\.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[naother]+@[^ ]+\.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("naother+@[^ ]+\.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[^ ]?@[^ ]+.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[^ ]+@[^ ]+.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[^ ]*@[^ ]+.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[^ ]{3}@[^ ]+.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[^ ]{3,6}@[^ ]+.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("^[^ ]+@[^ ]+.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("$[^ ]+@[^ ]+.[a-z]+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("[^ ]+@[^ ]+\.(?:com|de)+",re.IGNORECASE) 
matches = pattern.findall(text)
print(matches)