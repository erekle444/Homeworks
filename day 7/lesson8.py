# total_price = 0
# for i in range (13):
#     age = int(input())
#     if age <12:
#         total_price += 0
#     else:
#         total_price += 25
# print(total_price)
total_price = 0
i = 0
while i <=13:
    age = int(input())
    if age <12:
        total_price += 0
    else:
        total_price += 25
    i += 1
print(total_price)
