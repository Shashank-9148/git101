#program to match string
import re
text = "python is super easy"
regex = r"python"
match = re.match(regex,text)
print(match)
start,end = match.span()
print(text[match.start():match.end():])


#program to search and match
import re
text = "bengaluru is cool"
regex = r"cool"
match = re.search(regex,text)
print(match)
start,end = match.span()
print(text[match.start():match.end():])



import re
text = "tiptur is famous for copra"
regex = r"copra"
match = re.search(regex,text)
print(match)
print(text[match.start():match.end():])