Conda Hands-on Activity
=======================

[https://github.com/esrioceans/oceans-workshop-2016/conda-r/exercises](https://github.com/esrioceans/oceans-workshop-2016/conda-r/exercises)

Goal 
----

 - Use conda to install dependencies, then run a toolbox that won't otherwise work.

- Kevin suggested spatial methods in scikit-learn, look at that. Failing that, we should do something else which uses scikit-learn (or something similarly useful)

Steps
-----

1. Open toolbox, populate values.

2. Run it -- fails! Why's that?

3. Use conda -- command line, the UI doesn't support UAC yet.

    conda install scikit-learn

4. Add back data to toolbox, run again.

Bonus
-----

Jupyter notebooks allow interactive coding to be much simpler. We have Python API for Python which enables spatial data analysis moving between local data, ArcGIS Online data, and server data, enabled with (you guessed it) the SciPy stack.

To install with Conda:

    conda install arcgis

See details at the [ArcGIS API for Python](https://developers.arcgis.com/python/) site.
