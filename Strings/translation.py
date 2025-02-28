    #program to translate the words or vowels and to capitalize

s = "Error 404 page not found"
table = s.maketrans("aeiou","AEIOU","012345678")
s_table = s.translate(table)
print(s)
print(s_table)
