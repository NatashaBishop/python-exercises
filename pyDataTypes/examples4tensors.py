'''
1. Install Python
https://www.python.org/downloads/

2. update pip
python -m pip install --upgrade pip

3. install numpy first
  according to PyTorch official guide recommand that install numpy first.
pip install numpy

4. no cuda PyTorch 0.4.1 
pip install https://download.pytorch.org/whl/cpu/torch-0.4.1-cp37-cp37m-win_amd64.whl

5. Torchvision
pip install https://download.pytorch.org/whl/torchvision-0.1.6-py3-none-any.whl
'''
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




