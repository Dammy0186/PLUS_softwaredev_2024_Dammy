"""
This script contains three functions to calculate various vegetation and water indices.
Three indices currently represented:
- Normalized Difference Vegetation Index (ndvi)
- Enhanced Vegetation Index (evi)
- Normalized Difference Water Index (ndwi)

Example: ndvi(nir, red)
    evi(nir, red, blue)
    ndwi(nir, green)

where,
	red: red band of your dataset
	nir: near infrared band of your dataset
	blue: blue band of your dataset	
	green: green band of your dataset

"""

import numpy as np

##NDVI

def ndvi(nir, red):
    """
    Calculate the Normalized Difference Vegetation Index (NDVI).

    NDVI is calculated using the formula:
    (NIR - RED) / (NIR + RED)

    Args:
        nir (np.array): Near Infrared band
        red (np.array): Red band

    Returns:
        np.array: NDVI values
    """
    ndvi = np.where((nir + red) == 0., 0, (nir - red) / (nir + red))
    return ndvi

##EVI

def evi(nir, red, blue, G=2.5, L=1, C1=6, C2=7.5):
    """
    Calculate the Enhanced Vegetation Index (EVI).

    EVI is calculated using the formula:
    G * (NIR - RED) / (NIR + C1 * RED - C2 * BLUE + L)

    Args:
        nir (np.array): Near Infrared band
        red (np.array): Red band
        blue (np.array): Blue band
        G (float): Gain factor (default is 2.5)
        L (float): Canopy background adjustment (default is 1)
        C1 (float): Coefficient 1 for aerosol resistance term (default is 6)
        C2 (float): Coefficient 2 for aerosol resistance term (default is 7.5)

    Returns:
        np.array: EVI values
    """
    evi = np.where((nir + red) == 0., 0, G * ((nir - red) / (nir + C1 * red - C2 * blue + L)))
    return evi

##NDWI

def ndwi(nir, green):
    """
    Calculate the Normalized Difference Water Index (NDWI).

    NDWI is calculated using the formula:
    (GREEN - NIR) / (GREEN + NIR)

    Args:
        nir (np.array): Near Infrared band
        green (np.array): Green band

    Returns:
        np.array: NDWI values
    """
    ndwi = np.where((nir + green) == 0., 0, (green - nir) / (green + nir))
    return ndwi