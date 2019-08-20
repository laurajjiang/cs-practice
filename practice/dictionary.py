def dictionary(words):
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = 0
        dict[word] += 1
    return dict
