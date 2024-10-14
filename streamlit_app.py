import streamlit as st

def main():
    st.title("🎉 Happy Birthday, [Your Friend's Name]! 🎉")
    st.write("I made this special card just for you. Hope you enjoy the game too!")

    # Embed the personalized connections game
    st.subheader("Check out your Personalized Connections Game!")
    st.components.v1.iframe("https://custom-connections-game.vercel.app/F5f5Siaz1RhixW9glhOi", height=600, width=800)

if __name__ == "__main__":
    main()
