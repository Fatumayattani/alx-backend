#!/usr/bin/env python3
"""
Pagination: This script provides a Server class for paginating a database
of popular baby names.
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to handle pagination of popular baby names database."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset: Loads and caches the dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a list of baby names for the specified page and page size.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        [start, end] = index_range(page, page_size)
        return self.dataset()[start: end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the range of indexes for a given page and page size.
    Returns a tuple of size two containing a start index and an end index.
    """
    return ((page - 1) * page_size, page * page_size)
