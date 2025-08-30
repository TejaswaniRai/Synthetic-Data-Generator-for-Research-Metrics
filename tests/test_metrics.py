import unittest
import pandas as pd
import numpy as np
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.compute_metrics import compute_basic_metrics, compute_citation_distribution

class TestComputeMetrics(unittest.TestCase):
    
    def setUp(self):
        """Set up test data for metrics computation"""
        # Create sample data for testing that matches the actual data structure
        self.sample_data = pd.DataFrame({
            'researcher_id': [1, 1, 2, 2, 3],
            'paper_id': ['R1_P1', 'R1_P2', 'R2_P1', 'R2_P2', 'R3_P1'],
            'citations': [50, 100, 150, 200, 250],
            'co_authors': [2, 3, 1, 2, 4]
        })
    
    def test_compute_basic_metrics_returns_dataframe(self):
        """Test that compute_basic_metrics returns a pandas DataFrame"""
        result = compute_basic_metrics(self.sample_data)
        self.assertIsInstance(result, pd.DataFrame)
    
    def test_compute_basic_metrics_contains_expected_columns(self):
        """Test that the result contains expected metric columns"""
        result = compute_basic_metrics(self.sample_data)
        expected_columns = [
            'researcher_id', 'total_papers', 'total_citations', 
            'avg_citations', 'max_citations', 'min_citations'
        ]
        for col in expected_columns:
            self.assertIn(col, result.columns)
    
    def test_compute_basic_metrics_calculations(self):
        """Test that basic metrics are calculated correctly"""
        result = compute_basic_metrics(self.sample_data)
        
        # Check researcher 1: 2 papers, 150 total citations
        researcher_1 = result[result['researcher_id'] == 1].iloc[0]
        self.assertEqual(researcher_1['total_papers'], 2)
        self.assertEqual(researcher_1['total_citations'], 150)
        self.assertEqual(researcher_1['avg_citations'], 75.0)
        self.assertEqual(researcher_1['max_citations'], 100)
        self.assertEqual(researcher_1['min_citations'], 50)
    
    def test_compute_citation_distribution_returns_series(self):
        """Test that compute_citation_distribution returns a pandas Series"""
        result = compute_citation_distribution(self.sample_data)
        self.assertIsInstance(result, pd.Series)
    
    def test_compute_citation_distribution_values(self):
        """Test that citation distribution contains expected values"""
        result = compute_citation_distribution(self.sample_data)
        # Should have citation counts as index and frequencies as values
        self.assertEqual(result[50], 1)  # One paper with 50 citations
        self.assertEqual(result[100], 1)  # One paper with 100 citations
        self.assertEqual(result[150], 1)  # One paper with 150 citations
    
    def test_empty_dataframe(self):
        """Test behavior with empty DataFrame"""
        empty_df = pd.DataFrame(columns=['researcher_id', 'paper_id', 'citations', 'co_authors'])
        result = compute_basic_metrics(empty_df)
        self.assertEqual(len(result), 0)
        self.assertIsInstance(result, pd.DataFrame)
    
    def test_missing_columns(self):
        """Test behavior with missing required columns"""
        incomplete_df = pd.DataFrame({
            'researcher_id': [1, 2],
            'paper_id': ['P1', 'P2']
        })
        with self.assertRaises(KeyError):
            compute_basic_metrics(incomplete_df)
    
    def test_nan_values_handling(self):
        """Test handling of NaN values in input data"""
        data_with_nan = self.sample_data.copy()
        data_with_nan.loc[0, 'citations'] = np.nan
        result = compute_basic_metrics(data_with_nan)
        # Should handle NaN gracefully
        self.assertEqual(len(result), 3)  # Should still have 3 researchers
    
    def test_negative_citations(self):
        """Test behavior with negative citation values"""
        negative_data = self.sample_data.copy()
        negative_data.loc[0, 'citations'] = -10
        result = compute_basic_metrics(negative_data)
        # Should handle negative values appropriately
        self.assertTrue(result['min_citations'].min() <= 0)

if __name__ == '__main__':
    unittest.main()
