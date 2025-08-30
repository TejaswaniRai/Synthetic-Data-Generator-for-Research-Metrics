import pandas as pd
import numpy as np

def compute_basic_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute basic metrics for each researcher.
    
    Args:
        df: DataFrame containing researcher data
        
    Returns:
        DataFrame with metrics per researcher
    """
    metrics = df.groupby('researcher_id').agg(
        total_papers=pd.NamedAgg(column='paper_id', aggfunc='count'),
        total_citations=pd.NamedAgg(column='citations', aggfunc='sum'),
        avg_citations=pd.NamedAgg(column='citations', aggfunc='mean'),
        max_citations=pd.NamedAgg(column='citations', aggfunc='max'),
        min_citations=pd.NamedAgg(column='citations', aggfunc='min')
    ).reset_index()
    
    return metrics

def compute_citation_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Compute the distribution of citations across all papers.
    
    Args:
        df: DataFrame containing researcher data
        
    Returns:
        Series representing citation counts frequency
    """
    return df['citations'].value_counts().sort_index()

if __name__ == "__main__":
    try:
        df = pd.read_csv("data/researchers.csv")
        metrics_df = compute_basic_metrics(df)
        print("Basic Metrics per Researcher:")
        print(metrics_df.head())
        
        citation_dist = compute_citation_distribution(df)
        print("\nCitation Distribution:")
        print(citation_dist.head())
        
    except FileNotFoundError:
        print("Data file not found. Please run generate_data.py first.")
    except Exception as e:
        print(f"Error: {e}")
