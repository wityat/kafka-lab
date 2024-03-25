import streamlit as st
import matplotlib.pyplot as plt


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
    labels = list(st.session_state.data.keys())[:10]
    values = list(st.session_state.data.values())[:10]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel('Values')
    ax.set_title('TOP 10 Labels')

    return fig

