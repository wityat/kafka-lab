import ast
import logging
import os
import time

from consumer import VisualizationConsumer
from visualizator import plot_data, update_data_with_new_labels
import streamlit as st

consumer = VisualizationConsumer(
    ast.literal_eval(os.environ.get("VISUALIZATION_CONSUMER_CONFIG")),
    os.environ.get("ML_PROCESSOR_TOPIC")
)


def main():
    if "elapsed_time" not in st.session_state:
        st.session_state.elapsed_time = []
    if 'data' not in st.session_state:
        st.session_state.data = {}
    st.title("Visualization of Streamed Messages")
    chart_holder1 = st.empty()
    chart_holder2 = st.empty()
    while True:
        message = consumer.consume_data()
        logging.warning("Visualizing new data!")
        st.session_state.elapsed_time.append(message["elapsed_time"])
        update_data_with_new_labels(message["labels"])
        chart_holder1.line_chart(st.session_state.elapsed_time)
        chart_holder2.pyplot(plot_data())
        time.sleep(1)


if __name__ == '__main__':
    main()
