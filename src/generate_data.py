import numpy as np
import pandas as pd
import random
import os
from faker import Faker

fake = Faker()

def generate_researcher_data(
    n_researchers: int = 20,
    max_papers: int = 50,
    max_citations: int = 500,
    start_year: int = 1980,
    end_year: int = 2023,
    seed: int = 42
) -> pd.DataFrame:
    """
    Generate synthetic dataset of researchers with:
    - paper titles
    - author names
    - number of papers
    - citations per paper
    - co-author count per paper
    - publication year
    - journal name
    """
    np.random.seed(seed)
    random.seed(seed)
    Faker.seed(seed)

    data = []
    for researcher_id in range(1, n_researchers + 1):
        # Generate a fake author name for the researcher
        author_name = fake.name()
        num_papers = np.random.randint(5, max_papers)   # between 5 and max_papers
        for paper_id in range(1, num_papers + 1):
            citations = np.random.randint(0, max_citations)
            co_authors = np.random.randint(1, 10)  # number of co-authors
            year = np.random.randint(start_year, end_year + 1)
            journal = fake.catch_phrase() + " Journal"
            title = fake.sentence(nb_words=6).rstrip('.')
            # Generate co-author names (excluding main author)
            co_author_names = [fake.name() for _ in range(co_authors)]
            # Combine main author and co-authors
            authors = [author_name] + co_author_names
            authors_str = "; ".join(authors)

            data.append({
                "researcher_id": researcher_id,
                "author_name": author_name,
                "paper_id": f"R{researcher_id}_P{paper_id}",
                "title": title,
                "authors": authors_str,
                "co_authors_count": co_authors,
                "citations": citations,
                "year": year,
                "journal": journal
            })

    df = pd.DataFrame(data)
    return df


def save_dataset(df: pd.DataFrame, filename: str = "data/researchers.csv"):
    """Save DataFrame to CSV file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")


if __name__ == "__main__":
    df = generate_researcher_data(n_researchers=100)
    print(df.head())
    save_dataset(df, "data/researchers.csv")
