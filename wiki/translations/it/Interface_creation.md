# Interface creation/it
{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

Gli utenti esperti hanno la possibilità di creare delle interfacce che li aiutino a produrre strumenti complessi per i loro [addon](Addon/it.md) personalizzati, come le [macro](macros/it.md) o interi [ambienti](Workbenches/it.md) .


</div>

Le interfacce vengono create usando [PySide](PySide/it.md), che è una libreria per l\'utilizzo di Qt con [Python](Python/it.md).

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> 
*Due metodi generali per creare delle interfacce, includendo l'interfaccia nel file Python o usando i file `.ui*.`

## Descrizione

Esistono in genere due modi per creare delle interfacce con PySide.

### Interface in a .ui file 

In this method the interface is defined in a `.ui` file (an XML document that defines the structure of the interface), which is then imported into [Python](Python.md) code that uses it. This is the recommended approach.

-   It allows the programmer to work with the graphical interface separately from the logic that will use it.
-   It allows anybody to look at the interface alone, that is, the `.ui` file, without having to run Python code.
-   The `.ui` file may be designed by anybody without programming knowledge.
-   The `.ui` interface can be used in a standalone window (modal), or in an embedded window (non-modal); therefore, this method is ideal to create custom [task panels](Task_panel.md).
-   Since the `.ui` file just describes the \"appearance\" of the interface, it does not need to be tied to a particular programming language; it may be used both in [Python](Python.md) and C++ code.

### Interface completely in Python code 

In this method the entire interface is defined by several Python calls.

-   This is an older way of working with interfaces.
-   This method produces very verbose code because many details of the interface need to be specified by hand.
-   It is not simple to separate the interface from the logic that uses that code, meaning that a user would need to run the [Python](Python.md) file in the correct context in order to see how the interface would look.
-   This method has the advantage that several interfaces may be contained within a single document, at the expense of making the file very large.
-   This method is recommended only for small interfaces that don\'t define more than a few widgets, for example in [macros](Macros.md).

For examples on this method see [Interface creation completely in Python](Dialog_creation.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Interface creation/it
