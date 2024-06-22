import streamlit as st
from pet import Pet


def create_pet(name):
    return Pet(name)


if "pet" not in st.session_state:
    st.title("Pet Simulator Game")
    pet_name = st.text_input("Enter the name of your pet:")
    if pet_name:
        st.session_state.pet = create_pet(pet_name)
        st.session_state.initialized = True
        st.experimental_rerun()
else:
    pet = st.session_state.pet

    st.title("Pet Simulator Game")

    st.header("Pet Information")
    st.write(f"Name: {pet.name}")
    # st.write(f"Age: {pet.age}")
    st.write(f"Belly: {pet.belly}")
    mood_description = pet.determine_mood(pet.mood)
    st.header("Actions")
    action = st.selectbox("What would you like to do?", ["Feed", "Check Stats", "Sleep"])

    if action == "Feed":
        food = st.selectbox("What would you like to feed?",
                            ["Avocado", "Banana", "Black Olive", "Eggplant", "Kiwi", "Red Cherries", "Strawberry"])
        if st.button("Feed"):
            pet.feed_food(food.lower())
            st.write(f"You fed {pet.name} {food}!")
            st.session_state.pet = pet
            st.experimental_rerun()

    elif action == "Check Stats":
        stat = st.selectbox("What would you like to check?", ["Ability", "Age", "Belly", "Mood", "Name"])
        if st.button("Check"):
            pet.check_stats(stat.lower())
            st.write(f"{pet.name}'s {stat} is {getattr(pet, stat.lower())}")
            st.session_state.pet = pet

    elif action == "Sleep":
        st.write(f"{pet.name} fell asleep")
        st.stop()

    st.write("")

    if st.button("Update"):
        pet.increase_age()
        st.write(f"{pet.name} is now {pet.age} years old")
        st.session_state.pet = pet
        st.experimental_rerun()

    st.write("")

    if st.button("Check Habits"):
        st.write(f"{pet.name} has the habit of {pet.habit}")

    st.write("")

    if not st.session_state.get("initialized", False):
        st.write(f"Welcome, {pet.name}!")
        st.session_state.initialized = True
