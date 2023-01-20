dict_ = {
    3: ["x", "aa"],
    1: ["y", "bb"],
    2: ["x", "dd"],
    4: ["x", "cc"],
    5: ["x", "bb"]
}

# print(dict_.items())

A_sorted = sorted(dict_.items(), key = lambda x: -x[0])
# print(A_sorted)

B_sorted = sorted(dict_.values(), key = lambda x: x[1], reverse=True)
print(f"\n######\n{B_sorted}\n#####\n")

dict_[1], dict_[5] = dict_[5], dict_[1]
B_sorted = sorted(dict_.values(), key = lambda x: x[0], reverse=True)
print(B_sorted)
B_sorted = sorted(B_sorted, key = lambda x: x[1], reverse=True)
print(f"\n######\n{B_sorted}\n#####\n")

C_sorted = sorted(dict_.items(), key = lambda x: x[1][1])
# print(C_sorted)

D_sorted = sorted(dict_.items(), key = lambda x: x[1][0])
# print(D_sorted)