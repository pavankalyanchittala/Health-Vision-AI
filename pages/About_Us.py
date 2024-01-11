import streamlit as st
import streamlit.components.v1 as components


# Set page title
st.set_page_config(
    page_title="HealthVision AI | About Us",
    page_icon=":dna:",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
img{border-radius: 10px;}
</style> """, unsafe_allow_html=True)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)


PK = {
    'name': 'PAVAN KALYAN',
    'title': '',
    
}

MK = {
    'name': 'MANI KANTA',
    'title': 'Founders',
    
}

RA = {
    'name': 'RAHUL',
    'title': '',
    
}

RL = {
    'name': 'RAJYA LAXMI',
    'title': '',
    
}

# Define page layout
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            left: 0px;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#20D2FE, #5292FE);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">About Us</p>
    """,
    height=69,
)
st.write(f"## Founders")

# Add photos
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("Images/PK.png", width=150)
    st.write(PK['name'])

with col2:
    st.image("Images/MK.png", width=150)
    st.write(MK['name'])

with col3:
    st.image("Images/RA.png", width=150)
    st.write(RA['name'])

with col4:
    st.image("Images/RL.png", width=150)
    st.write(RL['name'])

st.divider()


# Add HealthVision description
st.markdown("## HealthVision")
st.write("HealthVision is an app that uses AI and machine learning to detect diseases from images uploaded by users. Our goal is to make healthcare more accessible and affordable by providing a fast, accurate, and reliable diagnosis tool. We believe that technology can revolutionize the way we approach healthcare, and we're excited to be at the forefront of this innovation.")


