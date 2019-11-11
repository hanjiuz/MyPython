#Province Capital is a game to guess the capital of the China provinces

#initialize the data
province_capital = {}
province_capital["AnHui"] = "HeFei"
province_capital["BeiJing"] = "BeiJing"
province_capital["HeBei"] = "ShiJiaZhuang"
province_capital["ShanDong"] = "JiNan"
province_capital["ZheJiang"] = "HangZhou"
province_capital["JiangSu"] = "NanJing"
province_capital["JiangXi"] = "NanChang"
province_capital["ShangHai"] = "ShangHai"
province_capital["HuNan"] = "ChangSha"
province_capital["HuBei"] = "WuHan"
province_capital["SiChuan"] = "ChengDu"
province_capital["HeNan"] = "ZhengZhou"

provinces = list(province_capital.keys())

import random

score = 0

#using for loop
#for number in [1,2,3,4,5]:
#   question = random.choice(provinces)
#   answer = input("What's the captial for the Province " + question + "? ")
#   if answer == province_capital[question]:
#       score = score + 1
#       print("Congratulations, your answer is correct!")
#   else:
#       print("Unfortunately, your answer is incorrect, the captital for province " + question + " is: " + province_capital[question]) 

#using while loop
while True:
   question = random.choice(provinces)
   answer = input("What's the captial for the Province " + question + "? ")
   if answer == "quit":
       break
   elif answer == province_capital[question]:
       score = score + 1
       print("Congratulations, your answer is correct!")
   else:
       print("Unfortunately, your answer is incorrect, the captital for province " + question + " is: " + province_capital[question]) 


print("All done! You got score " + str(score) + " of all 5.")
