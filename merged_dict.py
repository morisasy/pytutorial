dict_one = {'ramesh': 700, 'rahul': 500, 'printhi': 600}
dict_two = {'ram': 300, 'rahan': 800}

merged_dict = {}
for i in (dict_one, dict_two):
    for k, v in i.items():
        merged_dict[k]= v
print(merged_dict)

print({k:v for i in (dict_one, dict_two) for k, v in i.items()})
