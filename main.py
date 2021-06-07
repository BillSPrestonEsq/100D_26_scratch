# # # file1 = "file1.txt"
# # # file2 = "file2.txt"
# # # with open(file1) as f:
# # #     file1list = f.read().splitlines()
# # #
# # # with open(file2) as f:
# # #     file2list = f.read().splitlines()
# # #
# # # result = [int(n) for n in file1list if n in file2list]
# # #
# # # # Write your code above 👆
# # #
# # # print(result)
# #
# # sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # # Don't change code above 👆
# #
# # result = {word:len(word) for word in sentence.split()}
# #
# # # Write your code below:
# #
# # print(result)
# #
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
# weather_f = {day:(temp * 9/5 + 32) for (day, temp) in weather_c.items()}
#
# # Write your code 👇 below:
#
# print(weather_f)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row)