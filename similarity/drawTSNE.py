import cv2
import os
from os.path import isfile, join
import numpy as np
import dlib
from facenet_pytorch import InceptionResnetV1
from PIL import Image
import torchvision.transforms as transforms
from sklearn.manifold import TSNE
import matplotlib
import matplotlib.pyplot as plt 
from tqdm import tqdm
import platform

print(platform.system()) # 플랫폼 확인

# Window
if platform.system() == 'Windows':
    matplotlib.rc('font', family='Malgun Gothic')

to_tensor = transforms.ToTensor()
model = InceptionResnetV1(pretrained='vggface2').eval()

## 임베딩 벡터와 라벨 저장하는 array
features = []
labels = []

input_path = './data'
for person in tqdm(os.listdir(input_path)):

    for root, dirs, files in os.walk(input_path+'/'+person):
        for file_name in files:
            if file_name.split('.')[-1] in ['jpg', 'JPG']:
                img_path = os.path.join(root, file_name)
                img = Image.open(img_path).convert('RGB')
                # print("IMAGE OPENED")
                tensor = to_tensor(img)
                # print("TO TENSOR")
                img_emb = model(tensor.unsqueeze(0))
                features.append(img_emb[0].tolist())
                labels.append(person)

features = np.array(features)


tsne = TSNE(n_components=2).fit_transform(features)


def scale_to_01_range(x):
    # compute the distribution range
    value_range = (np.max(x) - np.min(x))

    # move the distribution so that it starts from zero
    # by extracting the minimal value from all its values
    starts_from_zero = x - np.min(x)

    # make the distribution fit [0; 1] by dividing by its range
    return starts_from_zero / value_range

# extract x and y coordinates representing the positions of the images on T-SNE plot
tx = tsne[:, 0]
ty = tsne[:, 1]

tx = scale_to_01_range(tx)
ty = scale_to_01_range(ty)

# initialize a matplotlib plot
fig = plt.figure()
ax = fig.add_subplot(111)

namelabels = os.listdir('./data')
# for every class, we'll add a scatter plot separately
for label in namelabels:
    # find the samples of the current class in the data
    indices = [i for i, l in enumerate(labels) if l == label]
    print("======>",indices)

    # extract the coordinates of the points of this class only
    current_tx = np.take(tx, indices)
    current_ty = np.take(ty, indices)

    # convert the class color to matplotlib format
    # color = np.array(255, dtype=np.float) / 255

    # add a scatter plot with the corresponding color and label
    ax.scatter(current_tx, current_ty, label=label)

# build a legend using the labels we set previously
ax.legend(loc='best')

# finally, show the plot
plt.show()
