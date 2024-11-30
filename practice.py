import streamlit as st

st.title("Hello Title")

st.subheader("Hello subheader")

st.info("Information")

st.write("Write here anything")
st.write("range(50)")

st.text("Text here")
st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("### Heading 3")

st.checkbox("Checkbox")
st.button("Button")
st.radio("pick one among them", ["One","Two","Three"])

st.selectbox("Pick you couser",["default","course 1","course 2","course 3"])

st.number_input("Pick a number",0,100)
st.text_input("Enter you name")
st.date_input("The date of opening is:  ")
st.time_input("The time is:")
st.text_area("write something on your mind")

st.file_uploader("Upload you file")