import numpy as np
n1 =np.array([1,2,3,4,5])
print(n1)

n2 =np.zeros((2,2))
print(n2)
n3 =np.full((2,2),10)
print(n3)


n4=np.arange(10,20)
print(n4)

n5=np.arange(10,100,10)
print(n5)

n6 =np.random.randint(10,100,10)
print(n6)

n7 =np.array([[1,2,3],[4,5,6]])
print(n7.shape)
n7.shape =(3,2)
print(n7)

n8 =np.array([10,20,30])
n9 =np.array([40,50,60])
n10 =np.vstack((n8,n9))
n11 =np.hstack((n8,n9))
n12 = np.column_stack((n8,n9))
print(n10)
print(n11)
print(n12)
n13 = np.intersect1d(n8,n9)
print(n13)
n14 = np.setdiff1d(n9,n8)
print(n14)
n15 = np.sum([n8,n9],axis = 0)  #applied on rows 
print(n15)
n16 = np.sum([n8,n9],axis = 1)  # applied on columns 
print(n16+1)
print(n16-1)
print(n16*2)
print(n16/10)
print(np.std(n16),"std")
print(np.mean(n16),"mean")
print(np.median(n16),"median")
n20 =np.array([10,20,30,40])
np.save('my_num',n20)
print(n20)
n21 = np.load('my_num.npy')
print(n21)
