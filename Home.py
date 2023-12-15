import streamlit as st
from PIL import Image
st.set_page_config("Home",layout="centered")

image = Image.open("newimg.png")
with open("Hong An Tran Resume.pdf",'rb') as f:
    pdf = f.read()
col1, col2 = st.columns([1,1.5])
with col1:
    st.image(image,width=268)
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
        st.markdown("Phone number: (714) 719-6372")
    with col22: 
        st.markdown("<a href='https://www.linkedin.com/in/hong-an-tran-4846b6255/'><u style='blue'>Linkedin</u></a>",unsafe_allow_html=True) 
    with col23:
        st.markdown("<a href='https://github.com/hongantran3804?tab=repositories'><u style='blue'>Github</u></a>",unsafe_allow_html=True)
        
select = st.multiselect(label="Select options",options=['Technical Skills','Professional Experience','Education',"Extracurricular Involment"]
                        ,default=['Professional Experience',"Technical Skills"])
if 'Technical Skills' in select:
    st.subheader("Technical Skills")
    st.markdown("<strong>Strengths: </strong> Analytical, Problem Solving, Well-Organization, Flexibility.",unsafe_allow_html=True)
    st.markdown("<strong>Programming Languages: </strong> Java, Python, C++, HTML/CSS, Git/Github, AWS-EC2.", unsafe_allow_html=True)
    st.markdown(f"<strong>Related Skills: </strong> Microsoft Office (Excel, Word).",unsafe_allow_html=True)
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
   <div>
   ●	Automated responses for price list requests, storing customer details, and assigning to sales reps.
   <br>
●	Streamlined handling of supplier emails, extracting data for the company’s price list, and categorizing unknown emails for targeted responses

   </div>
"""
    ,unsafe_allow_html=True)
if 'Education' in select:
    st.subheader("Education")
    st.markdown("""
                <div>
   <strong> Orange Coast College at Costa Mesa | Costa Mesa, CA</strong>
    <br>
   <strong> A.S. in Computer Science (In Progress) | </strong> GPA: 4.0/4.0
    <br>
   <strong> Expected Graduation Date:</strong> May 2025
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




