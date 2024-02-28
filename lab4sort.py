
def bubble_sort(list):
	length = len(list) - 1
	sorted = False

	while not sorted:
			sorted = True 
			'''if stops once everything is sorted'''
			for x in range(0, length):
				if list[x] > list[x + 1]:
					sorted = False
					list[x], list[x+1] = list[x+1], list[x]
	return list



print(bubble_sort([5,2,4,3,10,7,1,9,6,8]))
print(bubble_sort(['banana','apple','carrot','cardamon','donut','taco','pasta','mushrooms']))