# NOTE to the user: increment the model name on line 98 before each time training so that we have documentation of our success

from keras import layers
from keras import models
from keras import optimizers
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import os

main_folder = './re-classified'

# instantiating covnet
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',
                        input_shape=(1000, 1000, 3)))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

# configuring the model for training
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4, learning_rate=0.0001), metrics=['acc'])

# image preprocessing
train_datagen = ImageDataGenerator()
train_data = train_datagen.flow_from_directory(
    os.path.join(main_folder, 'train'),
    target_size=(1000, 1000),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=2,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix="",
    save_format="jpeg",
    follow_links=False,
    subset=None,
    interpolation="nearest",
)

validation_datagen = ImageDataGenerator()
validation_data = train_datagen.flow_from_directory(
    os.path.join(main_folder, 'validation'),
    target_size=(1000, 1000),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=2,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix="",
    save_format="jpeg",
    follow_links=False,
    subset=None,
    interpolation="nearest",
)

test_datagen = ImageDataGenerator()
test_data = train_datagen.flow_from_directory(
    os.path.join(main_folder, 'test'),
    target_size=(1000, 1000),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=2,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix="",
    save_format="jpeg",
    follow_links=False,
    subset=None,
    interpolation="nearest",
)

callback_list = [
    EarlyStopping(patience=2, monitor='val_loss', mode='auto'),
    ModelCheckpoint(
        filepath='drone_detection.h5'),
    TensorBoard(log_dir='./logs'),
]

history = model.fit(train_data, steps_per_epoch=100,
                    epochs=30, validation_data=validation_data, validation_steps=50, batch_size=20)

model.save('./models/drone_detection_2.h5')

# ================================================================================================================================
# plotting loss and accuracy graphs
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()
