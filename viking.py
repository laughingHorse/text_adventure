import streamlit as st
import random
import json

# ---------------------------
# Helper functions & Game Setup
# ---------------------------

def initialize_game():
    if "act" not in st.session_state:
        st.session_state["act"] = 1
    if "scores" not in st.session_state:
        st.session_state["scores"] = {
            "Aggression": 0,
            "Diplomacy": 0,
            "Self-Sacrifice": 0,
            "Avoidance": 0,
            "Evasion/Deception": 0
        }
    if "history" not in st.session_state:
        st.session_state["history"] = []

# Act multipliers: later acts have higher impact.
ACT_MULTIPLIERS = {1: 1, 2: 1.2, 3: 1.5, 4: 2, 5: 3}

# Define narrative and choices for each act
acts = {
    1: {
        "title": "Act 1: The Dawn of Destiny",
        "narratives": [
            "You awaken on the rugged shores of a misty fjord, the chill of the north biting at your skin.",
            "The first light of dawn reveals a world of untold mysteries and ancient runes.",
            "A hushed calm envelops the land as you take your first step into legend."
        ],
        "choices": [
            {"text": "Unsheathe your axe and challenge a band of marauders.", "scores": {"Aggression": 2}},
            {"text": "Attempt to broker peace with a nearby clan.", "scores": {"Diplomacy": 2}},
            {"text": "Share your mead and provisions with starving villagers.", "scores": {"Self-Sacrifice": 2}},
            {"text": "Retreat into the forest’s shadows to observe from afar.", "scores": {"Avoidance": 2}},
            {"text": "Craft a cunning plan to deceive rival warriors.", "scores": {"Evasion/Deception": 2}},
        ]
    },
    2: {
        "title": "Act 2: The Call of Adventure",
        "narratives": [
            "Rumors of a lost treasure echo through the valleys as you journey forth.",
            "The beating of distant war drums spurs you toward destiny.",
            "Mystical runes guide your path as the winds of change blow."
        ],
        "choices": [
            {"text": "Plunder a rival village in a show of raw power.", "scores": {"Aggression": 3}},
            {"text": "Forge alliances with local chieftains through dialogue.", "scores": {"Diplomacy": 3}},
            {"text": "Sacrifice your comforts to aid a suffering community.", "scores": {"Self-Sacrifice": 3}},
            {"text": "Avoid direct conflict by scouting the enemy’s camp.", "scores": {"Avoidance": 3}},
            {"text": "Employ trickery to lure enemies into a trap.", "scores": {"Evasion/Deception": 3}},
        ]
    },
    3: {
        "title": "Act 3: Trials of the Heart",
        "narratives": [
            "Amid raging storms and bitter cold, you face trials that test both body and spirit.",
            "Your journey is strewn with obstacles, each demanding a choice of courage or caution.",
            "In the frozen wilderness, every decision reveals more of your true nature."
        ],
        "choices": [
            {"text": "Lead a daring charge against overwhelming odds.", "scores": {"Aggression": 4}},
            {"text": "Seek wisdom from ancient elders to resolve conflicts.", "scores": {"Diplomacy": 4}},
            {"text": "Endure hardship to rescue a fellow clansman.", "scores": {"Self-Sacrifice": 4}},
            {"text": "Slip away into the shadows to avoid the onslaught.", "scores": {"Avoidance": 4}},
            {"text": "Use clever stratagems to outwit a formidable foe.", "scores": {"Evasion/Deception": 4}},
        ]
    },
    4: {
        "title": "Act 4: The Crossroads of Fate",
        "narratives": [
            "The tides of destiny are turning as you stand at a critical juncture.",
            "A decisive battle looms, and the weight of your choices presses upon you.",
            "In the heat of conflict, the true measure of a warrior is revealed."
        ],
        "choices": [
            {"text": "Duel a rival chieftain in a display of unmatched ferocity.", "scores": {"Aggression": 5}},
            {"text": "Unite fractious tribes with inspiring words of hope.", "scores": {"Diplomacy": 5}},
            {"text": "Make a noble sacrifice to protect the weak.", "scores": {"Self-Sacrifice": 5}},
            {"text": "Withdraw from battle, letting fate take its course.", "scores": {"Avoidance": 5}},
            {"text": "Set a trap using deceit to break enemy alliances.", "scores": {"Evasion/Deception": 5}},
        ]
    },
    5: {
        "title": "Act 5: The Final Reckoning",
        "narratives": [
            "At the crossroads of destiny, the final chapter of your saga unfolds.",
            "The echo of battle and the silence of the gods herald the end of your journey.",
            "Standing before your destiny, every choice converges to define your legacy."
        ],
        "choices": [
            {"text": "Smash your enemies with unrelenting brute force.", "scores": {"Aggression": 6}},
            {"text": "Assume the mantle of leadership with measured wisdom.", "scores": {"Diplomacy": 6}},
            {"text": "Sacrifice all for a cause greater than yourself.", "scores": {"Self-Sacrifice": 6}},
            {"text": "Vanish into the mists, leaving only whispers behind.", "scores": {"Avoidance": 6}},
            {"text": "Employ a final ruse to secure your escape from fate.", "scores": {"Evasion/Deception": 6}},
        ]
    }
}

