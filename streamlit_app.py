import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Bluemerry Oatmeal')
streamlit.text('🥗Kale, spinach & Rocket smoothie')
streamlit.text('🐔Hard-Boiled Free-range Egg')
streamlit.text('🥑🍞Hard-Boiled Free-range Egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
