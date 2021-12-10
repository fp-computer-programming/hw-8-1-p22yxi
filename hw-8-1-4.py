# Yongdong XI

def numberlst(lst0):
    lst1 = lst0.split()
    lst2 = lst0.split()
    del(lst2[-1])
    del(lst2[0])
    a = lst1[0]
    b = lst1[-1]
    want = input('Do you want the middle or ends')
    if want == 'middle':
        print(lst2)
    if want == 'end':
        print(a, b)
    
lst = input('Enter a list of numbers or letters separated by spaces')
numberlst(lst)
