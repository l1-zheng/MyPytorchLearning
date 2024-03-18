import torch
import numpy as np

XY = np.loadtxt('diabetes.csv.gz', delimiter=',', dtype=np.float32)
x_data = torch.from_numpy(XY[:, :-1])
y_data = torch.from_numpy(XY[:, [-1]])


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3  =torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x


model = Model()
criterion = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
for epoch in range(1000):
    y = model(x_data)
    loss = criterion(y, y_data)
    print(epoch, loss)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print('w1=', model.linear1.weight)
print('w2=', model.linear2.weight)
print('w3=', model.linear3.weight)
print('b1=', model.linear1.bias)
print('b2=', model.linear2.bias)
print('b3=', model.linear3.bias)
x_test = torch.tensor([0.99, 0.71, 0.56, 0.85, 0.98, 0.34, 0.54, 0.87])
y_test = model(x_test)
print('y=', y_test)


