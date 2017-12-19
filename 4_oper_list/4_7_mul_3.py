mul_3_nums = list(range(3, 30, 3))
for mul_3_num in mul_3_nums:
    print(mul_3_num, end='\t')
print()
mul_3_nums = [x for x in range(3, 30) if x % 3 == 0]
for mul_3_num in mul_3_nums:
    print(mul_3_num, end='\t')
