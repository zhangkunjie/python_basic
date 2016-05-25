
# coding=utf-8
"""
for iterating_var in sequence:
   statements(s)
"""
#求和
i=0
sum=0
for i in range(0,11): 
  sum+=i
print(sum) 
#字符串遍历
for letter in 'Python':     # First Example
   print ('Current Letter :', letter)
#list遍历   
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        
   print ('Current fruit :', fruit)
#通过索引遍历
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])
print ("Good bye!")