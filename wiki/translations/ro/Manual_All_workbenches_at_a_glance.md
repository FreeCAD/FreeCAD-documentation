# Manual:All workbenches at a glance/ro
{{Manual:TOC/ro}}


<div class="mw-translate-fuzzy">

Una dintre cele mai mari dificultăți pentru noii utilizatori de FreeCAD este să știm în ce atelier de lucru să găsim un instrument specific. Tabelul de mai jos vă va oferi o imagine de ansamblu asupra celor mai importante tabele de lucru și a instrumentelor acestora. Consultați fiecare pagină de atelier [workbench](Workbenches.md) în documentația FreeCAD pentru o listă mai completă.


</div>

Patru ateliere de lucru sunt, de asemenea, proiectate pentru a lucra în perechi, iar una dintre ele este pe deplin inclusă în cealaltă: Arch conține toate instrumentele Draft și PartDesign toate instrumentele Sketcher. Cu toate acestea, pentru claritate, acestea sunt separate mai jos.

### Part

Atelierul Part oferă instrumente de bază pentru lucrul cu componente solide: primitive, cum ar fi cuburile și sferele, precum și operații geometrice simple și operații booleene. Fiind punctul principal de ancorare cu OpenCasCade [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), atelierul Part furnizează fundamentul sistemului de geometrie al FreeCAD, iar aproape toate celelalte ateliere de lucru produc o geometrie bazată pe Part.


<div class="mw-translate-fuzzy">

  Tool                                                                                                               Description                                                               Tool                                                                                                                               Description
  ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------
  <img alt="" src=images/Part_Box.png  style="width:32px;"> _                                                    Desenează un con
  <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> _                                            Desenează o sferă
  <img alt="" src=images/Part_Torus.png  style="width:32px;"> _   Creează diverse alte primitive geometrice parametrice
  <img alt="" src=images/Part_Shapebuilder.png  style="width:32px;"> _                                                Siguranțe (sindicate) două obiecte
  <img alt="" src=images/Part_Common.png  style="width:32px;"> _                                                        Cuts (subtracts) one object from another
  <img alt="" src=images/Part_JoinConnect.png  style="width:32px;"> _                                Încorporează un obiect concav în alt obiect concav
  <img alt="" src=images/Part_JoinCutout.png  style="width:32px;"> _                                        Extrudează fațetele unui obiect
  <img alt="" src=images/Part_Fillet.png  style="width:32px;"> _                                        Creează un solid prin rotirea unui alt obiect (nu solid) în jurul unei axe
  <img alt="" src=images/Part_Section.png  style="width:32px;"> _                    Creează mai multe secțiuni transversale de-a lungul unui obiect
  <img alt="" src=images/Part_Chamfer.png  style="width:32px;"> _                                            Oglindirea unui obiect în raport cu un plan
  <img alt="" src=images/Part_RuledSurface.png  style="width:32px;"> _                                                Baleiere unul sau mai multe profiluri de-a lungul unei căi
  <img alt="" src=images/Part_Loft.png  style="width:32px;"> _                                            Creează o copie scalată a obiectului original
  <img alt="" src=images/Part_Thickness.png  style="width:32px;"> [Thickness](Part_Thickness.md)                Assign a thickness to the faces of a shape                                                                                                                                                                   


</div>

### Desen 2 D 

Atelierul Desen 2D (Draft) oferă instrumente pentru a efectua sarcini de bază de desenare 2D CAD: linii, cercuri etc. și o serie de instrumente generice, cum ar fi mișcarea, rotirea sau scalarea. Acesta oferă, de asemenea, mai multe ajutoare de desen, cum ar fi grila și ancorarea. Este în principal destinat să deseneze liniile directoare pentru obiectele Arch, dar servește și ca \"briceag elvețian\" bun la toate în FreeCAD.


