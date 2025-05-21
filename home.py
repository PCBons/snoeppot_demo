import streamlit as st
import geopandas

if 'lijst' not in st.session_state:
	st.session_state['lijst'] = []


gok = st.number_input('Gok het aantal snoepjes')
st.session_state['lijst'].append(gok)

st.write(st.session_state['lijst'])
st.write(len(st.session_state['lijst']))

wis = st.button('wis de data')
if wis:
	st.session_state['lijst'] = []
	st.rerun()
