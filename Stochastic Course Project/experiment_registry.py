import subprocess
import sys
import os
import geopandas
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EXPERIMENTS_DIR = BASE_DIR / "Experiments"
VISUALS_SCRIPT = BASE_DIR / "visualizations" / "generate_visuals.py"

EXPERIMENT_SCRIPTS = {
    "Baseline": "experiment_e1_baseline.py",
    "Low Fragility": "experiment_e2_low_fragility.py",
    "High Fragility": "experiment_e3_high_fragility.py",
    "Low Risk": "experiment_e4_low_risk.py",
    "High Risk": "experiment_e5_high_risk.py",
    "Low Capacity": "experiment_e6_low_capacity.py",
    "High Capacity": "experiment_e7_high_capacity.py",
    "Tight Budget": "experiment_e8_tight_budget.py",
    "Loose Budget": "experiment_e9_loose_budget.py"
}


def list_experiments():
    return list(EXPERIMENT_SCRIPTS.keys())


def run_experiment(name: str):
    if name not in EXPERIMENT_SCRIPTS:
        raise ValueError(f"Unknown experiment: {name}")

    script_path = EXPERIMENTS_DIR / EXPERIMENT_SCRIPTS[name]

    env = os.environ.copy()
    env["PYTHONPATH"] = str(BASE_DIR)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(BASE_DIR),
        env=env
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "return_code": result.returncode
    }
def run_visuals():
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BASE_DIR)

    result = subprocess.run(
        [sys.executable, str(VISUALS_SCRIPT)],
        cwd=str(BASE_DIR),
        capture_output=True,
        text=True,
        env=env
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "return_code": result.returncode
    }

def run_all_experiments():
    results = {}

    for name in EXPERIMENT_SCRIPTS.keys():
        results[name] = run_experiment(name)

    return results