
# Synthetic Data Generator for Academic Research Metrics

Welcome to the Synthetic Data Generator for Academic Research Metrics, an advanced computational framework engineered to produce high-fidelity synthetic datasets that emulate the intricate dynamics of scholarly publication ecosystems. This sophisticated tool empowers researchers, data scientists, and academic institutions to generate authentic-looking bibliometric data for experimental analysis, algorithm validation, and methodological development.

## Architectural Overview

The pipeline orchestrates a meticulously designed workflow encompassing synthetic data generation, quantitative metric computation, comprehensive analytical assessment, and publication-quality visualization. It synthesizes a rich corpus of academic researchers and their scholarly outputs, incorporating nuanced citation patterns, collaborative networks, temporal publication distributions, and disciplinary journal landscapes.

## Core Capabilities

- **Advanced Synthetic Data Synthesis:** Generates a heterogeneous dataset comprising 100 researchers and thousands of publications, faithfully replicating authentic academic productivity patterns with sophisticated citation dynamics and collaborative relationships.
- **Bibliometric Metric Computation:** Calculates fundamental scholarly impact indicators, encompassing citation distributions, researcher-specific performance metrics, and quantitative evaluation frameworks for academic productivity assessment.
- **Comprehensive Analytical Framework:** Produces detailed analytical reports encompassing aggregate statistics, H-index rankings for top-performing researchers, temporal publication trends, and disciplinary journal prominence analysis.
- **Publication-Quality Visualizations:** Renders an extensive suite of analytical plots depicting citation distributions, researcher productivity metrics, co-authorship network dynamics, chronological publication trajectories, journal distribution patterns, and collaborative author networks.
- **Rigorous Validation Testing:** Implements automated test suites to validate computational accuracy, data integrity, and methodological reliability of all analytical computations.

## Installation Prerequisites

Ensure Python 3.8 or higher is installed on your system. Initialize the virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

## Operational Execution

Execute the complete analytical pipeline using:

```bash
.venv\Scripts\python main.py
```

This command initiates a sequential execution of the following computational stages:

1. **Data Synthesis:** Generate synthetic researcher profiles and publication records, persisting to `data/researchers.csv`.
2. **Metric Calculation:** Compute bibliometric performance indicators and statistical distributions.
3. **Analytical Assessment:** Perform comprehensive data analysis and generate detailed reports in `results/reports/analysis_report.txt`.
4. **Visualization Rendering:** Create publication-quality plots and save to `results/plots/` directory.
5. **Validation Testing:** Execute automated test suites to ensure computational integrity and data reliability.

## Output Artifacts

- **Primary Dataset:** `data/researchers.csv` — Comprehensive synthetic corpus of researchers and scholarly publications.
- **Analytical Report:** `results/reports/analysis_report.txt` — Detailed bibliometric analysis and statistical insights.
- **Visual Analytics:** Multiple high-resolution PNG visualizations in `results/plots/` illustrating key scholarly metrics and trends.

## Project Architecture

```
synthetic-data-generator/
├── data/
│   └── researchers.csv              # Generated synthetic dataset
├── results/
│   ├── plots/                       # Analytical visualizations
│   └── reports/                     # Comprehensive analysis reports
├── src/
│   ├── generate_data.py             # Synthetic data generation engine
│   ├── compute_metrics.py           # Bibliometric computation module
│   ├── analyze.py                   # Advanced analytical framework
│   └── visualize.py                 # Visualization rendering system
├── tests/
│   └── test_metrics.py              # Validation test suite
├── notebooks/                       # Jupyter analysis notebooks
├── main.py                          # Primary pipeline orchestrator
├── requirements.txt                 # Dependency specifications
└── README.md                        # Project documentation
```

## Technical Dependencies

- Python 3.8+
- numpy==1.24.3
- pandas==2.0.3
- matplotlib==3.7.2
- Faker==19.3.0

