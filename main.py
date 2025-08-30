#!/usr/bin/env python3
"""
Main pipeline script for the fake data generator project.
Runs the complete workflow: data generation, metrics computation, analysis, and visualization.
"""

import os
import sys
import time
from datetime import datetime

def run_pipeline():
    """Run the complete data generation and analysis pipeline."""
    print("=" * 60)
    print("FAKE DATA GENERATOR PIPELINE")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Step 1: Generate data
    print("Step 1: Generating synthetic researcher data...")
    start_time = time.time()
    try:
        from src.generate_data import generate_researcher_data, save_dataset
        df = generate_researcher_data(n_researchers=100)
        save_dataset(df, "data/researchers.csv")
        print(f" Generated data for {len(df)} papers from {df['researcher_id'].nunique()} researchers")
        print(f"  Data saved to data/researchers.csv")
    except Exception as e:
        print(f" Error generating data: {e}")
        return False
    step1_time = time.time() - start_time
    
    # Step 2: Compute basic metrics
    print("\nStep 2: Computing basic metrics...")
    start_time = time.time()
    try:
        from src.compute_metrics import compute_basic_metrics, compute_citation_distribution
        basic_metrics = compute_basic_metrics(df)
        citation_dist = compute_citation_distribution(df)
        print(f" Computed metrics for {len(basic_metrics)} researchers")
        print(f"  Citation distribution: {len(citation_dist)} unique citation values")
    except Exception as e:
        print(f" Error computing metrics: {e}")
        return False
    step2_time = time.time() - start_time
    
    # Step 3: Analyze data and generate report
    print("\nStep 3: Analyzing data and generating report...")
    start_time = time.time()
    try:
        from src.analyze import analyze_researcher_metrics, calculate_overall_statistics, generate_analysis_report
        researcher_metrics = analyze_researcher_metrics(df)
        overall_stats = calculate_overall_statistics(df)
        generate_analysis_report(df, "results/reports/analysis_report.txt")
        print(f" Generated analysis report")
        print(f"  Total citations: {overall_stats['total_citations']:,}")
        print(f"  Total papers: {overall_stats['total_papers']:,}")
        print(f"  Average citations per paper: {overall_stats['avg_citations_per_paper']:.1f}")
    except Exception as e:
        print(f" Error in analysis: {e}")
        return False
    step3_time = time.time() - start_time
    
    # Step 4: Generate visualizations
    print("\nStep 4: Generating visualizations...")
    start_time = time.time()
    try:
        from src.visualize import generate_all_visualizations
        generate_all_visualizations(df)
        print(" Generated visualizations:")
        print("  - Citation distribution histogram")
        print("  - Researcher productivity scatter plot")
        print("  - Citations vs co-authors scatter plot")
        print("  - Publication trends over years")
        print("  - Journal distribution bar chart")
        print("  - Author network visualization")
        print("  Plots saved to results/plots/")
    except Exception as e:
        print(f" Error generating visualizations: {e}")
        return False
    step4_time = time.time() - start_time
    
    # Step 5: Run tests
    print("\nStep 5: Running tests...")
    start_time = time.time()
    try:
        import subprocess
        result = subprocess.run([sys.executable, "tests/test_metrics.py"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ All tests passed")
        else:
            print(f"✗ Tests failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error running tests: {e}")
        return False
    step5_time = time.time() - start_time
    
    # Summary
    total_time = step1_time + step2_time + step3_time + step4_time + step5_time
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Breakdown:")
    print(f"  Data generation: {step1_time:.2f}s")
    print(f"  Metrics computation: {step2_time:.2f}s")
    print(f"  Analysis: {step3_time:.2f}s")
    print(f"  Visualization: {step4_time:.2f}s")
    print(f"  Testing: {step5_time:.2f}s")
    print(f"\nResults available in:")
    print(f"  - data/researchers.csv (raw data)")
    print(f"  - results/reports/analysis_report.txt (analysis)")
    print(f"  - results/plots/ (visualizations)")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    success = run_pipeline()
    sys.exit(0 if success else 1)
