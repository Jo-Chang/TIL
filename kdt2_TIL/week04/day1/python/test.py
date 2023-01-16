number_list = [1, 2, 3, 4, -5]

# result : 0
result = 0

for number in number_list:

    result = result + number
print(result)


dict_var = {
    5: "hi",
    3: "this is",
    1: "world",
}

print(type(dict_var), dict_var)
print(type(dict_var.items()), dict_var.items())