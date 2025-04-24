# 🫁 Lung Cancer Risk Prediction App

🚀 A sleek and interactive **Machine Learning Web App** built using **Streamlit** that predicts the risk of **Lung Cancer** based on user input symptoms and lifestyle indicators.

🔗 **Live Demo:** [Click here to try it out!](https://mercydeez-lung-cancer-predictor-app-cc7nc0.streamlit.app/)  
👨‍💻 **Developer:** [Atharva Soundankar](https://www.linkedin.com/in/atharva-soundankar/)

---

## 💡 Features

- 🎂 Age, Gender, and Lifestyle symptom inputs
- 🧠 Random Forest Classifier-based prediction
- 📊 Visual dataset overview + heatmap
- 📈 Accurate model trained on sample symptom data
- 💛 Clean, emoji-rich, beginner-friendly UI
- 🚭 Motivational health message included

---

## 🛠 Tech Stack

| Tool            | Description                          |
|-----------------|--------------------------------------|
| Python 🐍       | Base programming language             |
| Streamlit ⚡    | For building the web interface        |
| scikit-learn 🤖 | Machine learning model                |
| pandas 🧾       | Data handling                         |
| seaborn 🎨      | Heatmap visualizations                |
| matplotlib 📊   | Basic plotting                        |
| pickle 🥒       | Saving the ML model                   |


---

## 📊 Dataset Details

This app uses a **manually created synthetic dataset** for practice purposes only. It includes the following fields:

- Age 🎂
- Gender ⚧️ (encoded: Male = 1, Female = 0)
- Smoker 🚬
- Yellow Fingers 💛
- Coughing 🤧
- Shortness of Breath 😤
- Swallowing Difficulty 😖
- Chest Pain 💢
- Fatigue 😴  
- **Target:** Lung Cancer (Yes = 1, No = 0)

> ⚠️ No real-world or medical data is involved. All dummy.

---
## 🧠 Model Info

- 🎯 **Algorithm Used**: RandomForestClassifier  
- 🔍 Trained on small custom data (10 samples for fun)  
- 🧪 Accuracy shown after model is trained  
- 💾 Model saved using Pickle (`model.pkl`)  
- ✅ Prediction done in real-time via Streamlit

---

## 🚀 How to Run Locally

> Make sure Python & pip are installed

```bash
# 1️⃣ Clone the repo
git clone https://github.com/your-username/lung-cancer-predictor.git
cd lung-cancer-predictor

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Launch the app
streamlit run app.py
```

# 🧪 App Sections Overview

| **Section**            | **Function**                                      |
|------------------------|---------------------------------------------------|
| **Sidebar**            | Take input values for prediction                  |
| **Model Prediction**   | Shows result based on input                       |
| **Dataset Viewer**     | Displays the dataset used                         |
| **Correlation Heatmap**| Shows relationship between features               |
| **Footer Message**     | Fun health reminder 😉                             |

---

# 🎨 UI Theme

The app uses:

- **Bold headers**
- **Emojis** for fun interpretation
- **Streamlit layout components**
- **Clean black background banner** for vibe

---

# 😅 Why this Project?

Felt like deploying something. *Thoda timepass, thoda learning.*

Wanted to test:

- ✅ ML model building workflow  
- ✅ Pickle for saving models  
- ✅ Streamlit for UI  
- ✅ Deployment via Streamlit Cloud  

---

# 📢 Disclaimer

⚠️ **This is not a medical tool.**  
This project is for educational/demo purposes only and should **never** be used for actual diagnosis.  
Please consult a real doctor for medical advice.

---

# 🚭 Random Health Message

> "**Smoking is harmful to health. Still, smokers be like — 'YOLO!' 😅**"

---

# 🪪 Credits

Just made for practice. Nothing too serious.  
If it helped you, feel free to **star ⭐ the repo**.  
**Cheers! 🙌**

---

👨‍💻 Developer & Maintainer
Developed with ❤️ by Atharva Soundankar
🔗 [LinkedIn](https://www.linkedin.com/in/atharva-soundankar/) • 📅 2025 • India 🇮🇳

---


## 📜 License
This project is licensed under the MIT License. Feel free to use, share, and modify with credit!
