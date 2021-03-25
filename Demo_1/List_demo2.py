# Add List Items

Days = ["momday","tuesday","wednesday","thursday","friday"]
Months = ["january","february","march","april","may","june"]
Colors = ("red","blue","orange","pink","purple")

Days.append("sunday")
Months.insert(1, "july")


# Range of indexes or Slicing
print(Days[1:4])

Days.extend(Months)

print(Days)

Days.extend(Colors)

print(Days)


