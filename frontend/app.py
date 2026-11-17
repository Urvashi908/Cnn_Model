
import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title="Potato Leaf Health Check",
    page_icon="🥔",
    layout="centered"
)

# Page styling
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
</style>
""", unsafe_allow_html=True)

# Page heading
st.markdown(
    '<div class="main-title">🥔 Potato Leaf Health Check</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered potato leaf disease detection</div>',
    unsafe_allow_html=True
)

st.write("Upload a potato leaf image to check its health.")

# Upload image
uploaded_file = st.file_uploader(
    "Choose a potato leaf image",
    type=["jpg", "jpeg", "png"]
)

# Friendly disease names
disease_info = {
    "Potato___Early_blight": {
        "name": "Early Blight Detected",
        "emoji": "⚠️",
        "message": "The model predicted signs associated with Early Blight."
    },
    "Potato___Late_blight": {
        "name": "Late Blight Detected",
        "emoji": "🚨",
        "message": "The model predicted signs associated with Late Blight."
    },
    "Potato___healthy": {
        "name": "Healthy Potato Leaf",
        "emoji": "🌿",
        "message": "The model predicted that this potato leaf is healthy."
    }
}

if uploaded_file is not None:

    # Display uploaded image
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

                # Send image to FastAPI backend
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

                # Get backend response
                result = response.json()

                disease = result["predicted_class"]
                confidence = float(result["confidence"])
                all_scores = result["all_scores"]

                # Display final prediction
                info = disease_info.get(disease)

                st.divider()
                st.subheader("📋 Analysis Result")

                if info is None:
                    st.error("Unknown disease class returned by model.")

                else:

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

                    st.markdown(f"### {info['message']}")

                    # Display confidence
                    st.subheader("🎯 Model Confidence")

                    confidence_percent = confidence * 100

                    st.progress(
                        max(0.0, min(confidence, 1.0))
                    )

                    st.metric(
                        label="Predicted Class Confidence",
                        value=f"{confidence_percent:.2f}%"
                    )

                # Display all three class scores
                st.divider()
                st.subheader("📊 All Disease Prediction Scores")

                for class_name, score in all_scores.items():

                    display_name = disease_info[class_name]["name"]

                    score = float(score)
                    score_percent = score * 100

                    st.write(f"**{display_name}**")

                    st.progress(
                        max(0.0, min(score, 1.0))
                    )

                    st.write(f"Score: {score_percent:.2f}%")

                st.caption(
                    "These are model prediction scores, not guaranteed "
                    "diagnoses or proof of the actual disease."
                )

            except requests.exceptions.RequestException as e:
                st.error(f"Could not connect to backend: {e}")

            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.divider()

st.caption(
    "Potato Leaf Disease Classifier | Powered by CNN, FastAPI and Streamlit"
)
