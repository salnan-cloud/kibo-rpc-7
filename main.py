# # # String
# # robot_name = "Robot Dary" 

# # # integer
# # age = 2 

# # #float
# # height = 1.86

# # #boolean
# # is_active = True 

# # #NoneType
# # warning = None

# # # print(robot_name)
# # # print("Robot Sok")

# # print("I have a robot named", robot_name, ". It aged",age)


# distance_a = 5.2
# distance_b = 3.9

# var_c = 5**2

# # print("Distance A: ", distance_a + distance_b)
# # print("Distance B:", distance_a - distance_b)
# # print("Distance A:", distance_a / distance_b)
# # print("Distance B: ", distance_a * distance_b)

# #floor the vision is devide that dun get pointer

# # x = 5
# # y = 2
# # z = x or y

# # # Assignment 

# # a = 5
# # a == 5

# # print("a =",a)


# x_min, x_max = 9.8, 11.20
# post_x = 11

# # is_safe = (post_x >= x_min and post_x <= x_max)

# # print("Is that safe?", is_safe)

# # # IF/ELSE
# # if post_x < x_min:
# #     print("Position is below the minimum limit.")
# # elif post_x > x_max:
# #     print("Position is above the maximum limit")
# # else:
# #     print("Position is limit")

# for post_x in [8.5,9.5,10.5,11]:
#     print(post_x)

telementry_line = "Status: OK | ID: 4 | Margin: 3"
fields = telementry_line.split('|')

status = fields[0].split(':')[1]

print(status)