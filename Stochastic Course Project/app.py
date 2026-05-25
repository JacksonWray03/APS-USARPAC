import streamlit as st
from experiment_registry import list_experiments, run_experiment, run_all_experiments
from visualizations.generate_visuals import main as generate_visuals
from pathlib import Path

st.set_page_config(page_title="Stochastic Optimization Dashboard", layout="centered")

st.title("Stochastic Optimization Dashboard")

st.markdown("Run experiments and generate analysis visualizations.")

# -------------------------
# Experiment selection
# -------------------------
experiment_name = st.selectbox(
    "Experiment",
    list_experiments()
)

st.divider()

# -------------------------
# Run experiment
# -------------------------
if st.button("Run Experiment"):
    st.write(f"Running: {experiment_name}")

    with st.spinner("Running simulation..."):
        run_experiment(experiment_name)

    st.success("Experiment complete")

st.divider()

if st.button("Run ALL Experiments"):
        st.write("Running full experiment suite...")
        results = run_all_experiments()
        st.write("All experiments completed.")

# -------------------------
# Generate visuals
# -------------------------

st.divider()
if st.button("Generate Visuals"):
    generate_visuals()

    st.success("Visuals generated")

    FIG_DIR = Path(__file__).resolve().parent / "visualizations" / "figures"

    for img in sorted(FIG_DIR.glob("*.png")):
        st.image(str(img))