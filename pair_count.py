def pair_count(num_list):
  count=0
  for i in range(0,len(num_list)-1):
    if num_list[i]+1==num_list[i+1]:
      count=count+1
  return count
list1=[1,2,5,7,9,0]
print(pair_count(list1))
