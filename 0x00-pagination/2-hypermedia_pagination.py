#!/usr/bin/env python3
"""
Pagination: This script provides a Server class for paginating a database
of popular baby names.
"""

import csv
import math
from typing import List, Tuple


class Server:
    """
    Server class to handle pagination of a database containing popular baby names.
    """

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

    def get_hyper(self, page: int, page_size: int) -> dict:
        """
        Return a dictionary containing pagination-related information for a given page and page size.
        The dictionary includes:
        - 'page_size': the length of the returned dataset page
        - 'page': the current page number
        - 'data': the dataset page (equivalent to the return from the 'get_page' method)
        - 'next_page': number of the next page, None if there is no next page
        - 'prev_page': number of the previous page, None if there is no previous page
        - 'total_pages': the total number of pages in the dataset as an integer
        """
        dataset_records = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(dataset_records),
            'page': page,
            'data': dataset_records,
            'next_page': page + 1 if (page + 1) <= total_pages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the range of indexes for a given page and page size.
    Returns a tuple of size two containing a start index and an end index.
    """
    return ((page - 1) * page_size, page * page_size)
