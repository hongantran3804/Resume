import streamlit as st
from PIL import Image
st.set_page_config("Home",layout="centered")

image = Image.open("newimg.png")
with open("Hong An Tran Resume.pdf",'rb') as f:
    pdf = f.read()
col1, col2 = st.columns([1,1.5])
with col1:
    st.image(image, width=255)
with col2:
    st.markdown("<h4>Hong An Tran</h4>",unsafe_allow_html=True)
    st.markdown("A Computer Science student seeking a summer Software Engineering internship.")
    st.download_button(
        label = " 📄 Download Resume",
        data=pdf,
        file_name = "Hong An Tran Resume.pdf",
        mime="application/pdf"
    )
    st.markdown("Email: <u style='color: blue;'>hongantran3804@gmail.com</u>",unsafe_allow_html=True)
    col21,col22,col23= st.columns([3,1.2,1])
    with col21:
        st.markdown("Phone number: 714-719-6372")
    with col22: 
        st.markdown("<a href='https://www.linkedin.com/in/hong-an-tran-4846b6255/'><u style='blue'>Linkedin</u></a>",unsafe_allow_html=True) 
    with col23:
        st.markdown("<a href='https://github.com/hongantran3804?tab=repositories'><u style='blue'>Github</u></a>",unsafe_allow_html=True)
        
select = st.multiselect(label="Select options",options=['Technical Skills','Professional Experience','Education',"Extracurricular Involment"]
                        ,default='Professional Experience')
if 'Technical Skills' in select:
    st.subheader("Technical Skills")
    st.markdown("<strong>Strength: </strong> Analytical, Problem Solving, Well-Organization, Flexibility",unsafe_allow_html=True)
    st.markdown("<strong>Propramming Language: </strong> Java, Python, C++, HTML/CSS, Git/Github, Microsoft Office - Excel, Word",
                unsafe_allow_html=True)
    st.markdown("<strong>Operating System: </strong> Windows 11",unsafe_allow_html=True)
if 'Professional Experience' in select:
    st.subheader("Professional Experience")
    with open("Lacaco_WorkFlow.pdf",'rb') as f:
        work_flow = f.read()
    st.download_button(
        label = "Download WorkFlow",
        data=work_flow,
        file_name="Lacaco_WorkFlow.pdf",
        mime='application/pdf'
    )
    st.markdown("<h5><strong>Software Engineer Intern | Lacaco Wholesales | Garden Grove, CA</strong></h5>",unsafe_allow_html=True)
    st.markdown("<h5><strong>August 2023 - Present</strong></h5>",unsafe_allow_html=True)
    st.markdown(
        """
    <div><strong>Developed an automated email response system utilizing Python, Gmail API, Drive API, AWS EC2, and OpenAI API to enhance email processing efficiency for a company.</strong>
    
    - Implemented an auto-reply feature for customer inquiries requesting price lists, seamlessly storing customer details in the company's database, and intelligently assigning them to appropriate sales representatives.
    <br>
    - Streamlined the reception and processing of supplier emails containing price lists. The system efficiently extracted and transferred supplier data into the company's price list, ensuring accuracy and saving valuable time.
    <br>
    - Engineered a predictive module for unknown emails, categorizing them as potential customers, suppliers, or advertisements. For potential customers, the system automatically sent requests to fill out the company's website form. Identified and labeled supplier emails within Gmail, optimizing communication channels.</div>
"""
    ,unsafe_allow_html=True)
if 'Education' in select:
    st.subheader("Education")
    st.markdown("""
                <div>
    Orange Coast College at Costa Mesa | Costa Mesa, CA
    <br>
    A.S. in Computer Science (In Progress) | GPA: 4.0/4.0
    <br>
    Expected Graduation Date: May 2025
    <br>
""",unsafe_allow_html=True)
if "Extracurricular Involment" in select:
    st.subheader("Extracurricular Involment")
    st.markdown("""
    <div>
<strong>Community Outreach, 2019:</strong>
<br>
●	 Volunteered at a Catholic Church in VietNam, cooking and serving meals.
<br>
●	 Engaged with orphaned children through play and distributed gifts to enhance their well-being.
<br><br>
<strong>Thanksgiving Volunteer, 2023:</strong>
<br>
●	Participated in a Thanksgiving event organized by VCSA (Vietnamese Community Student Association).
<br>
●	Contributed by bringing gifts to homeless individuals and took part in some dance performances to uplift the festive spirit.  
</div> 
 """,unsafe_allow_html=True)




