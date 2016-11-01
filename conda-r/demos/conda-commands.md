Starting Conda
--------------

From within ArcGIS Pro, you can open the Start Menu, Select ArcGIS > ArcGIS Pro > Python Command Prompt.

From the command line, navigate to <ArcGIS Pro install>/bin/Python/scripts and run ``proenv.bat``.

Getting Help
------------

Conda inline help:

```
conda --help
```

Supports specific help for every subcommand. For example,

```
conda install --help
```

Environment Information
-----------------------

Conda info reveals the current state of the environment:

```
conda info
```

We can also get a list of installed packages in the current environment:

```
conda list
```

    # packages in environment at C:\ArcGIS\bin\Python\envs\arcgispro-py3:
    #
    colorama                  0.3.7                    py35_0    defaults
    cycler                    0.10.0                   py35_0    defaults
    future                    0.15.2                   py35_0    defaults
    matplotlib                1.5.3              np111py35_0e  [arcgispro]  esri
    mpmath                    0.19                     py35_1    defaults
    netcdf4                   1.2.4                   py35_0e  [arcgispro]  esri
    nose                      1.3.7                    py35_1    defaults
    numexpr                   2.6.1              np111py35_0e  [arcgispro]  esri
    numpy                     1.11.2                  py35_0e  [arcgispro]  esri
    pandas                    0.19.0              np111py35_0    defaults
    pip                       8.1.2                    py35_0    defaults
    py                        1.4.31                   py35_0    defaults
    pyparsing                 2.1.4                    py35_0    defaults
    pypdf2                    1.26.0                     py_0    esri
    pytest                    2.9.2                    py35_0    defaults
    python                    3.5.2                         0    defaults
    python-dateutil           2.5.3                    py35_0    defaults
    pytz                      2016.6.1                 py35_0    defaults
    requests                  2.11.1                   py35_0    defaults
    scipy                     0.18.1             np111py35_0e  [arcgispro]  esri
    setuptools                27.2.0                   py35_1    defaults
    sympy                     1.0                      py35_0    defaults
    wheel                     0.29.0                   py35_0    defaults
    xlrd                      1.0.0                    py35_0    defaults
    xlwt                      1.1.2                    py35_0    defaults

Installing packages
-------------------

Install using:

```
conda install
```

For example, to install the Jupyter package:

```
conda install jupyter
```

Note that asking for a single package may actually install many packages, because conda resolves dependencies for packages.


Finding packages
----------------

From the command line:

```
conda search <name>
```

But it can be hard to find packages this way as only names are searched. Often it is more useful to look on [Anaconda.org](https://anaconda.org) for the package. Once you've located the package of interest, check that it has a verison for your environment ("win-64" are Windows packages), and the name of the channel. For example, to install the ``rtree`` package from the channel ``ocefpaf``:

```
conda install -c ocefpaf rtree
```
