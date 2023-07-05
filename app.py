import numpy as np
from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from skimage.transform import resize
from io import BytesIO
import cv2
import io
from PIL import Image
import base64

app = Flask(__name__)



# Load the trained TensorFlow model
model = tf.keras.models.load_model('models/RGB-Model')


# Required before prediction
def standardize(img):
    # Standardization of images using adjusted standard deviation

    N = np.shape(img)[0] * np.shape(img)[1]
    s = np.maximum(np.std(img), 1.0 / np.sqrt(N))
    m = np.mean(img)
    img = (img - m) / s
    del m, s, N
    #
    if np.ndim(img) == 2:
        img = np.dstack((img, img, img))

    return img

def convert(img):
    rgb_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    rgb_img[img == 0] = [51,102,204] # Blue
    rgb_img[img == 1] = [220,57,18] # Red
    rgb_img[img == 2] = [255,153,0] # Yellow

  #  rgb_img = cv2.resize(rgb_img, (256,256))

    return  rgb_img

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    model_type = request.form.get('model')
    model_path = f'models/{model_type}-Model'
    model = tf.keras.models.load_model(model_path)

    image_file = request.files['image']
    in_memory_file = io.BytesIO()
    image_file.save(in_memory_file)
    data = np.frombuffer(in_memory_file.getvalue(), dtype=np.uint8)  # change fromstring to frombuffer
    color_image_flag = 1
    img = cv2.imdecode(data, color_image_flag)
    width,height = img.shape[0], img.shape[1]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(256,256), interpolation = cv2.INTER_CUBIC)


    image = standardize(img)
    image_array = np.expand_dims(image, axis=0)  

    prediction = model.predict(image_array)
    output = np.argmax(prediction, axis=3)
    output = np.array(output, dtype='uint8')
    output = np.reshape(output, (256,256))
    output = convert(output)
    output = cv2.resize(output, (height,width), interpolation = cv2.INTER_CUBIC)


    output_image = Image.fromarray(output.astype('uint8'))

    # Save to BytesIO object
    buffered = BytesIO()
    output_image.save(buffered, format="PNG")

    # Base64 encode
    img_str = base64.b64encode(buffered.getvalue())
    img_str = img_str.decode('utf-8')

    # Send it in response
    return jsonify({'output_image': img_str})





if __name__ == "__main__":
    app.run(debug=True)
