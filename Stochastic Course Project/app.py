import streamlit as st
import pandas as pd
from experiment_registry import list_experiments, run_experiment, run_all_experiments,EXPERIMENT_SCRIPTS
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

    # --- correct folder derivation ---
    script_name = EXPERIMENT_SCRIPTS[experiment_name]  # e.g. experiment_e1_baseline.py
    folder_name = script_name.replace("experiment_", "").replace(".py", "")  # E1_baseline

    base_output = Path(__file__).resolve().parent / "output"
    summary_path = base_output / folder_name / "summary.csv"

    if summary_path.exists():
        st.subheader("Summary Results")
        df = pd.read_csv(summary_path)
        st.dataframe(df)
    else:
        st.warning(f"No summary.csv found at {summary_path}")

st.divider()

if st.button("Run ALL Experiments"):
    with st.spinner("Running full experiment suite..."):
        results = run_all_experiments()

    st.success("All experiments completed.")

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