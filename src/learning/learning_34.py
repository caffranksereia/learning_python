"""
split e join com list e str
split - divide uma string
join une uma string
"""

phrase = "                 Look at this! It's really interesting             "
list_words = phrase.split('!')

for i, phrase in enumerate(list_words):
   list_words[i] = list_words[i].strip()

print(list_words[i])