<div class="mw-translate-fuzzy">

  Tool                                                                                                                    Description                                                           Tool                                                                                                               Description
  ----------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Draft_Line.png  style="width:32px;"> _                                 Creează o linie formată din mai multe segmente de linie(polyline)
  <img alt="" src=images/Draft_Circle.png  style="width:32px;"> _                                     Desenează un segment de arc de la centru, rază, unghi de pornire și unghi de capăt
  <img alt="" src=images/Draft_Ellipse.png  style="width:32px;">_                     Desenează un poligon definit prin centru și o rază
  <img alt="" src=images/Draft_Rectangle.png  style="width:32px;"> _                                 Elaborează o notă text în mai multe linii
  <img alt="" src=images/Draft_Dimension.png  style="width:32px;"> _                     Desenează o funcție B-spline definită de serie de puncte
  <img alt="" src=images/Draft_Point.png  style="width:32px;"> _     Instrumentul ShapeString introduce o formă compusă reprezentând un șir de text într-un punct dat în documentul curent
  <img alt="" src=images/Draft_Facebinder.png  style="width:32px;"> _             Desenează o curbă Bezier dintr-o serie de puncte
  <img alt="" src=images/Draft_Move.png  style="width:32px;"> _                         Rotirea obiectelor cu un anumit unghi în jurul unui punct
  <img alt="" src=images/Draft_Offset.png  style="width:32px;"> _                         Taie, extinde sau extrudează un obiect
  <img alt="" src=images/Draft_Upgrade.png  style="width:32px;"> _             Retrimite sau unește obiecte într-un obiect de nivel inferior
  <img alt="" src=images/Draft_Scale.png  style="width:32px;"> _   Creează o proiecție 2D a unui alt obiect 3D
  <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> _                             Creează o multiplicare în matrice polară sau dreptunghiulară dintr-un obiect
  <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> _                             Creează clone dependentă de obiectul inițial
  <img alt="" src=images/Draft_Mirror.png  style="width:32px;"> [Mirror](Draft_Mirror.md)                              Oglindește un obiect față de o linie                                                                                                                                                     


</div>

### Sketcher

Sketcher Workbench conține instrumente pentru a construi și edita obiecte complexe 2D, numite schițe. Geometria din interiorul acestor schițe poate fi poziționată precis și relaționată de utilizarea constrângerilor. Acestea sunt în primul rând menite a fi elementele de bază ale geometriei PartDesign, dar sunt utile oriunde în FreeCAD.


<div class="mw-translate-fuzzy">

  Instrument                                                                                                                                                      Descriere                                                                                                                                       Instrument                                                                                                                                                Descriere
  --------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> _                                                         Desenează un segment de linie definit prin 2 puncte
  <img alt="" src=images/Sketcher_Arc.png  style="width:32px;"> _                      Desenează un arc de cerc definit prin 2 puncte de capăt și un punct de circumferință
  <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> _         Desenează un cerc definit prin 3 puncte pe circumferință
  <img alt="" src=images/Sketcher_CreateEllipse.png  style="width:32px;"> _   Desenează o elipsă definită prin axa majora (2 puncte) și centrul la semiaxa minoră
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width:32px;"> _                             Draws a line made of multiple line segments. Several drawing modes available
  <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> _                             Desenează un tringhi echilateral inscris unui cerc
  <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> _                             Desenează un pentagon regulat inscris într-un cerc
  <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> _                             Desenează un heptagon regulat înscris într-un cerc
  <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> _                                             Desenează un oval selectând cetrul unui semicerc și a unui punct final al celuilalt semicerc
  <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> _                                               Ajustează o linie , cerc sau arc de cerc începând cu punctul de clicl
  <img alt="" src=images/Sketcher_External.png  style="width:32px;"> _        Comută un element în / din modul de construcție. Elementele de construcție (în albastru) sunt ignorate în timpul unei operații de geometrie 3D și sunt vizibile numai atunci când schița care le conține este în modul de editare.
  <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> _            Creează o constrângere de membru (punct-pe-obiect) între un vârf și un alt obiect (linie, arc, cerc, axă \...).
  <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> _                          Crează o constrângere liniile selectate sau elementele de polilinie la o orientare orizontală reală. Pot fi selectate mai multe obiecte înainte de aplicarea acestei constrângeri.
  <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> _              Constrânge două linii a fi perpendiculare una pe alta sau perpendicular pe un punct final de arc.
  <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> _                           Constrânge două entități selectate a fi egale una cu celălaltă. Dacă sunt folosite pe cercuri sau arce, raza lor va fi egală.
  <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> _                                    Constrânge elementul selectat prin setarea distanțelor verticale și orizontale față de origine
  <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:32px;"> _        Fixează distanța verticală între 2 puncte sau capetele liniei. Dacă este selectat un singur element, distanța este setată de la origine.
  <img alt="" src=images/Constraint_Length.png  style="width:32px;"> _                                          Definește raza unui arc sau cerc selectat prin limitarea razei.
  <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> _                           Constrânge două linii pentru a se supune unei legi de refracție pentru a simula lumina care trece printr-o interfață
  <img alt="" src=images/Constraint_InternalAlignment.png  style="width:32px;"> _                                          Aplică o schiță pe o fațetă sau solidul selectat.
  <img alt="" src=images/Sketcher_MergeSketch.png  style="width:32px;"> _                                     Creează o schiță simetrică de-a lungul axei X, axei Y sau a originii.


