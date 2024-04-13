import numpy as np
from PIL import Image

import torch
from torchvision import transforms
from torchvision import models


device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

modeldamage = torch.load('ptichka_infobot/recycling.pth',  map_location=torch.device('cpu'))

def defect(img):
    image = Image.open(img)
    trfs = transforms.Compose([transforms.Resize((256, 256)),
                                transforms.ToTensor(),
                                # Use mean and std for pretrained models
                                # https://pytorch.org/docs/stable/torchvision/models.html
                                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                std=[0.229, 0.224, 0.225])])
    modeldamage.to(device)
    modeldamage.eval()
    prediction = modeldamage(torch.unsqueeze(trfs(image),dim=0).to(device))
    pred = prediction.cpu().detach().numpy()
    pred = np.exp(pred) / np.exp(pred).sum()
    lbl = np.argmax(pred)
    return f'Это похоже на {'Пластик' if lbl == 0 else 'Металл'}'
