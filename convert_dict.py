#Convert English-Chinese dictionary to a English words file

dict_file = "EnglishChinese_Dictionary.txt"
words = []

ec_dict = open(dict_file, "r")
for entry in ec_dict:
    print(entry)
    if "\t" in entry:
        entry = entry.replace("\t", " ")
    print(entry.split(" "))
    words.append(entry.split(" ")[1])
ec_dict.close()


english_words_file = open("english_words.txt", "w")
for word in words:
    english_words_file.write(word + "\n")

english_words_file.close()





