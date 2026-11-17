
import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title="Potato Leaf Health Check",
    page_icon="🥔",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 25px;
}
.result-card {
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #dddddd;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🥔 Potato Leaf Health Check</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered potato leaf disease detection</div>',
    unsafe_allow_html=True
)

st.write("Upload a potato leaf image to check its health.")

uploaded_file = st.file_uploader(
    "Choose a potato leaf image",
    type=["jpg", "jpeg", "png"]
)

# Convert technical class names into user-friendly names
disease_info = {
    "Potato___Early_blight": {
        "name": "Early Blight Detected",
        "emoji": "⚠️",
        "message": "The model detected signs associated with Early Blight.",
        "color": "orange"
    },
    "Potato___Late_blight": {
        "name": "Late Blight Detected",
        "emoji": "🚨",
        "message": "The model detected signs associated with Late Blight.",
        "color": "red"
    },
    "Potato___healthy": {
        "name": "Healthy Potato Leaf",
        "emoji": "🌿",
        "message": "Great! Your potato leaf appears healthy based on the model's prediction.",
        "color": "green"
    }
}

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Your Uploaded Potato Leaf",
        use_container_width=True
    )

    if st.button("🔍 Analyze Leaf", use_container_width=True):

        with st.spinner("AI is analyzing your leaf..."):

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
                    },
                    timeout=60
                )

                response.raise_for_status()
                result = response.json()

                disease = result["predicted_class"]
                confidence = float(result["confidence"])

                # Convert confidence into percentage
                confidence_percent = confidence * 100

                # Get friendly result details
                info = disease_info.get(disease)

                if info is None:
                    st.error("Unknown disease class returned by the model.")
                else:

                    st.divider()

                    st.subheader("📋 Analysis Result")

                    if disease == "Potato___healthy":
                        st.success(
                            f"{info['emoji']} {info['name']}"
                        )
                    elif disease == "Potato___Early_blight":
                        st.warning(
                            f"{info['emoji']} {info['name']}"
                        )
                    else:
                        st.error(
                            f"{info['emoji']} {info['name']}"
                        )

                    st.markdown(
                        f"### {info['message']}"
                    )

                    # Confidence score
                    st.markdown("#### 🎯 Model Confidence")

                    st.progress(
                        max(0.0, min(confidence, 1.0))
                    )

                    st.metric(
                        label="Confidence Score",
                        value=f"{confidence_percent:.2f}%"
                    )

                    st.caption(
                        "Note: Confidence is the model's prediction score, "
                        "not a guarantee of disease diagnosis."
                    )

            except requests.exceptions.RequestException as e:
                st.error(f"Could not connect to the backend: {e}")

            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.divider()

st.caption(
    "Potato Leaf Disease Classifier | Powered by CNN, FastAPI and Streamlit"
)
