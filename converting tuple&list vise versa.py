mytup = (23,56,78,69)

#converting into list

mylist = list(mytup)
print(mytup)
print(mylist)

mylist[1] = 58
mylist.append(60)
mylist += [70,70,50]

mylist.extend([60,70,50])
print(mylist)

for helo in [60,70,59]:
  mylist.append(helo)
  print(mylist)
  
  #converting back to tuple
  
  mytup = tuple(mylist)
  
  print(mytup)