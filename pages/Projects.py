import streamlit as st

st.set_page_config("Projects",layout="centered")

st.subheader("Wholesale Website (07/ 2024)")
st.markdown(
    "<strong>Tech Stack:</strong> Javascript, NextJS, AWS, Google APIs, TailwindCSS, MongoDB, Prisma, Vercel",
    unsafe_allow_html=True,
)
st.markdown(
    """
<div>
●   Developed an e-commerce platform for easy product search and purchase.
<br/>
●   Implemented Google Translate API and Google Maps APIs for multilingual shopping experiences and real-time order tracking.
<br/>
●   Integrated Google reCAPTCHA, NextAuth, and NodeMailer to establish robust user authentication,
fortifying security measures.
<br/>
●   Leveraged AWS (CloudFront, S3) and Vercel for high rendering speed and a seamless user experience.
<br/>
●   Achieved high server efficiency with Prisma by optimizing MongoDB queries.
</div>
""",
    unsafe_allow_html=True,
)
st.markdown(
    f"""<strong>Link:</strong> <a href = 'https://hongan-ecommerce-website.vercel.app/'><u style='color: blue'>HongAn-Eshop</u></a>""",
    unsafe_allow_html=True,
)

st.subheader("LinkedIn Jobs Scraping (12/ 2023)")
st.markdown("<strong>Tech Stack:</strong> Python, Selenium, Streamlit, Machine Learning", unsafe_allow_html=True)
st.markdown(
    """
<div>
●	Used Selenium to gather 1,000+ software engineer and data science jobs from LinkedIn automatically.
<br>
●	Created a dashboard for job analysis and salary prediction with 95% accuracy based on user data by
Streamlit and Machine Learning.
</div>
            """,
    unsafe_allow_html=True,
)
st.markdown("""
            <strong>Link: </strong>
            <a href = 'https://linkedin-job.streamlit.app/'><u style='color:blue'>LinkedIn-Job</u></a>
            """,unsafe_allow_html=True)

st.subheader("Games | Space Invader (03/ 2023)")
st.markdown(
    "<strong>Tech Stack:</strong> C++, Window API",
    unsafe_allow_html=True,
)
st.markdown(
    """
<div>
●	Developed a Space Invader game utilizing Object-Oriented Programming (OOP) principles, leveraging
data structures for efficient management and the Window API for rendering.
</div>
            """,
    unsafe_allow_html=True,
)

st.markdown("""<strong>Link: </strong>
        <a href='https://www.youtube.com/watch?v=cIVcRf7EKsQ'><u style='color:blue'>Space Invader</u></a>
            """,unsafe_allow_html=True)
