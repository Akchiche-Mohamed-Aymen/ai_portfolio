import streamlit as st

st.markdown("""
<style>
.contact-header {
    margin-bottom: 2rem;
}

.contact-header h1 {
    font-size: 1.6rem;
    font-weight: 700;
    margin: 0 0 0.3rem;
}

.contact-header p {
    color: gray;
    font-size: 0.9rem;
    margin: 0;
}

.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem;
    max-width: 800px;
}

.contact-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 1.25rem;
    border-radius: 12px;
    border: 1px solid rgba(128,128,128,0.15);
    background: rgba(128,128,128,0.03);
    text-decoration: none;
    transition: border-color 0.2s, background 0.2s;
    cursor: pointer;
}

.contact-card:hover {
    border-color: rgba(128,128,128,0.35);
    background: rgba(128,128,128,0.07);
}

.contact-icon {
    width: 42px;
    height: 42px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
}

.contact-info {
    display: flex;
    flex-direction: column;
    gap: 2px;
    overflow: hidden;
}

.contact-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: gray;
    font-weight: 500;
}

.contact-value {
    font-size: 0.88rem;
    font-weight: 500;
    color: inherit;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Per-platform icon backgrounds */
.icon-linkedin  { background: rgba(10,  102, 194, 0.12); }
.icon-telegram  { background: rgba(38,  161, 218, 0.12); }
.icon-facebook  { background: rgba(24,  119, 242, 0.12); }
.icon-email     { background: rgba(234,  88,  12, 0.12); }
.icon-phone     { background: rgba(34,  197,  94, 0.12); }
.icon-whatsapp  { background: rgba(37,  211, 102, 0.12); }
</style>
""", unsafe_allow_html=True)

# ── Page header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="contact-header">
    <h1>Contact me</h1>
    <p>Feel free to reach out through any of the channels below.</p>
</div>
""", unsafe_allow_html=True)

# ── Contact data — edit values here ─────────────────────────────────────────
contacts = [
    {
        "label":    "LinkedIn",
        "value":    "Mohamed Aymen Akchiche",
        "href":     "https://www.linkedin.com/in/mohamed-aymen-akchiche-b9b0b7303/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BIePej3xCQe6HljM31DBF%2Bg%3D%3D",
        "icon":     "🔗",
        "css_cls":  "icon-linkedin",
    },
    {
        "label":    "Telegram",
        "value":    "@أيمن",
        "href":     "https://t.me/Aqangi",
        "icon":     "✈️",
        "css_cls":  "icon-telegram",
    },
    {
        "label":    "Facebook",
        "value":    "@Aymen Akchiche",
        "href":     "https://www.facebook.com/share/1CpB1F3XMm/",
        "icon":     "📘",
        "css_cls":  "icon-facebook",
    },
    {
        "label":    "Email",
        "value":    "akchiche.mohamedaymen@univ-ouargla.dz",
        "href":     "mailto:akchiche.mohamedaymen@univ-ouargla.dz",
        "icon":     "📧",
        "css_cls":  "icon-email",
    },
    {
        "label":    "Phone",
        "value":    "+213 698841788",
        "href":     "tel:+213698841788",
        "icon":     "📞",
        "css_cls":  "icon-phone",
    },
    {
        "label":    "WhatsApp",
        "value":    "+213 698841788",
        "href":     "https://wa.me/213698841788",
        "icon":     "💚",
        "css_cls":  "icon-whatsapp",
    },
]

# ── Render cards ─────────────────────────────────────────────────────────────
cards_html = '<div class="contact-grid">'
for c in contacts:
    cards_html += f"""
    <a class="contact-card" href="{c['href']}" target="_blank" rel="noopener noreferrer">
        <div class="contact-icon {c['css_cls']}">{c['icon']}</div>
        <div class="contact-info">
            <span class="contact-label">{c['label']}</span>
            <span class="contact-value">{c['value']}</span>
        </div>
    </a>"""
cards_html += '</div>'

st.markdown(cards_html, unsafe_allow_html=True)