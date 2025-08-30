import pandas as pd
import numpy as np
from typing import Dict, Any, List

def calculate_h_index(citations_list: List[int]) -> int:
    """
    Calculate the h-index for a researcher.
    
    Args:
        citations_list: List of citation counts for a researcher's papers
        
    Returns:
        h-index value
    """
    citations_list.sort(reverse=True)
    h_index = 0
    for i, citations in enumerate(citations_list):
        if citations >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index

def analyze_researcher_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate various metrics for each researcher.
    
    Args:
        df: DataFrame containing researcher data
        
    Returns:
        DataFrame with researcher metrics
    """
    metrics = []
    
    for researcher_id in df['researcher_id'].unique():
        researcher_df = df[df['researcher_id'] == researcher_id]
        citations = researcher_df['citations'].tolist()
        
        h_index = calculate_h_index(citations)
        total_citations = sum(citations)
        num_papers = len(citations)
        avg_citations = total_citations / num_papers if num_papers > 0 else 0
        max_citations = max(citations) if citations else 0
        
        # Get author name (should be the same for all papers of this researcher)
        author_name = researcher_df['author_name'].iloc[0]
        
        # Get publication year range
        years = researcher_df['year'].tolist()
        year_range = f"{min(years)}-{max(years)}" if years else "N/A"
        
        # Get unique journals
        unique_journals = researcher_df['journal'].nunique()
        
        metrics.append({
            'researcher_id': researcher_id,
            'author_name': author_name,
            'h_index': h_index,
            'total_citations': total_citations,
            'num_papers': num_papers,
            'avg_citations': avg_citations,
            'max_citations': max_citations,
            'publication_years': year_range,
            'unique_journals': unique_journals
        })
    
    return pd.DataFrame(metrics)

def calculate_overall_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate overall statistics for the dataset.
    
    Args:
        df: DataFrame containing researcher data
        
    Returns:
        Dictionary with overall statistics
    """
    stats = {
        'total_researchers': df['researcher_id'].nunique(),
        'total_papers': len(df),
        'total_citations': df['citations'].sum(),
        'avg_citations_per_paper': df['citations'].mean(),
        'avg_papers_per_researcher': len(df) / df['researcher_id'].nunique(),
        'max_citations': df['citations'].max(),
        'min_citations': df['citations'].min(),
        'publication_year_range': f"{df['year'].min()}-{df['year'].max()}",
        'unique_journals': df['journal'].nunique(),
        'avg_co_authors': df['co_authors_count'].mean()
    }
    
    return stats

def generate_analysis_report(df: pd.DataFrame, output_path: str = "results/reports/analysis_report.txt"):
    """
    Generate a comprehensive analysis report.
    
    Args:
        df: DataFrame containing researcher data
        output_path: Path to save the report
    """
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    researcher_metrics = analyze_researcher_metrics(df)
    overall_stats = calculate_overall_statistics(df)
    
    with open(output_path, 'w') as f:
        f.write("RESEARCHER METRICS ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("Overall Statistics:\n")
        f.write("-" * 20 + "\n")
        for key, value in overall_stats.items():
            f.write(f"{key}: {value}\n")
        
        f.write("\nTop Researchers by H-index:\n")
        f.write("-" * 25 + "\n")
        top_researchers = researcher_metrics.nlargest(10, 'h_index')
        for _, row in top_researchers.iterrows():
            f.write(f"Researcher {row['researcher_id']} ({row['author_name']}): "
                   f"H-index = {row['h_index']}, Papers = {row['num_papers']}, "
                   f"Total Citations = {row['total_citations']}, Years: {row['publication_years']}\n")
        
        f.write("\nPublication Year Distribution:\n")
        f.write("-" * 30 + "\n")
        year_counts = df['year'].value_counts().sort_index()
        for year, count in year_counts.items():
            f.write(f"{year}: {count} papers\n")
        
        f.write("\nTop Journals by Publication Count:\n")
        f.write("-" * 35 + "\n")
        journal_counts = df['journal'].value_counts().head(10)
        for journal, count in journal_counts.items():
            f.write(f"{journal}: {count} papers\n")
    
    print(f"Analysis report saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    try:
        df = pd.read_csv("data/researchers.csv")
        metrics_df = analyze_researcher_metrics(df)
        print("Researcher Metrics:")
        print(metrics_df.head())
        
        stats = calculate_overall_statistics(df)
        print("\nOverall Statistics:")
        for key, value in stats.items():
            print(f"{key}: {value}")
            
        generate_analysis_report(df)
        
    except FileNotFoundError:
        print("Data file not found. Please run generate_data.py first.")
    except Exception as e:
        print(f"Error: {e}")
