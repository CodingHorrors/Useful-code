mydict = {"a": 1, "b": 4, "c": 2, "d": 3, "e": 6, "f": 5}

dict2 = {"a": 23939, "b": 49392, "c": 38282}

dict3 = {1: "Zeus", 2: "Jeff", 3: "Beter", 4: "Minzie", 5: "Ass"}

sorted_val = sorted(dict3.values(), reverse=True)
sorted_dict = {}

#double for loop: What does it mean???
for value in sorted_val:
    for key, val in dict3.items():
        if value == val:
            sorted_dict.setdefault(key, value)

print(sorted_dict)
