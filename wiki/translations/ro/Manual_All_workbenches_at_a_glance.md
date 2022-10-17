# Manual:All workbenches at a glance/ro
{{Manual   *TOC/ro}}


<div class="mw-translate-fuzzy">

Una dintre cele mai mari dificultăți pentru noii utilizatori de FreeCAD este să știm în ce atelier de lucru să găsim un instrument specific. Tabelul de mai jos vă va oferi o imagine de ansamblu asupra celor mai importante tabele de lucru și a instrumentelor acestora. Consultați fiecare pagină de atelier [workbench](Workbenches.md) în documentația FreeCAD pentru o listă mai completă.


</div>

Patru ateliere de lucru sunt, de asemenea, proiectate pentru a lucra în perechi, iar una dintre ele este pe deplin inclusă în cealaltă   * Arch conține toate instrumentele Draft și PartDesign toate instrumentele Sketcher. Cu toate acestea, pentru claritate, acestea sunt separate mai jos.

### Part

Atelierul Part oferă instrumente de bază pentru lucrul cu componente solide   * primitive, cum ar fi cuburile și sferele, precum și operații geometrice simple și operații booleene. Fiind punctul principal de ancorare cu OpenCasCade [OpenCasCade](https   *//en.wikipedia.org/wiki/Open_Cascade_Technology), atelierul Part furnizează fundamentul sistemului de geometrie al FreeCAD, iar aproape toate celelalte ateliere de lucru produc o geometrie bazată pe Part.


<div class="mw-translate-fuzzy">

  Tool                                                                                                           Description                                                               Tool                                                                                                                           Description
     
  <img alt="" src=images/Part_Box.png  style="width   *32px;"> [Box](Part_Box.md)                                        Draws a box                                                               <img alt="" src=images/Part_Cone.png  style="width   *32px;"> [Cone](Part_Cone.md)                                                    Desenează un con
  <img alt="" src=images/Part_Cylinder.png  style="width   *32px;"> [Cylinder](Part_Cylinder.md)                    Desenează un cilindru                                                     <img alt="" src=images/Part_Sphere.png  style="width   *32px;"> [Sphere](Part_Sphere.md)                                            Desenează o sferă
  <img alt="" src=images/Part_Torus.png  style="width   *32px;"> [Torus](Part_Torus.md)                                Desenează un tor (tor)                                                    <img alt="" src=images/Part_CreatePrimitives.png  style="width   *32px;"> [Create primitives](Part_CreatePrimitives.md)   Creează diverse alte primitive geometrice parametrice
  <img alt="" src=images/Part_Shapebuilder.png  style="width   *32px;"> [Shape builder](Part_Shapebuilder.md)   Creați forme mai complexe de la primitivi                                 <img alt="" src=images/Part_Union.png  style="width   *32px;"> [Union](Part_Union.md)                                                Siguranțe (sindicate) două obiecte
  <img alt="" src=images/Part_Common.png  style="width   *32px;"> [Common](Part_Common.md)                            Extrage partea comună (intersecție) a două obiecte                        <img alt="" src=images/Part_Cut.png  style="width   *32px;"> [Cut](Part_Cut.md)                                                        Cuts (subtracts) one object from another
  <img alt="" src=images/Part_JoinConnect.png  style="width   *32px;"> [JonConnect](Part_JoinConnect.md)         Conectează interioarele obiectelor cu pereți                              <img alt="" src=images/Part_JoinEmbed.png  style="width   *32px;"> [JoinEmbed](Part_JoinEmbed.md)                                Încorporează un obiect concav în alt obiect concav
  <img alt="" src=images/Part_JoinCutout.png  style="width   *32px;"> [Join Cutout](Part_JoinCutout.md)           Creează o decupare în peretele unui obiect pentru un alt obiect obturat   <img alt="" src=images/Part_Extrude.png  style="width   *32px;"> [Extrude](Part_Extrude.md)                                        Extrudează fațetele unui obiect
  <img alt="" src=images/Part_Fillet.png  style="width   *32px;"> [Fillet](Part_Fillet.md)                            Rotunjirea colțurilor                                                     <img alt="" src=images/Part_Revolve.png  style="width   *32px;"> [Revolve](Part_Revolve.md)                                        Creează un solid prin rotirea unui alt obiect (nu solid) în jurul unei axe
  <img alt="" src=images/Part_Section.png  style="width   *32px;"> [Section](Part_Section.md)                        Creează o secțiune prin intersectarea unui obiect cu o secțiune plană     <img alt="" src=images/Part_SectionCross.png  style="width   *32px;"> [SectionCross](Part_SectionCross.md)                    Creează mai multe secțiuni transversale de-a lungul unui obiect
  <img alt="" src=images/Part_Chamfer.png  style="width   *32px;"> [Chamfer](Part_Chamfer.md)                        Șanfrenarea muchiilor unui obiect                                         <img alt="" src=images/Part_Mirror.png  style="width   *32px;"> [Mirror](Part_Mirror.md)                                            Oglindirea unui obiect în raport cu un plan
  <img alt="" src=images/Part_RuledSurface.png  style="width   *32px;"> [Ruled Surface](Part_RuledSurface.md)   Creați o suprafață riglată între curbele selectate                        <img alt="" src=images/Part_Sweep.png  style="width   *32px;"> [Sweep](Part_Sweep.md)                                                Baleiere unul sau mai multe profiluri de-a lungul unei căi
  <img alt="" src=images/Part_Loft.png  style="width   *32px;"> [Part_Loft](Part_Loft.md)                               Lofts from one profile to another                                         <img alt="" src=images/Part_Offset.png  style="width   *32px;"> [Offset](Part_Offset.md)                                            Creează o copie scalată a obiectului original
  <img alt="" src=images/Part_Thickness.png  style="width   *32px;"> [Thickness](Part_Thickness.md)                Assign a thickness to the faces of a shape                                                                                                                                                               


</div>

### Desen 2 D 

Atelierul Desen 2D (Draft) oferă instrumente pentru a efectua sarcini de bază de desenare 2D CAD   * linii, cercuri etc. și o serie de instrumente generice, cum ar fi mișcarea, rotirea sau scalarea. Acesta oferă, de asemenea, mai multe ajutoare de desen, cum ar fi grila și ancorarea. Este în principal destinat să deseneze liniile directoare pentru obiectele Arch, dar servește și ca \"briceag elvețian\" bun la toate în FreeCAD.


<div class="mw-translate-fuzzy">

  Tool                                                                                                                Description                                                           Tool                                                                                                           Description
     
  <img alt="" src=images/Draft_Line.png  style="width   *32px;"> [Line](Draft_Line.md)                                      Desenează un segment de linie între 2 puncte                          <img alt="" src=images/Draft_Wire.png  style="width   *32px;"> [Wire](Draft_Wire.md)                                 Creează o linie formată din mai multe segmente de linie(polyline)
  <img alt="" src=images/Draft_Circle.png  style="width   *32px;"> [Circle](Draft_Circle.md)                              Draws a circle from center and radius                                 <img alt="" src=images/Draft_Arc.png  style="width   *32px;"> [Arc](Draft_Arc.md)                                     Desenează un segment de arc de la centru, rază, unghi de pornire și unghi de capăt
  <img alt="" src=images/Draft_Ellipse.png  style="width   *32px;">[Ellipse](Draft_Ellipse.md)                           Desenează o elipsă încadrată între două puncte de colț                <img alt="" src=images/Draft_Polygon.png  style="width   *32px;"> [Polygon](Draft_Polygon.md)                     Desenează un poligon definit prin centru și o rază
  <img alt="" src=images/Draft_Rectangle.png  style="width   *32px;"> [Rectangle](Draft_Rectangle.md)                  Desenează un dreptunghi definit de două puncte opuse                  <img alt="" src=images/Draft_Text.png  style="width   *32px;"> [Text](Draft_Text.md)                                 Elaborează o notă text în mai multe linii
  <img alt="" src=images/Draft_Dimension.png  style="width   *32px;"> [Dimension](Draft_Dimension.md)                  Creează o notă pentru dimensiuni                                      <img alt="" src=images/Draft_BSpline.png  style="width   *32px;"> [BSpline](Draft_BSpline.md)                     Desenează o funcție B-spline definită de serie de puncte
  <img alt="" src=images/Draft_Point.png  style="width   *32px;"> [Point](Draft_Point.md)                                  Inserează un punt unic                                                <img alt="" src=images/Draft_ShapeString.png  style="width   *32px;"> [Shapestring](Draft_ShapeString.md)     Instrumentul ShapeString introduce o formă compusă reprezentând un șir de text într-un punct dat în documentul curent
  <img alt="" src=images/Draft_Facebinder.png  style="width   *32px;"> [Facebinder](Draft_Facebinder.md)              Creează un obiect nou din fațetele selectate pe obiectele existente   <img alt="" src=images/Draft_BezCurve.png  style="width   *32px;"> [Bezier Curve](Draft_BezCurve.md)             Desenează o curbă Bezier dintr-o serie de puncte
  <img alt="" src=images/Draft_Move.png  style="width   *32px;"> [Move](Draft_Move.md)                                      Mută sau copiază obiecte de la o locație la alta                      <img alt="" src=images/Draft_Rotate.png  style="width   *32px;"> [Rotate](Draft_Rotate.md)                         Rotirea obiectelor cu un anumit unghi în jurul unui punct
  <img alt="" src=images/Draft_Offset.png  style="width   *32px;"> [Offset](Draft_Offset.md)                              Se compensează un obiect la o anumită distanță                        <img alt="" src=images/Draft_Trimex.png  style="width   *32px;"> [Trimex](Draft_Trimex.md)                         Taie, extinde sau extrudează un obiect
  <img alt="" src=images/Draft_Upgrade.png  style="width   *32px;"> [Upgrade](Draft_Upgrade.md)                          Retrimite sau unește obiecte într-un obiect de nivel superior         <img alt="" src=images/Draft_Downgrade.png  style="width   *32px;"> [Downgrade](Draft_Downgrade.md)             Retrimite sau unește obiecte într-un obiect de nivel inferior
  <img alt="" src=images/Draft_Scale.png  style="width   *32px;"> [Scale](Draft_Scale.md)                                  Scalează un obiect în raport cu un punct                              <img alt="" src=images/Draft_Shape2DView.png  style="width   *32px;"> [Shape 2D View](Draft_Shape2DView.md)   Creează o proiecție 2D a unui alt obiect 3D
  <img alt="" src=images/Draft_Draft2Sketch.png  style="width   *32px;"> [Draft to Sketch](Draft_Draft2Sketch.md)   Convertește un obiect Draft la o Sketch și invers                     <img alt="" src=images/Draft_Array.png  style="width   *32px;"> [Array](Draft_Array.md)                             Creează o multiplicare în matrice polară sau dreptunghiulară dintr-un obiect
  <img alt="" src=images/Draft_PathArray.png  style="width   *32px;"> [Path Array](Draft_PathArray.md)                 Creează o matrice a unui obiect pe o traiectorie dată                 <img alt="" src=images/Draft_Clone.png  style="width   *32px;"> [Clone](Draft_Clone.md)                             Creează clone dependentă de obiectul inițial
  <img alt="" src=images/Draft_Mirror.png  style="width   *32px;"> [Mirror](Draft_Mirror.md)                              Oglindește un obiect față de o linie                                                                                                                                                 


</div>

### Sketcher

Sketcher Workbench conține instrumente pentru a construi și edita obiecte complexe 2D, numite schițe. Geometria din interiorul acestor schițe poate fi poziționată precis și relaționată de utilizarea constrângerilor. Acestea sunt în primul rând menite a fi elementele de bază ale geometriei PartDesign, dar sunt utile oriunde în FreeCAD.


<div class="mw-translate-fuzzy">

  Instrument                                                                                                                                                  Descriere                                                                                                                                       Instrument                                                                                                                                            Descriere
     
  <img alt="" src=images/Sketcher_CreatePoint.png  style="width   *32px;"> [Point](Sketcher_CreatePoint.md)                                               Desenează un punct                                                                                                                              <img alt="" src=images/Sketcher_Line.png  style="width   *32px;"> [Line](Sketcher_CreateLine.md)                                                         Desenează un segment de linie definit prin 2 puncte
  <img alt="" src=images/Sketcher_Arc.png  style="width   *32px;"> [Arc](Sketcher_CreateArc.md)                                                                   Desenează un arc de cer definit prin centru , rază, unghiul de start și unghiul de finiș                                                        <img alt="" src=images/Sketcher_CreateArc3Point.png  style="width   *32px;"> [Arc 3 points](Sketcher_Create3PointArc.md)                      Desenează un arc de cerc definit prin 2 puncte de capăt și un punct de circumferință
  <img alt="" src=images/Sketcher_Circle.png  style="width   *32px;"> [Circle](Sketcher_CreateCircle.md)                                                       Desenează un cerc definit prin centru și rază                                                                                                   <img alt="" src=images/Sketcher_CreateCircle3Point.png  style="width   *32px;"> [ Circle 3 points](Sketcher_Create3PointCircle.md)         Desenează un cerc definit prin 3 puncte pe circumferință
  <img alt="" src=images/Sketcher_CreateEllipse.png  style="width   *32px;"> [Ellipse](Sketcher_CreateEllipseByCenter.md)                               Desenează o elipsă definită prin centru, semiaxa majoră și semiaxa minoră                                                                       <img alt="" src=images/Sketcher_CreateEllipse3Point.png  style="width   *32px;"> [Ellipse 3 points](Sketcher_CreateEllipseBy3Points.md)   Desenează o elipsă definită prin axa majora (2 puncte) și centrul la semiaxa minoră
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width   *32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md)                 Desenează un arc de elipsă definit prin punctul de centrucentrul semiaxei majore punctul de start și punctul de finiș                           <img alt="" src=images/Sketcher_CreatePolyline.png  style="width   *32px;"> [Polyline](Sketcher_CreatePolyline.md)                             Draws a line made of multiple line segments. Several drawing modes available
  <img alt="" src=images/Sketcher_CreateRectangle.png  style="width   *32px;"> [Rectangle](Sketcher_CreateRectangle.md)                               Desenează un dreptunghi definit prin 2 puncte opuse                                                                                             <img alt="" src=images/Sketcher_CreateTriangle.png  style="width   *32px;"> [Triangle](Sketcher_CreateTriangle.md)                             Desenează un tringhi echilateral inscris unui cerc
  <img alt="" src=images/Sketcher_CreateSquare.png  style="width   *32px;"> [Square](Sketcher_CreateSquare.md)                                           Desenează un pătrat inscris într-un cerc                                                                                                        <img alt="" src=images/Sketcher_CreatePentagon.png  style="width   *32px;"> [Pentagon](Sketcher_CreatePentagon.md)                             Desenează un pentagon regulat inscris într-un cerc
  <img alt="" src=images/Sketcher_CreateHexagon.png  style="width   *32px;"> [Hexagon](Sketcher_CreateHexagon.md)                                       Desenarea unui hexagon regulat înscris într-un cerc                                                                                             <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width   *32px;"> [Heptagon](Sketcher_CreateHeptagon.md)                             Desenează un heptagon regulat înscris într-un cerc
  <img alt="" src=images/Sketcher_CreateOctagon.png  style="width   *32px;"> [Octagon](Sketcher_CreateOctagon.md)                                       Desenează un octogaon regulat înscris într-un cerc                                                                                              <img alt="" src=images/Sketcher_CreateSlot.png  style="width   *32px;"> [Slot](Sketcher_CreateSlot.md)                                             Desenează un oval selectând cetrul unui semicerc și a unui punct final al celuilalt semicerc
  <img alt="" src=images/Sketcher_CreateFillet.png  style="width   *32px;"> [Fillet](Sketcher_CreateFillet.md)                                           Desenează o racordare între două linii care se unesc într-un punct                                                                              <img alt="" src=images/Sketcher_Trimming.png  style="width   *32px;"> [Trimming](Sketcher_Trimming.md)                                               Ajustează o linie , cerc sau arc de cerc începând cu punctul de clicl
  <img alt="" src=images/Sketcher_External.png  style="width   *32px;"> [External geometry](Sketcher_External.md)                                            Creează o muchie legată de o geometrie externă                                                                                                  <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width   *32px;"> [Construction mode](Sketcher_ToggleConstruction.md)        Comută un element în / din modul de construcție. Elementele de construcție (în albastru) sunt ignorate în timpul unei operații de geometrie 3D și sunt vizibile numai atunci când schița care le conține este în modul de editare.
  <img alt="" src=images/Constraint_PointOnPoint.png  style="width   *32px;"> [Point on point](Sketcher_ConstrainCoincident.md)                        Se aplică pentru a indica (coincidența cu) unul sau mai multe alte puncte.                                                                      <img alt="" src=images/Constraint_PointOnObject.png  style="width   *32px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)            Creează o constrângere de membru (punct-pe-obiect) între un vârf și un alt obiect (linie, arc, cerc, axă \...).
  <img alt="" src=images/Constraint_Vertical.png  style="width   *32px;"> [Vertical](Sketcher_ConstrainVertical.md)                                        Creează o constrângere verticală pe linia (ele) selectată (ele) sau segmentul (ele) de polilinie.                                               <img alt="" src=images/Constraint_Horizontal.png  style="width   *32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)                          Crează o constrângere liniile selectate sau elementele de polilinie la o orientare orizontală reală. Pot fi selectate mai multe obiecte înainte de aplicarea acestei constrângeri.
  <img alt="" src=images/Constraint_Parallel.png  style="width   *32px;"> [Parallel](Sketcher_ConstrainParallel.md)                                        Constrânge două sau mai multe linii a fi paralele una cu celaltă                                                                                <img alt="" src=images/Constraint_Perpendicular.png  style="width   *32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular.md)              Constrânge două linii a fi perpendiculare una pe alta sau perpendicular pe un punct final de arc.
  <img alt="" src=images/Constraint_Tangent.png  style="width   *32px;"> [Tangent](Sketcher_ConstrainTangent.md)                                            Creează o constrângere de tangență între două entități selectate sau o constrângere co-liniară între două segmente de linie.                    <img alt="" src=images/Constraint_EqualLength.png  style="width   *32px;"> [Equal length](Sketcher_ConstrainEqual.md)                           Constrânge două entități selectate a fi egale una cu celălaltă. Dacă sunt folosite pe cercuri sau arce, raza lor va fi egală.
  <img alt="" src=images/Constraint_Symmetric.png  style="width   *32px;"> [Symmetric](Sketcher_ConstrainSymmetric.md)                                    Constrânge două puncte a fi simetrice față de o linie sau constrânge primele două puncte simetric cu privire la un al treilea punct selectat.   <img alt="" src=images/Sketcher_ConstrainLock.png  style="width   *32px;"> [Lock](Sketcher_ConstrainLock.md)                                    Constrânge elementul selectat prin setarea distanțelor verticale și orizontale față de origine
  <img alt="" src=images/Constraint_HorizontalDistance.png  style="width   *32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)        Fixează distanța orizontală dintre două puncte sau capete de linie. Dacă este selectat un singur element, distanța este setată de la origine.   <img alt="" src=images/Constraint_VerticalDistance.png  style="width   *32px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md)        Fixează distanța verticală între 2 puncte sau capetele liniei. Dacă este selectat un singur element, distanța este setată de la origine.
  <img alt="" src=images/Constraint_Length.png  style="width   *32px;"> [Distance](Sketcher_ConstrainDistance.md)                                            Limitează distanțe prin limitarea lungimii liniei dselectate sau definește distanța dintre două puncte prin limitarea distanței dintre ele.     <img alt="" src=images/Constraint_Radius.png  style="width   *32px;"> [Radius](Sketcher_ConstrainRadius.md)                                          Definește raza unui arc sau cerc selectat prin limitarea razei.
  <img alt="" src=images/Constraint_InternalAngle.png  style="width   *32px;"> [Internal anglr](Sketcher_ConstrainAngle.md)                           Definește unghiul intern dintre două linii selectate.                                                                                           <img alt="" src=images/Constraint_SnellsLaw.png  style="width   *32px;"> [Snell\'s law](Sketcher_ConstrainSnellsLaw.md)                           Constrânge două linii pentru a se supune unei legi de refracție pentru a simula lumina care trece printr-o interfață
  <img alt="" src=images/Constraint_InternalAlignment.png  style="width   *32px;"> [Internal alignment](Sketcher_ConstrainInternalAlignment.md)   Aliniază elementele selectate la forma selectată (de exemplu, constrânge o linie pentru a deveni axa majoră a unei elipse).                     <img alt="" src=images/Sketcher_MapSketch.png  style="width   *32px;"> [Map sketch](Sketcher_MapSketch.md)                                          Aplică o schiță pe o fațetă sau solidul selectat.
  <img alt="" src=images/Sketcher_MergeSketch.png  style="width   *32px;"> [Merge](Sketcher_MergeSketches.md)                                             Fuzionează două sau mai multe schițe                                                                                                            <img alt="" src=images/Sketcher_MirrorSketch.png  style="width   *32px;"> [Mirror](Sketcher_MirrorSketch.md)                                     Creează o schiță simetrică de-a lungul axei X, axei Y sau a originii.


</div>

### Proiectarea Pieselor 

Atelierul Piese(Part Design) conține instrumente avansate pentru a construi părți solide. Acesta conține, de asemenea, toate instrumentele de la sketcher. Deoarece nu poate produce decât forme solide (regula numărul unu al Part Design), este atelierul principal de utilizat la proiectarea pieselor (Parts) care urmează a fi fabricate sau imprimate 3D, deoarece veți obține întotdeauna un obiect imprimabil.


<div class="mw-translate-fuzzy">

  Instrument                                                                                                                           Descriere                                                                                Instrument                                                                                                                              Descriere
     
  <img alt="" src=images/PartDesign_Pad.png  style="width   *32px;"> [Pad](PartDesign_Pad.md)                                            Extrudarea unui obiect solid dintr-o schiță selectată                                    <img alt="" src=images/PartDesign_Pocket.png  style="width   *32px;"> [Pocket](PartDesign_Pocket.md)                                   Crearea unui buzunar/cavitate av#nd forma schiței selectate. Schița trebuie să fie mapată la fața obiectului solid existent
  <img alt="" src=images/PartDesign_Revolution.png  style="width   *32px;"> [Revolution](PartDesign_Revolution.md)                Crearea unui solid prin rotirea unei schițe în judrul unei axe                           <img alt="" src=images/PartDesign_Groove.png  style="width   *32px;"> [Groove](PartDesign_Groove.md)                                   Crearea unei caneluri prin rotirea unei schițe în jurul unei axe
  <img alt="" src=images/PartDesign_Fillet.png  style="width   *32px;"> [Fillet](PartDesign_Fillet.md)                                Rotunjirea muchiilor unui obiect                                                         <img alt="" src=images/PartDesign_Chamfer.png  style="width   *32px;"> [Chamfer](PartDesign_Chamfer.md)                               Șanfrenarea muchiilor unui obiect
  <img alt="" src=images/PartDesign_Draft.png  style="width   *32px;"> [Draft](PartDesign_Draft.md)                                    Crează o pantă pe fețele unui obiect                                                     <img alt="" src=images/PartDesign_Mirrored.png  style="width   *32px;"> [Mirrored](PartDesign_Mirrored.md)                           Oglindirea unei caracteristici pe un plan sau o fațetă
  <img alt="" src=images/PartDesign_LinearPattern.png  style="width   *32px;"> [Linear pattern](PartDesign_LinearPattern.md)   Multiplică o caracterisctică după un model liniar matricial                              <img alt="" src=images/PartDesign_PolarPattern.png  style="width   *32px;"> [Polar pattern](PartDesign_PolarPattern.md)          Multiplică o caracteristică după un model circular/polar
  <img alt="" src=images/PartDesign_Scaled.png  style="width   *32px;"> [Scaled](PartDesign_Scaled.md)                                Scalează caracteristici la o mărime diferită                                             <img alt="" src=images/PartDesign_MultiTransform.png  style="width   *32px;"> [Multitransform](PartDesign_MultiTransform.md)   Permite crearea unui model cu orice combinație a celorlalte transformări
  <img alt="" src=images/PartDesign_WizardShaft.png  style="width   *32px;"> [Shaft wizard](PartDesign_WizardShaft.md)           Generă un arbore dintr-o tabelă de valori și permite analizarea forțelor și momentelor   <img alt="" src=images/PartDesign_InvoluteGear.png  style="width   *32px;"> [Involute gear wizard](PartDesign_InvoluteGear.md)   Vă permite să creați mai multe tipuri de angrenaje


</div>

### Architectură

Atelierul Architectură (sau pe scurt Arch) furnizează la FreeCAD instrumente pentru lucrul cu proiectele BIM (Construcții civile și arhitectură) [BIM](https   *//en.wikipedia.org/wiki/Building_information_modeling) projects (civil engineering and architecture). Acesta conține, de asemenea, toate instrumentele de la Atelierul Desen 2 D (Draft). Utilizarea principală a atelierului Arch este de a crea obiecte BIM sau de a da atribute BIM obiectelor construite cu alte ateliere de lucru, pentru a le exporta în format IFC [IFC](https   *//en.wikipedia.org/wiki/Industry_Foundation_Classes).


<div class="mw-translate-fuzzy">

  Instrument                                                                                        Descriere                                                                       Insrument                                                                                                      Descriere
     
  <img alt="" src=images/Arch_Wall.png  style="width   *32px;"> [Wall](Arch_Wall.md)                       Creează un zid pornind de la o shiță sau utilizând un obiect selectat ca bază   <img alt="" src=images/Arch_Structure.png  style="width   *32px;"> [Structure](Arch_Structure.md)                Creează un element structural de la zero sau utilizează un obiect selectat ca bază
  <img alt="" src=images/Arch_Rebar.png  style="width   *32px;"> [Rebar](Arch_Rebar.md)                   Creează o bară de armătură într-un element structural selectat C                <img alt="" src=images/Arch_Floor.png  style="width   *32px;"> [Floor](Arch_Floor.md)                                Creează un etaj incluzând obeictele selectate
  <img alt="" src=images/Arch_Building.png  style="width   *32px;"> [Building](Arch_Building.md)       Creează o clădite incluzând obiectele selectate                                 <img alt="" src=images/Arch_Site.png  style="width   *32px;"> [Site](Arch_Site.md)                                    Creează un site incluzând obeictele selectate
  <img alt="" src=images/Arch_Window.png  style="width   *32px;"> [Window](Arch_Window.md)               Creează o fereastră utilizând obiectul selectat ca bază                         <img alt="" src=images/Arch_SectionPlane.png  style="width   *32px;"> [Section plane](Arch_SectionPlane.md)   Adaugă un plan de secțiune la document
  <img alt="" src=images/Arch_Axis.png  style="width   *32px;"> [Axis](Arch_Axis.md)                       Adăugarea unui sistem de axe la document                                        <img alt="" src=images/Arch_Roof.png  style="width   *32px;"> [Roof](Arch_Roof.md)                                    Creează un acoperiș în pantă de o față selectată
  <img alt="" src=images/Arch_Space.png  style="width   *32px;"> [Space](Arch_Space.md)                   Creează un obiect spațiu în document                                            <img alt="" src=images/Arch_Stairs.png  style="width   *32px;"> [Stairs](Arch_Stairs.md)                            Creează un obiect tip scări în document
  <img alt="" src=images/Arch_Panel.png  style="width   *32px;"> [Panel](Arch_Panel.md)                   Creează un obiect tip panou de la obeictul 2D selectat                          <img alt="" src=images/Arch_Frame.png  style="width   *32px;"> [Frame](Arch_Frame.md)                                Creează un obiect cadru din layer selectat
  <img alt="" src=images/Arch_Equipment.png  style="width   *32px;"> [Equipment](Arch_Equipment.md)   Creează un obeict tip echipament sau mobilă                                     <img alt="" src=images/Arch_SetMaterial.png  style="width   *32px;"> [Material](Arch_SetMaterial.md)           Atribuie un material la obiectele selectate
  <img alt="" src=images/Arch_Schedule.png  style="width   *32px;"> [Schedule](Arch_Schedule.md)       Creează diferite tipuri of schedules                                            <img alt="" src=images/Arch_CutPlane.png  style="width   *32px;"> [Cut plane](Arch_CutPlane.md)                   Secționează un obiect cu un plan
  <img alt="" src=images/Arch_Add.png  style="width   *32px;"> [Add](Arch_Add.md)                           Adaugă obiecte la componentă                                                    <img alt="" src=images/Arch_Remove.png  style="width   *32px;"> [Remove](Arch_Remove.md)                            Extrage sau scade obiecte din componente
  <img alt="" src=images/Arch_Survey.png  style="width   *32px;"> [Survey](Arch_Survey.md)               Activează sau dezactivează modul de supraveghere                                                                                                                                               


</div>

### Desen 3 D 


<div class="mw-translate-fuzzy">

Atelierul de lucru Desen 3 D (Drawing) se ocupă de crearea și manipularea foilor de desen 2D, utilizate pentru afișarea vizualizărilor lucrării dvs. 3D în 2D. Aceste foi pot avea un chenar, un titlul, un logo și de asemenea pot fi apoi exportate în aplicații 2D în formate SVG sau DXF, într-un fișier PDF sau imprimate.


</div>

The Drawing Workbench handles the creation and manipulation of 2D drawing sheets, used for displaying views of your 3D work in 2D. These sheets can then be exported to 2D applications in SVG or DXF formats, to a PDF file or printed.


<div class="mw-translate-fuzzy">

  Instrument                                                                                                          Descriere                                                              instrument                                                                                                      Descriere
     
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width   *32px;"> [New sheet](Drawing_Landscape_A3.md)   Creează o nouă foaie de desen                                          <img alt="" src=images/Drawing_View.png  style="width   *32px;"> [View](Drawing_View.md)                            Se inserează în foaia de desen activă
  <img alt="" src=images/Drawing_Annotation.png  style="width   *32px;"> [Annotation](Drawing_Annotation.md)        Adaugă o adnotare în foaia de desen curent                             <img alt="" src=images/Drawing_Clip.png  style="width   *32px;"> [Clip](Drawing_Clip.md)                            Adaugă un grup de clipuri în foaia de desen curent
  <img alt="" src=images/Drawing_Openbrowser.png  style="width   *32px;"> [Open browser](Drawing_Openbrowser.md)   Deschide o previzualizare a foii curente din browser                   <img alt="" src=images/Drawing_Orthoviews.png  style="width   *32px;"> [Ortho views](Drawing_Orthoviews.md)   Creează automat vederi ortografice ale unui obiect
  <img alt="" src=images/Drawing_Symbol.png  style="width   *32px;"> [Symbol](Drawing_Symbol.md)                        Adaugă conținutul unui fișier SVG ca simbol în foii curente de desen   <img alt="" src=images/Drawing_DraftView.png  style="width   *32px;"> [Draft view](Drawing_DraftView.md)       Inserie o vizualizare grafică specială a obiectului selectat în foaia de desen curent
  <img alt="" src=images/Drawing_Save.png  style="width   *32px;"> [Save](Drawing_Save.md)                                Salvează foaia curentă ca fișier SVG                                                                                                                                                   


</div>

### Alte ateliere integrate 

Rezumând cele de mai sus, cele mai importante instrumente ale FreeCAD, sunt disponibile mai multe ateliere de lucru, printre care   *


<div class="mw-translate-fuzzy">

-   Atelierul de Plase [Mesh Workbench](Mesh_Workbench.md) permite lucrul cu [polygon meshes](https   *//en.wikipedia.org/wiki/Polygon_mesh).

Deși plasele nu sunt tipul de geometrie preferat pentru a lucra în FreeCAD, din cauza lipsei de precizie și a suportului pentru curbe, ochiurile de plasă au încă multe utilizări și sunt pe deplin suportate în FreeCAD. Mesh Workbench oferă, de asemenea, un număr de unelte de la o Piesă la o Plasă și invers, respectiv de la Mesh la o Parte.

-   Aelierul de randare [Raytracing Workbench](Raytracing_Workbench.md)

oferă instrumente de interfață cu randare a exteriorului, cum ar fi povray sau luxrender. Chiar din interiorul FreeCAD, acest atelier de lucru vă permite să realizați performanțe de înaltă calitate din modelele dvs.

-   Ateliereul Foi de calcul The [Spreadsheet Workbench](Spreadsheet_Workbench.md)

permite crearea și manipularea datelor din foaia de calcul, care pot fi extrase din modelele FreeCAD. Tabelele de foi de calcul pot fi de asemenea menționate în multe zone ale FreeCAD, permițându-le să le utilizeze ca structuri de date principale.

-   Atelierul de analiză cu Elementul Finit [FEM Workbench](FEM_Workbench.md) lucrează cu [Finite Elements Analysis](https   *//en.wikipedia.org/wiki/Finite_element_method),

și permite efectuarea calculelor FEM (Analiza elementului FInit) înainte și după prelucrare și afișarea grafică a rezultatelor.


</div>

### Ateliere externe 

Există, de asemenea, multe alte ateliere de lucru foarte folositoare produse de membrii comunității FreeCAD. Deși nu sunt incluse într-o instalare standard a FreeCAD, ele sunt ușor de instalat ca plugin-uri. Acestea sunt toate menționate în [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons) repertoriu. Printre cele mai dezvoltate sunt   *


<div class="mw-translate-fuzzy">

-   The [Drawing Dimensioning Workbench](https   *//github.com/hamish2014/FreeCAD_drawing_dimensioning) offers many new tools to work directly on Drawing Sheets and allow you to add dimensions, annotations and other technical symbols with great control over their aspect.
-   The [Fasteners Workbench](https   *//github.com/shaise/FreeCAD_FastenersWB) offers a wide range of ready-to-insert fasteners objects like screws, bolts, rods, washers and nuts. Many options and settings are available.
-   The [Assembly2 Workbench](https   *//github.com/hamish2014/FreeCAD_assembly2) offers a series of tools to mount and work with [assemblies](https   *//en.wikipedia.org/wiki/Assembly_modelling).


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
-   [The FreeCAD-addons repository](https   *//github.com/FreeCAD/FreeCAD-addons)


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:All workbenches at a glance/ro
