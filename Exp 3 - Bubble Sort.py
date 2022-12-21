#Bubble Sort
def bubblesort(array):
  for i in range(len(array)):
    for j in range(0,len(array)-1-1):
      if array[j]>array[j+1]:
        array[j],array[j+1]=array[j+1],array[j]
data=[-1,7,10,0,8,70]
bubblesort(data)
print(data)
