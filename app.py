import streamlit as st

# Data
companies = [
    {
        "name": "Oracle Health",
        "website": "https://www.oracle.com/health/",
        "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwHUaDLUfNRrg7tWk4TSeFaGnzjjlSZN06Gw&s",
        "social": {
            "LinkedIn": "https://www.linkedin.com/showcase/oraclehealth/",
            "Instagram": "https://www.instagram.com/oracle/",
            "Youtube": "https://www.youtube.com/@oracle"
        },
        "grades": {
            "Content": "B-",
            "SEO": "A",
            "Social": "A",
            "Overall": "A"
        },
        "description": "Oracle Health offers comprehensive health IT solutions that help providers streamline workflows and improve patient outcomes."
    },
    {
        "name": "Epic",
        "website": "https://www.epic.com/",
        "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsWZUWQAB2FTPdJCwurXjDehLGXjaOwPt7Tg&s",
        "social": {
            "LinkedIn": "https://www.linkedin.com/company/epic1979",
            "Instagram": "https://www.instagram.com/lifeatepic/",
            "Youtube": "https://www.youtube.com/c/EpicEHR"
        },
        "grades": {
            "Content": "C+",
            "SEO": "B",
            "Social": "B",
            "Overall": "B+"
        },
        "description": "Epic develops software to help healthcare organizations provide better care for patients, including electronic health records and other solutions."
    },
    {
        "name": "MEDITECH",
        "website": "https://ehr.meditech.com/",
        "logo": "https://ehr.meditech.com/themes/ehrmeditech/images/meditech-logo.svg",
        "social": {
            "LinkedIn": "https://www.linkedin.com/company/meditech",
            "Instagram": "https://www.instagram.com/meditechehr/",
            "Youtube": "https://www.youtube.com/channel/UCyj0QFHbuw4kViZWe309pYg"
        },
        "grades": {
            "Content": "C-",
            "SEO": "C",
            "Social": "C",
            "Overall": "C"
        },
        "description": "MEDITECH provides electronic health record solutions that empower healthcare organizations to deliver safe and efficient care."
    }
]

# Helper function to determine grade color
def grade_color(grade):
    if grade.startswith("A"):
        return "#2ecc71"  # Green
    elif grade.startswith("B"):
        return "#f39c12"  # Orange
    elif grade.startswith("C"):
        return "#e74c3c"  # Red
    return "#bdc3c7"  # Default grey for undefined

# Sort companies by overall grade
def sort_companies(companies):
    grade_order = {"A": 1, "B+": 2, "B": 3, "C": 4}  # Define custom sorting
    return sorted(companies, key=lambda c: grade_order.get(c["grades"]["Overall"], 99))

sorted_companies = sort_companies(companies)

# Streamlit app
st.set_page_config(page_title="Electronic Health Records - Report Cards", layout="wide")
st.title("Electronic Health Records - Report Cards")

for company in sorted_companies:
    name = company["name"]
    website = company["website"]
    logo = company["logo"]
    social = company["social"]
    grades = company["grades"]
    description = company["description"]

    with st.container(border=True):

        cols = st.columns([1, 2])  # Two-column layout

        # Left Column: Logo, Description, and Links
        with cols[0]:
            st.image(logo, width=100)
            st.markdown(f"<div style='font-size: 18px; margin-top: 10px;'>{description}</div>", unsafe_allow_html=True)
            st.markdown(f"[Website]({website})", unsafe_allow_html=True)
            st.markdown(f"[LinkedIn]({social['LinkedIn']})", unsafe_allow_html=True)
            st.markdown(f"[Instagram]({social['Instagram']})", unsafe_allow_html=True)
            st.markdown(f"[YouTube]({social['Youtube']})", unsafe_allow_html=True)

        # Right Column: Grades
        with cols[1]:
            st.markdown(f"<div style='font-size: 24px; font-weight: bold; color: #34495e;'>{name}</div>", unsafe_allow_html=True)

            st.markdown(
                f"<div style='font-size: 30px; font-weight: bold; color: {grade_color(grades['Overall'])};'>Overall: {grades['Overall']}</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div style='font-size: 18px; color: {grade_color(grades['Content'])};'>Content: {grades['Content']}</div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div style='font-size: 18px; color: {grade_color(grades['SEO'])};'>SEO: {grades['SEO']}</div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div style='font-size: 18px; color: {grade_color(grades['Social'])};'>Social: {grades['Social']}</div>",
                unsafe_allow_html=True
            )
