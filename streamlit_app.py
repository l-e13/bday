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
        
        # Create a button for each word using markdown
        with cols[i % 4]:
            if st.button(word, key=word):
                if word in st.session_state.selected_words:
                    st.session_state.selected_words.remove(word)
                else:
                    if len(st.session_state.selected_words) < 4:
                        st.session_state.selected_words.append(word)
        
        # Use st.markdown to display the button with color (you can customize the styling as needed)
        st.markdown(
            f'<button style="background-color: {color}; color: black; border: none; border-radius: 5px; padding: 10px; cursor: pointer; width: 100%;">{word}</button>',
            unsafe_allow_html=True
        )

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
    st.title("🎉 Happy Birthday, [Your Friend's Name]! 🎉")
    st.write("I made this special card just for you. Hope you enjoy the game too!")

    # Button to start the game
    if st.button("Start the Connections Game"):
        connections_game()

if __name__ == "__main__":
    main()


