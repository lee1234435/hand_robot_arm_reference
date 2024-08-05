import numpy as np
import os
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense, Dropout, BatchNormalization, Bidirectional
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import matplotlib.pyplot as plt
from sklearn.metrics import multilabel_confusion_matrix
from tensorflow.keras.initializers import HeNormal
import cv2
import mediapipe as mp
import time
from tensorflow.keras.models import load_model


os.environ['CUDA_VISIBLE_DEVICES'] = '1'
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

# # Load and prepare data
# actions = [
#     '1',
#     '2',
#     '3',
#     'O',
#     'X'
# ]

# data = np.concatenate([
#     np.load('/home/lee/Desktop/hand/dataset4/seq_1_1721655832.npy'),
#     np.load('/home/lee/Desktop/hand/dataset4/seq_2_1721655832.npy'),
#     np.load('/home/lee/Desktop/hand/dataset4/seq_3_1721655832.npy'),
#     np.load('/home/lee/Desktop/hand/dataset4/seq_O_1721655832.npy'),
#     np.load('/home/lee/Desktop/hand/dataset4/seq_X_1721655832.npy'),
# ], axis=0)

# data.shape
# x_data = data[:, :, :-1]
# labels = data[:, 0, -1]

# y_data = to_categorical(labels, num_classes=len(actions))

# x_data = x_data.astype(np.float32)
# y_data = y_data.astype(np.float32)

# x_train, x_val, y_train, y_val = train_test_split(x_data, y_data, test_size=0.1, random_state=2021)

# # 모델 정의
# model = Sequential([
#     Bidirectional(LSTM(64, activation='relu', return_sequences=True), input_shape=x_train.shape[1:3]),
#     Dropout(0.5),
#     LSTM(64, activation='relu'),
#     Dropout(0.5),
#     Dense(32, activation='relu'),
#     Dropout(0.5),
#     Dense(len(actions), activation='softmax')
# ])

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
# model.summary()

# # 모델 훈련
# history = model.fit(
#     x_train,
#     y_train,
#     validation_data=(x_val, y_val),
#     epochs=350,
#     # batch_size=32,
#     callbacks=[
#         ModelCheckpoint('models/model2_1.5.keras', monitor='val_acc', verbose=1, save_best_only=True, mode='auto'),
#         ReduceLROnPlateau(monitor='val_acc', factor=0.5, patience=20, verbose=1, mode='auto')
#     ]
# )

# 데이터 로드 및 전처리
actions = ['1', '2', '3', 'O', 'X']
seq_length = 30

# 데이터 로드
data = np.concatenate([
    np.load('/home/lee/Desktop/hand/dataset4/seq_1_1721655832.npy'),
    np.load('/home/lee/Desktop/hand/dataset4/seq_2_1721655832.npy'),
    np.load('/home/lee/Desktop/hand/dataset4/seq_3_1721655832.npy'),
    np.load('/home/lee/Desktop/hand/dataset4/seq_O_1721655832.npy'),
    np.load('/home/lee/Desktop/hand/dataset4/seq_X_1721655832.npy'),
], axis=0)

# 데이터와 레이블 분리
x_data = data[:, :, :-1]
labels = data[:, 0, -1]

# 레이블 원-핫 인코딩

y_data = to_categorical(labels, num_classes=len(actions))

# 데이터 타입 변경
x_data = x_data.astype(np.float32)
y_data = y_data.astype(np.float32)

# 데이터 분할
x_train, x_val, y_train, y_val = train_test_split(x_data, y_data, test_size=0.1, random_state=2021)

# 모델 정의
model = Sequential([
    Bidirectional(LSTM(64, activation='relu', return_sequences=True), input_shape=x_train.shape[1:3]),
    Dropout(0.5),
    Bidirectional(GRU(64, activation='relu')),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(len(actions), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.summary()

# 모델 훈련
history = model.fit(
    x_train,
    y_train,
    validation_data=(x_val, y_val),
    epochs=300,
    batch_size=32,
    callbacks=[
        ModelCheckpoint('models/model2_1.6.keras', monitor='val_acc', verbose=1, save_best_only=True, mode='auto'),
        ReduceLROnPlateau(monitor='val_acc', factor=0.5, patience=20, verbose=1, mode='auto')
    ]
)



# Plot training history
fig, loss_ax = plt.subplots(figsize=(16, 10))
acc_ax = loss_ax.twinx()

loss_ax.plot(history.history['loss'], 'y', label='train loss')
loss_ax.plot(history.history['val_loss'], 'r', label='val loss')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
loss_ax.legend(loc='upper left')

acc_ax.plot(history.history['acc'], 'b', label='train acc')
acc_ax.plot(history.history['val_acc'], 'g', label='val acc')
acc_ax.set_ylabel('accuracy')
acc_ax.legend(loc='upper left')

plt.show()

# Evaluate the model
model = load_model('models/model2_1.6.keras')
y_pred = model.predict(x_val)
multilabel_confusion_matrix(np.argmax(y_val, axis=1), np.argmax(y_pred, axis=1))