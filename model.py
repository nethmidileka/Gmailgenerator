import streamlit as st

st.set_page_config(page_title="Generate Emails",
                   page_icon='mail',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Generate Emails")

from_input = st.text_area('Enter the email topic', height=275)

col1,col2,col3=st.columns([10,10,5])
with col1:
    email_sender=st.text_input('Sender Name')
with col2:
    email_recipient = st.text_input('Recipient Name')
with col3:
    email_style =st.selectbox('Writing Style',
                                    ('Formal','Appreciating','Not Satisfied','Neutral'),
                                    index=0)
    
submit =st.button("Generate")

if submit:
    st.write("Response")
    
