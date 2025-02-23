import streamlit as st

Game State Management

if 'scene' not in st.session_state: st.session_state.scene = "intro" st.session_state.choices_made = []

def make_choice(choice, next_scene): st.session_state.choices_made.append(choice) st.session_state.scene = next_scene st.experimental_rerun()

Game Scenes

def intro(): st.title("Blood & Shadow: The Curse of the Volga") st.write("A Viking tale of fate, war, and the supernatural.") st.write("You are Eirik Thorsson, a Viking warrior who has returned home to a simple farm life. But the past does not rest.") st.write("One morning, you wake up to a strange whisper on the wind.")

st.button("Investigate the whisper", on_click=make_choice, args=("Investigate", "scene_1"))
st.button("Ignore it and focus on farming", on_click=make_choice, args=("Ignore", "scene_1"))
st.button("Speak a prayer to Odin for guidance", on_click=make_choice, args=("Pray", "scene_1"))

def scene_1(): st.title("Act I: The Haunting of the Homeland") st.write("Over the next few days, small disturbances appear. The air is colder than it should be. A raven perches outside your house, watching.") st.write("One of your old warband members, Ulf, is found dead – his body strangely bloated, as if drowned on dry land.")

st.button("Inspect the body", on_click=make_choice, args=("Inspect", "scene_2"))
st.button("Seek out the village Seer", on_click=make_choice, args=("Seer", "scene_2"))
st.button("Burn the body without question", on_click=make_choice, args=("Burn", "scene_2"))

def scene_2(): st.title("Act II: The Descent into the Cursed Past") st.write("The whispers grow stronger. The dreams of a burning village haunt your sleep. A foreign merchant mutters, 'The river remembers.'")

st.button("Demand the merchant explain", on_click=make_choice, args=("Demand", "scene_3"))
st.button("Threaten him for answers", on_click=make_choice, args=("Threaten", "scene_3"))
st.button("Let him leave, but his words linger", on_click=make_choice, args=("Let go", "scene_3"))

def scene_3(): st.title("Act III: The Reckoning of the Volga") st.write("The spirits of the Volga rise to pass judgment. The shaman’s spirit offers you a final deal.")

st.button("Accept the bargain and take power", on_click=make_choice, args=("Power", "ending"))
st.button("Reject the deal and fight", on_click=make_choice, args=("Fight", "ending"))
st.button("Offer yourself as sacrifice", on_click=make_choice, args=("Sacrifice", "ending"))

def ending(): st.title("Final Fate") last_choice = st.session_state.choices_made[-1]

if last_choice == "Power":
    st.write("You embrace your fate and take the throne of the restless dead, ruling the spectral warriors of the Volga.")
elif last_choice == "Fight":
    st.write("You stand defiant, but the battle was lost before it began. The curse does not break, and the cycle continues.")
elif last_choice == "Sacrifice":
    st.write("You offer yourself to the spirits. The whispers fade, and the curse is lifted—but at the cost of your own soul.")

st.write("The river remembers. Always.")
st.button("Restart", on_click=lambda: st.session_state.update(scene="intro", choices_made=[]))

Scene Router

if st.session_state.scene == "intro": intro() elif st.session_state.scene == "scene_1": scene_1() elif st.session_state.scene == "scene_2": scene_2() elif st.session_state.scene == "scene_3": scene_3() elif st.session_state.scene == "ending": ending()

