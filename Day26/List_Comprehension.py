'''List Comprehension'''

number = [1, 2, 3]
new_num = [i+1 for i in number]
print(new_num)

new_list = [ i*2 for i  in range(1,5)]
print(new_list)

names = [ "prakash","Anushka","amit","om"]
new_names= [name.upper() for name in names if len(name)>=5]
print(new_names)