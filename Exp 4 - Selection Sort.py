def selectionSort(l1, length):
    	for i in range(length):
		min = i
		for j in range(i + 1, length):
			if l1[j] < l1[min]:
				min = j
		l1[i], l1[min] = l1[min], l1[i]
l1 = [2, 45, 0, 11, 9,88,97,3,7]
length = len(l1)
selectionSort(l1,length)
print("Sorted:",l1)
