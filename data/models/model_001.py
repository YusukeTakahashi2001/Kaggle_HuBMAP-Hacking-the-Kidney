import numpy as np
import pathlib
import torch
import torch.nn as nn
from segmentation_models_pytorch.unet import Unet

ENCODER_NAME = 'se_resnext50_32x4d'

class HuBMAPModel(nn.Module):
    def __init__(self):
        super(HuBMAPModel, self).__init__()
        self.model = Unet(encoder_name = ENCODER_NAME, 
                          encoder_weights = None,
                          classes = 1,
                          activation = None)
        
    def forward(self, images):
        img_masks = self.model(images)
        return img_masks