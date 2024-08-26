#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd

# Load datasets
d1_path = 'Application_Ranking_Combined.xlsx'
d2_path = 'Application_Ranking_by_Category.xlsx'
d3_path = 'Application_Ranking_by_Genre.xlsx'

# Load the data
@st.cache_data
def load_data():
    df_d1 = pd.read_excel(d1_path)
    df_d2 = pd.read_excel(d2_path, sheet_name=None)  # Load all sheets as dict
    df_d3 = pd.read_excel(d3_path, sheet_name=None)  # Load all sheets as dict
    return df_d1, df_d2, df_d3

df_d1, df_d2, df_d3 = load_data()

# Sidebar Controls
st.sidebar.title("Filter")

# Global Search Option
search_query = st.sidebar.text_input("Search Application by Name:")

# Select N for Top/Bottom applications
n_value = st.sidebar.number_input("Enter N value:", min_value=1, value=10)

# Data Source Selection
data_source = st.sidebar.radio("Select Data Source:", ("Overall Data", "By Category", "By Genre"))

# Filter by Category or Genre if D2 or D3 is selected
category_selected = None
genre_selected = None

if data_source == "By Category":
    category_selected = st.sidebar.selectbox("Select Category:", list(df_d2.keys()))
elif data_source == "By Genre":
    genre_selected = st.sidebar.selectbox("Select Genre:", list(df_d3.keys()))

# Main Display
st.title("Interactive Application Ranking Viewer")

# Function to extract top and bottom N applications
def extract_top_bottom(df, top_n, bottom_n):
    # Calculate ScoreDifference
    rank_1_score = df['FinalScore'].max()
    df['ScoreDifference'] = df['FinalScore'] - rank_1_score
    
    top_apps = df.nsmallest(top_n, 'FinalRank')
    bottom_apps = df.nlargest(bottom_n, 'FinalRank')
    return top_apps, bottom_apps

# Columns to Display
columns_to_display = ['FinalRank', 'Application', 'Genre', 'Sub Genre', 'FinalScore', 'ScoreDifference', 'Downloads', 'Reviews', 'Ratings']

# Display Data based on selected filter
if data_source == "Overall Data":
    if 'Genre' in df_d1.columns and 'Sub Genre' in df_d1.columns:
        columns_to_display.extend(['Genre', 'Sub Genre'])
    top_apps, bottom_apps = extract_top_bottom(df_d1, n_value, n_value)
    st.subheader(f"Total Applications: {df_d1.shape[0]}")
    st.subheader(f"Top {n_value} Applications from Overall Data")
    st.dataframe(top_apps[columns_to_display].reset_index(drop=True))
    st.subheader(f"Bottom {n_value} Applications from Overall Data")
    st.dataframe(bottom_apps[columns_to_display].reset_index(drop=True))
elif data_source == "By Category" and category_selected:
    df_category = df_d2[category_selected]
    if category_selected.lower() == "paid":
        columns_to_display.append('Purchase Price')
    top_apps, bottom_apps = extract_top_bottom(df_category, n_value, n_value)
    st.subheader(f"Total Applications: {df_category.shape[0]}")
    st.subheader(f"Top {n_value} {category_selected} Applications")
    st.dataframe(top_apps[columns_to_display].reset_index(drop=True))
    st.subheader(f"Bottom {n_value} {category_selected} Applications")
    st.dataframe(bottom_apps[columns_to_display].reset_index(drop=True))
elif data_source == "By Genre" and genre_selected:
    df_genre = df_d3[genre_selected]
    columns_to_display.extend(['Genre', 'Sub Genre'])  # Ensure Genre and Sub Genre are displayed
    top_apps, bottom_apps = extract_top_bottom(df_genre, n_value, n_value)
    st.subheader(f"Total Applications: {df_genre.shape[0]}")
    st.subheader(f"Top {n_value} Applications for Genre: {genre_selected}")
    st.dataframe(top_apps[columns_to_display].reset_index(drop=True))
    st.subheader(f"Bottom {n_value} Applications for Genre: {genre_selected}")
    st.dataframe(bottom_apps[columns_to_display].reset_index(drop=True))



# In[ ]:




