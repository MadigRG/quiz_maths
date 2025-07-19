import streamlit as st

st.set_page_config(page_title="Prépa Maths - Associations", layout="centered")

st.title("🔗 Chapitre 1 : ")
st.markdown("""
Bienvenue ! Associe chaque **expression mathématique** à sa **valeur correcte**.  
Ce questionnaire couvre des notions de **fonctions, dérivées et limites**.

---
""")



options = [
    r"a^2 + b^2 = c^2",
    r"e^{i\pi} + 1 = 0",
    r"\int_0^\infty e^{-x} dx = 1",
    r"e^{i\pi} + 1 = 0"
]

answer = r"e^{i\pi} + 1 = 0"

if "selected" not in st.session_state:
    st.session_state.selected = None

cols = st.columns([1,10],vertical_alignment="center")

for i, formula in enumerate(options):
    with cols[0]:
        st.write("")
        if st.button("✔", key=f"btn_{i}"):  # Bouton simple
            st.session_state.selected = formula
    with cols[1]:
        st.write("")
        st.latex(formula)  # Rendu LaTeX au-dessus



if st.session_state.selected  == answer:
    st.success(f"✅ Bonne réponse")
    st.latex(r"e^{i\pi} + 1 = 0")

else:
        st.error(f"❌ Réponse incorrecte")