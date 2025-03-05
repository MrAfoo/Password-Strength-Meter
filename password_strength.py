import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    # Check uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🟡 Password should contain both uppercase and lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🟡 Password should contain at least one digit (0-9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("🟡 Password should include at least one special character (!@#$%^&*).")

    # Determine password strength
    if score == 4:
        strength = "🟢 Strong"
    elif 2 <= score <= 3:
        strength = "🟠 Moderate"
    else:
        strength = "🔴 Weak"

    return strength, feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password to check its strength and get improvement suggestions.")

# Input field
password = st.text_input("Enter your password", type="password")

# Check password when input is given
if password:
    strength, feedback = check_password_strength(password)
    
    # Display password strength
    st.subheader(f"Password Strength: {strength}")

    # Display feedback if password is weak or moderate
    if feedback:
        st.warning("Suggestions to improve your password:")
        for tip in feedback:
            st.write(tip)
