import streamlit as st
import random

# Function for the Connections Game
def connections_game():
    st.subheader("Connections Game")
    st.write("Group the words into categories related to your life!")

    # Game words and categories (Customize this list for your friend)
    words = [
        'Python', 'Java', 'C++', 'JavaScript',
        'Hiking', 'Reading', 'Gaming', 'Cooking',
        'Inside Joke 1', 'Inside Joke 2', 'Inside Joke 3', 'Inside Joke 4',
        'Data Structures', 'Algorithms', 'Machine Learning', 'Databases'
    ]
    
    categories = {
        'Programming Languages': ['Python', 'Java', 'C++', 'JavaScript'],
        'Hobbies': ['Hiking', 'Reading', 'Gaming', 'Cooking'],
        'Inside Jokes': ['Inside Joke 1', 'Inside Joke 2', 'Inside Joke 3', 'Inside Joke 4'],
        'Classes': ['Data Structures', 'Algorithms', 'Machine Learning', 'Databases']
    }
    
    # Shuffle words for randomness
    random.shuffle(words)
    
    # Store selected words in session state to keep track of user selections
    if 'selected_words' not in st.session_state:
        st.session_state.selected_words = []
    
    # Display words in a grid (4x4)
    st.write("### Select 4 words to group:")
    cols = st.columns(4)
    for i, word in enumerate(words):
        # Use color coding for selected words
        if word in st.session_state.selected_words:
            color = "lightgreen"
        else:
            color = "lightblue"
        
        # Create a button for each word
        with cols[i % 4]:
            if st.button(word, key=word, help=f"Click to select {word}", style=f"background-color: {color};"):
                if word in st.session_state.selected_words:
                    st.session_state.selected_words.remove(word)
                else:
                    if len(st.session_state.selected_words) < 4:
                        st.session_state.selected_words.append(word)

    st.write("Selected Words:", st.session_state.selected_words)
    
    # Submit button
    if st.button("Submit Group"):
        check_answer(st.session_state.selected_words, categories)

# Function to check the selected group against the correct categories
def check_answer(selected, categories):
    correct = False
    for category, items in categories.items():
        if set(selected) == set(items):
            correct = True
            st.success(f"Correct! The words belong to the '{category}' category.")
            break
    
    if not correct:
        st.error("Try again! The words don't match any category.")
    
    # Reset selected words after each submission
    st.session_state.selected_words = []

# Main birthday card display
def main():
    st.title("🎉 Happy 22nd Eva! 🤠")
    st.write("You're pretty great. You're always making me laugh. I hope you have a fun day")
    st.write("Told ya I'd code something to celebrate my favorite google intern")

    # Button to start the game
    if st.button("Start the Connections Game"):
        connections_game()

if __name__ == "__main__":
    main()

