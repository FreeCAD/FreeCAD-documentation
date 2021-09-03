


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Esta plantilla es la guía para un proyecto de desarrollo de FreeCAD. Sigue las reglas del proceso [Getting Things Done (GTD)](http://en.wikipedia.org/wiki/Getting_Things_Done#Methodology). Los proyectos se recogen en la [Hoja de ruta de desarrollo](Development_roadmap/es.md).

## Propósito y principios {#propósito_y_principios}

Este es un proyecto de desarrollo para encontrar, discutir e implementar un STEP i/o más avanzado en FreeCAD.

## Resultado

-   lectura/escritura de archivos STEP complejos en la definición de datos de ensamblaje (con color y toda la información adicional).
-   \....


<div class="mw-translate-fuzzy">

## Lluvia de ideas {#lluvia_de_ideas}

En primer lugar hay que recopilar toda la información sobre el asunto


</div>


<div class="mw-translate-fuzzy">

### STEP general {#step_general}

La norma ISO 10303 (STEP) es muy importante en este ámbito. Es la única buena definición estandarizada y ampliamente y reconocida definición de estructuras de producto que conozco.


</div>

![](images/Product_structure_modeling_Process-Data_diagram.gif ) 


<div class="mw-translate-fuzzy">

Aquí algunos enlaces con información:

-   [ISO 10303 en Wikipedia](http://en.wikipedia.org/wiki/ISO_10303)
-   [WikiStep.org](http://www.wikistep.org/index.php/Main_Page) con mucha información básica pero sobre todo hacia STEP-NC
-   La [estructura del producto](http://www.wikistep.org/index.php/Product_Basics) en STEP
-   Algunos [ejemplos](http://www.wikistep.org/index.php/STEP_Tutorial) sobre STEP
-   [ISO 10303-11](http://en.wikipedia.org/wiki/ISO_10303-11) sobre el lenguaje de modelado (EXPRESS)
-   [Un artículo de Wikipedia](http://en.wikipedia.org/wiki/Product_Structure_Modeling) sobre el modelado de productos
-   [Visión general de la Parte 41 \-- Fundamentos de la descripción y soporte de productos](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part41)
-   [Visión general de la Parte 44 (edición 2) \-- Configuración de la estructura del producto](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part44)
-   [Ejemplos de pequeños archivos AP 214](http://www.steptools.com/support/stdev_docs/express/ap214/index.html)
-   [Modelos de validación STEP](http://www.cax-if.org/library/index.html)
-   [Documentación interactiva con diagramas EXPRESS-G](http://jotneit.no/www2/www/pdm/pdm_schema/diagrams/diagram_0002.htm)
-   [STEPCode Doxygen docu con diagramas](http://stepcode.org/stepcode-use-doxygen)


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

### Literature & Papers {#literature_papers}

-   [Florian Arnold, Gerd Podehl, \"Best of Both Worlds - A Mapping from EXPRESS-G to UML, 1998\"](https://kluedo.ub.uni-kl.de/frontdoor/deliver/index/docId/459/file/no_series_8.pdf)

:   The paper introduces a mapping between EXPRESS-G and UML in order to define a linking bridge and bring the best of both worlds together. Feasibility of amapping is shown with representative examples; several problematic cases are discussed as well as possible solution

### Open Source Tools {#open_source_tools}

#### Tools working with EXPRESS schemes {#tools_working_with_express_schemes}

-   [Express Engine Project](http://exp-engine.sourceforge.net/), an ANSI Common Lisp based project to support EXPRESS (ISO 10303-11) information model schema development and data population validation, EXPRESS-X (ISO 10303-14) map and view development and EXPRESS-X map and view execution environment

-   [JSDAI](http://www.jsdai.net/), an Application Programming Interface (API) for reading, writing and runtime manipulation of object oriented data defined by an EXPRESS based data model.

#### Tools generating C++ code from EXPRESS schemes {#tools_generating_c_code_from_express_schemes}

-   [Stepcode github repository](https://github.com/stepcode/stepcode) STEPcode (formerly NIST\'s STEP Class Library) is used with IFC, STEP, and other standards that utilize the technologies of ISO10303 (STEP). It generates C++ and Python from EXPRESS (10303-11) schemas. The code is capable of reading and writing STEP Part 21 exchange files. It also utilizes Parts 22 and 23 (SDAI and its C++ binding).

-   [Le générateur Expressik LightCpp](http://www.unit.eu/cours/bim/u12/co/u12_020_12-1-1.html) The Expressik generator is the result of a collaboration between the University of Manchester, the European Space Agency (ESA) and the CSTB.


<div class="mw-translate-fuzzy">

### Información sobre el paso OCC {#información_sobre_el_paso_occ}

-   [documentación sobre el paso OCC](http://dev.opencascade.org/doc/overview/html/user_guides__step.html)


</div>

## Organización

## Próximas acciones {#próximas_acciones}

-   Recoger información y probar las clases OCC STEP



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
