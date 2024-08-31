#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd

# Load the data
@st.cache_data
def load_data():
    df_d1 = pd.read_excel(d1_path)
    df_d2 = pd.read_excel(d2_path, sheet_name=None)  # Load all sheets as dict
    df_d3 = pd.read_excel(d3_path, sheet_name=None)  # Load all sheets as dict
    
    # Ensure 'Sub Genre' NaN values are treated as blank for all datasets
    df_d1['Sub Genre'] = df_d1.get('Sub Genre', pd.Series()).fillna('')
    for df in df_d2.values():
        df['Sub Genre'] = df.get('Sub Genre', pd.Series()).fillna('')
    for df in df_d3.values():
        df['Sub Genre'] = df.get('Sub Genre', pd.Series()).fillna('')
    
    return df_d1, df_d2, df_d3

# Load datasets
d1_path = 'Application_Ranking_Combined.xlsx'
d2_path = 'Application_Ranking_by_Category.xlsx'
d3_path = 'Application_Ranking_by_Genre.xlsx'

df_d1, df_d2, df_d3 = load_data()

def set_dynamic_header(selected_filter, category_selected=None):
    filter_text = {"Overall Data": "(Overall Data)", "By Category": f"({category_selected} Apps)", "By Genre": "(By Genre)"}
    return f"THE ADVENT OF SMARTPHONE APPLICATIONS RANKING<br><span style='font-size:20px;'>{filter_text.get(selected_filter, '')}</span>"

# Sidebar Controls
st.sidebar.image("SCMHRD.png", use_column_width=True)
st.sidebar.markdown('<h2 style="text-align: center;">Filters</h2>', unsafe_allow_html=True)
search_query = st.sidebar.text_input("Search by Name:")
n_value = st.sidebar.number_input("Enter N value:", min_value=1, value=5)
data_source = st.sidebar.radio("Select Data Source:", ("Overall Data", "By Category", "By Genre"))

category_selected, genre_selected, sub_genre_selected = None, None, None

if data_source == "By Category":
    category_selected = st.sidebar.selectbox("Select Category:", list(df_d2.keys()))
elif data_source == "By Genre":
    genre_df_sorted = df_d1.groupby('Genre')['FinalScore'].sum().reset_index().sort_values(by='FinalScore', ascending=False)
    genre_options = [f"{genre} ({len(df_d3[genre]['Sub Genre'].unique())} | {len(df_d3[genre])})" for genre in genre_df_sorted['Genre']]
    genre_selected = st.sidebar.selectbox("Select Genre (Total Sub Genre | Total Application):", genre_options).split(" (")[0]
    df_genre = df_d3[genre_selected]
    sub_genres = [sub_genre for sub_genre in df_genre['Sub Genre'].unique() if sub_genre.strip()]
    sub_genre_selected = st.sidebar.multiselect("Select Sub Genre(s):", options=sub_genres) if sub_genres else None
    df_genre = df_genre[df_genre['Sub Genre'].isin(sub_genre_selected)] if sub_genre_selected else df_genre

# Display Header
st.markdown(
    f"""
    <style>.header {{ font-size:30px; font-weight:bold; text-align: center; padding: 10px; background-color: #006400; color: white; }}</style>
    <div class="header">{set_dynamic_header(data_source, category_selected)}</div>
    """, unsafe_allow_html=True)

# Sidebar Footer
st.sidebar.markdown('<div class="sidebar-footer">Created by Team Great Knight Eagle</div>', unsafe_allow_html=True)

# Function to Extract and Display Applications
def display_top_bottom_applications(df, n):
    rank_1_score = df['FinalScore'].max()
    df['ScoreDifference'] = df['FinalScore'] - rank_1_score
    top_apps = df.nsmallest(n, 'FinalRank').round({'FinalRank': 2, 'Ratings': 2})
    bottom_apps = df.nlargest(n, 'FinalRank').round({'FinalRank': 2, 'Ratings': 2})
    st.markdown(f"<h3 style='text-align: center;' class='underline'>Top {n} Applications</h3>", unsafe_allow_html=True)
    st.dataframe(top_apps.style.set_properties(**{'background-color': '#89C55F', 'color': 'white'}))
    st.markdown(f"<h3 style='text-align: center;' class='underline'>Bottom {n} Applications</h3>", unsafe_allow_html=True)
    st.dataframe(bottom_apps.style.set_properties(**{'background-color': '#8B0000', 'color': 'white'}))

# Apply Global Search Filter
if search_query:
    df_d1 = df_d1[df_d1['Application'].str.contains(search_query, case=False, na=False)]
    df_d2 = {k: v[v['Application'].str.contains(search_query, case=False, na=False)] for k, v in df_d2.items()}
    df_d3 = {k: v[v['Application'].str.contains(search_query, case=False, na=False)] for k, v in df_d3.items()}

# Display Data Based on Selected Filter
if data_source == "Overall Data":
    display_top_bottom_applications(df_d1, n_value)
elif data_source == "By Category" and category_selected:
    display_top_bottom_applications(df_d2[category_selected], n_value)
elif data_source == "By Genre" and genre_selected:
    st.markdown(f"<h3 style='text-align: center;' class='underline'>{genre_selected}</h3>", unsafe_allow_html=True)
    sub_genres_display = ' | '.join(sub_genres) if sub_genres else "No Sub Genres"
    st.markdown(f"<h4 style='text-align: left;'>Total Sub Genres: {len(sub_genres)}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: left;'>Name of Sub Genres: {sub_genres_display}</h4>", unsafe_allow_html=True)
    display_top_bottom_applications(df_genre, n_value)

# Global Footer
st.markdown(
    """
    <style>.footer { font-size:16px; text-align: center; padding: 10px; background-color: #006400; color: white; font-weight: bold; }</style>
    <div class="footer">Created by Team Great Knight Eagle</div>
    """, unsafe_allow_html=True)

