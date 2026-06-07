import streamlit as st
import json


with open("./data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

projects = data["projects"]

# =========================
# Check Selected Project
# =========================
if "project_id" not in st.session_state:
    st.warning("No project selected.")

    if st.button("Back to Projects"):
        st.switch_page("pages/Projects.py")

    st.stop()

# =========================
# Get Project
# =========================
project_id = st.session_state["project_id"]

project = next(
    (
        p for p in projects
        if p["id"] == project_id
    ),
    None
)

# =========================
# Project Not Found
# =========================
if project is None:
    st.error("Project not found.")

    if st.button("Back to Projects"):
        st.switch_page("pages/Projects.py")

    st.stop()

# =========================
# Back Button
# =========================
if st.button("⬅ Back to Projects"):
    st.switch_page("pages/Projects.py")

st.divider()

# =========================
# Project Header
# =========================
st.title(project["title"])

categories_text = " • ".join(
    [cat.upper() for cat in project["categories"]]
)

st.caption(categories_text)

st.write(project["description"])

st.divider()

# =========================
# Project Overview
# =========================
st.subheader("Overview")

st.write(
    project.get(
        "overview",
        "No overview provided."
    )
)

# =========================
# Problem
# =========================
st.subheader("Problem")

st.write(
    project.get(
        "problem",
        "No problem description provided."
    )
)

# =========================
# Approach
# =========================
st.subheader("Approach")

st.write(
    project.get(
        "approach",
        "No approach provided."
    )
)

# =========================
# Tech Stack
# =========================
st.subheader("Tech Stack")

tech_stack = project.get("techStack", [])

tech_cols = st.columns(3)

for i, tech in enumerate(tech_stack):

    with tech_cols[i % 3]:
        st.success(tech)

st.divider()

# =========================
# Metrics
# =========================
if "metrics" in project:

    st.subheader("Metrics")

    metric_cols = st.columns(len(project["metrics"]))

    for col, (metric, value) in zip(
        metric_cols,
        project["metrics"].items()
    ):

        with col:
            st.metric(
                label=metric.upper(),
                value=value
            )

    st.divider()

# =========================
# Project Links
# =========================
st.subheader("Links")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "💻 GitHub Repository",
        project["gitLink"],
        use_container_width=True
    )

with col2:
    st.link_button(
        "🚀 Live Demo",
        project["liveDemo"],
        use_container_width=True
    )