
##List comprehension -- divisible  by 3 or not.....

abc = [66,40, 33, 71, 40]
newlist = []

for x in abc :
  if x%3==0:
    newlist.append(x)

print(newlist)


##Square of even numbers in the list


newlist = []
abz = [6,4,3,7,4,9]
for x in abz :
  if x%2==0:
    a=x**2
    newlist.append(a)

print(newlist)





# sum of digits of all even numbers
aby = [2,5,7,9,3,6,7,20]
evensum=0
for x in aby:
   if x%2==0:
       while(x>1):
           t=x%10
           evensum=evensum+t
           x=x//10
print("sum of digits of all even numbers",evensum)


### Removing Duplicate elements
abn = [2,3,6,3,2,8,9]
res=[]
print("Before removing:", abn)
[res.append(x) for x in abn if x not in res]
print("After removing:" ,res)






### DICT using Birth date
roaster = {"Coach": "19.2.25", "player": "52.6.89", "player2" : "18.9.69"}
def birthDate(name):
    if name in (roaster.keys()):
        print(roaster.get(name))
    else:
        print("name not in dictionary")

name = input('enter name')
birthDate(name)


