import torch
a = torch.tensor([1,2,3,4])
b = torch.tensor([5,6,7,8])
c = torch.add(a,b)
#print(c)

#create 2d tensor
aa = torch.tensor([[1,2,3,4],[2,3,4,5]])
bb = torch.tensor([[4,3,2,1],[5,4,3,2]])

print(aa.shape) #the structure of aa
#print(help(torch.mm)) #mm 4 matrix multiplication
print(torch.mm(aa,bb.T)) #T 4 transpose




