#!/usr/bin/env python3
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

