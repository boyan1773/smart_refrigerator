import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
import torch.optim as optim

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def main():
    transform = transforms.Compose([
        transforms.Resize((100, 100)),
        transforms.ColorJitter(brightness=(0.2,0.8), contrast=(0.2,0.8), saturation=0.2),
        transforms.ToTensor(),
    ])

    trainset = datasets.ImageFolder(root='./smart_refrigerator/data/Training', transform=transform)
    trainloader = DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

    testset = datasets.ImageFolder(root='./smart_refrigerator/data/Test', transform=transform)
    testloader = DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

    class SimpleCNN(nn.Module):
        def __init__(self):
            super(SimpleCNN, self).__init__()
            self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
            self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
            self.conv3 = nn.Conv2d(64, 128, 3, padding=1)

            self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
            
            self.fc1 = nn.Linear(18432, 256)
            self.fc2 = nn.Linear(256, 128)
            self.fc3 = nn.Linear(128, len(trainset.classes))

            self.dropout = nn.Dropout(0.5)

        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = self.pool(F.relu(self.conv3(x)))
            x = x.view(x.size(0), -1)
            x = torch.flatten(x, 1)
            x = F.relu(self.fc1(x))
            x = self.dropout(x)
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    net = SimpleCNN().to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(net.parameters(), lr=0.001)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)

    for epoch in range(60):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()

            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 2000 == 1999:
                print(f'epoch: {epoch + 1} sample: {i+1} loss: {running_loss / 2000:.3f}')
                running_loss = 0.0

        scheduler.step()
    
    torch.save(net.state_dict(), 'smart_refrigerator/simple_cnn.pth')

    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy : {100 * correct // total}%')

if __name__ == '__main__':
    main()