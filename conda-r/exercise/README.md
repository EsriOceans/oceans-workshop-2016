Conda Hands-on Activity
=======================

Goal 
----

 - Use conda to install dependencies, then run a toolbox that won't otherwise work.

- Kevin suggested spatial methods in scikit-learn, look at that. Failing that, we should do something else which uses scikit-learn (or something similarly useful)

Steps
-----

1. Open toolbox, `sdm.pyt`, populate values.

2. Run it -- fails! Why's that?

3. Use conda, either from the command line, or from the UI.
   + To install from the command line, run:

    ```sh
        conda install scikit-learn
    ```
    
   + To install from Pro:
     1. Click on "Project" then select "Python".
     2. Select the "Add Packages" tab.
     3. In the search box type "scikit". Select the `scikit-learn` package.
     4. Click "Install".
    

4. Add back data to toolbox, run again.

Bonus
-----

Jupyter notebooks allow interactive coding to be much simpler. We have Python API for Python which enables spatial data analysis moving between local data, ArcGIS Online data, and server data, enabled with (you guessed it) the SciPy stack.

To install with Conda:

    conda install arcgis

See details at the [ArcGIS API for Python](https://developers.arcgis.com/python/) site.
