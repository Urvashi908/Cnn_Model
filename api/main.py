
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
from io import BytesIO

from api.model import predict_disease

app = FastAPI(title="Potato Leaf Disease Detection API")


@app.get("/")
def home():
    return {
        "message": "Potato Leaf Disease Detection API is running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    try:
        # Read uploaded image
        image_bytes = await file.read()

        # Open image
        image = Image.open(BytesIO(image_bytes))

        # Get prediction from CNN model
        result = predict_disease(image)

        # Return result to frontend
        return result

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction failed: {str(e)}"
        )
