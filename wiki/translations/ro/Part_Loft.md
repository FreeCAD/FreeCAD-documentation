---
 GuiCommand:
   Name: Part Loft
   Name/ro: Part Loft
   MenuLocation: Part , Loft...
|
   Workbenches: Part_Workbench/ro
   SeeAlso: Part Sweep/ro
---

# Part Loft/ro


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

## Prezentare generală 

Instrumentul Loft din Atelierul (Part Workbench) este utilizat pentru a crea o fațetă, o cochilie sau o formă solidă (corp) plecând de la două sau mai multe profiluri. Profilele pot fi un punct (vertex), o linie (margine), o polilinie sau o fațetă. Muchiile și poliliniile pot fi deschise sau închise. Există mai multe limitări și complicații [limitations and complications](Part_Loft#limitations_and_complications.md) , vezi mai jos, însă profilurile pot proveni de la primitivele geometrice din Atelierul Part/Piese, de la funcționalitățile Aelierului Draft Workbench și de la Atelierul Sketch.


</div>

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles. <small>(v0.20)</small> 

## Options

#### Create solid 


<div class="mw-translate-fuzzy">

Dacă \"Solid\" are valoarea \"true\" FreeCAD creează un solid dacă profilele sunt forme geometrice închise, dacă valorea este \"false\" FreeCAD creează o fațetă sau (dacă are mi mult de o fațetă) o cochilie dacă este un profil închis sau deschis.


</div>

#### Ruled surface 


<div class="mw-translate-fuzzy">

Dacă este true\" , \"Ruled\" FreeCAD creează o fațetă, fațetele sau solidele din suprafețele riglate. [Ruled surface page on Wikipedia.](http://en.wikipedia.org/wiki/Ruled_surface)


</div>

#### Closed


<div class="mw-translate-fuzzy">

FreeCAD încearcă să atașeze ultimul profil la primul profil pentru a crea o figură închisă.


</div>


<div class="mw-translate-fuzzy">

Pentru mai multe informații supra modului cum profilele sunt legate împreună , referiți-vă la pagina [Part Loft Technical Details](Part_Loft_Technical_Details.md) .


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

-   Closed Lofts
    -   Rezultatele loft-urilor închise pot fi neașteptate - mansarda/loft ul poate dezvolta răsuciri sau deformări. Lofting-ul este foarte sensibil la Plasamentul profilurilor și la complexitatea curbelor necesare pentru conectarea Vârfurilor corespunzătoare în toate profilurile.


</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/ro
