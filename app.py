import streamlit as st

st.set_page_config(
    page_title="AI Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    padding-top: 0;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 0;
}

.profile-block {
    padding: 2rem 1.25rem 1.5rem;
    text-align: center;
}

.avatar-wrapper {
    width: 88px;
    height: 88px;
    border-radius: 50%;
    overflow: hidden;
    margin: 0 auto 1rem;
    border: 2px solid rgba(128, 128, 128, 0.2);
}

.avatar-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.profile-name {
    font-size: 0.95rem;
    font-weight: 600;
    margin: 0 0 0.3rem;
    color: inherit;
}

.profile-role {
    font-size: 0.9rem;
    color: inherit;
    margin: 0 0 1rem;
    letter-spacing: 0.02em;
}

.profile-badge {
    display: inline-block;
    font-size: 0.7rem;
    padding: 3px 10px;
    border-radius: 20px;
    background: rgba(34, 197, 94, 0.12);
    color: #16a34a;
    border: 1px solid rgba(34, 197, 94, 0.25);
    letter-spacing: 0.03em;
}

.nav-section-label {
    padding: 0.75rem 1.25rem 0.4rem;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: gray;
    opacity: 0.6;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class="profile-block">
        <div class="profile-name">Mohamed Aymen Akchiche</div>
        <div class="profile-role">ML &amp; AI Engineer</div>
        <span class="profile-badge">&#x25cf;&nbsp; Available</span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()


# Page definitions
home_page     = st.Page("pages/Home.py",    title="Home",    icon="🏠", default=True)
profile_page  = st.Page("pages/Profile.py", title="Profile", icon="👤")
projects_page = st.Page("pages/Projects.py",title="Projects",icon="📂")
contact_page  = st.Page("pages/Contact.py", title="Contact", icon="📩")

project_details_page = st.Page(
    "pages/project_details.py", title="-"
)

pg = st.navigation({
    "Main": [home_page, profile_page, projects_page, contact_page , project_details_page]
})
pg.run()