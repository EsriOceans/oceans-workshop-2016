SciPy Hands-on Activity
=======================

[https://github.com/esrioceans/oceans-workshop-2016/scipy/exercises](https://github.com/esrioceans/oceans-workshop-2016/scipy/exercises)

Goal
----

 - See what NumPy data looks like
 - Use a SciPy tool to analyze NumPy data
 - Use Benthic Terrain Modeler (BTM) to perform analysis

Steps
-----

0. Download the data... with Python!
```python
import arcpy
import numpy as np
import scipy.ndimage as nd
from matplotlib import pyplot as plt
import urllib

try:
    from urllib import urlretrieve as retrieve
except:
    from urllib.request import urlretrieve as retrieve

input_raster = "input_raster.tif"
data_url = "https://github.com/scw/scipy-devsummit-2016-talk/raw/master/examples/data/input_raster.tif"
retrieve(data_url, input_raster)
```

1. Convert a raster into a NumPy array:

```python
# convert to a NumPy array
r = arcpy.RasterToNumPyArray(input_raster, "", 200, 200, 0)
```    

2. What's in a NumPy Array?

```python
r.shape

r.dtype

print(r)
```
Much much more, but in the interest of time skipping the details. Check the [SciPy lecture notes](http://www.scipy-lectures.org/) for great examples of using NumPy and SciPy.

3. Run a _median filter_ over the data, plot the results.

```python
fig = plt.figure(figsize=(10, 10))
size = 25
med = nd.median_filter(r, size)

plt.imshow(med, interpolation='nearest')
a.set_title('{}x{}'.format(size, size))
plt.axis('off')

plt.savefig("median-filter.png", bbox_inches='tight')

# open the resulting figure
os.startfile("median-filter.png")
```

4. Use Benthic Terrain Model to simplify the workflow

 - Get started by [downloading BTM](https://4326.us/esri/btm-3.0-final.zip) and installing it:

    + Unzip the BTM zip file to your desired location.
    + Close any existing ArcMap sessions.
    + Double-click the btm.esriaddin file in your workspace, which will install both the graphical user interface and the toolbox into ArcGIS.
    + In addition to the user interface, you can also add the tools to ArcToolbox. Open the ArcToolbox window and pin it to the display. Right-click on the ArcToolbox top folder in the window and select Add Toolbox. Navigate to where you unzipped BTM and add the file btm.pyt.
    + To view important documentation on each script right-click on that script in the BTM toolset and select Item Description as well as Properties.
    + Click on the Add Data button in ArcMap and proceed to add your bathymetry data to your ArcMap session. You may now run the BTM tools on your data.

![Installation](https://raw.github.com/EsriOceans/btm/master/resources/btm-install.gif)


 - Open toolbox in ArcMap or ArcGIS Pro

 - Run the following tools against our raster dataset:

  + Multi-Scale Analysis > Compare Scales of Analysis
  + Surface Derivatives and Statistics > Calculate Metrics (Depth Statistics)

Bonus
-----

Can also convert NetCDF and HDF files directly in Python. These objects support both NumPy operations, and specialized operations for multi-dimensional data, and give finer grained control than the equivalent Geoprocessing tools &mdash; both are useful in different contexts.

```python
    # mention that we could also convert this to a NetCDF object -- show this but 
    # don't include it in the code snippet that they have.
    import netCDF4
    ds = netCDF4.Dataset("input.nc")

    # now, ds is a NetCDF dataset that we can manipulate
```
