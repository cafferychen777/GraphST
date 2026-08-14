"""Public GraphST API."""

from importlib.metadata import PackageNotFoundError, version

__author__ = "Yahui Long"
__email__ = "long_yahui@immunol.a-star.edu.sg"

from .preprocess import (
    add_contrastive_label,
    construct_interaction,
    fix_seed,
    get_feature,
    permutation,
    preprocess,
    preprocess_adj,
)
from .utils import clustering, project_cell_to_spot

try:
    __version__ = version("graphst-modern")
except PackageNotFoundError:
__version__ = "1.1.1.post2"

__all__ = [
    "add_contrastive_label",
    "clustering",
    "construct_interaction",
    "fix_seed",
    "get_feature",
    "permutation",
    "preprocess",
    "preprocess_adj",
    "project_cell_to_spot",
]
