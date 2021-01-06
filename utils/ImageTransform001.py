import glob
import os.path as osp
import torch.utils.data as data
from torchvision import models, transforms
from PIL import Image
import sys,os

class ImageTransform():

    def __init__(self, resize, mean, std):
        self.data_transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean,std)])

    def __call__(self, img):
       
        return self.data_transform(img)


class Dataset(data.Dataset):

    def __init__(self, file_list, transform=None, phase='train'):
        self.file_list = file_list  
        self.transform = transform  
        self.phase = phase  

    def __len__(self):
       
        return len(self.file_list)

    def __getitem__(self, index):
        

        img_path = self.file_list[index]
        img = Image.open(img_path) 
        img = img.convert('RGB')

        img_transformed = self.transform(img) 
    
        if "/normal/" in img_path:
            label = 0
        elif "/broken/" in img_path:
            label = 1
        return img_transformed, label

