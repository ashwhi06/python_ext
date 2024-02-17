# 1. Write a function flatten_dict() to flatten a nested dictionary by joining the keys with . character.
# >>> flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}) {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
# Hint: You can assume that all dictionary keys will be of type string, and that nested dictionaries will only be nested one layer deep (a dictionary of dictionaries will not have another dictionary nested inside it).
def flatten_dict(d):
    result = dict()
    #loop through input
    for key, value in d.items():
        #check if each value is a dictionary
        if isinstance(value, dict):
            #if it is, call the function again with the value as the argument
            for subkey, subvalue in flatten_dict(value).items():
                #add the key and subkey to the result dictionary
                result[key + "." + subkey] = subvalue
            #else, add the key and value to the result dictionary
        else:
            result[key] = value
    return result

print(f"Flatten Dictionary:" ,flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))
    

# 2. Write a function unflatten_dict() to do reverse of flatten_dict.
# >>> unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}) {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
# Hint: You can assume that the keys for the dictionary will all be of type string, and that you never need to create more than one layer of nested dictionary. 
# It may be helpful to create an empty dictionary as the value for the outer key ('b' in this example), then fill it in iteratively as you find keys that belong to that dictionary.
# def unflatten_dict(d):
#     result = dict()
#     #loop through input
#     for key, value in d.items():
#         #split the key by the. character
#         keys = key.split(".")
#         #create a reference to the current dictionary
#         current_dict = result 
#         #loop through the keys
#         for subkey in keys[:-1]:
#             #if the key doesn't exist in the current dictionary, create it
#             if subkey not in current_dict:
#                 #create a new dictionary
#                 current_dict[subkey] = dict()
#                 #set the current dictionary to the new dictionary
#             current_dict = current_dict[subkey]
#             #if the key exists in the current dictionary, set the current dictionary to the value of the key
#         current_dict[keys[-1]] = value
#         #return the result dictionary
#     return result

# print(f"Unflatten Dictionary:" ,unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))
    
    
def unflatten_dict(d):
    unflatten_dict = dict()
    #loop through input
    for key, value in d.items():
        #split the key by the. character
        split_key = key.split(".")
        #create a reference to the current dictionary
        if len(split_key) > 1:
            #set the current dictionary to the value of the outer key
            outer_key = split_key[0]
            #set the inner key to the value of the inner key
            inner_key = split_key[1]
            #check if the outer key exists in the unflatten dictionary
            if outer_key in unflatten_dict:
                #check if the inner key exists in the current dictionary
                inner_dict = unflatten_dict[outer_key]
                #if it does, set the current dictionary to the value of the inner key
                inner_dict[inner_key] = value
                #else, create a new dictionary and set the current dictionary to the value of the inner key
            else:
                unflatten_dict[outer_key] = {inner_key:value}
        #else, set the current dictionary to the value of the key
        else:
            unflatten_dict[key] = value
    return unflatten_dict
print(f"Unflatten Dictionary:" ,unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))           
                    

# 3. Write a function treemap() to map a function over nested list.
# >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]) [1, 4, [9, 16, [25]]]
# Hint: Using recursion may make this function easier to code. 
# Don't forget to check the type of the element you are iterating over.
def treemap(func, nested_list):
    #if the nested list is a list, call the function again for each item in the list
    if isinstance(nested_list, list):
        #return a list of the results of calling the function again for each item in the list
        return [treemap(func, item) for item in nested_list]
    #else, return the result of calling the function on the nested list
    else:
        return func(nested_list)
    
print(f"TreeMap:", treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))
    
    
    
    
    
   
