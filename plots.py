import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


dfs = []

# Loop over the feather files and read them into data frames
for i in range(1, 8):
    filename = f'toi_data_cleaned_part{i}.feather'
    df = pd.read_feather(filename)
    dfs.append(df)

# Concatenate the data frames into a single data frame
cleaned_data = pd.concat(dfs, ignore_index=True)


st.header('Analysis of word usage across years in TOI(Times Of India) ')
word_of_interest = st.text_input('Please enter the word/words')
st.write('Note: Enter the root word as all the combinations of the words are selected and multiple words can be entered with a comma and no spaces eg. "game,sport"' )
if st.button('Submit'):
    # Iterate over each year's data and extract the word count for the word of interest
    word_of_interest = word_of_interest.split(',')
    word_of_interest = [word.lower() for word in word_of_interest]
    # Create a list to store the word count for the word of interest for each year
    word_count_by_year = []

    # Iterate over each year's data and extract the word count for the word of interest
    for year in range(2002, 2023):
        year_data = cleaned_data[cleaned_data['Year'] == year]
        year_word_count = year_data.Content.str.count('|'.join(word_of_interest)).sum()
        word_count_by_year.append(year_word_count)

    # Plot a line graph of the word count across years
    # Generate the plot
    fig, ax = plt.subplots()
    ax.plot(range(2002, 2023), word_count_by_year)
    ax.set_xlabel("Year")
    ax.set_ylabel("Word count")
    ax.set_title(f"'{word_of_interest}' across years")

    # Display the plot using st.pyplot()
    st.pyplot(fig)



