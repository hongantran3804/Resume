import streamlit as st
from PIL import Image

st.set_page_config("Home", layout="centered")

image = Image.open("newimg.png")
with open("HongAnTran Resume.pdf", "rb") as f:
    pdf = f.read()
col1, col2 = st.columns([1, 1.5])
with col1:
    st.image(image, width=268)
with col2:
    st.markdown("<h4>Hong An Tran</h4>", unsafe_allow_html=True)
    st.markdown(
        "A Computer Science student seeking a summer Software Engineering internship."
    )
    st.download_button(
        label=" 📄 Download Resume",
        data=pdf,
        file_name="HongAnTran Resume.pdf",
        mime="application/pdf",
    )
    st.markdown(
        "Email: <u style='color: blue;'>hongantran3804@gmail.com</u>",
        unsafe_allow_html=True,
    )
    col21, col22, col23 = st.columns([3, 1.2, 1])
    with col21:
        st.markdown("Phone number: (714) 719-6372")
    with col22:
        st.markdown(
            "<a href='https://www.linkedin.com/in/hong-an-tran-4846b6255/'><u style='blue'>Linkedin</u></a>",
            unsafe_allow_html=True,
        )
    with col23:
        st.markdown(
            "<a href='https://github.com/hongantran3804?tab=repositories'><u style='blue'>Github</u></a>",
            unsafe_allow_html=True,
        )

select = st.multiselect(
    label="Select options",
    options=["Technical Skills", "Work Experience", "Education"],
    default=["Technical Skills", "Work Experience", "Education"],
)

if "Education" in select:
    st.subheader("Education")
    st.markdown(
        """
                <div>
   <strong> Cal Poly Pomona || Pomona, CA</strong>
    <br>
   <strong> B.S. Computer Science | </strong> GPA: 4.0/4.0
    <br>
   <strong> Expected Graduation Date:</strong> May 2027
    <br><br>
""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
                <div>
   <strong> Orange Coast College || Costa Mesa, CA</strong>
    <br>
   <strong> A.S. Computer Science | </strong> GPA: 4.0/4.0
    <br>
   <strong> Expected Graduation Date:</strong> May 2025
    <br>
    <strong> Relavant Coursework:</strong>  Data Structures and Algorithms, Object-Oriented Programming
""",
        unsafe_allow_html=True,
    )
if "Work Experience" in select:
    st.subheader("Work Experience")
    with open("Lacaco_WorkFlow.pdf", "rb") as f:
        work_flow = f.read()

    st.markdown(
        "<h5><strong>CodeDay Labs | Open Source Contributor | Remote</strong></h5>",
        unsafe_allow_html=True,
    )
    st.markdown("<h5><strong>04/ 2025 – 05/ 2025</strong></h5>", unsafe_allow_html=True)
    st.markdown(
        """
   <div>
   	●	Contributed to HuggingChat, an open-source chat UI with 1.2 million active users and 42 million monthly visits.
   <br>
    ●	Developed a <a href = 'https://github.com/huggingface/chat-ui/pull/1823'><u style='color: blue'>pop-up search</u></a> feature (Ctrl/Cmd + K) using Svelte, TypeScript, MongoDB, and Docker to enable real-time conversation lookup via client-side filtering.
    <br><br>
   </div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h5><strong>Product Manager Accelerator | Software Engineer Intern | Remote</strong></h5>",
        unsafe_allow_html=True,
    )
    st.markdown("<h5><strong>09/ 2024 – 12/ 2024</strong></h5>", unsafe_allow_html=True)
    st.markdown(
        """
   <div>
   	●	Developed an AI-powered platform to help students practice their interviewing skills with the AI interviewer.
   <br>
    ●	Collaborated with data science team to develop AI-powered interview feedback models, resulting in improved interview preparation.
    <br>
    ●	Deployed platform using AWS (EC2, RDS, ElastiCache), Nginx, and Docker, ensuring scalability and efficient resource management.
    <br><br>
   </div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h5><strong>Lacaco Wholesales | Software Engineer Intern | Hungtington Beach, CA</strong></h5>",
        unsafe_allow_html=True,
    )
    st.markdown("<h5><strong>05/ 2023 - 08/ 2023</strong></h5>", unsafe_allow_html=True)
    st.markdown(
        """
   <div>
   	●	Built an automated email response system to streamline customer support with Python, Gmail API, and AWS – EC2, resulting in a 50% reduction in response time.
   <br>
	●	Achieved a 95%+ accuracy rate in email classification using OPENAI model, resulting in efficient work assignment to appropriate teams.
    <br>
    ●	Boosted operational efficiency by 20% with Python and Drive API, formatting vendor prices and distributing updated prices to the sales team.
   </div>
""",
        unsafe_allow_html=True,
    )
if "Technical Skills" in select:

    st.subheader("Technical Skills")
    st.markdown(
        """
   <div>
   	●	C++, Python, Java, Javascript, Typescript, Git, HTML/CSS
   <br>
	●	AWS, Google APIs, ReactJS, NodeJS, Docker, Nginx, MongoDB, Prisma, PostgreSQL, Selenium, Stripe
    <br>
   </div>
""",
        unsafe_allow_html=True,
    )
