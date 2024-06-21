#!/usr/bin/env python3
"""  a function named index_range that takes two integer
     arguments page and page_size  return a tuple of size two containing
     a start index and an end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ the described function above"""

    end = page_size * page
    start = end - page_size
    return start, end
