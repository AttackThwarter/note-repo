# class Point:
#     pass

# p1 = Point()

# #  اضافه کردن صفت  (attrebute)
# p1.x = 3
# p1.y = 5

# print(p1.x)
# print(p1.y)
########################################################

# class Point:
#     #  اضافه کردن رفتار (method)
#     def restart(self):
#         self.x = 0
#         self.y = 0

# p1 = Point()

# #  اضافه کردن صفت  (attrebute)
# p1.x = 3
# p1.y = 5

# print("x : ",p1.x)
# print("y : ",p1.y)

# p1.restart()
# # or
# # Point.restart(p1)

# print("x : ",p1.x)
# print("y : ",p1.y)
#############################################################

# # __new__ --> Create object (ساخت شی)
# # __init__ -->initialize object (مقداردهی شی)

# class Point:
#     # method
#     # atribute --> defult / non defult
    
#     #                   نوع مقدار خروجی      نوع پارامتر ورودی
#     def __init__ (self , x:float , y:float ) -> None:
#         self.x = x
#         self.y = y
#         # atribute -> non defult |^|

# p1 = Point(10,12)

# print("x : ",p1.x)
# print("y : ",p1.y)
##########################################

# # __new__ --> Create object (ساخت شی)
# # __init__ -->initialize object (مقداردهی شی)

# class Point:
#     # method
#     # atribute --> defult / non defult
    
#     #                   نوع مقدار خروجی      نوع پارامتر ورودی
#     def __init__ (self , x:float = 0 , y:float = 0 ) -> None:
#         self.x = x
#         self.y = y
#         # atribute -> defult |^|

# p1 = Point()

# print("x : ",p1.x)
# print("y : ",p1.y)
#######################################

# __new__ --> Create object (ساخت شی)
# __init__ -->initialize object (مقداردهی شی)

class Point:
    # method
    # atribute --> defult / non defult
    
    #                   نوع مقدار خروجی      نوع پارامتر ورودی
    def __init__ (self , x:float = 0 , y:float = 0 ) -> None:
        self.move(x,y)
        # atribute -> method |^|

    def move(self, x:float ,y:float) -> None:
        self.x = x
        self.y = y

p1 = Point()

print("x : ",p1.x)
print("y : ",p1.y)