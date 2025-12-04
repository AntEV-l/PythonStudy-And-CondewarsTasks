d = dict.fromkeys(["apple", "orange", "banana"])
d.clear()
d = {"apple": 1, "orange": 2, "banana": 3}
d.copy()
d2 = dict(d)
d.get("apple", False)
d.setdefault("fruit", "some fruit") #{"fruit": some fruit}
print(d)
d.pop("fruit", False) # return key or False

d3 = dict(one = 1, two = 2, three = "3", four = "4")
d4 = {2: "неудовлетворительно", 3: "удовлетворительно", 'four': "хорошо", 5: "отлично"}
d5 = { **d4, **d3 }
print(d5)