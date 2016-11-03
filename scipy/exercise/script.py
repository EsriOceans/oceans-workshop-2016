import arcpy
import numpy as np
import scipy.ndimage as nd
from matplotlib import pyplot as plt
import os

try:
    from urllib import urlretrieve as retrieve
except:
    from urllib.request import urlretrieve as retrieve

input_raster = "input_raster.tif"
data_url = "https://github.com/scw/scipy-devsummit-2016-talk/raw/master/examples/data/input_raster.tif"
retrieve(data_url, input_raster)
if os.path.exists(input_raster):
    print("download succeeeded")
else:
    print("download failed, try again.")

# 1. Convert a raster into a NumPy array:

# convert to a NumPy array
r = arcpy.RasterToNumPyArray(input_raster, "", 200, 200, 0)

# 2. What's in a NumPy Array?

r.shape

r.dtype

print(r)

# 3. Run a _median filter_ over the data, plot the results.

fig = plt.figure(figsize=(10, 10))
size = 25
med = nd.median_filter(r, size)

plt.imshow(med, interpolation='nearest')
plt.title('{}x{}'.format(size, size))
plt.axis('off')

plt.savefig("median-filter.png", bbox_inches='tight')

# open the resulting figure
os.startfile("median-filter.png")
