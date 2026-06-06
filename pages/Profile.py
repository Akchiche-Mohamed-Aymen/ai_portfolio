import streamlit as st
import json

# =========================
# Load Data
# =========================
with open("./data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

profile = data["profile"]
skills = data["skills"]
categories = data["categories"]

# =========================
# Header
# =========================
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "./images/profile.webp",
        width=180
    )

with col2:
    st.title("👤 Profile")

    st.markdown(f"""
    ## {profile["name"]}
    ### {profile["title"]}
    """)

    st.write(profile["bio"])
st.divider()

# =========================
# Skills
# =========================
st.subheader("Skills")

cols = st.columns(3)

for i, skill in enumerate(skills):
    with cols[i % 3]:
        st.info(skill)

st.divider()

# =========================
# Categories
# =========================
st.subheader("AI Focus Areas")

cols = st.columns(len(categories))

for col, cat in zip(cols, categories):
    with col:
        st.success(cat.upper())

st.divider()

# =========================
# Career Focus
# =========================
st.subheader("Career Focus")

st.write("""
- Machine Learning Engineering  
- Generative AI Systems  
- NLP Applications  
""")