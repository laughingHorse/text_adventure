import time
import streamlit as st

def slow_print(text):
    st.write(f"<p style='text-align: justify;'>{text}</p>", unsafe_allow_html=True)

def main():
    st.title("The Outcast’s Saga: A Viking Text Adventure")
    if "page" not in st.session_state:
        st.session_state.page = "intro"
    if "choice" not in st.session_state:
        st.session_state.choice = None
    
    if st.session_state.page == "intro":
        intro()
    elif st.session_state.page == "choose_path":
        choose_path()
    elif st.session_state.page == "iceland":
        iceland()
    elif st.session_state.page == "greenland":
        greenland()
    elif st.session_state.page == "gather_crew":
        gather_crew()
    elif st.session_state.page == "voyage":
        voyage()
    elif st.session_state.page == "voyage_prepared":
        voyage_prepared()
    elif st.session_state.page == "vinland":
        vinland()
    elif st.session_state.page == "peaceful_contact":
        peaceful_contact()
    elif st.session_state.page == "conflict":
        conflict()
    elif st.session_state.page == "escape":
        escape()
    elif st.session_state.page == "end_game":
        end_game()

def intro():
    slow_print("You are Luke Bealesson, a handsome Viking warrior cast out from Norway for a crime you may or may not have committed... Let's face it you did commit the crime but ask for forgiveness not permission ammiright?")
    if st.button("Continue"):
        st.session_state.page = "choose_path"
        st.rerun()

def choose_path():
    choice = st.radio("Do you sail to Iceland for safety and expensive beers, or take a bold course to the new lands of Greenland?", ("Iceland", "Greenland"))
    if st.button("Confirm Choice"):
        st.session_state.choice = choice
        st.session_state.page = "iceland" if choice == "Iceland" else "greenland"
        st.rerun()

def iceland():
    slow_print("You arrive in Iceland, battered but alive. You just want to get some dinner but the settlers here do not trust an exile...")
    choice = st.radio("You hear tales of a vast land beyond Greenland. What do you do?", ("Gather a crew", "Try to survive here"))
    if st.button("Confirm Choice"):
        st.session_state.choice = choice
        if choice == "Gather a crew":
            st.session_state.page = "gather_crew"
        else:
            st.session_state.page = "end_game"
        st.rerun()

def end_game():
    slow_print("You live a hard life with your goat and chickens, frostbite takes you nose. You are never truly accepted. Your saga ends here.")
    if st.button("Restart Game"):
        st.session_state.page = "intro"
        st.rerun()

def greenland():
    slow_print("You make landfall in the harsh ice of Greenland. The settlers are wary but let you stay...")
    if st.button("Continue"):
        st.session_state.page = "gather_crew"
        st.rerun()

def gather_crew():
    slow_print("You recruit outcasts, debt-ridden farmers, and mercenaries. Together, you build a longship...")
    choice = st.radio("A seer throws some rat bones and warns you: ‘You will go beyond the edge of maps, the bones predict a tough voyage! You will all perish! Ah HAHAHAHA!’", ("Heed the warning", "Dismiss it"))
    if st.button("Confirm Choice"):
        st.session_state.choice = choice
        if choice == "Heed the warning":
            slow_print("You take extra supplies and reinforce your ship, preparing for the unknown.")
            st.session_state.page = "voyage_prepared"
        else:
            st.session_state.page = "voyage"
        st.rerun()

def voyage():
    slow_print("Your longship sets sail into the unknown... but you lack enough provisions, and a storm forces you back!")
    slow_print("Without proper preparation, you are forced to return to Greenland in disgrace.")
    if st.button("Restart Game"):
        st.session_state.page = "intro"
        st.rerun()

def voyage_prepared():
    slow_print("Your longship sets sail into the unknown, well-stocked and reinforced for the dangers ahead...")
    if st.button("Continue"):
        st.session_state.page = "vinland"
        st.rerun()

def vinland():
    slow_print("Vinland is lush and full of resources. You encounter the Skraelings, the native people.")
    choice = st.radio("How do you approach them?", ("Trade peacefully", "Raid their village"))
    if st.button("Confirm Choice"):
        st.session_state.choice = choice
        st.session_state.page = "peaceful_contact" if choice == "Trade peacefully" else "conflict"
        st.rerun()

def peaceful_contact():
    slow_print("Trade goes well at first, but after a bad trade one of your crew slaps a Skraeling with a wet fish. The Skrealings take offence and attack in number and you run for the ships")
    if st.button("Continue"):
        st.session_state.page = "escape"
        st.rerun()

def conflict():
    slow_print("The Skraelings fight fiercely! Many of your crew fall, and you must retreat...")
    if st.button("Continue"):
        st.session_state.page = "escape"
        st.rerun()

def escape():
    slow_print("Your time in Vinland is over. You barely escape back to Greenland, your dreams shattered and many of your men dead.")
    if st.button("Restart Game"):
        st.session_state.page = "intro"
        st.rerun()

if __name__ == "__main__":
    main()
