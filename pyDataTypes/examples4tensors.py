import torch
a = torch.tensor([1,2,3,4])
b = torch.tensor([5,6,7,8])
c = torch.add(a,b)
print(c)

#create 2d tensor
aa = torch.tensor([[1,2,3,4],[2,3,4,5],[1,6,3,8]])

print(aa.shape) #the structure of aa
print(help(torch(mm))) #mm 4 matrix multiplication
torch.mm(a,b.T) #T 4 trancepose
