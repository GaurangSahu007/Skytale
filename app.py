{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ebc19e70",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#!pip install streamlit pandas openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4db19b9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-08-25 11:01:39.012 No runtime found, using MemoryCacheStorageManager\n"
     ]
    },
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: '/Application_Ranking_Combined.xlsx'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 17\u001b[0m\n\u001b[0;32m     14\u001b[0m     df_d3 \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(d3_path, sheet_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m)  \u001b[38;5;66;03m# Load all sheets as dict\u001b[39;00m\n\u001b[0;32m     15\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m df_d1, df_d2, df_d3\n\u001b[1;32m---> 17\u001b[0m df_d1, df_d2, df_d3 \u001b[38;5;241m=\u001b[39m load_data()\n\u001b[0;32m     19\u001b[0m \u001b[38;5;66;03m# Sidebar Controls\u001b[39;00m\n\u001b[0;32m     20\u001b[0m st\u001b[38;5;241m.\u001b[39msidebar\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mApplication Ranking Viewer\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\caching\\cache_utils.py:168\u001b[0m, in \u001b[0;36mmake_cached_func_wrapper.<locals>.wrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    166\u001b[0m \u001b[38;5;129m@functools\u001b[39m\u001b[38;5;241m.\u001b[39mwraps(info\u001b[38;5;241m.\u001b[39mfunc)\n\u001b[0;32m    167\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mwrapper\u001b[39m(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs):\n\u001b[1;32m--> 168\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m cached_func(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\caching\\cache_utils.py:197\u001b[0m, in \u001b[0;36mCachedFunc.__call__\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    195\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_info\u001b[38;5;241m.\u001b[39mshow_spinner \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_info\u001b[38;5;241m.\u001b[39mshow_spinner, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    196\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m spinner(message, _cache\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m):\n\u001b[1;32m--> 197\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_get_or_create_cached_value(args, kwargs)\n\u001b[0;32m    198\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    199\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_get_or_create_cached_value(args, kwargs)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\caching\\cache_utils.py:224\u001b[0m, in \u001b[0;36mCachedFunc._get_or_create_cached_value\u001b[1;34m(self, func_args, func_kwargs)\u001b[0m\n\u001b[0;32m    222\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m CacheKeyNotFoundError:\n\u001b[0;32m    223\u001b[0m     \u001b[38;5;28;01mpass\u001b[39;00m\n\u001b[1;32m--> 224\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_handle_cache_miss(cache, value_key, func_args, func_kwargs)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\caching\\cache_utils.py:280\u001b[0m, in \u001b[0;36mCachedFunc._handle_cache_miss\u001b[1;34m(self, cache, value_key, func_args, func_kwargs)\u001b[0m\n\u001b[0;32m    276\u001b[0m \u001b[38;5;66;03m# We acquired the lock before any other thread. Compute the value!\u001b[39;00m\n\u001b[0;32m    277\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_info\u001b[38;5;241m.\u001b[39mcached_message_replay_ctx\u001b[38;5;241m.\u001b[39mcalling_cached_function(\n\u001b[0;32m    278\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_info\u001b[38;5;241m.\u001b[39mfunc, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_info\u001b[38;5;241m.\u001b[39mallow_widgets\n\u001b[0;32m    279\u001b[0m ):\n\u001b[1;32m--> 280\u001b[0m     computed_value \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_info\u001b[38;5;241m.\u001b[39mfunc(\u001b[38;5;241m*\u001b[39mfunc_args, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mfunc_kwargs)\n\u001b[0;32m    282\u001b[0m \u001b[38;5;66;03m# We've computed our value, and now we need to write it back to the cache\u001b[39;00m\n\u001b[0;32m    283\u001b[0m \u001b[38;5;66;03m# along with any \"replay messages\" that were generated during value computation.\u001b[39;00m\n\u001b[0;32m    284\u001b[0m messages \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_info\u001b[38;5;241m.\u001b[39mcached_message_replay_ctx\u001b[38;5;241m.\u001b[39m_most_recent_messages\n",
      "Cell \u001b[1;32mIn[6], line 12\u001b[0m, in \u001b[0;36mload_data\u001b[1;34m()\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;129m@st\u001b[39m\u001b[38;5;241m.\u001b[39mcache_data\n\u001b[0;32m     11\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mload_data\u001b[39m():\n\u001b[1;32m---> 12\u001b[0m     df_d1 \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(d1_path)\n\u001b[0;32m     13\u001b[0m     df_d2 \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(d2_path, sheet_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m)  \u001b[38;5;66;03m# Load all sheets as dict\u001b[39;00m\n\u001b[0;32m     14\u001b[0m     df_d3 \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(d3_path, sheet_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m)  \u001b[38;5;66;03m# Load all sheets as dict\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\excel\\_base.py:478\u001b[0m, in \u001b[0;36mread_excel\u001b[1;34m(io, sheet_name, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, parse_dates, date_parser, date_format, thousands, decimal, comment, skipfooter, storage_options, dtype_backend)\u001b[0m\n\u001b[0;32m    476\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(io, ExcelFile):\n\u001b[0;32m    477\u001b[0m     should_close \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m--> 478\u001b[0m     io \u001b[38;5;241m=\u001b[39m ExcelFile(io, storage_options\u001b[38;5;241m=\u001b[39mstorage_options, engine\u001b[38;5;241m=\u001b[39mengine)\n\u001b[0;32m    479\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m engine \u001b[38;5;129;01mand\u001b[39;00m engine \u001b[38;5;241m!=\u001b[39m io\u001b[38;5;241m.\u001b[39mengine:\n\u001b[0;32m    480\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    481\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEngine should not be specified when passing \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    482\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124man ExcelFile - ExcelFile already has the engine set\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    483\u001b[0m     )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\excel\\_base.py:1496\u001b[0m, in \u001b[0;36mExcelFile.__init__\u001b[1;34m(self, path_or_buffer, engine, storage_options)\u001b[0m\n\u001b[0;32m   1494\u001b[0m     ext \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mxls\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1495\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m-> 1496\u001b[0m     ext \u001b[38;5;241m=\u001b[39m inspect_excel_format(\n\u001b[0;32m   1497\u001b[0m         content_or_path\u001b[38;5;241m=\u001b[39mpath_or_buffer, storage_options\u001b[38;5;241m=\u001b[39mstorage_options\n\u001b[0;32m   1498\u001b[0m     )\n\u001b[0;32m   1499\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ext \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m   1500\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m   1501\u001b[0m             \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mExcel file format cannot be determined, you must specify \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1502\u001b[0m             \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124man engine manually.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1503\u001b[0m         )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\excel\\_base.py:1371\u001b[0m, in \u001b[0;36minspect_excel_format\u001b[1;34m(content_or_path, storage_options)\u001b[0m\n\u001b[0;32m   1368\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(content_or_path, \u001b[38;5;28mbytes\u001b[39m):\n\u001b[0;32m   1369\u001b[0m     content_or_path \u001b[38;5;241m=\u001b[39m BytesIO(content_or_path)\n\u001b[1;32m-> 1371\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m get_handle(\n\u001b[0;32m   1372\u001b[0m     content_or_path, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m\"\u001b[39m, storage_options\u001b[38;5;241m=\u001b[39mstorage_options, is_text\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m   1373\u001b[0m ) \u001b[38;5;28;01mas\u001b[39;00m handle:\n\u001b[0;32m   1374\u001b[0m     stream \u001b[38;5;241m=\u001b[39m handle\u001b[38;5;241m.\u001b[39mhandle\n\u001b[0;32m   1375\u001b[0m     stream\u001b[38;5;241m.\u001b[39mseek(\u001b[38;5;241m0\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\common.py:868\u001b[0m, in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    859\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(\n\u001b[0;32m    860\u001b[0m             handle,\n\u001b[0;32m    861\u001b[0m             ioargs\u001b[38;5;241m.\u001b[39mmode,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    864\u001b[0m             newline\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    865\u001b[0m         )\n\u001b[0;32m    866\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    867\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[1;32m--> 868\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n\u001b[0;32m    869\u001b[0m     handles\u001b[38;5;241m.\u001b[39mappend(handle)\n\u001b[0;32m    871\u001b[0m \u001b[38;5;66;03m# Convert BytesIO or file objects passed with an encoding\u001b[39;00m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '/Application_Ranking_Combined.xlsx'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load datasets\n",
    "d1_path = '/Application_Ranking_Combined.xlsx'\n",
    "d2_path = '/Application_Ranking_by_Category.xlsx'\n",
    "d3_path = '/Application_Ranking_by_Genre.xlsx'\n",
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
   "execution_count": 4,
   "id": "9d1b1e20",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3737097518.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[4], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run app.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run app.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1768125f",
   "metadata": {},
   "outputs": [],
   "source": []
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
