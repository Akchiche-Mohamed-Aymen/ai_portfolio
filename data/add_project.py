import streamlit as st
from add_project_route import add
st.set_page_config(page_title="Create Project", page_icon="🚀")

st.title("🚀 Create New Project")

with st.form("project_form"):

    # Title
    title = st.text_input("Project Title")
    height = 150 
    # Description
    description = st.text_area(
        "Project Description",
        height = height
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
    tech_stack= st.multiselect(
        "Technologie(s)",
        options=[
            "Scikit-learn" , "Python" , 'Numpy' , 'Pandas' , 'Nltk' , 'Streamlit' , 'Tensorflow' , 'LangChain'
        ]
    )
    overview = st.text_area("Overview" , height=height)
    problem = st.text_area("Problem" , height=height)
    approach = st.text_area("Approach" , height=height)
    gitLink = st.text_input("Github Link")
    liveDemo = st.text_input("Live Demo")

    submitted = st.form_submit_button("Create Project")

if submitted:
    

    project = {
        "title": title,
        "description": description,
        "categories": categories,
        "techStack": tech_stack,
        "gitLink" : gitLink ,
        "overview" : overview ,
        "problem" : problem ,
        "approach" : approach ,
        "liveDemo" : liveDemo
    }
    try:
        add(project)
        st.success("Project created successfully!")
    except Exception as ex:
        st.exception(ex)
    