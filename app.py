import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
def create_sample_dataset():
    data = {
        "Age 🎂": [55, 63, 45, 70, 35, 50, 60, 67, 40, 58],
        "Gender ⚧️": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
        "Smoker 🚬": [1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
        "Coughing 🤧": [1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        "Chest Pain 💢": [1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        "Fatigue 😴": [1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        "Swallowing Difficulty 😖": [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        "Yellow Fingers 💛": [1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
        "Shortness of Breath 😤": [1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        "Lung Cancer 🫁": [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    df["Gender ⚧️"] = df["Gender ⚧️"].map({"Male": 1, "Female": 0})
    return df

# Train and save model
def train_and_save_model():
    df = create_sample_dataset()
    X = df.drop("Lung Cancer 🫁", axis=1)
    y = df["Lung Cancer 🫁"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))
    st.sidebar.success(f"🎯 Model Trained with Accuracy: {round(accuracy*100, 2)}%")

    # Save the trained model
    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)

# Train if model doesn't exist
if not os.path.exists("model.pkl"):
    train_and_save_model()

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit main function
def main():
    st.set_page_config(page_title="Lung Cancer Risk Predictor", page_icon="🫁")
    st.title("🫁 Lung Cancer Risk Prediction App")
    st.markdown("🚀 _Check if a person is at risk of lung cancer based on symptoms!_")

    st.sidebar.header("👤 Input Patient Info")
    age = st.sidebar.slider("🎂 Age", 18, 100, 45)
    gender = st.sidebar.radio("⚧️ Gender", ["Male", "Female"])
    smoker = st.sidebar.radio("🚬 Smoker", ["Yes", "No"])
    cough = st.sidebar.checkbox("🤧 Coughing")
    chest_pain = st.sidebar.checkbox("💢 Chest Pain")
    fatigue = st.sidebar.checkbox("😴 Fatigue")
    swallowing = st.sidebar.checkbox("😖 Swallowing Difficulty")
    yellow_fingers = st.sidebar.checkbox("💛 Yellow Fingers")
    short_breath = st.sidebar.checkbox("😤 Shortness of Breath")

    input_data = np.array([[
        age,
        1 if gender == "Male" else 0,
        1 if smoker == "Yes" else 0,
        int(cough),
        int(chest_pain),
        int(fatigue),
        int(swallowing),
        int(yellow_fingers),
        int(short_breath)
    ]])

    if st.sidebar.button("🔍 Predict"):
        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        st.subheader("📋 Prediction Result")
        if prediction == 1:
            st.error(f"⚠️ High Risk of Lung Cancer ({round(prob*100, 2)}%)")
        else:
            st.success(f"✅ Low Risk of Lung Cancer ({round(prob*100, 2)}%)")

    # Dataset Overview & Correlation Heatmap
    st.subheader("📊 Dataset Overview & Heatmap")
    df_vis = create_sample_dataset()
    st.dataframe(df_vis)

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(df_vis.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    st.pyplot(fig)

    # Fun and motivational message with emojis
    st.markdown(""" 
        <p style="font-size: 20px; color: #ff6347; text-align: center;">
            🚭 Smoking is harmful to health, but still, smokers say: 'Enjoy now, regret later!' 😜
        </p>
    """, unsafe_allow_html=True)

    # Sexy & Responsive Footer
    st.markdown("""
    <hr style="margin-top: 30px; border: 1px solid #eee;" />
    <div style='display: flex; flex-direction: column; align-items: center; font-size: 15px; color: #888;'>
        <p> Developed with ❤️ by 
        <a href='https://www.linkedin.com/in/atharva-soundankar/' 
           style='color:#00ffff; text-decoration: none;' 
           target='_blank'><strong>Atharva Soundankar</strong></a> &copy; 2025</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
