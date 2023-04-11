dicts = [{1:[1,2,3,4,5], 2:[6,7,8], 3:[1,3,5,7,9]},{1:[2,3,4], 2:[6,7], 3:[1,3,5]}]

result = { k: set(dicts[0][k]).intersection(*(d[k] for d in dicts[1:])) for k in dicts[0].keys() }

print(result)