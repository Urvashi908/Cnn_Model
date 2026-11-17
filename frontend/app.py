
import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title="Potato Disease Detection",
    page_icon="🥔"
)

st.title("🥔 Potato Leaf Disease Detection")

st.write(
    "Upload a potato leaf image to detect its disease."
)

uploaded_file = st.file_uploader(
    "Choose a potato leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Potato Leaf",
        use_container_width=True
    )

    if st.button("Predict Disease"):

        with st.spinner("Analyzing image..."):

            try:
                uploaded_file.seek(0)

                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type
                        )
                    }
                )

                response.raise_for_status()

                result = response.json()

                disease = result["predicted_class"]
                confidence = result["confidence"]

                st.success("Prediction Completed!")

                st.subheader("Prediction Result")

                st.write("Disease:", disease)

                st.write(
                    f"Confidence: {confidence * 100:.2f}%"
                )

            except requests.exceptions.RequestException as e:
                st.error(f"Backend connection error: {e}")

            except Exception as e:
                st.error(f"Error: {e}")
