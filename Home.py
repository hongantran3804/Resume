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
        
select = st.multiselect(label="Select options",options=['Technical Skills','Professional Experience','Education']
                        ,default=['Professional Experience',"Technical Skills"])
if 'Technical Skills' in select:
    col1,col2,col3 = st.columns(3)
    with col2:
        st.subheader("Technical Skills")
    col4, col5, col6 = st.columns([1,30,1])
    with col5:
        
        st.markdown(f"Java | Python | C++ | HTML/CSS | Git/Github | AWS - EC2 | Prompt Engineering | Microsoft Office")
if 'Professional Experience' in select:
    col1,col2,col3 = st.columns([1.5,3,1])
    with col2:
        st.subheader("Professional Experience")   
    with open("Lacaco_WorkFlow.pdf",'rb') as f:
        work_flow = f.read()
    
    st.markdown("<h5><strong>Software Engineer Intern | Lacaco Wholesales | Garden Grove, CA</strong></h5>",unsafe_allow_html=True)
    st.markdown("<h5><strong>August 2023 - Present</strong></h5>",unsafe_allow_html=True)
    st.markdown(
        """
   <div>
   	●	Developed a tool leveraging Python, Gmail API for customer inquiries processing, incorporating EC2 for scalable deployment, resulting in a 50% reduction in response time, improving customer engagement.
   <br>
	●	Integrated prompt engineering to implement ChatGPT-based models with 95%+ accuracy for auto  incoming email classification, leading to the efficient work assignment to appropriate teams.
    <br>
    ●	Enhanced operation efficiency by developing Python scripts to automatically convert diverse vendor price lists into company format, maintain them on cloud drive, and send updated prices to sales team.
   </div>
"""
    ,unsafe_allow_html=True)
if 'Education' in select:
    col1,col2,col3 = st.columns([2.5,3,1])
    with col2:
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




