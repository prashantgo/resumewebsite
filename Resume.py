import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
# st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)
st.set_page_config(page_title="Home Page", page_icon=":tada:", layout="wide")
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer" />', unsafe_allow_html=True)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

with open("assets/resume_latest.pdf", "rb") as pdf_file:
    pdfbytes = pdf_file.read()

def icon_span(icon, item, mclass="inline-icons"):
    return f'<span>{icon.replace("fa-", f"{mclass} fa-", 1)} {item}</span>'
    # return f'<span><span class="{mclass}">{icon}</span> {item}</span>' material icons way of doing things

# ---- HEADER SECTION ----
with st.container():
    col1, col2 = st.columns((4, 1))
    col1.markdown(f'<div class="titleheader"><a href="{st.secrets.pagelinks.home_page}" target="_blank">PRASHANT GOYAL</a></div>', unsafe_allow_html=True)
    col1.markdown('<div class="titlesubheader">Software Development Engineer</div>', unsafe_allow_html=True)
    col2.download_button("Download Resume", file_name="resume_prashant.pdf", mime="application/octet-stream", data=pdfbytes)

    cols = st.columns((1.3, 0.7, 1, 0.5))
    l = ['prashant.goyal.che15@itbhu.ac.in', '+91-8813801058',  'prashant-goyal-31a588137']
    icons = ['<i class="fa-solid fa-envelope marg"></i>', '<i class="fa-solid fa-phone marg"></i>', '<i class="fa-brands fa-linkedin marg"></i>']
    for index, (item, icon, col) in enumerate(zip(l, icons, cols[:3])):
        text = icon_span(icon, item)
        if index == 2:
            text = f"<a href='{st.secrets.pagelinks.linkedin_page}' target='_blank'>{text}</a>"
        col.markdown(text, unsafe_allow_html=True)

st.markdown("#")
# ---- WHAT I DID ----
with st.container():
    text = icon_span('<i class="fa-solid fa-briefcase"></i>', "PROFESSIONAL EXPERIENCE")
    st.markdown(f'##### {text}', unsafe_allow_html=True)
    st.divider()
    
    col1, col2 = st.columns((4, 1))
    col1.markdown("**SDE-I,** *Innovaccer Pvt Ltd.*")
    col2.write("Jun 2019 - Sep 2021")
    st.write(
            """
            - Designed and developed multiple APIs in Python (DRF) using TDD approach.
            - Hands on working experience with DevOps tools like Docker, Ansible, Jenkins and CI/CD.
            - Automated many pre-deployment steps reducing the dependence on ad-hoc scripts.
            """
        )

    col1, col2 = st.columns((4, 1))
    col1.markdown("**Intern - Data Analytics,** *Valiance Solutions Pvt Ltd*")
    col2.write("May 2018 - Jul 2018")
    st.write(
            """         
            - Assisted Machine Learning team in data extraction
            - Build a generalised crawler for scraping n number of websites with bouncing IPs.
            - Build crawlers for Google Adwords, Google Scholar
            - Developed a crawler for carefully gathering data from 9000 pages of a website.
            """
        )

# ---- SKILLS -----
with st.container():
    text = icon_span('<i class="fa-solid fa-code-compare"></i>', "SKILLS")
    st.markdown(f'##### {text}', unsafe_allow_html=True)
    st.divider()

    cols = st.columns(4)
    items = [
        "**Tech Stack**",
        """
        - Python, AWS, DRF
        - Django, FastAPI, Pandas
        - Git, Docker, Flask, Pydantic
        """,
        "**Database**",
        """
        - MongoDB, Redis
        - PostgreSql, Redshift
        - ElasticSearch
        """,
        "**Others**",
        """
        - RestAPI, Celery, Streamlit
        - Ansible, Jenkins
        - Keras, Scikit-Learn, C/C++
        """
    ]
    for heading, skills, col in zip(items[::2], items[1::2], cols[:3]):
        col.markdown(heading)
        col.markdown(skills)

# ---- Education ---
with st.container():
    text = icon_span('<i class="fa-sharp fa-solid fa-graduation-cap"></i>', "EDUCATION")
    st.markdown(f'##### {text}', unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns((4, 1))
    col1.markdown("**Indian Institute of Technology (BHU) Varanasi**")
    col2.write("Jul 2015 - May 2019")
    st.markdown(
        """
            *B.Tech - Chemical Engineering and Technology (7.91/10)*
            - Coursework 
                * Macroeconomics-I, Introduction to HPC, Time Series Analysis
                * Data Structures & Algorithms, Computer Programming(C)
            - Institute Projects
                * Built a word complexity identification system.
                * Graph similarity using high-performance computing algorithms.
                * Worked on increasing the catalytic activity of γ-Alumina - a catalyst.
        """
    )

# ---- PROJECTS ---
with st.container():
    text = icon_span('<i class="fa-solid fa-folder-open"></i>', "PROJECTS")
    st.markdown(f'##### {text}', unsafe_allow_html=True)
    st.divider()

    st.markdown(
        """
            **Self Learning Projects**
            - Text and music notes generation using LSTMs
            - Created blog using NodeJS, Django and Flask
            - Content-based recommendation system, Tweets Sentimental Analysis
            - Designed neural netsto compute and model various mathematical functions
            - Multiple dashboards and a resume page using Tableau and Streamlit
        """
    )

# ---- ONLINE COURSES ----
with st.container():
    text = icon_span('<i class="fa-solid fa-book-open"></i>', "COURSES")
    st.markdown(f'##### {text}', unsafe_allow_html=True)
    st.divider()

    st.markdown(
        """
            **Machine learning and Data Science courses,** *Udacity, Coursera*
            - Introduction to Machine Learning - Udacity
            - Intro to Deep Learning - Udacity
            - deep.ai specialization, Machine Learning - Andrew NG
        """
    )
    st.markdown(
        """
            **Web Developer Bootcamp,** *Udemy*
            - 43 hours course on full stack web development covering Jquery, JavaScript, NodeJS, BootStrap,
            - SemanticUI, MongoDB, Heroku, RestAPI, EJX
        """
    )

# ---- CONTACT ----
st.markdown("#")
with st.container():
    text = icon_span('<i class="fa-solid fa-paper-plane"></i>', "Get In Touch With Me!")
    st.markdown(f'##### {text}', unsafe_allow_html=True)
    st.divider()

    # Documention: https://formsubmit.co/
    contact_form = """
        <form action="https://formsubmit.co/227344826367dbc0020767377227a3f6" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" rows=6 placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()