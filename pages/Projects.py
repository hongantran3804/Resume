import streamlit as st

st.set_page_config("Projects",layout="centered")

st.subheader("Wholesale Website (06/ 2024 – 07/ 2024)")
st.markdown(
    "<strong>Tech Stack:</strong> Javascript, NextJS, AWS, Google APIs, TailwindCSS, MongoDB, Prisma, Vercel",
    unsafe_allow_html=True,
)
st.markdown(
    """
<div>
●   Implemented Google Translate API and Google Maps APIs to improve the shopping experience and enable
real-time order tracking.
<br/>
●   Integrated Google reCAPTCHA, NextAuth, and NodeMailer to establish robust user authentication,
fortifying security measures.
<br/>
●   Achieved a significant 50% rendering speed increase through load balancing and CDN (Content
Delivery Network) on Vercel, AWS - CloudFront and AWS - S3.
<br/>
●   Utilized Prisma to optimize MongoDB queries, resulting in a 40% reduction in server response time.
</div>
""",
    unsafe_allow_html=True,
)
st.markdown(
    f"""<strong>Link:</strong> <a href = 'https://hongan-ecommerce-website.vercel.app/'><u style='color: blue'>HongAn-Eshop</u></a>""",
    unsafe_allow_html=True,
)

st.subheader("LinkedIn Jobs Scraping (10/ 2023 - 12/ 2023)")
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

st.subheader("Games | Space Invader (02/ 2023 - 03/ 2023)")
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
