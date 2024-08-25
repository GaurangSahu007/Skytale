{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "463256bc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\sahug\\anaconda3\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: pandas in c:\\users\\sahug\\anaconda3\\lib\\site-packages (2.0.3)\n",
      "Requirement already satisfied: openpyxl in c:\\users\\sahug\\anaconda3\\lib\\site-packages (3.0.10)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (5.4.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (1.8.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (10.2.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (5.27.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from pandas) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: et_xmlfile in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from openpyxl) (1.1.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: narwhals>=1.1.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.5.5)\n",
      "Requirement already satisfied: colorama in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\sahug\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit pandas openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "089073d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-08-25 10:40:50.295 No runtime found, using MemoryCacheStorageManager\n",
      "2024-08-25 10:40:56.670 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load datasets\n",
    "d1_path = 'Application_Ranking_Combined.xlsx'\n",
    "d2_path = 'Application_Ranking_by_Category.xlsx'\n",
    "d3_path = 'Application_Ranking_by_Genre.xlsx'\n",
    "\n",
    "# Load the data\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    df_d1 = pd.read_excel(d1_path)\n",
    "    df_d2 = pd.read_excel(d2_path, sheet_name=None)  # Load all sheets as dict\n",
    "    df_d3 = pd.read_excel(d3_path, sheet_name=None)  # Load all sheets as dict\n",
    "    return df_d1, df_d2, df_d3\n",
    "\n",
    "df_d1, df_d2, df_d3 = load_data()\n",
    "\n",
    "# Sidebar Controls\n",
    "st.sidebar.title(\"Application Ranking Viewer\")\n",
    "st.sidebar.write(\"Select your options to view top and bottom applications.\")\n",
    "\n",
    "# Select N for Top/Bottom applications\n",
    "n_value = st.sidebar.number_input(\"Enter N value:\", min_value=1, value=10)\n",
    "\n",
    "# Data Source Selection\n",
    "data_source = st.sidebar.radio(\"Select Data Source:\", (\"Combined Data (D1)\", \"By Category (D2)\", \"By Genre (D3)\"))\n",
    "\n",
    "# Filter by Category or Genre if D2 or D3 is selected\n",
    "category_selected = None\n",
    "genre_selected = None\n",
    "\n",
    "if data_source == \"By Category (D2)\":\n",
    "    category_selected = st.sidebar.selectbox(\"Select Category:\", list(df_d2.keys()))\n",
    "elif data_source == \"By Genre (D3)\":\n",
    "    genre_selected = st.sidebar.selectbox(\"Select Genre:\", list(df_d3.keys()))\n",
    "\n",
    "# Search Feature\n",
    "search_term = st.sidebar.text_input(\"Search for an application:\", \"\")\n",
    "\n",
    "# Main Display\n",
    "st.title(\"Application Ranking Viewer\")\n",
    "\n",
    "# Function to extract top and bottom N applications\n",
    "def extract_top_bottom(df, top_n, bottom_n):\n",
    "    if search_term:\n",
    "        df = df[df['Application'].str.contains(search_term, case=False, na=False)]\n",
    "    \n",
    "    top_apps = df.nsmallest(top_n, 'FinalRank')[['Application', 'Downloads', 'Reviews', 'Ratings', 'FinalRank']]\n",
    "    bottom_apps = df.nlargest(bottom_n, 'FinalRank')[['Application', 'Downloads', 'Reviews', 'Ratings', 'FinalRank']]\n",
    "    return top_apps, bottom_apps\n",
    "\n",
    "# Display Data\n",
    "if data_source == \"Combined Data (D1)\":\n",
    "    top_apps, bottom_apps = extract_top_bottom(df_d1, n_value, n_value)\n",
    "    st.subheader(f\"Top {n_value} Applications from D1\")\n",
    "    st.table(top_apps)\n",
    "    st.subheader(f\"Bottom {n_value} Applications from D1\")\n",
    "    st.table(bottom_apps)\n",
    "elif data_source == \"By Category (D2)\" and category_selected:\n",
    "    df_category = df_d2[category_selected]\n",
    "    top_apps, bottom_apps = extract_top_bottom(df_category, n_value, n_value)\n",
    "    st.subheader(f\"Top {n_value} Applications from D2 - Category: {category_selected}\")\n",
    "    st.table(top_apps)\n",
    "    st.subheader(f\"Bottom {n_value} Applications from D2 - Category: {category_selected}\")\n",
    "    st.table(bottom_apps)\n",
    "elif data_source == \"By Genre (D3)\" and genre_selected:\n",
    "    df_genre = df_d3[genre_selected]\n",
    "    top_apps, bottom_apps = extract_top_bottom(df_genre, n_value, n_value)\n",
    "    st.subheader(f\"Top {n_value} Applications from D3 - Genre: {genre_selected}\")\n",
    "    st.table(top_apps)\n",
    "    st.subheader(f\"Bottom {n_value} Applications from D3 - Genre: {genre_selected}\")\n",
    "    st.table(bottom_apps)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "155afab3",
   "metadata": {},
   "outputs": [],
   "source": [
    "stre"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
