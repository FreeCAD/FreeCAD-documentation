---
- TutorialInfo:/ro
   Topic: Blueprints / Drawings
   Level: Beginner
   Time: 15 minutes
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
   FCVersion:0.16 or above
   Files:
---

# Drawing tutorial/ro

 **Development of the [[Drawing Workbench]] stopped in FreeCAD 0.16, and the new [[TechDraw Workbench]] aiming to replace it was introduced in v0.17. Both workbenches are still provided in v0.17, but the Drawing Workbench may be removed in future releases.**




<div class="mw-translate-fuzzy">

### Introducere

Acest tutorial are rolul de a prezenta cititorului fluxul de lucru de bază al atelierului [ Drawing Workbench](Drawing_Workbench.md), precum și majoritatea instrumentelor disponibile pentru a crea planuri.


</div>

<img alt="" src=images/Drawing_tutorial_result.png  style="width:480px;">

### Cerințe

-   FreeCAD version 0.16 sau mai recent
-   cititorul are noțiunile de bază pentru a utiliza Atelierele Part and PartDesign Workbenches
-   Cititorul a finalizat [Draft tutorial](Draft_tutorial.md)

### Procedura

#### Pregătiri

Pentru a reduce timpul necesar pentru acest tutorial, este obligatoriu să grupați elemente similare în vederea arborescentă**Tree View** pentru a aplica operațiuni în același timp pentru mai multe elemente.

#### Gruparea elementelor 

=

1.  În **Tree View**, faceți clic dreapta pe numele documentului. În acest caz **Unnamed**.
2.  Selectați **Creați un grup**. Puteți modifica numele grupului făcând dublu clic pe acesta din **Vizualizarea arborescentă**.
3.  Selectați elementele pe care doriți să le adăugați și glisați-l în grup

Creează următoarele grupuri:

-   Draft\_objects
-   Draft\_dimensions
-   Draft\_annotations\_text

#### Șabloane de Desenat 

Șabloanele sunt baza pentru crearea de desene, puteți utiliza șabloanele furnizate sau creați-vă propriile.

1.  Selectați meniul derulant de lângă <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [New A3 landscape drawing](Drawing_Landscape_A3.md)
2.  Selectați **A4 Landscape**

We now have a folder called **Page** in the **Tree View**. This object will contain everything related to the **Drawing**.

#### Proiecții

Proiecțiile sunt definite ca reprezentarea vizuală a unui obiect pe un anumit plan, acesta afișează proprietățile obiectului care sunt vizibile din acea orientare specifică.

##### Proiecție Ortograpică 

Acestea sunt folosite în Inginerie pentru a specifica proprietățile unui obiect care va fi prelucrat. Există două standarde comune: proiecțiile **Angle Third** și **First Angle**.

Pentru acest tutorial, aceste proiecții nu sunt folosite deoarece obiectele noastre au o reprezentare semnificativă în planul XY.

1.  Selectați obiectul pe care îl doriți să-l proiectați în desen.
2.  Selectați <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews.md)
3.  Selectați tipul de **projection** pe care doriți a-l folosi
4.  Selectați vizualizarea pe care doriți a o adăuga

In the **General** and **Axonometric** tabs you can specify the **location**, **scale** and **separation** of each view.

##### Other Part Projections 

It is possible to create custom views of the object.

1.  Select the object you wish to project into the drawing.
2.  Select <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Insert a view](Drawing_View.md)
3.  In the **Data** tab edit the **Direction** of the **Shape View** by altering the values for the **X**, **Y**, and **Z** axes. By default, the values are **(0, 0, 1)**

You can also alter the **location**, **scale** and **rotation** of the **View** from within the **Data** tab. The same can be done for the **Orthographic Projections**.

##### Draft Projections 

The preferred way to add elements created in the **Draft Workbench** is with a tool contained in the **Draft Workbench** designed specifically for this. With this procedure, it is possible to import **Dimensions**, **Annotations**, **Shapestrings** and any other element created whithin the **Draft** Workbench.

1.  Switch to the **Draft** Workbench
2.  Select the **group** or **elements** that you wish to project. In this case **Draft\_dimensions**
3.  Select ![](images/Draft_PutOnSheet.png ) [Drawing](Draft_Drawing.md)
4.  Edit the **X** and **Y** coordinates to **(140,100)**
5.  Set the scale to 0.5

Repeat for each group and set the values to the ones specified above.

#### Exporting your work 

FreeCAD supports the export of SVG and PDF files based on your **Drawings**

##### SVG

1.  Select <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save sheet](Drawing_Save.md)
2.  Specify the path and name of the exported file

##### PDF

1.  In the **File** menu, select **Export PDF \...**
2.  Specify the path and name of the exported file


<div class="mw-translate-fuzzy">

Încheiem acum cu fluxul de lucru de bază pentru [Drawing Workbench](Drawing_Workbench.md).


</div>


<div class="mw-translate-fuzzy">

## Recommended Reading 


</div>

-   To learn how to create custom templates see [Drawing Template HowTo](Drawing_Template_HowTo.md)
-   For more information about the tools available check out the [Drawing Workbench](Drawing_Workbench.md) page


 {{Drawing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Drawing](Drawing_Workbench.md) > Drawing tutorial/ro
