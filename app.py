import random
import streamlit as st
from ai_module import web_search

st.title("Unfold Yoga Assistant 🧘")
yoga_quotes = [
    "Yoga is the journey of the self, through the self, to the self. - The Bhagavad Gita",
    "Yoga is the fountain of youth. You're only as young as your spine is flexible. - Bob Harper",
    "Yoga teaches us to cure what need not be endured and endure what cannot be cured. - B.K.S. Iyengar",
    "Yoga is the practice of quieting the mind. - Patanjali",
    "Yoga is the perfect opportunity to be curious about who you are. - Jason Crandell",
    "Yoga is not about touching your toes, it's about what you learn on the way down. - Jigar Gor",
    "Yoga is a dance between control and surrender - between pushing and letting go - and when to push and to let go becomes part of the creative process, part of the open-ended exploration of your being. - Joel Kramer",
    "Yoga is the journey of the self, to the self, through the self. - The Bhagavad Gita",
    "Yoga is not just repetition of few postures - it is more about the exploration and discovery of the subtle energies of life. - Amit Ray",
    "Yoga is the space where flower blossoms. - Amit Ray"
]


with st.sidebar:
    st.header("Quote of the day")
    rnd = random.randint(0, len(yoga_quotes)-1)
    st.markdown(f'" {yoga_quotes[rnd]} "')
    st.divider()
    st.markdown('''## Wellness Tips

- **Stay Hydrated**: Drink plenty of water.
- **Eat Nutritious Foods**: Include fruits, vegetables, whole grains, lean proteins, and healthy fats.
- **Get Adequate Sleep**: Aim for 7-9 hours of quality sleep.
- **Exercise Regularly**: Engage in physical activity for at least 30 minutes most days.
- **Practice Stress Management**: Deep breathing, meditation, or spending time in nature.
- **Prioritize Mental Health**: Take time for self-care activities.''')


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "please tell me how you're feeling today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = web_search(prompt)

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
