import streamlit as st

st.set_page_config(
    page_title="Data Galeria",
    layout="wide"  # Use 'wide' to take full advantage of the screen space
)
# Title
st.title("Hi 👋, I'm Srinag Marni")
st.write(
    "### Graduate student in Data Science at the State University of New York, Buffalo, "
    "and experienced .NET Developer with a passion for solving complex problems, exploring LLMs, "
    "Retrieval-Augmented Generation (RAG), and leveraging AI/ML technologies."
)

# Professional Experience
st.write("💼 I have professional experience as a **Systems Engineer at TCS**, developing standalone .NET applications for major automotive clients")
st.write("👨‍💻 Check out my GitHubs: [**Master's Data Science: msrinag**](https://github.com/msrinag) ,   [**BTech C.S.E: 20171CSE0680**](https://github.com/20171CSE0680)")
st.write("💬 Feel free to ask me about **LLM, RAT, RAG, .NET, Python, Machine Learning, AI, and Data Science**")
st.write("📫 How to reach me: **msrinag@gmail.com, srinagma@buffalo.edu**")
st.write("🌟 Know More | [Resume](https://drive.google.com/file/d/1ThOTlbARmXcL6apmDF-jB6F3k49bYYaa/view?usp=sharing)")

# Connect with Me
st.write("### Connect with me:")
st.markdown(
    """
    <a href="https://linkedin.com/in/srinag-marni" target="_blank">
        <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="srinag-marni" height="30" width="40" />
    </a>
    """, unsafe_allow_html=True
)

# Languages and Tools
st.write("### Languages and Tools:")
languages = [
    {"name": "dotnet", "url": "https://dotnet.microsoft.com/", "img": "https://raw.githubusercontent.com/devicons/devicon/master/icons/dot-net/dot-net-original-wordmark.svg"},
    {"name": "python", "url": "https://www.python.org", "img": "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"},
    {"name": "pandas", "url": "https://pandas.pydata.org/", "img": "https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg"},
    {"name": "selenium", "url": "https://www.selenium.dev/", "img": "https://raw.githubusercontent.com/devicons/devicon/master/icons/selenium/selenium-original.svg"},
    {"name": "flutter", "url": "https://flutter.dev/", "img": "https://raw.githubusercontent.com/devicons/devicon/master/icons/flutter/flutter-original.svg"},
    {"name": "LangChain", "url": "https://python.langchain.com/", "img": "https://avatars.githubusercontent.com/u/126733545?s=48&v=4?text=🦜️🔗"},
    {"name": "gemini", "url": "https://gemini.google.com/", "img": "https://avatars.githubusercontent.com/u/161781182?s=200&v=4"},
    {"name": "openai", "url": "https://openai.com/", "img": "https://github.com/user-attachments/assets/5f403872-dd92-4a6f-bc56-4d7b413e52b6"},
    {"name": "huggingface", "url": "https://huggingface.co/", "img": "https://huggingface.co/front/assets/huggingface_logo.svg"},
    {"name": "llama", "url": "https://github.com/facebookresearch/llama", "img": "https://avatars.githubusercontent.com/u/153379578?s=48&v=4?text=🦙"}
]
imgcol=st.columns([1 for i in languages])
imgi=0
for lang in languages:
    with imgcol[imgi]:
        st.markdown(
        f'<a href="{lang["url"]}" target="_blank" rel="noreferrer">'
        f'<img src="{lang["img"]}" alt="{lang["name"]}" width="40" height="40"/></a> ',
        unsafe_allow_html=True
        )
        imgi+=1

# Sample data for personal projects
projects = [
    {
        "name": "CipherStockX",
        "url": "https://github.com/msrinag/CipherStockX",
        "description": "Real-time Stock Analysis Platform - Decodes market trends and insights using AI.",
        "image": "https://raw.githubusercontent.com/msrinag/CipherStockX/refs/heads/main/Assets/Demo.gif"  # Replace with actual image URLs
    },
    {
        "name": "AutoPitch",
        "url": "https://github.com/msrinag/AutoPitch",
        "description": "Cold Email Generator - Generates customized cold emails from job postings.",
        "image": "https://raw.githubusercontent.com/msrinag/AutoPitch/refs/heads/main/assets/AutoPitch_Demo.gif"  # Replace with actual image URLs
    },
    {
        "name": "Story Image Generator",
        "url": "https://colab.research.google.com/drive/14o50hfO4eGWL47h2B4W_yUejPf_4fSYd?usp=sharing",
        "description": "Converts story paragraphs into illustrative images using Diffusion Models.",
        "image": "assets/storyimg.png"  # Replace with actual image URLs
    },
    {
        "name": "Car Resale Price Prediction App",
        "url": "https://pricemaster.streamlit.app/",
        "description": "ML model predicting resale prices.",
        "image": "assets/cars.png"  # Replace with actual image URLs
    },
    {
        "name": "Gesture Based Mouse Control",
        "description": "Face detection using image processing.",
        "image": "assets/Mouse Control-0694.gif"  # Replace with actual image URLs
    },
    {
        "name": "AI Weather Report",
        "url": "https://colab.research.google.com/drive/1Z_8bD2vdM8ohc2TpGwHENn6jc9suPaBo?usp=sharing",
        "description": "AI-driven tool providing real-time weather forecasts.",
        "image": "https://raw.githubusercontent.com/msrinag/AI-Weather-Report/refs/heads/main/resources/ai_weather_short.gif"  # Replace with actual image URLs
    },
    {
        "name": "Zomato Data Analysis",
        "url": "https://msrinag.github.io/dv/",
        "description": "Analyzes Zomato restaurant data to explore cuisine types.",
        "image": "https://brandmusiq.com/assets/work_banner_vyEql_Zomato.jpg"  # Replace with actual image URLs
    },
]

# Title
st.write("### Personal Projects:")

# Create data cards
cols = st.columns(3)  # Adjust the number based on how many cards you want per row

for index, project in enumerate(projects):
    with cols[index % 3]:  # Cycle through the columns
        st.image(project["image"], use_column_width=True)  # Use an actual image URL here
        st.markdown(f"**[{project['name']}]({project['url']})**" if "url" in project else f"**{project['name']}**")
        st.write(project["description"])