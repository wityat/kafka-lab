import ast
import logging
import os
import time

from consumer import VisualizationConsumer
import streamlit as st
import matplotlib.pyplot as plt

consumer = VisualizationConsumer(
    ast.literal_eval(os.environ.get("VISUALIZATION_CONSUMER_CONFIG")),
    os.environ.get("ML_PROCESSOR_TOPIC")
)


def update_data_with_new_labels(labels):
    """
    Обновляет данные для графика на основе новых лейблов.
    labels - список кортежей вида (label, value)
    """
    for label, value in labels:
        if label in st.session_state.data:
            st.session_state.data[label] += 1
        else:
            st.session_state.data[label] = 1


def plot_data():
    """
    Создает и отображает график столбцов на основе актуальных данных.
    """
    labels = list(st.session_state.data.keys())[:5]
    values = list(st.session_state.data.values())[:5]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel('Values')
    ax.set_title('TOP 5 Labels')

    return fig


def main():
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.elapsed_time = []
    if 'data' not in st.session_state:
        st.session_state.data = {}
    st.title("Visualization of Image Classification Inference")
    st.markdown("### Inference Time for Each Image")
    chart_holder = st.empty()
    chart_holder1 = st.empty()
    while True:
        message = consumer.consume_data()
        logging.warning("Visualizing new data!")
        st.session_state.messages.append(message)
        st.session_state.elapsed_time.append(message["elapsed_time"])
        update_data_with_new_labels(message["labels"])
        chart_holder.line_chart(st.session_state.elapsed_time)
        fig = plot_data()
        chart_holder1.pyplot(fig)
        time.sleep(1)
        plt.close(fig)


if __name__ == '__main__':
    main()