# Map the dominant personality trait to a final outcome description.
outcomes = {
    "Aggression": "The Warlord: You ruled through strength and might, conquering lands with your ferocity.",
    "Diplomacy": "The Wise King: Your balanced rule and wise counsel united disparate peoples.",
    "Self-Sacrifice": "The Martyr: Your selfless sacrifices forged a legacy of honor and compassion.",
    "Avoidance": "The Shadow: You faded into obscurity, remembered only as a mysterious presence.",
    "Evasion/Deception": "The Exile: You chose a life of cunning, forever roaming the fringes of society."
}

# ---------------------------
# Save and Load Functionality
# ---------------------------

def save_game():
    save_data = {
        "act": st.session_state["act"],
        "scores": st.session_state["scores"],
        "history": st.session_state["history"]
    }
    save_json = json.dumps(save_data)
    st.sidebar.download_button(
        label="Download Save",
        data=save_json,
        file_name="viking_adventure_save.json",
        mime="application/json"
    )

def load_game(uploaded_file):
    try:
        data = json.loads(uploaded_file.read())
        st.session_state["act"] = data.get("act", 1)
        st.session_state["scores"] = data.get("scores", {
            "Aggression": 0,
            "Diplomacy": 0,
            "Self-Sacrifice": 0,
            "Avoidance": 0,
            "Evasion/Deception": 0
        })
        st.session_state["history"] = data.get("history", [])
        st.sidebar.success("Game Loaded!")
    except Exception as e:
        st.sidebar.error(f"Failed to load save: {e}")

# ---------------------------
# Game Flow Functions
# ---------------------------

def play_act(act_number):
    act_data = acts[act_number]
    st.header(act_data["title"])
    
    # Randomize narrative text for variation
    narrative = random.choice(act_data["narratives"])
    st.write(narrative)
    
    multiplier = ACT_MULTIPLIERS[act_number]
    st.write(f"**Act Multiplier:** {multiplier}")
    
    st.write("### Choose your action:")
    for idx, choice in enumerate(act_data["choices"]):
        if st.button(choice["text"], key=f"act{act_number}_choice{idx}"):
            # Update scores using the act multiplier
            for trait, value in choice["scores"].items():
                st.session_state["scores"][trait] += value * multiplier
            # Log the choice in history
            st.session_state["history"].append({
                "act": act_number,
                "choice": choice["text"],
                "scores": choice["scores"],
                "multiplier": multiplier
            })
            st.session_state["act"] += 1
            st.experimental_rerun()

def show_final_outcome():
    st.header("Final Outcome")
    scores = st.session_state["scores"]
    
    st.write("### Your Final Personality Scores:")
    for trait, score in scores.items():
        st.write(f"- **{trait}:** {score}")
    
    # Determine the dominant trait
    highest_trait = max(scores, key=scores.get)
    st.write("---")
    st.subheader(outcomes[highest_trait])
    st.write("Thank you for playing this Viking adventure!")

# ---------------------------
# Main Application
# ---------------------------

def main():
    st.title("Viking Adventure: A Text-Based Journey")
    
    # Initialize game state
    initialize_game()
    
    # Sidebar Menu for Save/Load and Restart
    st.sidebar.title("Game Menu")
    if st.sidebar.button("Restart Game"):
        st.session_state.clear()
        st.experimental_rerun()
    
    save_game()  # Provide a save/download option
    
    uploaded_file = st.sidebar.file_uploader("Load Save", type=["json"])
    if uploaded_file is not None:
        load_game(uploaded_file)
    
    # Game progression: either play the current act or show final outcome.
    current_act = st.session_state["act"]
    if current_act <= 5:
        play_act(current_act)
    else:
        show_final_outcome()
        if st.button("Play Again"):
            st.session_state.clear()
            st.experimental_rerun()

if __name__ == "__main__":
    main()
