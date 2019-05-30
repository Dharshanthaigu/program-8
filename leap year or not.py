def leap_year(year):
  if(year%4==0 or year%400==0 or year%100!=0):
    print('yes')
  else:
    print('no')
  return leap_year
c=int(input())
v=leap_year(c)
print(v)
  
