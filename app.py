import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
import pandas as pd

# Load YOLO model
model = YOLO("models/yolov8s.pt")

st.title("📷 Smart Office Object Detection")
st.write("Upload an image, and filter detections by category dynamically.")

uploaded_file = st.file_uploader("Upload an office CCTV image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Run YOLO
    results = model(img)
    boxes = results[0].boxes
    names = model.names

    # ✅ Build list of detected classes dynamically
    detected_classes = sorted(set([names[int(box.cls[0])] for box in boxes]))

    # Add 'All' option at the top
    detected_classes = ["All"] + detected_classes

    #
    selected_class = st.selectbox("🎯 Filter by detected category:", detected_classes)


    filtered_boxes = []
    for box in boxes:
        cls = int(box.cls[0])
        label = names[cls]

        if selected_class == "All" or label == selected_class:
            filtered_boxes.append(box)


    annotated_img = np.array(img.convert("RGB"))

    for box in filtered_boxes:
        cls = int(box.cls[0])
        label = names[cls]
        conf = float(box.conf[0])

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # 🟢 Draw THICK rectangle
        cv2.rectangle(annotated_img, (x1, y1), (x2, y2), (0, 255, 0), thickness=5)

        # Label background
        (text_w, text_h), _ = cv2.getTextSize(f"{label} {conf:.2f}",
                                              cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
        cv2.rectangle(annotated_img, (x1, y1 - text_h - 10),
                      (x1 + text_w + 5, y1), (0, 255, 0), -1)

        # Label text
        cv2.putText(annotated_img, f"{label} {conf:.2f}", (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    # Show annotated image
    st.image(annotated_img, caption="Filtered Detections", use_container_width=True)

    # Count only filtered objects
    class_counts = {}
    for box in filtered_boxes:
        cls = int(box.cls[0])
        label = names[cls]
        class_counts[label] = class_counts.get(label, 0) + 1

    # Show table
    if class_counts:
        df = pd.DataFrame(list(class_counts.items()), columns=["Object", "Count"])
        st.subheader("📊 Detection Summary")
        st.table(df)
    else:
        st.write("No objects detected for the selected category.")
