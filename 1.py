list1 = ["Dhurandar", "F1", "Openheimer", "Avatar", "Titanic"]
print ("old list :" , list1)


list1.insert (2,"Avenger") 

list1.append("IronMan")
print ("added list :", list1)


list1.remove("F1")
print("removed list :", list1)

list1.sort()

list1.reverse()
print("sorted and reversed list : " , list1)

list1[4] = "Lucky The Racer"
print("Final list :", list1)