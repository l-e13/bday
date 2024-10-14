import streamlit as st

def main():
    st.title("🎉 Happy 22nd Eva! 🤠")
    st.write("You're pretty great. You're always making me laugh. Hope you have a sweet day")
    st.write("Told ya I'd code something to celebrate my favorite google intern (hopefully employee soon)")

    # Embed the personalized connections game
    st.subheader("Check out your Personalized Connections Game!")
    st.components.v1.iframe("https://custom-connections-game.vercel.app/F5f5Siaz1RhixW9glhOi", height=600, width=800)

if __name__ == "__main__":
    main()
