import streamlit as st
import pandas as pd
import numpy as np

name=st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name} !!! Welcome here")

st.set_page_config(page_title="Data Science Portal", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", [
    "Home", 
    "Data Explorer", 
    "Visualizer", 
    "Statistical Summary", 
    "Machine Learning", 
    "About"
])

# --- COMPONENT 1: HOME ---
if selection == "Home":
    st.title("🚀 Welcome to my Data Science Portal")
    st.write("This portal showcases 6 different components built with Streamlit.")
    st.image("https://images.unsplash.com/photo-1551288049-bbda3865c670?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80")

# --- COMPONENT 2: DATA EXPLORER ---
elif selection == "Data Explorer":
    st.title("🔍 Data Explorer")
    upload_file = st.file_uploader("Upload a CSV file", type="csv")
    if upload_file:
        df = pd.read_csv(upload_file)
        st.write("### Raw Data Preview", df.head())
    else:
        st.info("Please upload a CSV file to begin.")

# --- COMPONENT 3: VISUALIZER ---
elif selection == "Visualizer":
    st.title("📊 Chart Visualizer")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
    st.line_chart(chart_data)
    st.bar_chart(chart_data)

# --- COMPONENT 4: STATISTICAL SUMMARY ---
elif selection == "Statistical Summary":
    st.title("📈 Statistical Summary")
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    st.write("### Descriptive Statistics", df.describe())

# --- COMPONENT 5: MACHINE LEARNING ---
elif selection == "Machine Learning":
    st.title("🤖 ML Playground")
    st.write("Adjust the parameters to simulate a model training.")
    epochs = st.slider("Number of Epochs", 1, 100, 10)
    learning_rate = st.select_slider("Learning Rate", options=[0.001, 0.01, 0.1, 1.0])
    st.success(f"Model ready to train with {epochs} epochs and {learning_rate} LR!")

# --- COMPONENT 6: ABOUT ---
elif selection == "About":
    st.title("ℹ️ About This Project")
    st.write("Developed for the Data Science and AI Class.")
    st.balloons()