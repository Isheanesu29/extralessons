

countries = {'Ghana','Zimbabwe','Sweden','Monaco'}
cities = {'Monaco','Stockholm','Harare','London'}

# Union
union = cities.union(countries)
# print(union)                      # it printed out everything 

# Intersection
intersection = cities.intersection(countries)
# print(intersection)

# Differences
defferences = cities.difference(countries)
print(defferences)
