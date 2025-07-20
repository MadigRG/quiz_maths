
import streamlit as st

questions = [
    {"question": r"Une suite qui ne converge pas tend vers +\infty ou -\infty." ,
     "options": ["Vrai","Faux"] , 
     "reponse": "Faux" ,
     "explication": r"test"},
    {"question": r"Si (u_{2n}) et (u_{2n+1}) convergent alors (u_n) converge.",
      "options": ["Vrai","Faux"],
      "reponse": "Faux",
      "explication": r"Contre-exemple : u_n = (-1)^n" }
 
]

def afficher_questions(dico) : 
    
    st.session_state.reponse_util = None

    st.latex(dico["question"])

    cols = st.columns([1,10],vertical_alignment="center")

    for i, formula in enumerate(dico["options"]):
        with cols[0]:
            st.write("")
            if st.button("✔", key=f"btn_{i}"):  # Bouton simple
                st.session_state.reponse_util = formula
        with cols[1]:
            st.write("")
            st.latex(formula)  # Rendu LaTeX au-dessus

def verifier_reponse(reponse_util, bonne_reponse): 
    if reponse_util != bonne_reponse and reponse_util != None: 
        st.error("Essaye encore")
    elif reponse_util == bonne_reponse and reponse_util != None: 
        st.success("Bravo !")




def commencer():
    import streamlit as st
    st.session_state["question"] = 0

def suivant() :
    import streamlit as st 
    st.session_state.question= st.session_state.question + 1

def precedent() : 
    import streamlit as st 
    st.session_state.question= st.session_state.question- 1


    