""" """ """ # you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

arr =[]
def solution(arr):
    # write your code in Python 3.6
    n= int(input("num"))
    for i in range(0,n):
        eles=int(input("write eles"))
        arr.append(eles)

    max_num=max(arr)
    flag=False
    if(max_num <=0):
        print(1)
    else:
        for x in range(1,max_num+1):
            if x not in arr:
                flag=True
                print(x)
                break

    if(flag==False):
        print(max_num+1)
      
    pass """
    def solution(A):
    B = set(sorted(A))
    m = 1
    for x in B:
        if x == m:
            m+=1
    return m
 """

  """