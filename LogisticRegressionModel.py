import torch
import torch.nn.functional as F

x_data = torch.tensor([[1.0], [2.0], [3.0]])
y_data = torch.tensor([[0], [0], [1]])


class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LogisticRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        return F.sigmoid(self.linear(x))


model = LogisticRegressionModel()
criterion = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
for epoch in range(1000):
    y = model(x_data)
    loss = criterion(y.float(), y_data.float())
    print(epoch, loss)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print('w=', model.linear.weight.item())
print('b=', model.linear.bias.item())
x_test = torch.tensor([4.0])
y_test = model(x_test)
print('y=', y_test)

