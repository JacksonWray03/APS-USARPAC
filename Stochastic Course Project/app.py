import streamlit as st

from streamlit_runner import run_baseline_experiment


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Disaster Relief Stochastic Model",
    layout="wide",
)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("Disaster Relief Stochastic Optimization Model")

st.markdown(
    """
    Current functionality:
    - Run baseline experiment
    - Generate standard output CSVs
    """
)


# ============================================================
# BASELINE EXPERIMENT SECTION
# ============================================================

st.header("Baseline Experiment")


if st.button("Run Baseline Experiment"):


    with st.spinner("Running optimization model..."):

        try:
            run_baseline_experiment()
            st.success("Baseline experiment completed successfully.")

            st.markdown(
                """
                Output files were written to the `output/` directory.
                """
            )

        except Exception as error:


            st.error("Experiment execution failed.")

            st.exception(error)