# import json
#
# json_file = "index.json"
#
# family = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#         },
#         {
#             "firstName": "Bob",
#             "age": 8
#         }
#     ]
# }
# print(family["children"])
#
# family['children'][0]["favorite_color"] = "yellow",
# family['children'][1]["favorite_color"] = "red",
# json_family = json.dumps(family)
# print(family["children"])
#
# print(json_family)
#
# with open(json_file, 'w') as file_obj:
#     json.dump(family, file_obj, indent = 2, sort_keys=False)
# import json
#
# json_file = 'index.json'
# with open(json_file, 'r') as file_obj:
#      family = json.load(file_obj)
#
# print(family)
# try:
#     f = open("Exercises.py", "a+")
#     f.write("\n this is a new line")
# finally:
#     f.close()

# with open("Exercises.py", "a+") as f:
#     f.write("\n Je suis un grand developper")


p = "the"
n = "man"
print(n,p)