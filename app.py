import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


opcao = st.sidebar.selectbox("Distributions", ("Normal", "Exponential",
                                              "Chi-squared", "T student", "Binomial", "Poisson"))

np.random.seed(999)
if opcao == "Normal":
    st.header("Probability Density Function")
    histog = st.sidebar.checkbox('Histogram')
    curve = st.sidebar.checkbox('Curve', value=True)
    mm = st.sidebar.checkbox('Mean/Median')

    mu = st.sidebar.number_input('Mean:', step=0.5)
    sd = st.sidebar.number_input('Standard Deviation:', min_value=0.0, value=1.0, step=0.5)
    nor1 = np.random.normal(mu, sd, size=1000)
    

    fig, ax = plt.subplots()
    ax.set_ylabel("Probability Density")
    if histog:
        ax.hist(nor1, 40, range=(-8, 8), density=True, alpha=0.6)
    plt.xlim(-9, 9)
    plt.ylim(0, 0.8)
    if mm:
        plt.axvline(x=mu, color='y', ls="-.", label='Mean and Median')
    plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')

    st.pyplot(fig)
