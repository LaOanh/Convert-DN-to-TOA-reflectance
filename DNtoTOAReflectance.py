'''create on 23 April 2021 by Oanh Thi La
purpose: converting DN to TOA reflectance for Landsat 8'''


import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import numpy as np
import rasterio as rio


def get_MTLfile():
    Root = tkinter.Tk()  # Create a Tkinter.Tk() instance
    Root.withdraw()  # Hide the Tkinter.Tk() instance

    metadata = askopenfilename(title=u'Open MTL file', filetypes=[("MTL", ".txt")])
    fh = open(metadata)
    # Get rescaling parameters and sun_elevation angle
    mult_term = []
    add_term = []
    sun_elevation = float()
    for line in fh:
        # Read the file line-by-line looking for the reflectance transformation parameters
        if "REFLECTANCE_MULT_BAND_" in line:
            mult_term.append(float(line.split("=")[1].strip()))
        elif "REFLECTANCE_ADD_BAND_" in line:
            add_term.append(float(line.split("=")[1].strip()))
        elif "SUN_ELEVATION" in line:
            # We're also getting the sun elevation from the metadata. It has

            sun_elevation = float(line.split("=")[1].strip())
    fh.close()  # Be sure to close an open file

    return mult_term, add_term, sun_elevation

[mult_term, add_term, sun_elevation] = get_MTLfile()


def DN_toTOAreflectance(mult_term, add_term, sun_elevation):
    Root = tkinter.Tk()  # Create a Tkinter.Tk() instance
    Root.withdraw()
    bandlist = filedialog.askopenfilenames(title='Choose band files', filetypes=[("TIF", ".tif")])

    with rio.open(bandlist[0]) as src1:
        image_band1 = src1.read(1)
    image_masked_band1 = np.ma.masked_array(image_band1, mask=(image_band1 == 0))  # exclude 0 value
    constant = 0.01745329251994444444444444444444  # Constant is calculated (3.14/180) which is converting the sun-angle to sun_radians which was suggested by WOlfgang
    toa1 = (mult_term[0] * image_masked_band1.astype(float) + add_term[0])
    solar_z = np.cos((90 - float(sun_elevation)) * float(constant))
    toa_band1 = (toa1.astype(float) / solar_z)

    with rio.open(bandlist[1]) as src2:
        image_band2 = src2.read(1)
    image_masked_band2 = np.ma.masked_array(image_band2, mask=(image_band2 == 0))  # exclude 0 value
    constant = 0.01745329251994444444444444444444  # Constant is calculated (3.14/180) which is converting the sun-angle to sun_radians which was suggested by WOlfgang
    toa2 = (mult_term[1] * image_masked_band2.astype(float) + add_term[1])
    solar_z = np.cos((90 - float(sun_elevation)) * float(constant))
    toa_band2 = (toa2.astype(float) / solar_z)

    with rio.open(bandlist[2]) as src3:
        image_band3 = src3.read(1)
    image_masked_band3 = np.ma.masked_array(image_band3, mask=(image_band3 == 0))  # exclude 0 value
    constant = 0.01745329251994444444444444444444  # Constant is calculated (3.14/180) which is converting the sun-angle to sun_radians which was suggested by WOlfgang
    toa3 = (mult_term[2] * image_masked_band3.astype(float) + add_term[2])
    solar_z = np.cos((90 - float(sun_elevation)) * float(constant))
    toa_band3 = (toa3.astype(float) / solar_z)

    with rio.open(bandlist[3]) as src4:
        image_band4 = src4.read(1)
    image_masked_band4 = np.ma.masked_array(image_band4, mask=(image_band4 == 0))  # exclude 0 value
    constant = 0.01745329251994444444444444444444  # Constant is calculated (3.14/180) which is converting the sun-angle to sun_radians which was suggested by WOlfgang
    toa4 = (mult_term[3] * image_masked_band4.astype(float) + add_term[3])
    solar_z = np.cos((90 - float(sun_elevation)) * float(constant))
    toa_band4 = (toa4.astype(float) / solar_z)

    with rio.open(bandlist[4]) as src5:
        image_band5 = src5.read(1)
    image_masked_band5 = np.ma.masked_array(image_band5, mask=(image_band5 == 0))  # exclude 0 value
    constant = 0.01745329251994444444444444444444  # Constant is calculated (3.14/180) which is converting the sun-angle to sun_radians which was suggested by WOlfgang
    toa5= (mult_term[4] * image_masked_band5.astype(float) + add_term[4])
    solar_z = np.cos((90 - float(sun_elevation)) * float(constant))
    toa_band5 = (toa5.astype(float) / solar_z)

    with rio.open(bandlist[5]) as src6:
        image_band6 = src6.read(1)
    image_masked_band6 = np.ma.masked_array(image_band6, mask=(image_band6 == 0))  # exclude 0 value
    constant = 0.01745329251994444444444444444444  # Constant is calculated (3.14/180) which is converting the sun-angle to sun_radians which was suggested by WOlfgang
    toa6= (mult_term[5] * image_masked_band6.astype(float) + add_term[5])
    solar_z = np.cos((90 - float(sun_elevation)) * float(constant))
    toa_band6 = (toa6.astype(float) / solar_z)

    with rio.open(bandlist[6]) as src7:
        image_band7 = src7.read(1)
    image_masked_band7 = np.ma.masked_array(image_band7, mask=(image_band7 == 0))  # exclude 0 value
    constant = 0.01745329251994444444444444444444  # Constant is calculated (3.14/180) which is converting the sun-angle to sun_radians which was suggested by WOlfgang
    toa7= (mult_term[6] * image_masked_band7.astype(float) + add_term[6])
    solar_z = np.cos((90 - float(sun_elevation)) * float(constant))
    toa_band7 = (toa7.astype(float) / solar_z)

    with rio.open(bandlist[7]) as src8:
        image_band8 = src8.read(1)
    image_masked_band8 = np.ma.masked_array(image_band8, mask=(image_band8 == 0))  # exclude 0 value
    constant = 0.01745329251994444444444444444444  # Constant is calculated (3.14/180) which is converting the sun-angle to sun_radians which was suggested by WOlfgang
    toa8= (mult_term[7] * image_masked_band8.astype(float) + add_term[7])
    solar_z = np.cos((90 - float(sun_elevation)) * float(constant))
    toa_band8 = (toa8.astype(float) / solar_z)

    return src1, toa_band1, toa_band2, toa_band3, toa_band4, toa_band5, toa_band6, toa_band7, toa_band8

[src1, toa_band1, toa_band2, toa_band3, toa_band4, toa_band5, toa_band6, toa_band7, toa_band8] = \
    DN_toTOAreflectance(mult_term, add_term, sun_elevation)

ras_meta = src1.meta
ras_meta['dtype'] = "float32"
outfile = tkinter.filedialog.asksaveasfilename(title=u'Save TOA file', filetypes=[("TIF", ".tif")])
with rio.open(outfile, 'w', **ras_meta) as dst:
    dst.write_band(1, toa_band1.astype(rio.float32))


# import matplotlib.pyplot as plt
# imgplot = plt.imshow(toa_band2)
# plt.show()







