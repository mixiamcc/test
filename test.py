import os

n = 0
line = list()
with open('log_files/201811113016.log',encoding='utf-8') as dir_list:
  for line in dir_list:
    line = dir_list.readline()
    number = line[14:26]
    if  number == '201811113016':
      n=n+1
print(n)   
dir_list.close()








