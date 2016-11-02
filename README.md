Scientific Tools for Marine and MetOcean Analysis
=================================================

### Kevin A. Butler, Brett Rose, Shaun Walbridge
### 2016 Esri Oceans Forum

SciPy
-----

**[View the Slides](https://4326.us/esri/scipy-ws)**
**[Exercises](./scipy/exercises)**


Conda and R
-----------

**[View the Slides](https://4326.us/esri/conda-r-ws)**
**[Exercises](./conda-r/exercises)**

Description
-----------

Esri leads the way in developing innovative geospatial solutions for the scientific community. The ArcGIS platform is a comprehensive system of engagement that enables organizations to better understand scientific data throughout the process of collection, analysis, and dissemination. In this hands-on workshop participants will explore a variety of tools for Marine, MetOcean, and Atmospheric GIS, including The R-Bridge SciPy, and Multi-Dimensional Spatial Statistics.  This workshop is led by Esri scientific staff from the development team.  Familiarity with ArcGIS geoprocessing tools is recommended.

Agenda
------

Time | Activity
-----|---------
9:00 – 9:15 | Presentation: Overview/Context (Kevin & Brett & Shaun)
9:15 – 9:45 | Presentation & Demos: Traditional Geoprocesing Workflows (acquiring, managing and analyzing multidimensional data)
9:45 – 10:30 | Directed and independent hands-on activities on MD GP workflows
10:30 – 10:45 | Break
10:45 – 11:15 | SciPy Overview/Context (Shaun & Kevin)
11:15 – 11:45 | SciPy Hand-on activity
11:45 – 1:00 | Lunch
1:00 – 1:30 | Extending ArcGIS (Shaun)
1:30 – 2:00 | Conda Hands-on activity
2:00 – 2:15 | ModelBuilder as a scientific workbench (Kevin & Shaun)
2:15 – 3:00 | ModelBuilder Hands-on (link a GP, R and Scipy tool)
3:00 – 3:15 | Spatial Statistics tools (overview) (Brett)
3:15 – 4:00 | Spatial Statistics Hand-on

Building
--------

 - From `slides/`, run `make` to rebuild the slide deck from the included slides.md file. Requires [Pandoc](http://johnmacfarlane.net/pandoc/).
 - Check links with `make check`, requires [LinkChecker](https://pypi.python.org/pypi/LinkChecker).
 - Generate handout version with `make pdf`. Requires XeTeX and pandoc.
 - Generate high-quality PDF with `make fullpdf`. Requires [decktape.js](https://github.com/astefanutti/decktape)
