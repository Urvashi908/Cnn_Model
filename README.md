# 🥔 Potato Leaf Disease Classifier

A deep learning-based web application that detects potato leaf diseases using a Convolutional Neural Network (CNN).

Users can upload a potato leaf image and get the predicted disease along with its confidence score. The application uses TensorFlow/Keras for image classification, FastAPI for backend processing, and Streamlit for the frontend interface.

## ✨ Features

- Disease classification into three categories:
  - Early Blight
  - Late Blight
  - Healthy
- CNN-based image classification using TensorFlow/Keras.
- FastAPI backend for model predictions.
- Streamlit frontend for image uploads.
- Displays predicted disease and confidence score.
- Supports JPG, JPEG, and PNG images.

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- FastAPI
- Streamlit
- NumPy
- Pillow (PIL)
- Uvicorn

## 📁 Project Structure

```text
archive/
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── model.py
│
├── frontend/
│   └── app.py
│
├── models/
│   └── potato_cnn_model.keras
│
├── data/
│   ├── Potato___Early_blight/
│   ├── Potato___Late_blight/
│   └── Potato___healthy/
│
├── cnn_code.ipynb
├── classification_report.txt
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Prerequisites

- Python
- pip
- Git

## 🚀 Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd archive
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate the virtual environment:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Usage

The backend and frontend must run in two separate terminals.

### 1. Run the FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Backend URL:

http://127.0.0.1:8000

API Documentation:

http://127.0.0.1:8000/docs

### 2. Run the Streamlit Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

Frontend URL:

http://localhost:8501

## 🖥️ How to Use

1. Open the Streamlit application in your browser.
2. Upload a potato leaf image.
3. Click the **Predict Disease** button.
4. The CNN model analyzes the uploaded image.
5. View the predicted disease and confidence score.

## 🧠 Model Details

| Parameter         | Description                             |
| ----------------- | --------------------------------------- |
| Model Type        | Convolutional Neural Network (CNN)      |
| Framework         | TensorFlow / Keras                      |
| Input Image Size  | 128 × 128                               |
| Number of Classes | 3                                       |
| Model File        | potato_cnn_model.keras                  |
| Output            | Disease prediction and confidence score |

_Note: Update the input image size if your trained model uses a different size._

## 🌿 Disease Categories

1. **Early Blight** – Detects potato leaves affected by early blight.
2. **Late Blight** – Detects potato leaves affected by late blight.
3. **Healthy** – Identifies healthy potato leaves.

## 🔄 Application Workflow

```text
User Uploads Potato Leaf Image
              |
              v
       Streamlit Frontend
              |
              v
        FastAPI Backend
              |
              v
       Image Preprocessing
              |
              v
         CNN Model
              |
              v
      Disease Prediction
              |
              v
       Confidence Score
              |
              v
       Display Result
```

## 📊 Example Prediction

Example API response:

```json
{
  "predicted_class": "Potato___Early_blight",
  "confidence": 0.95
}
```

_The above response is an example. Actual predictions depend on the uploaded image._

## 🔮 Future Improvements

- Improve model accuracy.
- Add more plant disease categories.
- Improve the user interface.
- Deploy the application online.

GitHub: https://github.com/Urvashi908/Cnn_Model

---

⭐ If you find this project useful, consider giving it a star!
