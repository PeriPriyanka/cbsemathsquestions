import numpy as np
#(CBSE 2007-Question 2)
A1 = np.array([[1, 6], [3, -8]])
B1 = np.array([6,5])
x1 = np.linalg.solve(A1, B1) 
#x1 = [x, 1/y]
print(x1)
#(CBSE 2007-Question 3)
A2 = np.array([[3, 2], [2, 3]])
B2 = np.array([47,53])
x2 = np.linalg.solve(A2, B2) 
print(x2)
#(CBSE 2007-Question 21)
A=np.array([7,10])
A.resize(2,1)
B=np.array([-2,5])
B.resize(2,1)
C=np.array([3,-4])
C.resize(2,1)
#checking the right angle
if ((A-C).T@(B-C)==0):
	print("ABC is a right triangle and right angle at c")
elif ((A-B).T@(C-B)==0):
	print("ABC is a right triangle and right angle at B")
elif ((B-A).T@(C-A)==0):
	print("ABC is a right triangle and right angle at A")
else:
	print("ABC is a not right triangle")
if((A-C).T@(B-C)==(A-B).T@(C-B)):
    print("ABC is a isosceles and AC=AB")
elif((B-A).T@(C-A)==(A-B).T@(C-B)):
    print("ABC is a isosceles and BC=AC")
elif((B-A).T@(C-A)==(A-C).T@(B-C)):
    print("ABC is a isosceles and BC=AB")
else:
    print("ABC is a not isosceles triangle")
#(CBSE 2007-Question 22)
n= np.array([1,-1])
A3= np.array([3,-1])
B3= np.array([8,9])
c=2
k= (c-A3.T@n)/(B3.T@n-c)
print(k)