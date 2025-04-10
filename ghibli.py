import streamlit as st
from PIL import Image
import io

# Placeholder for the actual style transfer function
def ghibli_style_transfer(image: Image.Image) -> Image.Image:
    # Dummy transformation: convert to grayscale for demo
    # Replace this with your model/API logic
    return image.convert("L").convert("RGB")

st.title("Ghibli Style Image Maker")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file).convert("RGB")
    st.subheader("Original Image")
    st.image(image, use_column_width=True)

    with st.spinner("Generating Ghibli-style image..."):
        ghibli_image = ghibli_style_transfer(image)

    st.subheader("Ghibli Style Image")
    st.image(ghibli_image, use_column_width=True)

    # Optional: Download button
    img_byte_arr = io.BytesIO()
    ghibli_image.save(img_byte_arr, format='PNG')
    st.download_button(
        label="Download Ghibli Image",
        data=img_byte_arr.getvalue(),
        file_name="ghibli_style.png",
        mime="image/png"
    )
