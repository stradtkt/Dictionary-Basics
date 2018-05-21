kevin = {
  "name": "Kevin Stradtman",
  "age": 28,
  "country": "USA",
  "favorite_language": "JavaScript"
}
john = {
  "name": "John Kellington",
  "age":60,
  "country": "USA",
  "favorite_language": "Java"
}
debra = {
  "name": "Debra Kellington",
  "age":60,
  "country": "USA",
  "favorite_language": "Java"
}
def print_keys_values(dictionary):
  for key, value in dictionary.items():
    print(key, ": ", value)


print_keys_values(kevin)
print_keys_values(john)
print_keys_values(debra)