# LGTM/pl
## Overview


{{TOCright}}

[LGTM](https://www.lgtm.com) is a code analysis tool that can be integrated into multiple online software version control systems and supports several different languages. It\'s an excellent code-quality checker, identifying code problems that often get missed by other code checkers and linters.

LGTM is well-suited as a code-analysis tool for developing FreeCAD Python workbenches and other small-to-mid-sized projects. This page provides an overview of how to get started using LGTM with a FreeCAD Python Workbench.

## Getting Started 

Getting started with LGTM depends on the online version control platform you\'re using. The LGTM documentation for [automated code review](https://lgtm.com/help/lgtm/about-automated-code-review) provides a good overview of how to get LGTM integrated into your project for several platforms.

In addition it\'s possible to do a wide range of in-depth analyses of code on LGTM, which is beyond the scope of this tutorial. You can read more about that in the LGTM documentation on [configuring code analysis](https://lgtm.com/help/lgtm/configuring-lgtm-analysis-project).

## Getting Results 

Once you\'ve set up LGTM and provided access to your code repositories, analyses are typically done daily on the repository. So, pushed changes will not yeild results immediately. It is possible to have LGTM analyze pull requests when they are submitted, as described in the LGTM documentation.

Reviewing the results simply requires logging in to your LGTM dashboard and selecting the desired project. From there, code analyses will provide a list of issues (like bugs, bad coding practices, useless/irrelevant/unused code, etc.) for your perusal. In addition LGTM provides overall code \'ratings\' (A, B, C, D) depending on the number of issue you have compared to the overall size of your project.

Probably, the most useful, immediate way to manage the results of your code analysis is simply filtering out files in your project that you don\'t want analyzed. That is, suppose you\'re developing new code that is incomplete, keeping around legacy code that is otherwise unused, or have a good deal of testing code that doesn\'t need analysis. LGTM provides [file classification](https://lgtm.com/help/lgtm/file-classification), an easy way to filter those files so they don\'t pollute your analysis results.

### Creating a .lgtm.yml File 

To enable file classification, first create a file named \".lgtm.yml\" in your projects top-most directory. Then, in that file, add some classifications.

Below is an example from the FreeCAD Trails Python workbench:


```python
path_classifiers:
  template:
    - freecad/trails/resources
    - freecad/trails/project/commands/command_template.py
    - freecad/trails/init_gui.py
 
  test:
    - freecad/trails/project/commands/spiral_test.py
    - freecad/trails/TestFPO.py
 
  legacy:
    - freecad/trails/corridor/loft
    - freecad/trails/alignment/VerticalAlignment.py
    - freecad/trails/alignment/VerticalCurve.py
    - freecad/trails/alignment/GenerateVerticalAlignment.py
    - freecad/trails/alignment/ImportVerticalCurve.py
    - freecad/trails/corridor/template/TemplateLibrary.py
```

Note that indent levels are important in LGTM. Incorrect indenting will result in failed file classification.

Also, some classifications (like \'template\' and \'test\') are used by LGTM for queries and other analysis components. You may also define your own custom tags, which will filter code and provide additional queryable results.

### Relevant Links 

-   [Continuous Integration](Continuous_Integration.md)
-   LGTM [FreeCAD forum discussion thread](https://www.forum.freecadweb.org/viewtopic.php?f=10&t=40228)
-   FreeCAD .lgtm.yml file on [Github](https://github.com/FreeCAD/FreeCAD/blob/master/lgtm.yml)
-   freecad.trails .lgtm.yml on [Github](https://github.com/joelgraff/freecad.trails/blob/dev/.lgtm.yml)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > LGTM/pl
