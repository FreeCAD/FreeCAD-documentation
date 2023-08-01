# <img alt="Surface workbench icon" src=images/Workbench_Surface.svg  style="width:64px;"> Surface Workbench/ro






## Introducere

Atelierul**Surface**oferă instrumente pentru crearea și modificarea suprafețelor. Are o funcționalitate foarte asemănătoare cu [Part Shape builder](Part_Shapebuilder/ro.md) *Face from edges*, dar este parametrică și oferă opțiuni suplimentare. Funcționalile sale sunt:

-   Creați suprafețe de la margini
-   Aliniați curbura de la fațetele vecine
-   Constrângeți suprafețele la curbe sau vârfuri suplimentare.
-   Extindeți fațetele (trebuie să aflați cum!)
-   O plasă poate fi utilizată ca șablon pentru a crea curbe spline pe suprafața sa.

Some of the features provided are:

-   Creation of surfaces from boundary edges.
-   Alignment of the curvature from neighboring faces.
-   Constraining of surfaces to additional curves and vertices.
-   Extension of faces.
-   A mesh can be used as a template to create spline curves on its surface.

<img alt="" src=images/Surface_example.png  style="width:350px;">

## Usage

Scopul atelierului de lucru de suprafață este de a crea fațete cu forme care nu sunt disponibile cu uneltele standard din celelalte ateliere. Kernelul Open Cascade CAD oferă ca exemplu un colț rotunjit al unei casete dreptunghiulare cu diferite raze la marginile sale. Un alt exemplu este prezentat aici. Este o formă de jucărie din plastic, creată cu atelierul de lucru de suprafață.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">



*Surface created with sketches placed in datum planes with the tools of the [PartDesign Workbench](PartDesign_Workbench.md)*

Atelierul suprafețe este integrat cu alte atelierele FreeCAD. Exemplul de mai sus a fost creat din [sketches](Sketcher_Workbench/ro.md) plasat pe [datum planes](PartDesign_Plane/ro.md) în [PartDesign workbench](PartDesign_Workbench/ro.md). Desegnul poate fi în întregime parametri, cânt toate planurile și scițele de referință sunt definite în acest sens.

Versiunea actuală a FreeCAD (v0.17) nu permite plasarea unor suprațfete în corpul din atelierul PartDesign . Dar suprafețele pot fi plasat în interiorul unei piese [Part](Std_Part/ro.md) împreună cu corpul care deține toate plaenel și schițele de referință. Piesa non parametrică [Part Shape builder](Part_Shapebuilder/ro.md) trebuie încă utilizată pentru a crea o [shell](Glossary/ro#Shell.md) și un solid regular [solid](Glossary/ro#Solid.md) dincol de suprafețe.



## Instrumentul Surface 

-   <img alt="" src=images/Filling.svg  style="width:32px;"> [Filling\...](Surface_Filling/ro.md): umple o serie de curbe de graniță cu o suprafață. Suprafața poate fi modificată prin adăugarea curbelor de constrângeri și a vârfurilor. Suprafața își schimbă forma astfel încât suprafața să treacă prin elementele de constrângere adăugate.
-   <img alt="" src=images/BSplineSurf.svg  style="width:32px;"> [Fill boundary curves](Surface_GeomFillSurface/ro.md):

creează o suprafață de la două, trei sau patru margini de graniță. Sunt disponibile trei moduri diferite de umplere: Stretch, Coons, Curved.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Fill boundary curves](Surface_GeomFillSurface.md): creates a surface from two, three or four boundary edges.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Sections](Surface_Sections.md): creates a surface from edges that represent transversal sections of surface.

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Extend face](Surface_ExtendFace.md): extrapolates the surface at the boundaries with its local U parameter and V parameter.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> [Curve on mesh](Surface_CurveOnMesh.md): creates approximated spline segments on top of a selected [mesh](Mesh_Workbench.md).

-   <img alt="" src=images/Surface_BlendCurve.svg  style="width:32px;"> [Blend Curve](Surface_BlendCurve.md): creates a Bezier curve between two edges, with desired continuity.


<div class="mw-translate-fuzzy">





{{Userdocnavi/ro}}


</div>


{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Surface](Category_Surface.md) > Surface Workbench/ro
