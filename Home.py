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
    col1,col2,col3 = st.columns([1,3,1])
    with col2:
        st.subheader("Technical Skills")
    st.markdown(
            """
   <div>
   	●	C++, Python, Java, Javascript, Typescript, Git, HTML/CSS
   <br>
	●	AWS, Google APIs, ReactJS, NodeJS, NextJS, TailwindCSS, MongoDB, Prisma, Selenium, Streamlit, Stripe
    <br>
   </div>
""",
            unsafe_allow_html=True,
        )
if 'Professional Experience' in select:
    col1,col2,col3 = st.columns([1.5,3,1])
    with col2:
        st.subheader("Professional Experience")   
    with open("Lacaco_WorkFlow.pdf",'rb') as f:
        work_flow = f.read()

    st.markdown(
        "<h5><strong>Software Engineer Intern | Lacaco Wholesales | Garden Grove, CA</strong></h5>",
        unsafe_allow_html=True,
    )
    st.markdown("<h5><strong>10/ 2024 – 12/ 2024</strong></h5>", unsafe_allow_html=True)
    st.markdown(
        """
   <div>
   	●	Developed a mock interview platform with trained AI models using ReactJS, NodeJS, and Python.
   <br>
	●	Boosted PostgreSQL performance by 80% using Redis caching for frequent queries and session management.
    <br>
    ●	Built text-to-speech and speech-to-text APIs with MeloTTS and Whisper, achieving 4.5/5 naturalness rating and 95% transcription accuracy.
    <br>
    ●	Collaborated with data science team to develop AI-powered interview feedback models achieving 95%+ accuracy, resulting in improved user performance and interview preparation.
    <br><br>
   </div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("<h5><strong>Software Engineer Intern | Lacaco Wholesales | Garden Grove, CA</strong></h5>",unsafe_allow_html=True)
    st.markdown("<h5><strong>05/ 2023 - 08/ 2023</strong></h5>",unsafe_allow_html=True)
    st.markdown(
        """
   <div>
   	●	Developed an automatic tool for customer inquiries with Python, Gmail API, and AWS – EC2, resulting in a 50% reduction in response time.
   <br>
	●	Achieved a 95%+ accuracy rate in email classification by prompting ChatGPT-based models, resulting in efficient work assignment to appropriate teams.
    <br>
    ●	Boosted operational efficiency by 20% with Python and Drive API, formatting vendor prices and distributing updated prices to the sales team.
   </div>
""",
        unsafe_allow_html=True,
    )
if 'Education' in select:
    col1,col2,col3 = st.columns([2.5,3,1])
    with col2:
        st.subheader("Education")
    st.markdown(
        """
                <div>
   <strong> Orange Coast College at Costa Mesa | Costa Mesa, CA</strong>
    <br>
   <strong> A.S. in Computer Science (In Progress) | </strong> GPA: 4.0/4.0
    <br>
   <strong> Expected Graduation Date:</strong> May 2025
    <br>
    <strong> Relavant Coursework:</strong>  C++, Data Structures and Algorithms, Object-Oriented Programming, Python, Java, HTML/CSS, Javascript
""",
        unsafe_allow_html=True,
    )
