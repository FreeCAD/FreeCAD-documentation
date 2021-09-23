# STEP project/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Questo modello contiene le linea guida per il progetto di sviluppo di FreeCAD. Esso segue le regole della metodologia \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\]. I progetti sono raccolti nel [Piano di sviluppo](Development_roadmap/it.md) (Development roadmap).

### Finalità e principi 

Si tratta di un progetto di sviluppo per individuare, discutere e implementare un sistema più avanzato di importazione e esportazione dei file STEP in FreeCAD.

### Risultati

-   lettura e scrittura di file STEP complessi nel sistema di definizione dei dati di Assembly (con il colore e tutte le informazioni aggiuntive).
-   \....


<div class="mw-translate-fuzzy">

### Riflessioni

In primo luogo è necessario riunire tutte le informazioni sulla questione.


</div>


<div class="mw-translate-fuzzy">

### Aspetti generali su STEP 

La norma ISO 10303 (STEP) è molto importante in questo campo. È l\'unico buono standard, ampiamente discusso e riconosciuto di definizione di strutture di prodotto che conosco.


</div>

![](images/Product_structure_modeling_Process-Data_diagram.gif ) 


<div class="mw-translate-fuzzy">

Ecco alcuni link con delle informazioni:

-   [ISO 10303 on Wikipedia](http://en.wikipedia.org/wiki/ISO_10303)
-   [WikiStep.org](http://www.wikistep.org/index.php/Main_Page) with a lot of basic info but mostly toward STEP-NC
-   The [product structure](http://www.wikistep.org/index.php/Product_Basics) in STEP
-   Some [examples](http://www.wikistep.org/index.php/STEP_Tutorial) about STEP
-   [ISO 10303-11](http://en.wikipedia.org/wiki/ISO_10303-11) about the modeling language (EXPRESS)
-   [A Wikipedia article](http://en.wikipedia.org/wiki/Product_Structure_Modeling) about product modeling
-   [Overview of Part 41 \-- Fundamentals of Product Description and Support](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part41)
-   [Overview of Part 44 (edition 2) \-- Product Structure Configuration](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part44)
-   [Examples of small AP 214 files](http://www.steptools.com/support/stdev_docs/express/ap214/index.html)
-   [STEP validation models](http://www.cax-if.org/library/index.html)
-   [Interactive documentation with EXPRESS-G diagrams](http://jotneit.no/www2/www/pdm/pdm_schema/diagrams/diagram_0002.htm)
-   [STEPCode Doxygen docu with diagrams](http://stepcode.org/stepcode-use-doxygen)


</div>

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


<div class="mw-translate-fuzzy">

### Informazioni sull\'importazione e esportazione OCC Step 

-   [documentation on OCC step](http://dev.opencascade.org/doc/overview/html/user_guides__step.html)


</div>

### Organizzazione

### Azioni successive 

-   raccogliere informazioni e testare le classi OCC STEP



[Category:Roadmap](Category:Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category:Roadmap.md) > STEP project/it
