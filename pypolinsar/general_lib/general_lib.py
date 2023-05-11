import scipy as sp
import numpy as np


def smooth_fast(im,size_filter):

    """this function makes a smooth interapolation of image
      it handles nan values as easy as with idl smooth (array,/nan)

    Parameters
    ----------

    im : array
        N-dimensional array to be smoothed

    size_filter: Int or tuple
        one int or N size tuple to set the smooth window


    Returns
    -------
    im_smoothed : array
        smoothed N-dimensional array


    Notes
    -----
    Author : Roman Guliaev
    Data : November 2021
    based on https://stackoverflow.com/questions/18697532/gaussian-filtering-a-image-with-nan-in-python/36307291

    """

    U = im.copy()
    V = U.copy()
    V[np.isnan(U)] = 0
    VV = sp.ndimage.uniform_filter(V, size=size_filter)

    W = 0 * U.copy() + 1
    W[np.isnan(U)] = 0
    WW = sp.ndimage.uniform_filter(W, size=size_filter)
    im_smoothed = VV / WW
    return im_smoothed
