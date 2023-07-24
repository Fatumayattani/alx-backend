#!/usr/bin/env python3
"""
Pagination
"""

from typing import Tuple


def index_range(page_number: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate and return a tuple containing a start index and an end
    index for a specific page in a paginated list.
    """
    start_index = (page_number - 1) * page_size
    end_index = page_number * page_size
    return start_index, end_index
