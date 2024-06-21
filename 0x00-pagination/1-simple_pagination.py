#!/usr/bin/env python3
""" Class Server used to paginate a dataset """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ the described function above"""

    end = page_size * page
    start = end - page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ takes two integer arguments page with default value 1 and page_size
            with default value 10. """
        data = self.dataset()

        assert isinstance(page, int)
        assert page > 0

        assert isinstance(page_size, int)
        assert page_size > 0

        start, end = index_range(page, page_size)

        return data[start:end]
