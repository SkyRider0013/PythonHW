# # В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# # Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

class1 = (int(input("введите число учеников в первом классе")) + 1) // 2
class2 = (int(input("введите число учеников во втором классе")) + 1) // 2
class3 = (int(input("введите число учеников в третьем классе")) + 1) // 2

print(class1 + class2 + class3)