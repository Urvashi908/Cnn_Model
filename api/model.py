
import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "models/potato_cnn_model.keras"

CLASS_NAMES = [
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy"
]

IMG_SIZE = (128, 128)

# Load trained CNN model
model = tf.keras.models.load_model(MODEL_PATH)


def predict_disease(image):
    # Convert image to RGB
    image = image.convert("RGB")

    # Resize image according to model input
    image = image.resize(IMG_SIZE)

    # Convert image into NumPy array
    image_array = np.array(image, dtype=np.float32)

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # CNN prediction
    predictions = model.predict(image_array)

    # Find predicted class
    predicted_index = int(np.argmax(predictions[0]))

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(predictions[0][predicted_index])

    return {
        "predicted_class": predicted_class,
        "confidence": confidence
    }
