from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np


app = FastAPI()

model = tf.keras.models.load_model('model.h5')
labels = {
    0: 'mountain',
    1: 'street',
    2: 'glacier',
    3: 'buildings',
    4: 'sea',
    5: 'forest'
}



@app.post("/predict/")
async def preds(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = tf.image.decode_image(image_bytes, channels=3)
    x = tf.keras.preprocessing.image.img_to_array(image)
    x = tf.image.resize(image, (150, 150))
    x = np.asarray([x])
    preds = model.predict(x)
    image_class = labels[np.argmax(preds)]
    
    return {'Filename' : file.filename, 
            'Class' : image_class}


    