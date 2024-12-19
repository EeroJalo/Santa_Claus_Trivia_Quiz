import streamlit as st
from PIL import Image

# Define quiz questions and answers
questions = [
    {
        "question": "What is Santa Claus's traditional outfit color?",
        "options": ["Green", "Blue", "Red", "White"],
        "answer": "Red",
    },
    {
        "question": "What is the name of Santa's most famous reindeer?",
        "options": ["Dasher", "Blitzen", "Rudolph", "Vixen"],
        "answer": "Rudolph",
    },
    {
        "question": "Where does Santa Claus live?",
        "options": ["The South Pole", "Lapland", "The North Pole", "Greenland"],
        "answer": "Lapland",
    },
    {
        "question": "What does Santa traditionally say as he flies away?",
        "options": [
            "Goodbye and good luck!",
            "Ho, ho, ho! Merry Christmas!",
            "See you next year!",
            "Happy Holidays!"
        ],
        "answer": "Ho, ho, ho! Merry Christmas!",
    },
    {
        "question": "What do children leave out for Santa on Christmas Eve?",
        "options": ["Milk and cookies", "Pizza", "Carrots", "Hot chocolate"],
        "answer": "Milk and cookies",
    },
]

# App title
st.title("🎅 Santa Claus Trivia Quiz 🎄")
st.write("Test your knowledge about Santa Claus! Answer the questions below.")

# Display a festive image
image = Image.open("santa_claus.jpg")
st.image(image, caption="Santa Claus", use_container_width=True)

# Initialize score and responses
if "score" not in st.session_state:
    st.session_state.score = 0
if "responses" not in st.session_state:
    st.session_state.responses = [None] * len(questions)

# Display each question
for i, q in enumerate(questions):
    st.subheader(f"Question {i + 1}")
    response = st.radio(q["question"], q["options"], key=f"q{i}")

    # Store the response
    if st.session_state.responses[i] != response:
        st.session_state.responses[i] = response

# Submit button
if st.button("Submit Quiz"):
    st.session_state.score = sum(
        1 for i, q in enumerate(questions) if st.session_state.responses[i] == q["answer"]
    )
    st.success(f"You scored {st.session_state.score} out of {len(questions)}! 🎉")
    
    # Display correct answers
    st.write("Here are the correct answers:")
    for q in questions:
        st.write(f"- **{q['question']}**: {q['answer']}")

# Additional styling and visualizations
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fdf6e4;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)
