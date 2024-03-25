import io

from torchvision import transforms
import torch
from PIL import Image


def preprocess_image(image: Image):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img_t = preprocess(image)
    batch_t = torch.unsqueeze(img_t, 0)
    buffer = io.BytesIO()
    torch.save(batch_t, buffer)
    buffer.seek(0)
    return buffer.read()
