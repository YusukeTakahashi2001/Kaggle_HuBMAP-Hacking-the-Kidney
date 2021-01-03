# https://gist.github.com/brunodoamaral/e130b4e97aa4ebc468225b7ce39b3137

# module
import numpy as np

# -----

def dice_coefficient(img1,img2):
    """
    Computes the Dice coefficient, a measure of set similarity.

    Parameters
    ----------
    img1 : array-like, bool
        Any array of arbitrary size. If not boolean, will be converted.
    img2 : array-like, bool
        Any other array of identical size. If not boolean, will be converted.
    Returns
    -------
    dice : float
        Dice coefficient as a float on range [0,1].
        Maximum similarity = 1
        No similarity = 0
        
    Notes
    -----
    The order of inputs for `dice` is irrelevant. The result will be
    identical if `img1` and `img2` are switched.
    """
    img1 = np.asarray(img1).astype(np.bool)
    img2 = np.asarray(img2).astype(np.bool)

    if img1.shape != img2.shape:
        raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")

    im_sum = img1.sum() + img2.sum()
    
    if im_sum == 0:
        return 'empty_score'

    # Compute Dice coefficient
    intersection = np.logical_and(img1, img2)

    return 2. * intersection.sum() / im_sum