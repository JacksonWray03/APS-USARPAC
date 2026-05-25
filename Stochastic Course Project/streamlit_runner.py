
from Experiments.common import run_single_experiment

def run_baseline_experiment() -> None:
    run_single_experiment(
        experiment_code="E1",
        experiment_label="Baseline",
        gamma=0.5,
        beta=0.90,
        p_max=5,
        budget=None,
        tau=4,
        rho=0.3,
        num_scenarios=10,
        base_output_dir="output",
        verbose=False,
    )