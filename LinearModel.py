import torch
x_data = torch.tensor([[1.0], [2.0], [3.0]])
y_data = torch.tensor([[2.0], [4.0], [6.0]])


class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    # 必须要叫forward这个名字。为什么必须要叫forward，因为forward是Module中的函数，
    # 这里也写forward是为了覆盖掉Module中的forward
    def forward(self, x):
        return self.linear(x)


model = LinearModel()

criterion = torch.nn.MSELoss(size_average=True, reduce=True, reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
for epoch in range(1000):
    y = model(x_data)
    loss = criterion(y, y_data)
    print(epoch, loss)
    optimizer.zero_grad() #梯度归零
    loss.backward()
    optimizer.step() #更新


print('w=', model.linear.weight.item())
print('b=', model.linear.bias.item())
x_test = torch.tensor([4.0])
y_test = model(x_test)
print('y=', y_test.data)


