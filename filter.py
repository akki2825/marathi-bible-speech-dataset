"""
Filter functions to remove specific parts.
"""
from typing import List


def filter_ipas(sentence: str, ipas_lst: List[str]) -> List[str]:
    """
    filters the list of ipas passed.
    """
    return [sentence for item in ipas_lst if item in sentence]
