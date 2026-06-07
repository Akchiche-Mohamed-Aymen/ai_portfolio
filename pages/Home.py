import streamlit as st
import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
data_path =   BASE_DIR / "data.json"
with open('./data.json', "r", encoding="utf-8" ) as file:
    data = json.load(file)
def edit_number(num):
    if num > 10 :
        return f"{num - 5}+"
    elif num >= 5:
        return f"{num - 3}+"
    elif num >= 3:
        return f"{num - 2}+"
    elif num > 1:
        return f"{num - 1}+"
    return f"{num}"

st.markdown("""
### Machine Learning & Generative AI Engineer
""")

st.write(
    """
    Building intelligent systems using Machine Learning,
    NLP, and modern Generative AI technologies.
    """
)

st.divider()

col1, col2, col3 = st.columns(3)
projects_count = edit_number(len(data["projects"]))
skills_count = edit_number(len(data["skills"]))
categories_count = edit_number(len(data["categories"]))
with col1:
    st.metric(
        label="Projects",
        value=f"{projects_count}"
    )

with col2:
    st.metric(
        label="Skills",
        value=f"{skills_count}"
    )

with col3:
    st.metric(
        label="Categories",
        value=f"{categories_count}"
    )

st.divider()
st.subheader("Focus Areas")

cols = st.columns(len(data["categories"]))

for col, category in zip(cols, data["categories"]):
    with col:
        st.info(category.upper())

st.divider()

st.subheader("Explore")

col1, col2 = st.columns(2)

with col1:
    if st.button("📂 View Projects", use_container_width=True):
        st.switch_page("pages/Projects.py")

with col2:
    if st.button("👤 View Profile", use_container_width=True):
        st.switch_page("pages/Profile.py")