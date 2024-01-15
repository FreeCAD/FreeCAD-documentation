# Part Loft/it
---
 GuiCommand:   Name: Part Loft   Name/it: Loft   MenuLocation: Part , Loft...   ---


</div>

## Description

The <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Loft](Part_Loft.md) command creates a face, a shell, or a solid shape from two or more profiles (cross-sections).

<img alt="" src=images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg  style="width:400px;"> 
*Loft from three profiles which are two [Part Circles](Part_Circle.md) and one [Part Ellipse](Part_Ellipse.md). Parameters are Solid "True" and Ruled "True".*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Loft.svg" width=16px> [Loft...](Part_Loft.md)** button.
    -   Select the **Part → <img src="images/Part_Loft.svg" width=16px> Loft...** option from the menu.
2.  The Loft [task panel](Task_panel.md) opens.
3.  In the *Available Profiles* list on the left select the first profile and click on the right arrow to place it in the *Selected profiles* list on the right.
4.  Repeat for the second profile and again if more than two profiles are desired.
5.  Optionally use the up and down arrows to reorder the selected profiles.
6.  Define options [Create solid](#Data.md), [Ruled surface](#Data.md), and [Closed](#Data.md).
7.  Click **OK**.

### Accepted geometry 


<div class="mw-translate-fuzzy">

## Introduzione

Lo strumento Loft di FreeCAD (dell\'ambiente Parte), viene utilizzato per creare una faccia, un guscio o una forma solida da due o più profili. I profili possono essere un punto (vertice), una linea (bordo), una spezzata o una faccia. I bordi e le polilinee possono essere di tipo aperto o chiuso. Ci sono varie [limitazioni e complicazioni](Part_Loft/it#Limitazioni_e_complicazioni.md), descritte in seguito, tuttavia i profili possono provenire da primitive di Parte, da funzioni di Draft e da Schizzi.


</div>

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles. <small>(v0.20)</small> 

## Options

#### Create solid 


<div class="mw-translate-fuzzy">

Se \"Solid\" è \"true\" FreeCAD crea un solido se i profili sono una geometria chiusa, se è \"false\" crea una faccia oppure un guscio se c\'è più di una faccia, sia per profili aperti che chiusi.


</div>

#### Ruled surface 


<div class="mw-translate-fuzzy">

Se \"Ruled\" è \"true\" FreeCAD crea una faccia, oppure delle facce o un solido dalle superfici rigate. Vedere la pagina [Ruled surface in Wikipedia.](http://en.wikipedia.org/wiki/Ruled_surface)


</div>

#### Closed


<div class="mw-translate-fuzzy">

Se \"Closed\" è \"true\" FreeCAD tenta di collegare l\'ultimo profilo al primo profilo per creare una figura chiusa.


</div>


<div class="mw-translate-fuzzy">

Per ulteriori informazioni su come sono uniti i profili, fare riferimento alla pagina [Dettagli tecnici di Part Loft](Part_Loft_Technical_Details/it.md).


</div>

## Properties

See also: [Property editor](Property_editor.md).

A Part Loft object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Loft}}

-    **Sections|LinkList**: lists the sections used.

-    **Solid|Bool**: true or false (default). True creates a solid.

-    **Ruled|Bool**: true or false (default). True creates a ruled surface.

-    **Closed|Bool**: rue or false (default). True creates a closed loft by connecting last to first profile.

-    **Max Degree|IntegerConstraint**: Maximum degree.

## Limitations

A Part Loft has the same limitations as a [Part Sweep](Part_Sweep#Limitations.md).

### Closed Lofts 


<div class="mw-translate-fuzzy">

-   Loft chiusi
    -   I risultati dei loft chiusi possono essere inaspettati - il loft può produrre torsioni o piegature. L\'operazione Loft è molto sensibile al posizionamento dei profili e per collegare i corrispondenti vertici in tutti i profili servono curve molto complesse.


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/it
