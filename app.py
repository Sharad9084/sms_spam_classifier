import streamlit as st
import pickle

# Load the model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Streamlit App
st.title("📩 SMS Spam Classifier")

st.write("Enter an SMS message below to check whether it's **Spam** or **Not Spam**.")

# Text input box
sms_input = st.text_area("Enter your message here:")

# Predict button
if st.button("Predict"):
    if sms_input.strip() == "":
        st.warning("⚠️ Please enter a message to classify.")
    else:
        # Transform input and predict
        input_vector = vectorizer.transform([sms_input])
        prediction = model.predict(input_vector)[0]

        # Output result
        if prediction == 1:
            st.error("🚫 This message is **Spam**.")
        else:
            st.success("✅ This message is **Not Spam**.")