</div>

### Proiectarea Pieselor 

Atelierul Piese(Part Design) conține instrumente avansate pentru a construi părți solide. Acesta conține, de asemenea, toate instrumentele de la sketcher. Deoarece nu poate produce decât forme solide (regula numărul unu al Part Design), este atelierul principal de utilizat la proiectarea pieselor (Parts) care urmează a fi fabricate sau imprimate 3D, deoarece veți obține întotdeauna un obiect imprimabil.


<div class="mw-translate-fuzzy">

  Instrument                                                                                                                               Descriere                                                                                Instrument                                                                                                                                  Descriere
  ---------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> _                                   Crearea unui buzunar/cavitate av\#nd forma schiței selectate. Schița trebuie să fie mapată la fața obiectului solid existent
  <img alt="" src=images/PartDesign_Revolution.png  style="width:32px;"> _                                   Crearea unei caneluri prin rotirea unei schițe în jurul unei axe
  <img alt="" src=images/PartDesign_Fillet.png  style="width:32px;"> _                               Șanfrenarea muchiilor unui obiect
  <img alt="" src=images/PartDesign_Draft.png  style="width:32px;"> _                           Oglindirea unei caracteristici pe un plan sau o fațetă
  <img alt="" src=images/PartDesign_LinearPattern.png  style="width:32px;"> _          Multiplică o caracteristică după un model circular/polar
  <img alt="" src=images/PartDesign_Scaled.png  style="width:32px;"> _   Permite crearea unui model cu orice combinație a celorlalte transformări
  <img alt="" src=images/PartDesign_WizardShaft.png  style="width:32px;"> _   Vă permite să creați mai multe tipuri de angrenaje


</div>

### Architectură

Atelierul Architectură (sau pe scurt Arch) furnizează la FreeCAD instrumente pentru lucrul cu proiectele BIM (Construcții civile și arhitectură) [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) projects (civil engineering and architecture). Acesta conține, de asemenea, toate instrumentele de la Atelierul Desen 2 D (Draft). Utilizarea principală a atelierului Arch este de a crea obiecte BIM sau de a da atribute BIM obiectelor construite cu alte ateliere de lucru, pentru a le exporta în format IFC [IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes).


<div class="mw-translate-fuzzy">

  Instrument                                                                                            Descriere                                                                       Insrument                                                                                                          Descriere
  ----------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  <img alt="" src=images/Arch_Wall.png  style="width:32px;"> _                Creează un element structural de la zero sau utilizează un obiect selectat ca bază
  <img alt="" src=images/Arch_Rebar.png  style="width:32px;"> _                                Creează un etaj incluzând obeictele selectate
  <img alt="" src=images/Arch_Building.png  style="width:32px;"> _                                    Creează un site incluzând obeictele selectate
  <img alt="" src=images/Arch_Window.png  style="width:32px;"> _   Adaugă un plan de secțiune la document
  <img alt="" src=images/Arch_Axis.png  style="width:32px;"> _                                    Creează un acoperiș în pantă de o față selectată
  <img alt="" src=images/Arch_Space.png  style="width:32px;"> _                            Creează un obiect tip scări în document
  <img alt="" src=images/Arch_Panel.png  style="width:32px;"> _                                Creează un obiect cadru din layer selectat
  <img alt="" src=images/Arch_Equipment.png  style="width:32px;"> _           Atribuie un material la obiectele selectate
  <img alt="" src=images/Arch_Schedule.png  style="width:32px;"> _                   Secționează un obiect cu un plan
  <img alt="" src=images/Arch_Add.png  style="width:32px;"> _                            Extrage sau scade obiecte din componente
  <img alt="" src=images/Arch_Survey.png  style="width:32px;"> [Survey](Arch_Survey.md)               Activează sau dezactivează modul de supraveghere                                                                                                                                                   


</div>

### Desen 3 D 


<div class="mw-translate-fuzzy">

