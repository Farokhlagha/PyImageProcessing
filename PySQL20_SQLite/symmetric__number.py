# Write a program to check if an array is symmetrical. 
# For example [1, 4, 3, 4, 1] is symmetrical. But not [1, 2, 3].

array=[]

while True:
    data=input("enter array or type end:")
    if data=="end":
        break
    else:
        array.append(data)
        
    print("input array=", array)
    n=len(array)

    for data in range(n//2):
        if array[data] != array[n-data-1]:
          print("the array is not symmetric") 
          break 

    else:
        print("the array is symmetric")
    