import streamlit as st
from PIL import Image

# Judul aplikasi
st.title("Rotating Picture App")

# Upload gambar
gupl = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if gupl is not None:
    # Membuka gambar yang diunggah
    img = Image.open(gupl)

    # Menampilkan gambar asli
    st.subheader("Original Image")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Slider untuk menentukan rotasi
    rotation_angle = st.slider("Select Rotation Angle (degrees):", -360, 360, 0)

    # Memutar gambar
    rotated_img = img.rotate(rotation_angle, expand=True)

    # Menampilkan gambar yang telah diputar
    st.subheader("Rotated Image")
    st.image(rotated_img, caption=f"Image rotated by {rotation_angle} degrees", use_column_width=True)

    # Tombol untuk mengunduh gambar yang telah diputar
    img_download = rotated_img.convert("RGB")
    img_bytes = io.BytesIO()
    img_download.save(img_bytes, format="JPEG")
    img_bytes.seek(0)

    st.download_button(
        label="Download Rotated Image",
        data=img_bytes,
        file_name="rotated_image.jpg",
        mime="image/jpeg"
    )
