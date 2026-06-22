import streamlit as st
from add_project_route import add
st.set_page_config(page_title="Create Project", page_icon="🚀")

st.title("🚀 Create New Project")

with st.form("project_form"):

    # Title
    title = st.text_input("Project Title")

    # Description
    description = st.text_area(
        "Project Description",
        height=150
    )

    # Categories
    categories = st.multiselect(
        "Categories",
        options=[
            "ML",
            "DL",
            "NLP",
            "Gen AI"
        ]
    )

    # Tech Stack
    tech_stack_input = st.text_input(
        "Tech Stack (comma-separated)",
        placeholder="Python, TensorFlow, Streamlit, LangChain"
    )

    submitted = st.form_submit_button("Create Project")

if submitted:
    tech_stack = [
        tech.strip()
        for tech in tech_stack_input.split(",")
        if tech.strip()
    ]

    project = {
        "title": title,
        "description": description,
        "categories": categories,
        "techStack": tech_stack
    }
    try:
        add(project)
        st.success("Project created successfully!")
    except Exception as ex:
        st.exception(ex)
    