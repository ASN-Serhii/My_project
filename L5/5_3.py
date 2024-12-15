# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
# - ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# - підсумкова довжина hashtag має бути не більше 140 символів.
# - кожне слово починається з великої літери.
# - якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
#'Python Community' -> #PythonCommunity
#'i like python community!' -> #ILikePythonCommunity
#'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
#1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 And More

#другое исполнение прохода по удалению знаков пунктуации
# while any (char in string.punctuation for char in str) :
#     for char in str :
#         if char in string.punctuation :
#             str = str.replace(char, "", 1)
#             break

import string

str = input("Please input a string: ")
str = "".join(char for char in str if char not in string.punctuation)
str = str.title()
str = "#" + str.replace(" ", "")
if len(str) > 140 :
    str = str[:140]
print(str)



