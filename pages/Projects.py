import streamlit as st
import json

# =========================
# Load Data
# =========================
with open("./data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

projects = data["projects"]
categories = data["categories"]

# =========================
# Page Header
# =========================
st.title("📂 Projects")

st.write("""
Explore AI projects across Machine Learning,
Deep Learning, NLP, and Generative AI.
""")

st.divider()

# =========================
# Category Filter
# =========================
selected_category = st.selectbox(
    "Filter by Category",
    options=["all"] + categories
)

# =========================
# Filter Projects
# =========================
if selected_category == "all":
    filtered_projects = projects
else:
    filtered_projects = [
        project
        for project in projects
        if selected_category in project["categories"]
    ]

# =========================
# Projects Grid
# =========================
cols = st.columns(2)

for index, project in enumerate(filtered_projects):

    with cols[index % 2]:

        with st.container(border=True):

            # -----------------
            # Title
            # -----------------
            st.subheader(project["title"])

            # -----------------
            # Categories
            # -----------------
            categories_text = " • ".join(
                [cat.upper() for cat in project["categories"]]
            )

            st.caption(categories_text)

            # -----------------
            # Description
            # -----------------
            st.write(project["description"])

            # -----------------
            # Tech Stack
            # -----------------
            if "techStack" in project:

                st.markdown("#### Tech Stack")

                tech_cols = st.columns(2)

                for i, tech in enumerate(project["techStack"]):
                    with tech_cols[i % 2]:
                        st.success(tech)

            st.divider()

            # -----------------
            # Buttons
            # -----------------
            btn_col1, btn_col2, btn_col3 = st.columns(3)

            # View Details
            with btn_col1:

                if st.button(
                    "View Details",
                    key=f"details_{project['id']}",
                    use_container_width=True
                ):

                    st.session_state["project_id"] = project["id"]
                    try:
                        st.switch_page(
                            "pages/project_details.py"
                        )
                    except Exception as e:
                        st.error(
                            e
                        )
            # GitHub
            with btn_col2:

                st.link_button(
                    "GitHub",
                    project["gitLink"],
                    use_container_width=True
                )

            # Live Demo
            with btn_col3:

                st.link_button(
                    "Live Demo",
                    project["liveDemo"],
                    use_container_width=True
                )