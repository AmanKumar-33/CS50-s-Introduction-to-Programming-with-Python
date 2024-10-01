import emoji
print(emoji.emojize(':thumbs_up:'))
print(emoji.emojize("Python is fun :smiley_cat:"))

user_answer = input("Input:")
output = emoji.emojize(user_answer,language='alias')
print("output:",output)
