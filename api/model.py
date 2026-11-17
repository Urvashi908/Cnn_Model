
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

    # Step 1: Convert image to RGB
    image = image.convert("RGB")

    # Step 2: Resize image
    image = image.resize(IMG_SIZE)

    # Step 3: Convert image into NumPy array
    image_array = np.array(image, dtype=np.float32)

    # Step 4: Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # Step 5: CNN prediction
    predictions = model.predict(image_array, verbose=0)

    # Step 6: Get scores for all three classes
    scores = predictions[0]

    all_scores = {
        CLASS_NAMES[i]: float(scores[i])
        for i in range(len(CLASS_NAMES))
    }

    # Step 7: Find highest scoring class
    predicted_index = int(np.argmax(scores))

    predicted_class = CLASS_NAMES[predicted_index]

    # Step 8: Get confidence score
    confidence = float(scores[predicted_index])

    # Step 9: Return prediction and all scores
    return {
        "predicted_class": predicted_class,
        "confidence": confidence,
        "all_scores": all_scores
    }
