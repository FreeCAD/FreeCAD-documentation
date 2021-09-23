# Conda
 

## Introduction

 

This page is meant to introduce Conda as a package, dependency, and environment manager for FreeCAD.

Currently this page mainly catalogs links to relevant FreeCAD forum discussion and other places on the web, but the hope is to document the salient points from those links into this page.

See also a [video tutorial](https://www.youtube.com/watch?v=sCs8xlrw2nM) of the contents of this page

## Motivation

The motivation for using Conda is multi-fold, as is Conda\'s purpose.

Let\'s break it down.

### Conda as a Package Manager 

First, Conda is a package manager \-- similar to apt or pip.

This means we can install **packages** with a a simple conda install from various [channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html#what-is-a-conda-channel) such as [conda-forge](https://conda-forge.org/).

Conda Forge is analogous to [the Python Package Index (PyPI)](https://pypi.org/), a community channel made up of thousands of contributors, and serves [freecad](https://anaconda.org/conda-forge/freecad) as a conda package.

### Conda as a Dependency Manager 

Next, Conda is a dependency manager, also similar to apt or pip.

Conda can manage the dependencies and install the dependencies for a project like FreeCAD.

Why not just use pip? pip works really well for managing the dependencies of projects that *only* use python.

Conda works for multiple languages, and is therefore better suited for managing the dependencies of projects like FreeCAD that have dependencies across a variety of languages like C / C++ and Python.

### Conda as a Environment Manager 

Conda has the concept of an [environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) which is the unique combination of packages and versions needed to run a piece of software. For example, a FreeCAD workbench.

With environments, you can easily \"activate\" and \"deactivate\" them, or switch between versions of packages needed for particular pieces of software.

This is useful for testing how a workbench behaves with a particular set of packages. For example, how does a workbench behave in FreeCAD 18.4 vs 19?

Conda environments allow you to reproduce the same exact environment on different machines.

For example, multiple local developer machines, or a remote build-server hosted by Travis CI.

## Installing Conda 

1\. [Install Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2\. Verify your installation was successful and familiarize yourself with the  

## Installing FreeCAD Using Conda 

First, you need to decide whether you want to install a **stable** version of FreeCAD, or experiment with the latest **unstable** code from FreeCAD master.

Stable released versions of FreeCAD are served on the conda-forge channel, while the latest from FreeCAD master is served on the freecad/label/dev channel.

  Conda Channel         Stable?
  --------------------- ---------
  conda-forge         Yes ✔️
  freecad/label/dev   No ❌

Secondly, since you can easily create dedicated environments in conda, it\'s recommended to create one for FreeCAD.

The  
```python
conda create --name fcenv --channel conda-forge freecad
``` **Tip:** You can alternatively tell  
```python
conda config --add channels conda-forge
``` The weekly builds can be installed from the  
```python
conda create --name fcenv-dev --channel freecad/label/dev freecad
```

## FreeCAD Forum Discussion 

-   [Let\'s talk about Conda](https://forum.freecadweb.org/viewtopic.php?t=39656)
-   [Packaging solution: (ana)conda](https://forum.freecadweb.org/viewtopic.php?f=10&t=15197)
-   [FreeCAD Conda Distribution](https://forum.freecadweb.org/viewtopic.php?f=8&t=45582)

## See Also 

-   <https://docs.conda.io/en/latest/>
-   <https://conda-forge.org/docs/>
-   <https://docs.conda.io/projects/conda-build/en/latest/>
-   <https://anaconda.org/conda-forge/freecad>
-   <https://anaconda.org/freecad/freecad>
-   <https://github.com/FreeCAD/FreeCAD_Conda>
-   <https://github.com/FreeCAD/FreeCAD-AppImage>



[Category:Developer\_Documentation](Category:Developer_Documentation.md) [Category:Developer](Category:Developer.md)
