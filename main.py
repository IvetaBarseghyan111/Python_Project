# import re
#
# my_string = "1900"
# result = re.findall(r"1[1-8]\d{2}", my_string) # Regex for correct year check.Should start from 1, then second value
# # should be int between 1 and 8, check of other part is that should be only two int
# print(result)
#
#
# if my_string.isdigit() and len(my_string) < 5 :
#         if my_string[0] == "1" and my_string[1] in "12345678":
#            print(my_string)
#         else:
#             print("Year is not between 12 and 18th century")
# else:
#     print("Not a correct year")


unsorted_string = "fgjfogkfdp"
sorted_string = "".join(sorted(unsorted_string))
print(sorted_string)



