# -*- coding: utf-8 -*-
"""

Entry point for the CNN
   
"""
import tensorflow as tf
from tensorflow import keras
import sklearn.metrics as metrics
import numpy as np
import load_and_preprocessing
from timeit import default_timer as timer
#from tensorflow.compat.v1.keras.backend import set_session

class TimingCallback(keras.callbacks.Callback):
    def __init__(self, logs={}):
        self.logs=[]
    def on_epoch_begin(self, epoch, logs={}):
        self.starttime = timer()
    def on_epoch_end(self, epoch, logs={}):
        self.logs.append(timer()-self.starttime)

#config = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=1,
#                        inter_op_parallelism_threads=1,
#                        allow_soft_placement=True,
#                        device_count = {'CPU' : 1})

#session = tf.compat.v1.Session(config=config)
#set_session(session)

start_time = timer()
(x_train, y_train), (x_test, y_test) = load_and_preprocessing.execute()
print("load and preprocessing time: ", timer()-start_time)

batch_size = 32
num_classes = 5
epochs = 6

# vocab size -> 0,1,2,3,4 = N,A,C,T,G = 5
vocab_size = 5
embedding_dim = 8
maxlen= x_train[0].size

# Convert class vectors to binary class matrices.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# Have it as an array of integers:
y_test1 = np.argmax(y_test,axis=1)
y_train1 = np.argmax(y_train,axis=1)
    
model = keras.models.Sequential()
model.add(keras.layers.Embedding(input_dim=vocab_size, 
                           output_dim=embedding_dim, 
                           input_length=maxlen))
model.add(keras.layers.Conv1D(128, 2, activation='relu',
                     input_shape=x_train.shape[1:]))
model.add(keras.layers.MaxPooling1D(pool_size=2))
model.add(keras.layers.Conv1D(64, 2, activation='relu',
                     input_shape=x_train.shape[1:]))
model.add(keras.layers.MaxPooling1D(pool_size=2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

callbacks = [
    TimingCallback(),        
]

start_time = timer()
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          callbacks=callbacks,
          validation_data=(x_test, y_test),
          shuffle=True)

print("training time: ", timer()-start_time)


y_predicted = model.predict(x_test)
print("Prediction: ", y_predicted)

y_pred_labels = np.argmax(y_predicted, axis=1)

print("Confusion matrix")
confusion_matrix = metrics.confusion_matrix(y_true=y_test1, y_pred=y_pred_labels)
print(confusion_matrix)
target_names = ['Covid', 'Dengue', 'Ebola', 'Mers', 'Sars']
disp = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=target_names)
disp.plot() 

print()
print("Classification report")
report = metrics.classification_report(y_test1, y_pred_labels, target_names=target_names)
print(report)

print()
print("Training time")
print(callbacks[0].logs)
