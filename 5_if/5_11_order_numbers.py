# numbers = list(range(1, 10))
# for number in numbers:
#     print(number, end='\t')
# print()
# for number in numbers:
#     if number == 1:
#         print(number, 'st', sep='')
#     elif number == 2:
#         print(number, 'nd', sep='')
#     elif number == 3:
#         print(number, 'rd', sep='')
#     else:
#         print(number, 'th', sep='')

numbers = list(range(1, 10))
for number in numbers:
    print(number, end='\t')
print()
for number in numbers:
    if number == 1:
        suffix = 'st'
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(number, suffix, sep='')
