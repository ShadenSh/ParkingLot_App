import streamlit as st
import requests


def send_email(name, message,sender_email):
    api_key="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"
    api_url="https://api.sendgrid.com/v3/mail/send"

    data = {
        "personalizations":[
            {
            "to": [{"email": "shaden.sharif@gmail.com"}],
            "subject": "Contact from Parking Lot Streamlit App"
            }
            ],
        "from":{
            "email": "shaden.sharif@gmail.com"
        },
        "content":[{
            "type": "text/plain",
            "value": f"Name: {name}\n Email: {sender_email}\n Message: {message}"
            }]
        }
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(api_url , json=data , headers=headers)

    if response.status_code == 202:
        st.success("Email sent successfully!")
    else:
        st.error(f"Error sending email: {response.text}")


st.title('Welcome to my Contact Page')

text1="""I appreciate your assistance in improving my service! If you notice any discrepancies in the parking space availability updates, please let me know by filling out the form below. Be sure to include:
"""
text2="""- Details of the issue :"""
text3=""" Describe the parking spaces that weren't updating, along with the specific time and date when encountered the issue."""
text4="""- Suggestions for improvement : """
text5=""" I welcome any suggestions you have to enhance my service and provide a better for all users."""
st.markdown(f"#### {text1}")
st.markdown(f"#### :orange[{text2}]{text3}")
st.markdown(f"#### :orange[{text4}]{text5}")
thanks_text="""Thank you for helping me maintain the accuracy of my project updates and for contributing to my continuous improvement efforts!"""
st.markdown(f"#### {thanks_text}")
name = st.text_input("Enter your Name")
email = st.text_input("Enter your mail address")
msg = st.text_area("Message")
submit_button = st.button("Send")

st.markdown(":car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car:")

if submit_button:
    if not email:
        st.error("Please enter your mail address")
    if not msg:
        st.error("Please enter a message.")
    else:
        send_email(name,msg,email)

