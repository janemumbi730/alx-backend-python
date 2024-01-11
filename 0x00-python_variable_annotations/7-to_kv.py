#!/usr/bin/env python3
"""
Module 7-to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string k and an int OR float v as arguments
    """
    return (k, (v ** 2))
