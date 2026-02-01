
person = {
    "Name": "Asta",
    "Age": 19,
    "City": "Pune"
}
person["Email"] = "asta@gmail.com"
print("After adding new element:", person)

# 2) Update an existing element

person["Age"] = 21
print("After updating Age:", person)

# 3) Remove an element

person.pop("City")
print("After removing City:", person)

# 4) Merge two dictionaries
extra_info = {
    "Course": "CSE",
    "Year": "First"
}

merged_dict = person | extra_info 
print("After merging dictionaries:", merged_dict)


