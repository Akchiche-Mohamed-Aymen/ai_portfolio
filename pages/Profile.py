import streamlit as st
import json

# =========================
# Load Data
# =========================
with open("./data/data.json", "r", encoding="utf-8") as file:
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
        "./images/profile.png",
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
        logo_url = skill.get("logo", "")
        skill_name = skill["name"]

        if logo_url:
            st.markdown(
                f"""
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    background-color: #f0f2f6;
                    border-radius: 8px;
                    padding: 10px 14px;
                    margin-bottom: 10px;
                ">
                    <img src="{logo_url}" width="28" height="28"
                         style="object-fit: contain; flex-shrink: 0; border-radius: 4px;"
                         onerror="this.style.display='none'" />
                    <span style="font-size: 0.95rem; font-weight: 500; color: red">{skill_name}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.info(skill_name)

st.divider()

st.subheader("AI Focus Areas")

cols = st.columns(len(categories))

for col, cat in zip(cols, categories):
    with col:
        st.success(cat.upper())

st.divider()

st.subheader("Career Focus")

st.write("""
- Machine Learning Engineering  
- Generative AI Systems  
- NLP Applications  
""")