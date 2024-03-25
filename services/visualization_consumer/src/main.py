import ast
import logging
import os

from consumer import VisualizationConsumer
from visualizator import display_messages
import streamlit as st

consumer = VisualizationConsumer(
    ast.literal_eval(os.environ.get("VISUALIZATION_CONSUMER_CONFIG")),
    os.environ.get("ML_PROCESSOR_TOPIC")
)
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.elapsed_time = []

st.title("Visualization of Streamed Messages")


def main():
    while True:
        message = consumer.consume_data()
        logging.info("Visualizing new data!")
        st.session_state.messages.append(message)
        display_messages()


if __name__ == '__main__':
    main()
