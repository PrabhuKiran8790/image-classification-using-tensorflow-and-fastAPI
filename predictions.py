import argparse
import tensorflow as tf
import numpy as np
import os

parser = argparse.ArgumentParser(description='Predict the class of an image')

parser.add_argument('i', metavar='image',
                    type=str, 
                    help='Path to the image to predict')


def predict(image):
    getclass = {0: 'mountain',
                1: 'street',
                2: 'glacier',
                3: 'buildings',
                4: 'sea',
                5: 'forest'}
    
    model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'model.h5'))
    img = tf.keras.preprocessing.image.load_img(image, target_size=(150, 150))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.asarray([img])
    preds = model.predict(np.asarray(img))
    return getclass[np.argmax(preds)]  


if __name__ == '__main__':
    args = parser.parse_args()
    image = args.i
    print(predict(image))
