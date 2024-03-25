import torch

from torchvision import models


def predict_image_labels(image):
    image = torch.load(image)
    model = models.resnet50(pretrained=False)
    model.load_state_dict(torch.load("src/data/resnet50.pth"))
    model.eval()

    with torch.no_grad():
        preds = model(image)

    _, indices = torch.sort(preds, descending=True)
    percentage = torch.nn.functional.softmax(preds, dim=1)[0] * 100

    with open("src/data/imagenet_classes.txt") as f:
        classes = [line.strip() for line in f.readlines()]

    result = []
    for idx in indices[0][:3]:
        print(classes[idx], percentage[idx].item())
        result.append((classes[idx], percentage[idx].item()))
    return result
