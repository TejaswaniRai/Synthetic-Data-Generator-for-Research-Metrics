import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Optional

def create_citations_distribution_plot(df: pd.DataFrame, output_path: str = "results/plots/citations_distribution.png"):
    """
    Create a histogram of citation distribution.
    
    Args:
        df: DataFrame containing researcher data
        output_path: Path to save the plot
    """
    plt.figure(figsize=(12, 6))
    plt.hist(df['citations'].tolist(), bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Distribution of Citation Counts')
    plt.xlabel('Number of Citations')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Citations distribution plot saved to {output_path}")

def create_researcher_productivity_plot(df: pd.DataFrame, output_path: str = "results/plots/researcher_productivity.png"):
    """
    Create a scatter plot of papers vs citations per researcher.
    
    Args:
        df: DataFrame containing researcher data
        output_path: Path to save the plot
    """
    researcher_stats = df.groupby(['researcher_id', 'author_name']).agg({
        'citations': 'sum',
        'paper_id': 'count'
    }).reset_index()
    researcher_stats.columns = ['researcher_id', 'author_name', 'total_citations', 'num_papers']
    
    plt.figure(figsize=(12, 8))
    plt.scatter(researcher_stats['num_papers'].tolist(), researcher_stats['total_citations'].tolist(), 
                alpha=0.6, color='orange', s=50)
    plt.title('Researcher Productivity: Papers vs Citations')
    plt.xlabel('Number of Papers')
    plt.ylabel('Total Citations')
    plt.grid(True, alpha=0.3)
    
    # Annotate top 5 researchers
    top_researchers = researcher_stats.nlargest(5, 'total_citations')
    for _, row in top_researchers.iterrows():
        author_name = str(row['author_name'])
        num_papers = float(row['num_papers'])
        total_citations = float(row['total_citations'])
        plt.annotate(author_name, 
                    (num_papers, total_citations),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8, alpha=0.8)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Researcher productivity plot saved to {output_path}")

def create_citations_vs_coauthors_plot(df: pd.DataFrame, output_path: str = "results/plots/citations_vs_coauthors.png"):
    """
    Create a scatter plot of citations vs co-authors.
    
    Args:
        df: DataFrame containing researcher data
        output_path: Path to save the plot
    """
    plt.figure(figsize=(12, 6))
    plt.scatter(df['co_authors_count'].tolist(), df['citations'].tolist(), 
                alpha=0.6, color='green', s=30)
    plt.title('Citations vs Number of Co-Authors')
    plt.xlabel('Number of Co-Authors')
    plt.ylabel('Citations')
    plt.grid(True, alpha=0.3)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Citations vs co-authors plot saved to {output_path}")

def create_publication_trends_plot(df: pd.DataFrame, output_path: str = "results/plots/publication_trends.png"):
    """
    Create a line plot showing publication trends over years.
    
    Args:
        df: DataFrame containing researcher data
        output_path: Path to save the plot
    """
    yearly_stats = df.groupby('year').agg({
        'paper_id': 'count',
        'citations': 'mean'
    }).reset_index()
    yearly_stats.columns = ['year', 'papers_count', 'avg_citations']
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Papers per year
    ax1.plot(yearly_stats['year'].tolist(), yearly_stats['papers_count'].tolist(), 
             marker='o', linewidth=2, markersize=4, color='blue')
    ax1.set_title('Publications per Year')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Papers')
    ax1.grid(True, alpha=0.3)
    
    # Average citations per year
    ax2.plot(yearly_stats['year'].tolist(), yearly_stats['avg_citations'].tolist(), 
             marker='s', linewidth=2, markersize=4, color='red')
    ax2.set_title('Average Citations per Year')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Average Citations')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication trends plot saved to {output_path}")

def create_journal_distribution_plot(df: pd.DataFrame, output_path: str = "results/plots/journal_distribution.png"):
    """
    Create a bar plot showing top journals by publication count.
    
    Args:
        df: DataFrame containing researcher data
        output_path: Path to save the plot
    """
    journal_counts = df['journal'].value_counts().head(15)
    
    plt.figure(figsize=(14, 8))
    journal_counts.plot(kind='bar', color='purple', alpha=0.7)
    plt.title('Top 15 Journals by Publication Count')
    plt.xlabel('Journal Name')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Journal distribution plot saved to {output_path}")

def create_author_network_plot(df: pd.DataFrame, output_path: str = "results/plots/author_network.png"):
    """
    Create a simple visualization of author collaboration patterns.
    
    Args:
        df: DataFrame containing researcher data
        output_path: Path to save the plot
    """
    # Get top 20 authors by total citations
    author_stats = df.groupby('author_name').agg({
        'citations': 'sum',
        'paper_id': 'count'
    }).reset_index()
    top_authors = author_stats.nlargest(20, 'citations')['author_name'].tolist()
    
    # Filter data for top authors
    top_author_data = df[df['author_name'].isin(top_authors)]
    
    plt.figure(figsize=(14, 10))
    for author in top_authors:
        author_papers = top_author_data[top_author_data['author_name'] == author]
        sizes = [c/10 + 20 for c in author_papers['citations'].tolist()]  # Size based on citations
        plt.scatter(author_papers['year'].tolist(), [author] * len(author_papers), 
                   s=sizes, alpha=0.6, label=author)
    
    plt.title('Top Authors: Publication Timeline and Citation Impact')
    plt.xlabel('Publication Year')
    plt.ylabel('Author Name')
    plt.grid(True, alpha=0.3)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Author network plot saved to {output_path}")

def generate_all_visualizations(df: pd.DataFrame):
    """
    Generate all visualizations for the dataset.
    
    Args:
        df: DataFrame containing researcher data
    """
    create_citations_distribution_plot(df)
    create_researcher_productivity_plot(df)
    create_citations_vs_coauthors_plot(df)
    create_publication_trends_plot(df)
    create_journal_distribution_plot(df)
    create_author_network_plot(df)
    print("All visualizations generated successfully!")

if __name__ == "__main__":
    # Example usage
    try:
        df = pd.read_csv("data/researchers.csv")
        generate_all_visualizations(df)
    except FileNotFoundError:
        print("Data file not found. Please run generate_data.py first.")
    except Exception as e:
        print(f"Error: {e}")
