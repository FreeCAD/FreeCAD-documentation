# STEP project/fr
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

This template is the guideline for a FreeCAD development project. It follows the rules of the [Getting Things Done (GTD)](http://en.wikipedia.org/wiki/Getting_Things_Done#Methodology) process. The projects are collected in the [Development roadmap](Development_roadmap.md).

## Purpose and principles 

This is a development project to find, discuss and implement a more advanced STEP i/o in FreeCAD.

## Outcome

-   reading/writing complex STEP files into Assembly data definition (with color and all the additional information).
-   \....

## Brainstorming

First we need to collect all the information about the matter

### STEP in general 

The ISO 10303 (STEP) is very important in this field. Its the only good standardized and widely discussed and recognized definition of product structures I know of.

![](images/Product_structure_modeling_Process-Data_diagram.gif ) 

### Informative Links 

-   [ISO 10303 General informations on Wikipedia](http://en.wikipedia.org/wiki/ISO_10303)
-   [ISO 10303-11](https://en.wikipedia.org/wiki/EXPRESS_(data_modeling_language)) EXPRESS a data modeling language defined in ISO 10303-11
-   [Product structure modeling](http://en.wikipedia.org/wiki/Product_Structure_Modeling) Wikipedia article about product modeling
-   [Overview of Part 41 \-- Fundamentals of Product Description and Support](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part41) authentification required
-   [Overview of Part 44 (edition 2) \-- Product Structure Configuration](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part44) authentification required
-   [Examples of small AP 214 files](http://www.steptools.com/support/stdev_docs/express/ap214/index.html) authentification required
-   [STEP File Library](https://www.cax-if.org/cax/cax_stepLib.php)
-   [EXPRESS (data modeling language)](https://en.wikipedia.org/wiki/EXPRESS_(data_modeling_language))
-   [Express Data Manager™](https://jotneit.no/component/content/article/32-products/109-express-datamanager-tm)
-   [ppt presentation about Data Models for Engineering Data](https://www.dbse.ovgu.de/en/-p-594/_/dmea-04-data%20models.pdf)

### Literature & Papers 

-   [Florian Arnold, Gerd Podehl, \"Best of Both Worlds - A Mapping from EXPRESS-G to UML, 1998\"](https://kluedo.ub.uni-kl.de/frontdoor/deliver/index/docId/459/file/no_series_8.pdf)

:   The paper introduces a mapping between EXPRESS-G and UML in order to define a linking bridge and bring the best of both worlds together. Feasibility of amapping is shown with representative examples; several problematic cases are discussed as well as possible solution

### Open Source Tools 

#### Tools working with EXPRESS schemes 

-   [Express Engine Project](http://exp-engine.sourceforge.net/), an ANSI Common Lisp based project to support EXPRESS (ISO 10303-11) information model schema development and data population validation, EXPRESS-X (ISO 10303-14) map and view development and EXPRESS-X map and view execution environment

-   [JSDAI](http://www.jsdai.net/), an Application Programming Interface (API) for reading, writing and runtime manipulation of object oriented data defined by an EXPRESS based data model.

#### Tools generating C++ code from EXPRESS schemes 

-   [Stepcode github repository](https://github.com/stepcode/stepcode) STEPcode (formerly NIST\'s STEP Class Library) is used with IFC, STEP, and other standards that utilize the technologies of ISO10303 (STEP). It generates C++ and Python from EXPRESS (10303-11) schemas. The code is capable of reading and writing STEP Part 21 exchange files. It also utilizes Parts 22 and 23 (SDAI and its C++ binding).

-   [Le générateur Expressik LightCpp](http://www.unit.eu/cours/bim/u12/co/u12_020_12-1-1.html) The Expressik generator is the result of a collaboration between the University of Manchester, the European Space Agency (ESA) and the CSTB.

### OCC STEP Interface 

-   [Open CASCADE Technology - STEP Translator](https://dev.opencascade.org/doc/overview/html/occt_user_guides__step.html)

## Organizing

## Next actions 

-   collecting information and testing OCC STEP classes



[Category:Roadmap](Category:Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category:Roadmap.md) > STEP project/fr
