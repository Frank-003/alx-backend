#!/usr/bin/env python3
"""
Adds `get_hyper` method to `Server` class
"""

import csv
from typing import Dict, List, Tuple, Union



def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start index and end index for pagination.

    Parameters:
    - page (int): The page number (1-indexed).
    - page_size (int): The size of each page.

    Returns:
    - tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset: Optional[List[List]] = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.

        Parameters:
        - page (int): The page number (default is 1).
        - page_size (int): The number of items per page (default is 10).

        Returns:
        - List[List]: A list of lists representing a page from the dataset.
        """
        # Ensure page and page_size are valid
        assert isinstance(page, int) and page > 0, "Page number must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Get dataset
        dataset = self.dataset()

        # Get the index range for the current page
        start_idx, end_idx = index_range(page, page_size)

        # Return the appropriate page of the dataset
        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination details.

        Parameters:
        - page (int): The page number (default is 1).
        - page_size (int): The number of items per page (default is 10).

        Returns:
        - Dict: A dictionary with pagination details.
        """
        # Get the data for the current page using get_page
        data = self.get_page(page, page_size)

        # Calculate total pages
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        # Determine next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return the pagination details as a dictionary
        return {
            "page_size": len(data),       # Number of items returned in this page
            "page": page,                 # Current page number
            "data": data,                 # Data of the current page
            "next_page": next_page,       # Next page number or None if there's no next page
            "prev_page": prev_page,       # Previous page number or None if there's no previous page
            "total_pages": total_pages    # Total number of pages
        }


