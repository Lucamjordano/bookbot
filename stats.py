def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    split_words = file_contents.split()
    count_words = 0
    for word in split_words:
        count_words += 1
    print(f"Found {count_words} total words")
def sort_on(item):
    return item["num"]
def char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        lowercase_contents = file_contents.lower()
        char_list = []
        for char in lowercase_contents:
            if char not in char_list and char.isalpha():
                char_list.append(char)
            else:
                continue
        #print(char_list)
        char_dic_list = []
        for char in char_list:
            char_dic_list.append({"char": char , "num": lowercase_contents.count(char)})
        char_dic_list.sort(key=sort_on, reverse=True)
        for dic in char_dic_list:
            print(dic["char"] + ": " + str(dic["num"]))
