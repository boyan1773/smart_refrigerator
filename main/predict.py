import torch
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import torchvision.datasets as datasets
import os

path = 'data/Training'
root = os.path.join(os.getcwd(), path)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
trainset = datasets.ImageFolder(root)

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

def ai():
    net = SimpleCNN().to(device)
    net.load_state_dict(torch.load("simple_cnn.pth",weights_only=True))
    net.eval() 

    image_path = 'apple.jpg'

    def predict(image_path):
        image = Image.open(image_path)
        width, height = image.size
        if width > height :
            size = height
        else:
            size = width
        transform = transforms.Compose([
            transforms.CenterCrop(size),
            transforms.Resize((100, 100)),
            transforms.ToTensor(),
            ])
        image = transform(image).unsqueeze(0)
        image = image.to(device)

        with torch.no_grad():
            outputs = net(image)
            _, predicted = torch.max(outputs, 1)

        return predicted.item()

    class_names = trainset.classes
    
    predicted_class_idx = predict(image_path)
    predicted_class_name = class_names[predicted_class_idx]

    print(f'Predicted class: {predicted_class_name}')