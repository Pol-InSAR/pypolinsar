import numpy as np
from pypolinsar.polsar.decompositions import h_a_alpha_decomposition

def test_h_a_alpha_decomposition_dimensionality():
    # for a single matrix, the four outputs are scalars
    matrix = np.eye(3, 3, dtype=np.cfloat) # shape (3, 3)
    h, a, am, ad = h_a_alpha_decomposition(matrix)
    assert h.shape == ()
    assert a.shape == ()
    assert am.shape == ()
    assert ad.shape == ()
    # for a batch of matrices, the four outputs are vectors that follow the batch dimensions    
    matrix_batch = np.tile(matrix, (7, 11, 5, 1, 1)) # shape (7, 11, 5, 3, 3)
    h, a, am, ad = h_a_alpha_decomposition(matrix_batch)
    assert h.shape == (7, 11, 5)
    assert a.shape == (7, 11, 5)
    assert am.shape == (7, 11, 5)
    assert ad.shape == (7, 11, 5)
