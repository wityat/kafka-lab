import base64
import io
import logging

import streamlit as st
from PIL import Image


def display_messages():
    for message in st.session_state.messages:
        display_message(message)

chart_holder = st.empty()
def display_message(message):
    im = base64.b64decode(message["value"])
    logging.info(im)
    b = io.BytesIO(im)
    b.seek(0)
    image = Image.open(b)
    st.image(image, use_column_width=True)

    st.write("Labels and probabilities:")
    for label, probability in message["labels"]:
        st.write(f"{label}: {probability}%")

    chart_holder.line_chart(st.session_state.elapsed_time)





