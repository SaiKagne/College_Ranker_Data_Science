import pickle
from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
from annotated_text import annotated_text

st.set_page_config(page_title="College Ranker - Data Science", page_icon=":bar_chart:",
layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

names = ["Data Science Intern"]
usernames = ["Intern"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {"usernames":{}}
for un, name, pw in zip(usernames, names, hashed_passwords):
    user_dict = {"name":name,"password":pw}
    credentials["usernames"].update({un:user_dict})

authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lot_week1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
    lot_pro1 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_w51pcehl.json")
    lot_week2 = load_lottieurl('https://assets6.lottiefiles.com/private_files/lf30_wqypnpu5.json')
    lot_pro2 = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_bdlrkrqv.json')
    lot_week3 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_49rdyysj.json")
    lot_pro3 = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_ajzyv37m.json')
    lot_pro4 = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_zrqthn6o.json')
    lot_week4 = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_yEvR1T.json')

    with st.container():
        selected = option_menu(None, ['Week 1', 'Week 2','Week 3','Week 4'],
                    icons=["calendar-week", "calendar-week","calendar-week","calendar-week"],
                    menu_icon="cast", default_index = 0, orientation = 'horizontal',
                    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {"color": "black","font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"color": "white","background-color": "green"}})

    if selected == 'Week 1':
        with st.container():
            st.subheader("Hello Data Science Interns, I'm Saiprasad Kagne :wave:")
            left_column, right_column = st.columns(2)
            with left_column:
                st.write("""Welcome to the full fledged **Data Science Bootcamp** organized by College Ranker. In this bootcamp, you will study Python Language Concepts, Data Science Libraries , Data Analysis , Data Visualization and many more.""")
                st.write('[**Connect with me >**](https://www.linkedin.com/in/saiprasad-kagne-659a14198/)')

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("{} - Timeline & Instructions :dart:".format(selected))
                st.write("##")
                st.write(
                    """
                    Here, you will be studying **Python Language Concepts** for Data Science:
                    - Course content includes Python Basics, Data Structures, Programming Fundamentals and etc.
                    - Go through each and every course modules.
                    - Get the **sub-course** completion certificate.
                    """)
                st.write('[**Python for Data Science >**](https://cognitiveclass.ai/courses/python-for-data-science)')

            with right_column:
                st_lottie(lot_week1, height=300, key="coding")

        with st.container():
            st.write("---")
            st.header("{} - Project Assignment :white_check_mark:".format(selected))
            st.write("##")
            lottie_column, text_column = st.columns((1, 2))
            with lottie_column:
                st_lottie(lot_pro1)
            with text_column:
                st.subheader("Grade Average Calculator App in Python")
                st.write(
                    """
                    Learn how to use Python basic concepts such as user input, printing message,
                    storing data in the lists, using in-bulit functions and many more. **User interactions** make your app more engaging and fun.
                    In this Assignment, you will get good amount of **hands on experience** in Python.
                    """
                    )
                st.write("##")
                with open('DS_Week_1.zip', 'rb') as f:
                    st.download_button('Download Assignment', f, file_name = 'DS_Week_1.zip')

    elif selected == 'Week 2':
        with st.container():
            st.subheader("Data Analytics Fun Fact :wave:")
            left_column, right_column = st.columns(2)
            with left_column:
                st.write("""In a **Data Science** project, more than 60% of the time **Analyst** and **Scientist** spend on
                Data Analysis process such as Data Collection, Data Cleaning, Data Interpretation and etc.""")
                st.write('[**View Guide >**](https://careerfoundry.com/en/blog/data-analytics/the-data-analysis-process-step-by-step/)')

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("{} - Timeline & Instructions :dart:".format(selected))
                st.write("##")
                st.write(
                    """
                    Here, you will be studying **Data Analytics Concepts** for Data Science:
                    - Course content includes Importing Datasets, Preparing Data, Model Deployment and etc.
                    - Go through each and every course modules.
                    - Get the **sub-course** completion certificate.
                    """)
                st.write('[**Data Analytics with Python >**](https://cognitiveclass.ai/courses/data-analysis-python)')

            with right_column:
                st_lottie(lot_week2, height=300, key="coding")

        with st.container():
            st.write("---")
            st.header("{} - Project Assignment :white_check_mark:".format(selected))
            st.write("##")
            lottie_column, text_column = st.columns((1, 2))
            with lottie_column:
                st_lottie(lot_pro2)
            with text_column:
                st.subheader("Data Analytics - Hands on using Python")
                st.write(
                    """
                    Learn how to use Python Libraries concepts of **Numpy** & **Pandas** for Data Analytics process.
                    Operations such as Series, DataFrame, Groupby, Merge, Pivot Table and many more functions.
                    In this Assignment, you will get good amount of **hands on experience** in Python Libraries.
                    """
                    )
                st.write("##")
                with open('DS_Week_2.zip', 'rb') as f:
                    st.download_button('Download Assignment', f, file_name = 'DS_Week_2.zip')

    elif selected == 'Week 3':
        with st.container():
            st.subheader("Data Visualization Fun Fact :wave:")
            left_column, right_column = st.columns(2)
            with left_column:
                st.write("""A study found that in organizations using visual data discovery tools, **74%** of organizations
                that use visual data discovery empower managers to make **decisions** when necessary""")
                st.write('[**View Guide >**](https://piktochart.com/blog/data-visualization-statistics/)')

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("{} - Timeline & Instructions :dart:".format(selected))
                st.write("##")
                st.write(
                    """
                    Here, you will be studying **Data Visualization Concepts** for Data Science:
                    - Course content includes Area Chart, Bar Chart, Pie Chart and many more various charts.
                    - Go through each and every course modules.
                    - Get the **sub-course** completion certificate.
                    """)
                st.write('[**Data Visualization with Python >**](https://cognitiveclass.ai/courses/data-visualization-python)')

            with right_column:
                st_lottie(lot_week3, height=300, key="coding")

        with st.container():
            st.write("---")
            st.header("{} - Project Assignment :white_check_mark:".format(selected))
            st.write("##")
            lottie_column, text_column = st.columns((1, 2))
            with lottie_column:
                st_lottie(lot_pro3)
            with text_column:
                st.subheader("Data Visualization - Hands on using Python")
                st.write(
                    """
                    Learn how to use Python Libraries concepts of **Matplotlib** & **Seaborn** for Data Visualization process.
                    Advanced Plots such as Scatter Plot, Box Plot, Waffle Chart, Word Clouds, Regression Plot and many more plots.
                    In this Assignment, you will get good amount of **hands on experience** in Visualization Libraries.
                    """
                    )
                st.write("##")
                with open('DS_Week_3.zip', 'rb') as f:
                    st.download_button('Download Assignment', f, file_name = 'DS_Week_3.zip')

    else:
        with st.container():
            st.subheader("Data Science Fun Fact :wave:")
            left_column, right_column = st.columns(2)
            with left_column:
                st.write("""According to Data Science statistics, **91%** of the data used comprises text data. Similarly,
                unstructured data comprises **33%** images, **11%** audio, **15%** video, and **20%** other data.""")
                st.write('[**View Guide >**](https://www.bacancytechnology.com/blog/data-science-stats-and-facts)')

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("{} - Timeline & Instructions :dart:".format(selected))
                st.write("##")
                st.write(
                    """
                    Here, you will be building your **Data Science Internship Project** from scratch:
                    - Internship Project includes **Data Analytics** & **Data Visualization** concepts.
                    - Go through each and every internship content modules.
                    - Get the **Internship** completion certificate in the end.
                    """)
                st.write('[**Download Resources >**](https://drive.google.com/drive/folders/1wETzG5eTKkrrzKppNradqx17TW4XmjOe?usp=sharing)')

            with right_column:
                st_lottie(lot_week4, height=300, key="coding")

        with st.container():
            st.write("---")
            st.header("{} - Final Internship Assignment :white_check_mark:".format(selected))
            st.write("##")
            lottie_column, text_column = st.columns((1, 2))
            with lottie_column:
                st_lottie(lot_pro4)
            with text_column:
                st.subheader("Data Science - Internship Project in Python")
                st.write(
                    """
                    Learn how to combine features of multiple Python Libraries together such as **Numpy**, **Pandas**, **Matplotlib** & **Seaborn**
                    for Data Science process. You have to choose any **1** topic as your Internship Project from the given list of topics.
                    In this Final Assignment, you will get huge amount of **hands on experience** in Data Science field.
                    """
                    )
                st.write("##")
                with open('DS_Week_4.zip', 'rb') as f:
                    st.download_button('Download Internship Projects', f, file_name = 'DS_Week_4.zip')

    with st.container():
        st.write('---')
        st.write('##')
        logout_column, text_column = st.columns(2)
        with logout_column:
            authenticator.logout("Logout", "main")
        with text_column:
            annotated_text(("Developed", "by"),("Saiprasad Kagne", "Mentor",'#ed4539'),".")
