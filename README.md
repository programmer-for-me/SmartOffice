📷 Smart Office Object Detection Dashboard
A Streamlit web app that uses YOLOv8 to detect people and key office objects from CCTV images.
This project was built for the Smart Office Challenge to demonstrate how AI can monitor office environments.

🚀 Features
✅ Detects people & office objects – supports:

👤 Person

💺 Chair

🖥 Monitor

⌨ Keyboard

💻 Laptop

📱 Phone

✅ Interactive Streamlit dashboard – upload any office CCTV image and get:

📊 Bounding boxes with labels & confidence scores

📋 Object count table

🎯 Category filter (choose which object type to highlight)

✅ Lightweight & fast – uses YOLOv8 pre-trained model for instant detection.

🛠 Tech Stack
YOLOv8 – state-of-the-art object detection model

Streamlit – interactive web app framework

OpenCV – image drawing & annotation

Python 3.10+

📂 Project Structure
bash
Copy
Edit
📦 SmartOfficeYOLO
 ┣ 📂 models
 ┃ ┗ yolov8s.pt              # pre-trained YOLOv8 model
 ┣ 📜 app.py                  # Streamlit dashboard
 ┣ 📜 requirements.txt        # project dependencies
 ┣ 📜 README.md               # documentation
⚙️ Installation & Setup
1️⃣ Clone the repo
bash
Copy
Edit
git clone https://github.com/yourusername/smart-office-yolo.git
cd smart-office-yolo
2️⃣ Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Download YOLOv8 model weights
We used the YOLOv8s (small) model from Ultralytics:

bash
Copy
Edit
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt -P models/
(Or download manually and place yolov8s.pt inside the models/ folder.)

▶️ Running the App
Run the Streamlit app locally:

bash
Copy
Edit
streamlit run app.py
Then open your browser at http://localhost:8501.

🖥 How to Use
1️⃣ Upload an image (e.g., CCTV frame of your office).
2️⃣ The model will detect objects (people, laptops, phones, etc.).
3️⃣ You will see:

✅ Image with bounding boxes

✅ Table showing object counts
4️⃣ Optional: Use the dropdown filter to show only one category (e.g., “Person” only).
