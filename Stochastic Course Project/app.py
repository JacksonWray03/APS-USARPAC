import streamlit as st
from experiment_registry import list_experiments, run_experiment

st.title("Stochastic Optimization Dashboard")

experiment_name = st.selectbox(
    "Select Experiment",
    list_experiments()
)

if st.button("Run Experiment"):
    st.write(f"Running: {experiment_name}")

    result = run_experiment(experiment_name)

    st.subheader("Console Output")

    st.text_area("stdout", result["stdout"], height=300)

    if result["stderr"]:
        st.subheader("Errors")
        st.text_area("stderr", result["stderr"], height=200)

    st.write("Exit code:", result["return_code"])