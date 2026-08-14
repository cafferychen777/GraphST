import numpy as np
import pandas as pd
import scanpy as sc
import torch

from GraphST.GraphST import GraphST
from GraphST.preprocess import sparse_mx_to_torch_sparse_tensor
from GraphST.utils import refine_label


def _adata() -> sc.AnnData:
    rng = np.random.default_rng(42)
    adata = sc.AnnData(rng.poisson(2.0, size=(24, 12)).astype(np.float32))
    adata.var["highly_variable"] = True
    adata.obsm["spatial"] = np.column_stack(
        (np.arange(24, dtype=float), np.zeros(24, dtype=float))
    )
    return adata


def test_representation_training_is_finite_and_deterministic() -> None:
    first = GraphST(_adata(), epochs=2, dim_output=4, random_seed=7).train()
    second = GraphST(_adata(), epochs=2, dim_output=4, random_seed=7).train()

    # GraphST publishes the reconstructed expression representation used by
    # its official downstream clustering workflow, not the latent bottleneck.
    assert first.obsm["emb"].shape == (24, 12)
    assert np.isfinite(first.obsm["emb"]).all()
    np.testing.assert_allclose(first.obsm["emb"], second.obsm["emb"], atol=1e-6)


def test_sparse_conversion_uses_supported_coo_tensor() -> None:
    from scipy import sparse

    matrix = sparse.eye(3, format="coo", dtype=np.float32)
    tensor = sparse_mx_to_torch_sparse_tensor(matrix)

    assert tensor.layout == torch.sparse_coo
    assert tensor.is_coalesced()
    np.testing.assert_allclose(tensor.to_dense().numpy(), np.eye(3))


def test_refinement_uses_neighbor_majority() -> None:
    adata = _adata()[:4].copy()
    adata.obsm["spatial"] = np.array([[0, 0], [1, 0], [2, 0], [3, 0]])
    adata.obs["domain"] = pd.Categorical(["a", "b", "b", "b"])

    assert refine_label(adata, radius=2, key="domain")[0] == "b"
