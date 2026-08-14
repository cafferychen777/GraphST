# GraphST Modern

`graphst-modern` is a maintained distribution of
[GraphST](https://github.com/JinmiaoChenLab/GraphST), the graph
self-supervised learning method for spatial transcriptomics.

The original PyPI metadata listed only `requests`, although the import package
requires PyTorch, Scanpy, SciPy, scikit-learn, POT, pandas, and NumPy. This
distribution declares the complete runtime graph and supports Python 3.11-3.14.
It keeps the original import name and numerical API:

```bash
pip install graphst-modern
```

```python
from GraphST.GraphST import GraphST
```

The optional R-based mclust helper is available with
`pip install 'graphst-modern[r-clustering]'`. GraphST representation learning
does not require R.

This repository intentionally contains only importable source, tests, and
packaging metadata. Upstream example datasets and generated images are not
runtime dependencies and are not duplicated here.

GraphST is distributed under the GNU Affero General Public License v3. The
original authors and source revision are recorded in `NOTICE.md`.
