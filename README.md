# 💰 Insurance Charges Prediction App

An interactive **Streamlit web application** that predicts **medical insurance charges** based on user inputs such as **age**, **BMI**, and **smoking habits**.  
Built using a regression model trained on the [Kaggle Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance).

---

## 🚀 Features

- 🧠 Predicts insurance charges using a trained ML model  
- 🎛️ Intuitive sidebar with sliders and radio buttons  
- 📊 Interactive visualizations (Plotly)  
- 💎 Beautiful gradient UI with smooth animations  
- 🧾 Responsive layout and modern design  
- ⚙️ Easy to deploy on Streamlit Cloud or locally  

---

## 🧮 Model Details

The model is trained using the following features:

| Feature | Description |
|----------|--------------|
| `age` | Age of the insured person |
| `bmi` | Body Mass Index (health indicator) |
| `smoker_yes` | 1 if smoker, 0 if not |
| `charges` | Target variable (medical cost billed by insurance) |

**Input:** `age`, `bmi`, `smoker_yes`  
**Output:** Predicted `charges`

---

## 🏗️ Tech Stack

- **Python 3.10+**
- **Streamlit** – for interactive web UI  
- **Plotly** – for dynamic charts  
- **Scikit-learn** – for ML model  
- **Joblib** – for model persistence  
- **Pandas / NumPy** – for data manipulation  

---

## 📂 Project Structure

insurance-predictor/
│
├── insurance_app.py # Main Streamlit app
├── insurance_model.pkl # Trained model file
├── requirements.txt # Dependencies list
├── README.md # Project documentation
└── dataset_source.txt # (Optional) Dataset link or notes

yaml
Copy code

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/insurance-predictor.git
   cd insurance-predictor
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app

bash
Copy code
streamlit run insurance_app.py
Open your browser and go to 👉 http://localhost:8501

🧾 Example Prediction
Input	Output
Age = 30	
BMI = 27.5	
Smoker = Yes	Predicted Charges = $28,345.67

🌟 Screenshots
🏠 Home Page

📊 Charts & Visuals

☁️ Deployment
To deploy this app on Streamlit Cloud:

Push your repository to GitHub

Go to share.streamlit.io

Connect your repo and select insurance_app.py as the entry point

That’s it — your app will be live! 🌍

🧑‍💻 Author
Your Name
📧 your.email@example.com
🔗 LinkedIn | GitHub

📜 License
This project is open source and available under the MIT License.

💡 "Predict your health costs before they predict you!"
