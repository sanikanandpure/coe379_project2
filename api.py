from flask import Flask, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)

model = tf.keras.models.load_model('models/damage.keras')

@app.route('/summary', methods=['GET'])
def model_info():
   return {
      "version": "v1",
      "name": "damage",
      "description": "Classifies images of buildings after a hurricane as being damaged or not",
      "number_of_parameters": model.count_params()
   }


def preprocess_input(im):
   """
   Converts user-provided input into an array that can be used with the model.
   This function could raise an exception.
   """
   # read bytes from image file
   im_bytes = im.read()
   d = tf.io.decode_image(im_bytes, channels=3)

   # resize image, normalize, and add dim for batch_size of 1
   d = tf.image.resize(d, (128, 128))
   d = tf.cast(d, tf.float32) / 255.0 
   d = tf.expand_dims(d, 0)
   return d


@app.route('/inference', methods=['POST'])
def classify_damage_image():
   if 'image' not in request.files:
      return {"error": "user must upload an image"}, 404

   img = request.files['image']
   try: 
   	data = preprocess_input(img)
   except Exception as e:
      return {"error": f"Could not process the `image` field; details: {e}"}, 404
   pred = model.predict(data)
   label = "damage" if pred[0] < 0.5 else "no_damage"

   return { "prediction": label}



# start the development server
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
