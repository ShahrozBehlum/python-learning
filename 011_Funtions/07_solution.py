def sum_all(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
    # print(args)  #it give tuple
    # return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3))