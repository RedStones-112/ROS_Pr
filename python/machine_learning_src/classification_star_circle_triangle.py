



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import time
import os
import cv2
import tensorflow as tf
import matplotlib.image as mpimg
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import fetch_olivetti_faces
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import accuracy_score
from skimage.transform import resize
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from skimage.color import rgb2gray
from tqdm.notebook import tqdm
from mpl_toolkits.mplot3d import Axes3D
from tensorflow.keras import layers, models
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout

gpus = tf.config.experimental.list_physical_devices('GPU') #with import tensorflow
tf.config.experimental.set_memory_growth(gpus[0], True) # me too

# 1. 데이터셋 만들기
# 2. 데이터셋 나눠서 훈련 및 테스트
# 3. 모델 저장
# 4. 별도 파일에서 모델 불러오기 후 카메라 이미지판별
# 
#

path = "./python/cv_data/figure/train_data" ##
label = os.listdir(path)

seed = 13
tf.random.set_seed(seed)
np.random.seed(seed)

train_df = pd.DataFrame({"file" : os.listdir(path)})
train_df["label"] = train_df["file"].apply(lambda x: x.split(".")[0])##



# test_df = pd.DataFrame({"file":os.listdir(path[:-7 + "test_data"])})
# test_df["label"] = test_df["file"].apply(lambda x: x.split(".")[0])##




train_data, val_data = train_test_split(train_df,
                                        test_size=0.2,
                                        stratify=train_df["label"],
                                        random_state=13)

train_datagen = ImageDataGenerator(
    rotation_range = 90,
    horizontal_flip=True,
    vertical_flip=True,
    preprocessing_function = preprocess_input
)
val_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)


FILES = path
w = 224
h = 224
c = 3
batch_size = 10
train_generator = train_datagen.flow_from_dataframe(
    dataframe = train_data,
    directory = FILES,
    x_col = "file",
    y_col = "label",
    class_mode = "categorical",
    target_size = (w, h),
    batch_size = batch_size,
    seed = 13,
)


val_generator = val_datagen.flow_from_dataframe(
    dataframe = val_data,
    directory = FILES,
    x_col = "file",
    y_col = "label",
    class_mode = "categorical",
    target_size = (w, h),
    batch_size = batch_size,
    seed = 13,
    shuffle=False
)


base_model = VGG16(
    weights = "imagenet",
    input_shape = (w, h, c),
    include_top = False
)

for layers in base_model.layers:
  layers.trainable=False




def vgg16_pretrained():
  model = Sequential([
      base_model,
      GlobalAveragePooling2D(),
      Dense(100, activation="relu"),
      Dropout(0.4),
      Dense(64, activation="relu"),
      Dense(3,activation="softmax")
  ])
  return model

tf.keras.backend.clear_session()


model = vgg16_pretrained()

model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics="accuracy")




reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor="val_accuracy",
    patience=2,
    verbose=1,
    factor=0.5,
    min_lr=0.000000001
)

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor="val_accuracy",
    patience=5,
    verbose=1,
    mode="max"
)


directory = './'
if not os.path.exists(directory):
    os.makedirs(directory)
checkpoint = tf.keras.callbacks.ModelCheckpoint(
    monitor = "val_accuracy",
    filepath = os.path.join(directory, "catdog_vgg16_.{epoch:02d}-{val_accuracy:.6f}.hdf5"),
    verbose = 1,
    save_best_only = True,
    save_weights_only = True
)



history = model.fit(
    train_generator,
    epochs = 10,
    validation_data = val_generator,
    validation_steps = val_data.shape[0] // batch_size,
    steps_per_epoch=train_data.shape[0] // batch_size,
    callbacks = [reduce_lr, early_stopping, checkpoint]
    
)

model.save("SCT_model.h5")

