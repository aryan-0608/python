# s1 = {1,3,4,6}
# s2 = {4,5,6,7}
# print(s1.union(s2))  # Union of s1 and s2
# s1.update(s2) 
# print(s1)  # s1 after update with s2

# cities = {"New York", "Los Angeles", "Chicago"}
# cities2 = {"Chicago", "Houston", "Phoenix"}
# cities.intersection(cities2)
# print(cities)

# cities = {"New York", "Los Angeles", "Chicago, Houston"}
# cities2 = {"Chicago", "Houston", "Phoenix, New York"}
# cities.intersection_update(cities2)
# print(cities)

# cities = {"sehore", "mumbai", "bhopal", "indore"}
# cities2 = {"indore", "delhi", "sehore"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"sehore", "mumbai", "bhopal", "indore"}
# cities2 = {"indore", "delhi", "sehore"}
# cities3 = cities.difference(cities2)
# print(cities3)

# cities = {"sehore", "mumbai", "bhopal", "indore"
# cities2 = {"indore", "delhi", "sehore"

# cities = {"sehore", "mumbai", "bhopal", "indore"}
# cities.add("pune")
# print(cities)

# cities = {"janpur", "agra", "delhi"}
# cities.remove("agra")
# print(cities)

# cities = {"janpur", "agra", "delhi"}
# item = cities.pop() 
# print(cities)
# print(item)

# cities ={"janpur", "agra", "delhi"}
# del cities
# print(cities)  # This will raise an error since 'cities' is deleted

info = {"aryan",19,False,3.8, 5.9}
if "aryan" in info:
    print(" aryan is present.")
else:
    print(" aryan is  absent.")