Atelierul de lucru Desen 3 D (Drawing) se ocupă de crearea și manipularea foilor de desen 2D, utilizate pentru afișarea vizualizărilor lucrării dvs. 3D în 2D. Aceste foi pot avea un chenar, un titlul, un logo și de asemenea pot fi apoi exportate în aplicații 2D în formate SVG sau DXF, într-un fișier PDF sau imprimate.


</div>

The Drawing Workbench handles the creation and manipulation of 2D drawing sheets, used for displaying views of your 3D work in 2D. These sheets can then be exported to 2D applications in SVG or DXF formats, to a PDF file or printed.

  Instrument                                                                                                              Descriere                                                              instrument                                                                                                          Descriere
  ----------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> _                            Se inserează în foaia de desen activă
  <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> _                            Adaugă un grup de clipuri în foaia de desen curent
  <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> _   Creează automat vederi ortografice ale unui obiect
  <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> _       Inserie o vizualizare grafică specială a obiectului selectat în foaia de desen curent
  <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save](Drawing_Save.md)                                Salvează foaia curentă ca fișier SVG                                                                                                                                                       

### Alte ateliere integrate 

Rezumând cele de mai sus, cele mai importante instrumente ale FreeCAD, sunt disponibile mai multe ateliere de lucru, printre care:


<div class="mw-translate-fuzzy">

-   Atelierul de Plase [Mesh Workbench](Mesh_Workbench.md) permite lucrul cu [polygon meshes](https://en.wikipedia.org/wiki/Polygon_mesh).

Deși plasele nu sunt tipul de geometrie preferat pentru a lucra în FreeCAD, din cauza lipsei de precizie și a suportului pentru curbe, ochiurile de plasă au încă multe utilizări și sunt pe deplin suportate în FreeCAD. Mesh Workbench oferă, de asemenea, un număr de unelte de la o Piesă la o Plasă și invers, respectiv de la Mesh la o Parte.

-   Aelierul de randare [Raytracing Workbench](Raytracing_Workbench.md)

oferă instrumente de interfață cu randare a exteriorului, cum ar fi povray sau luxrender. Chiar din interiorul FreeCAD, acest atelier de lucru vă permite să realizați performanțe de înaltă calitate din modelele dvs.

-   Ateliereul Foi de calcul The [Spreadsheet Workbench](Spreadsheet_Workbench.md)

permite crearea și manipularea datelor din foaia de calcul, care pot fi extrase din modelele FreeCAD. Tabelele de foi de calcul pot fi de asemenea menționate în multe zone ale FreeCAD, permițându-le să le utilizeze ca structuri de date principale.

-   Atelierul de analiză cu Elementul Finit [FEM Workbench](FEM_Workbench.md) lucrează cu [Finite Elements Analysis](https://en.wikipedia.org/wiki/Finite_element_method),

și permite efectuarea calculelor FEM (Analiza elementului FInit) înainte și după prelucrare și afișarea grafică a rezultatelor.


</div>

### Ateliere externe 

Există, de asemenea, multe alte ateliere de lucru foarte folositoare produse de membrii comunității FreeCAD. Deși nu sunt incluse într-o instalare standard a FreeCAD, ele sunt ușor de instalat ca plugin-uri. Acestea sunt toate menționate în [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) repertoriu. Printre cele mai dezvoltate sunt:


<div class="mw-translate-fuzzy">

-   The [Drawing Dimensioning Workbench](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) offers many new tools to work directly on Drawing Sheets and allow you to add dimensions, annotations and other technical symbols with great control over their aspect.
-   The [Fasteners Workbench](https://github.com/shaise/FreeCAD_FastenersWB) offers a wide range of ready-to-insert fasteners objects like screws, bolts, rods, washers and nuts. Many options and settings are available.
-   The [Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2) offers a series of tools to mount and work with [assemblies](https://en.wikipedia.org/wiki/Assembly_modelling).


</div>

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [The complete list of workbenches](Workbenches.md)
-   [The Part Workbench](Part_Workbench.md)
-   [The Draft Workbench](Draft_Workbench.md)
-   [The Sketcher and Part Design Workbench](PartDesign_Workbench.md)
-   [The Arch Workbench](Arch_Workbench.md)
-   [The Drawing Workbench](Drawing_Workbench.md)
-   [The FEM Workbench](FEM_Workbench.md)
-   [The FreeCAD-addons repository](https://github.com/FreeCAD/FreeCAD-addons)


</div>

---
[documentation index](../README.md) > Manual:All workbenches at a glance/ro
