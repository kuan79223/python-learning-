#list內部分取值採用[ n:m ]方式，n與m是整數。
# n 代表起始位置，第一個為 0。
# m 代表結束位置，不包含這個位置。
list1=['H','e','l','l','o', 'W','o','r','l','d']
print(list1[2:]) #index2之後包括2
print(list1[:3]) #index3之前不包括3
print(list1[3:5]) #index3,4

citys = ['taipei','tainan','koahsiung']
print(citys[0:2])   #index0,1
print(citys[::2])   #index0,2
print(citys[::-2])  #index-1,-3
print(citys[::-1])  #index-1(包括)之前