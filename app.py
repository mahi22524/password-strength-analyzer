import streamlit as st
import re

# ---------------------------------
# Common Password List
# ---------------------------------
COMMON_PASSWORDS = [
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "abc123",
    "iloveyou"
]

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔒",
    layout="centered"
)

# ---------------------------------
# Title
# ---------------------------------
st.title("🔒 Password Strength Analyzer")
st.write("Analyze the strength of your password and receive security recommendations.")

# ---------------------------------
# Password Input
# ---------------------------------
password = st.text_input(
    "Enter your password",
    type="password"
)

# ---------------------------------
# Password Analysis
# ---------------------------------
if password:

    st.subheader("Password Checklist")

    checks = {
        "At least 8 characters": len(password) >= 8,
        "Contains uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Contains lowercase letter": bool(re.search(r"[a-z]", password)),
        "Contains number": bool(re.search(r"[0-9]", password)),
        "Contains special character": bool(
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
        ),
    }

    score = 0

    for item, passed in checks.items():
        if passed:
            st.success(f"✔ {item}")
            score += 1
        else:
            st.error(f"✘ {item}")

    st.divider()

    # ---------------------------------
    # Password Details
    # ---------------------------------
    st.subheader("Password Details")

    st.write(f"**Password Length:** {len(password)}")
    st.write(f"**Security Score:** {score}/5")

    progress = score / 5
    st.progress(progress)
    st.write(f"**Strength Percentage:** {int(progress * 100)}%")

    # ---------------------------------
    # Password Strength
    # ---------------------------------
    if score <= 2:
        st.error("🔴 Weak Password")
    elif score <= 4:
        st.warning("🟡 Medium Password")
    else:
        st.success("🟢 Strong Password")

    # ---------------------------------
    # Password Uniqueness
    # ---------------------------------
    st.subheader("Password Uniqueness")

    if password.lower() in COMMON_PASSWORDS:
        st.error("⚠ This password is commonly used. Choose a more unique password.")
    else:
        st.success("✅ This password is not in the common password list.")

    # ---------------------------------
    # Suggestions
    # ---------------------------------
    st.subheader("Suggestions")

    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase the password length to at least 8 characters.")

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        suggestions.append("Add at least one lowercase letter.")

    if not re.search(r"[0-9]", password):
        suggestions.append("Include at least one numeric digit.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Include at least one special character.")

    if suggestions:
        for suggestion in suggestions:
            st.info(suggestion)
    else:
        st.success("Excellent! Your password meets all basic security requirements.")