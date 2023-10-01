
import streamlit as st 
from lancgahinhelper import *
st.title("Restaurent Name generator ")

cuisine_name =  st.sidebar.selectbox("Pick a Cuisine",("Indian","Chinese","Italian","Mexican","Thai","American","Japanese","Korean","French","Spanish","Greek","Turkish","Lebanese","Vietnamese","Moroccan","Ethiopian","Brazilian","Peruvian","Argentinian","Cuban","Colombian","Chilean","Venezuelan","Ecuadorian","Bolivian","Uruguayan","Paraguayan","Costa Rican","Honduran","Salvadoran","Nicaraguan","Panamanian","Guatemalan","Puerto Rican","Dominican","Jamaican","Haitian","Bahamian","Barbadian","Trinidadian","Surinamese","Guyanese","Belizean","Antiguan","Grenadian","Saint Lucian"))
                     
if cuisine_name:
    response = generate_restaurent_name_and_items(cuisine_name)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split("\n-")
    st.write("**Menu Items**")
    for item in menu_items:
        st.text(item.strip())