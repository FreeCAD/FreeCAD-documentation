# FEM Mesh/pl
## Stwórz siatkę elementów skończonych 

Analiza metodą elementów skończonych (MES) jest przeprowadzana na siatce składającej się z wielu trójkątnych i czworokątnych elementów skończonych, na które podzielona jest oryginalna geometria. Im gęstsza siatka, tym dokładniejsze będą wyniki, ale też dłużej potrwają obliczenia. Równowaga między rozmiarem siatki a czasem obliczeń i dokładnością wyników to istotna charakterystyka dobrze zdefiniowanej analizy MES.

W [środowisku pracy MES](FEM_Workbench/pl.md) dostępne są różne sposoby przygotowywania siatki:

-   Narzędzie [Gmsh](FEM_MeshGmshFromShape/pl.md) z interfejsu graficznego użytkownika.
-   Narzędzie [Netgen](FEM_MeshNetgenFromShape/pl.md) z interfejsu graficznego użytkownika.
-   Import siatki z zewnętrznego środowiska. Uściślając, Gmsh i Netgen mogą być użyte poza programem FreeCAD aby stworzyć siatkę dla brył takich jak modele w plikach Step.
-   Ręczne tworzenie siatki poprzez skrypty [Pythona](Python/pl.md).

Narzędzia Gmsh i Netgen wspierają tworzenie siatki dla obiektów tworzonych w środowiskach pracy [Część](Part_Workbench/pl.md) i [Projekt Części](PartDesign_Workbench/pl.md), jak również prostych kopii tych obiektów. W ogólności, każde środowisko pracy, które generuje bryły, jak [Architektura](Arch_Workbench/pl.md) może być użyte do przygotowania geometrii, na której zostanie utworzona siatka. Zwróć uwagę, że siatka używana do analiz MES jest inna niż siatka tworzona lub importowana ze środowiska pracy [Siatka](Mesh_Workbench/pl.md).

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;"> 
*Środowisko pracy MES wywołuje zewnętrzne narzędzie Gmsh aby uzyskać siatkę z bryły utworzonej w dowolnym środowisku pracy we FreeCAD; może również zaimportować siatkę utworzoną poza FreeCAD*

<img alt="" src=images/FEM_Mesh.png  style="width:600px;"> 
*(1) Bryła utworzona w środowisku pracy Projekt Części, (2) siatka utworzona przez narzędzie Gmsh w środowisku pracy MES (same trójkąty) oraz (3) siatka utworzona zewnętrznie w programie Gmsh, wyeksportowana do formatu Abaqusa **.inp* a następnie zaimportowana do FreeCAD (same czworokąty)**

Narzędzia [Gmsh](FEM_MeshGmshFromShape/pl.md) i [Netgen](FEM_MeshNetgenFromShape/pl.md) są wygodnymi procedurami do szybkiego tworzenia siatka dla ciał i dlatego nie posiadają pełnych możliwości tych programów; normalnie tworzą siatki trójkątne, które mogą nie być idealne dla niektórych typów analiz. Jeśli chcesz mieć większą kontrolę nad tworzoną siatką (używać tylko czworokątów, precyzyjnie określać rozmiar i liczbę elementów, zmienną rozdzielczość siatki itd.), powinieneś skorzystać z tych programów poza FreeCAD, utworzyć plik siatki we wspieranym formacie (**.inp**, **.unv**, **.vtk**, **.z88**) i zaimportować ten plik do FreeCAD.

Poprzednio, Netgen był dołączony do programu FreeCAD i można było z niego korzystać od razu. Obecnie, Netgen i Gmsh mogą wymagać instalacji przed użyciem w środowisku pracy [MES](FEM_Workbench/pl.md). Zobacz instrukcję na stronie [MES: Instalacja](FEM_Install/pl.md).



## Oprogramowanie do tworzenia siatek 

Oprogramowanie do tworzenia siatek operuje na bryłach, które mogą się różnić formatami, jak Step i Brep. Te programy mogą być używane niezależnie od FreeCAD i zwykle mają wiele opcji do sterowania algorytmami tworzenia siatki, rozmiarem elementów i warunkami brzegowymi.

Środowisko pracy [MES](FEM_Workbench/pl.md) posiada prosty interfejs komunikacji aby używać Gmsh i Netgen bezpośrednio we FreeCAD. Inne programy nie mają interfejsu, ale może to ulec zmianie w przyszłości jeśli będzie zainteresowanie ze strony społeczności i jeśli te programy będą łatwe do zintegrowania. Programy do tworzenia siatek można komplikować i dystrybuować razem z FreeCAD tylko jeśli ich licencje są kompatybilne z licencją LGPL2, inaczej program musi być używany jako zewnętrzna biblioteka, tak jak Gmsh (licencja GPL2).



### Interfejs zaimplementowany we FreeCAD 

-   Gmsh: [strona główna](http://gmsh.info/), [kod źródłowy](https://gitlab.onelab.info/gmsh/gmsh)
-   Netgen: [strona główna](https://ngsolve.org/), [kod źródłowy](https://github.com/NGSolve/netgen)



### Brak interfejsu we FreeCAD 

-   ENigMA, [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=33048), [kod źródłowy](https://github.com/bjaraujo/ENigMA)
-   libMesh, [strona główna](http://libmesh.github.io/), [kod źródłowy](https://github.com/libMesh/libmesh), [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=33621); to bardzo aktywnie rozwijany projekt, jest tylko w C++
-   PythonOCC, [strona główna](http://www.pythonocc.org/)
-   SnappyHexMesh, [strona główna](https://openfoamwiki.net/index.php/SnappyHexMesh)
-   Tetgen, [strona główna](http://wias-berlin.de/software/tetgen/)



## Elementy skończone we FreeCAD 

FreeCAD wspiera różne typy elementów skończonych. Ten artykuł wyjaśnia różnice między nimi i ich zastosowania: [Meshing Your Geometry: When to Use the Various Element Types](https://www.comsol.com/blogs/meshing-your-geometry-various-element-types/).

<table>
<caption>Import i eksport elementów siatki</caption>
<thead>
<tr class="header">
<th><p>Element</p></th>
<th><p>Element</p></th>
<th><p>FreeCAD API</p></th>
<th><p>FreeCAD GUI</p></th>
<th><p>med</p></th>
<th><p>unv</p></th>
<th><p>inp</p></th>
<th><p>frd</p></th>
<th><p>txt</p></th>
<th><p>xml</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Med</p></td>
<td><p>CalculiX</p></td>
<td><p>Python</p></td>
<td><p>FEM Mesh</p></td>
<td><p>SMESH</p></td>
<td><p>IDEAS/FreeCAD</p></td>
<td><p>Abaqus/CalculiX</p></td>
<td><p>Siatka wynikowa</p></td>
<td><p>Z88</p></td>
<td><p>FEniCS</p></td>
</tr>
<tr class="even">
<td><p>Nazwa</p></td>
<td><p>Nazwa</p></td>
<td><p>utwórz elementy</p></td>
<td><p>przeglądaj elementy</p></td>
<td><p>import/eksport</p></td>
<td><p>import/eksport</p></td>
<td><p>import/eksport</p></td>
<td><p>import</p></td>
<td><p>import/eksport</p></td>
<td><p>import/eksport</p></td>
</tr>
<tr class="odd">
<td><p>seg 2</p></td>
<td><p>B31</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>seg 3</p></td>
<td><p>B32</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><p>NI</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>tria 3</p></td>
<td><p>S3</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>tria 6</p></td>
<td><p>S6</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>quad 4</p></td>
<td><p>S4</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>quad 8</p></td>
<td><p>S8</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>tetra 4</p></td>
<td><p>C3D4</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>tetra 10</p></td>
<td><p>C3D10</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>hexa 8</p></td>
<td><p>C3D8</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><p>(<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />) format pozwala na to,<br />
ale nie jest to do odczytu ani zapisu przez FEniCS</p></td>
</tr>
<tr class="even">
<td><p>hexa 20</p></td>
<td><p>C3D20</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>penta 6</p></td>
<td><p>C3D6</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><p>?</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>penta 15</p></td>
<td><p>C3D15</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><p>?</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>pyra 5</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>pyra 13</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" />
<figcaption>Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" />
<figcaption>Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
</tbody>
</table>

: Import i eksport elementów siatki

-   \"NI\" oznacza, że dany typ elementów nie jest zaimplementowany we FreeCAD, ale format by go wspierał.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:20px;"> oznacza, że specyfikacja formatu nie wspiera tego typu elementów, więc FreeCAD nie może ich wspierać.
-   \"?\" oznacza, że nie wiadomo czy format wspiera ten typ elementów.



## Typy elementów skończonych 

Więcej informacji o elementach i ich strukturze danych we FreeCAD można znaleźć na stronie [Typy elementów skończonych](FEM_Element_Types/pl.md).



## Element 1D 

<img alt="" src=images/FEM_mesh_elements_1_segment.svg  style="width:600px;">



## Element trójkątny 

<img alt="" src=images/FEM_mesh_elements_2_triangle.svg  style="width:600px;">



### Element czworokątny 

<img alt="" src=images/FEM_mesh_elements_3_quadrangle.svg  style="width:600px;">



## Element czworościenny 

<img alt="" src=images/FEM_mesh_elements_4_tetrahedron.svg  style="width:600px;">



## Element prostopadłościenny 

<img alt="" src=images/FEM_mesh_elements_5_hexahedron.svg  style="width:600px;">



## Element pięciościenny 

<img alt="" src=images/FEM_mesh_elements_6_pentahedron.svg  style="width:600px;">



## Element piramidalny 

<img alt="" src=images/FEM_mesh_elements_7_pyramid.svg  style="width:600px;">



## Skrypty



### Utwórz siatkę MES całkowicie w Python 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

API Pythona pozwala użytkownikowi definiować elementy siatki poprzez bezpośrednie dodawanie pojedynczych węzłów i definiowanie krawędzi, ścian i objętości.

Siatka sama w sobie jest typu `Fem::FemMesh`, który musi być dołączony do odpowiedniego obiektu dokumentu typu `Fem::FemMeshObject`.


```python
App.ActiveDocument.Mesh_object.TypeId = Fem::FemMeshObject
                              .
                              .
                              .FemMesh.TypeId = Fem::FemMesh
```



#### Tworzenie siatki z jednym elementem Tet-10 

Utwórz pusty obiekt siatki FemMesh, wypełnij go węzłami, utwórz objętość i wreszcie wywołaj `Fem.show()` aby utworzyć obiekt dokumentu z odpowiadającą mu siatką.


```python
import FreeCAD, Fem

m = Fem.FemMesh()

m.addNode(0,    1,    0)
m.addNode(0,    0,    1)
m.addNode(1,    0,    0)
m.addNode(0,    0,    0)
m.addNode(0,    0.5,  0.5)
m.addNode(0.5,  0.03, 0.5)
m.addNode(0.5,  0.5,  0.03)
m.addNode(0,    0.5,  0)
m.addNode(0.03, 0,    0.5)
m.addNode(0.5,  0,    0)

m.addVolume([1,2,3,4,5,6,7,8,9,10])
Fem.show(m)
obj = FreeCAD.ActiveDocument.ActiveObject
```

Jeśli chcesz mieć predefiniowaną numerację węzłów i elementów, podaj odpowiednie ID do metod tworzenia węzłów i objętości.

Aby utworzyć właściwy obiekt dokumentu, zamiast `Fem.show()` możesz też użyć metody dokumentu `addObject()`, następnie dołączyć utworzoną siatkę do atrybutu `FemMesh` tego obiektu.


```python
a = Fem.FemMesh()

a.addNode(0,    1,    0,    1)
a.addNode(0,    0,    1,    2)
a.addNode(1,    0,    0,    3)
a.addNode(0,    0,    0,    4)
a.addNode(0,    0.5,  0.5,  5)
a.addNode(0.5,  0.03, 0.5,  6)
a.addNode(0.5,  0.5,  0.03, 7)
a.addNode(0,    0.5,  0,    8)
a.addNode(0.03, 0,    0.5,  9)
a.addNode(0.5,  0,    0,   10)

a.addVolume([1,2,3,4,5,6,7,8,9,10], 1)
obj_2 = FreeCAD.ActiveDocument.addObject("Fem::FemMeshObject")
obj_2.Placement.Base = FreeCAD.Vector(2, 0, 0)
obj_2.FemMesh = a
```



#### Właściwości wizualne 

Gdy obiekt FemMesh jest utworzony z `Fem.show()`, część jego wizualnych właściwości można zmienić poprzez modyfikację różnych atrybutów jego `ViewObject`. To może być przydatne do postprocessingu siatki po uzyskaniu rozwiązania analizy.

Podświetl niektóre węzły siatki 
```python
Fem.show(m)
obj = FreeCAD.ActiveDocument.ActiveObject

obj.ViewObject.HighlightedNodes = [1, 2, 3]
```

Poszczególne elementy siatki można zmodyfikować poprzez podanie słownika z odpowiednimi parami `key:value`.

Ustaw objętość 1 na czerwony


```python
obj.ViewObject.ElementColor = {1:(1,0,0)}
```

Ustaw węzły 1, 2 i 3 na określony kolor, ściany pomiędzy węzłami będą korzystały ze zinterpolowanego koloru.


```python
obj.ViewObject.NodeColor = {1:(1,0,0), 2:(0,1,0), 3:(0,0,1)}
```

Przemieść węzły 1 i 2 o wartość i kierunek określony przez wektor.


```python
obj.ViewObject.NodeDisplacement = {1:FreeCAD.Vector(0,1,0), 2:FreeCAD.Vector(1,0,0)}
```

Podwój współczynnik pokazanego przemieszczenia. (**Notatka dla edytorów: usunięte w nowszych wersjach?**)


```python
obj.ViewObject.animate(2.0)
```



## Przykłady skrytpów dla każdego wspieranego typu elementów 



### Belka, 2 węzły linia, seg2 (liniowa) 


```python
import Fem

seg2 = Fem.FemMesh()
seg2.addNode( 0, 0, 0, 1)
seg2.addNode(10, 0, 0, 2)
seg2.addEdge(1, 2)
print(seg2)

obj = FreeCAD.ActiveDocument.addObject("Fem::FemMeshObject", "seg2")
obj.FemMesh = seg2
obj.Placement.Base = FreeCAD.Vector(0, 110, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```



### Belka, 3 węzły linia, seg3 (kwadratowa) 


```python
import Fem

seg3 = Fem.FemMesh()
seg3.addNode( 0, 0, 0, 1)
seg3.addNode(10, 0, 0, 2)
seg3.addNode( 5, 0, 0, 3)
seg3.addEdge([1, 2, 3])
print(seg3)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "seg3")
obj.FemMesh = seg3
obj.Placement.Base = FreeCAD.Vector(30, 110, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```



### Powłoka, 3 węzły trójkąt, tria3 (liniowy) 


```python
import Fem

tria3 = Fem.FemMesh()
tria3.addNode( 0,  0, 0, 1)
tria3.addNode( 6, 12, 0, 2)
tria3.addNode(12,  0, 0, 3)
tria3.addFace([1, 2, 3])
print(tria3)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "tria3")
obj.FemMesh = tria3
obj.Placement.Base = FreeCAD.Vector(0, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Dodaj ścianę z numerem elementu.


```python
elemtria3 = Fem.FemMesh()
nodes = tria3.Nodes
for n in nodes:
    elemtria3.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtria3.addFace([1, 2, 3], 88)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemtria3")
obj.FemMesh = elemtria3
obj.Placement.Base = FreeCAD.Vector(200, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemtria3.Faces)
```



### Powłoka, 6 węzłów trójkąt, tria6 (kwadratowy) 


```python
import Fem

tria6 = Fem.FemMesh()
tria6.addNode( 0,  0, 0, 1)
tria6.addNode( 6, 12, 0, 2)
tria6.addNode(12,  0, 0, 3)
tria6.addNode( 3,  6, 0, 4)
tria6.addNode( 9,  6, 0, 5)
tria6.addNode( 6,  0, 0, 6)
tria6.addFace([1, 2, 3, 4, 5, 6])
print(tria6)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "tria6")
obj.FemMesh = tria6
obj.Placement.Base = FreeCAD.Vector(30, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Dodaj ścianę z numerem elementu.


```python
elemtria6 = Fem.FemMesh()
nodes = tria6.Nodes
for n in nodes:
    elemtria6.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtria6.addFace([1, 2, 3, 4, 5, 6], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemtria6")
obj.FemMesh = elemtria6
obj.Placement.Base = FreeCAD.Vector(230, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemtria6.Faces)
```



### Powłoka, 4 węzły czworokąt, quad4 (liniowy) 


```python
import Fem

quad4 = Fem.FemMesh()
quad4.addNode( 0, 10, 0, 1)
quad4.addNode(10, 10, 0, 2)
quad4.addNode(10,  0, 0, 3)
quad4.addNode( 0,  0, 0, 4)
quad4.addFace([1, 2, 3, 4])
print(quad4)

obj = FreeCAD.ActiveDocument.addObject("Fem::FemMeshObject", "quad4")
obj.FemMesh = quad4
obj.Placement.Base = FreeCAD.Vector(60, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Dodaj ścianę z numerem elementu.


```python
elemquad4 = Fem.FemMesh()
nodes = quad4.Nodes
for n in nodes:
    elemquad4.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemquad4.addFace([1, 2, 3, 4], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemquad4")
obj.FemMesh = elemquad4
obj.Placement.Base = FreeCAD.Vector(260, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemquad4.Faces)
```



### Powłoka, 8 węzłów czworokąt, quad8 (kwadratowy) 


```python
import Fem

quad8 = Fem.FemMesh()
quad8.addNode( 0, 10, 0, 1)
quad8.addNode(10, 10, 0, 2)
quad8.addNode(10,  0, 0, 3)
quad8.addNode( 0,  0, 0, 4)
quad8.addNode( 5, 10, 0, 5)
quad8.addNode(10,  5, 0, 6)
quad8.addNode( 5,  0, 0, 7)
quad8.addNode( 0,  5, 0, 8)
quad8.addFace([1, 2, 3, 4, 5, 6, 7, 8])
print(quad8)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "quad8")
obj.FemMesh = quad8
obj.Placement.Base = FreeCAD.Vector(90, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Dodaj ścianę z numerem elementu.


```python
elemquad8 = Fem.FemMesh()
nodes = quad8.Nodes
for n in nodes:
    elemquad8.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemquad8.addFace([1, 2, 3, 4, 5, 6, 7, 8], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemquad8")
obj.FemMesh = elemquad8
obj.Placement.Base = FreeCAD.Vector(290, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemquad8.Faces)
```



### Objętość, 4 węzły czworościan, tetra4 (liniowy) 


```python
import Fem

tetra4 = Fem.FemMesh()
tetra4.addNode( 6, 12, 18, 1)
tetra4.addNode( 0,  0, 18, 2)
tetra4.addNode(12,  0, 18, 3)
tetra4.addNode( 6,  6,  0, 4)
tetra4.addVolume([1, 2, 3, 4])
print(tetra4)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "tetra4")
obj.FemMesh = tetra4
obj.Placement.Base = FreeCAD.Vector(0, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Dodaj objętość z numerem elementu.


```python
elemtetra4 = Fem.FemMesh()
nodes = tetra4.Nodes
for n in nodes:
    elemtetra4.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtetra4.addVolume([1, 2, 3, 4], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemtetra4")
obj.FemMesh = elemtetra4
obj.Placement.Base = FreeCAD.Vector(200, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemtetra4.Volumes)
```



### Objętość, 10 węzłów czworościan, tetra10 (kwadratowy) 


```python
import Fem

tetra10 = Fem.FemMesh()
tetra10.addNode( 6, 12, 18, 1)
tetra10.addNode( 0,  0, 18, 2)
tetra10.addNode(12,  0, 18, 3)
tetra10.addNode( 6,  6,  0, 4)

tetra10.addNode( 3,  6, 18, 5)
tetra10.addNode( 6,  0, 18, 6)
tetra10.addNode( 9,  6, 18, 7)

tetra10.addNode( 6,  9,  9, 8)
tetra10.addNode( 3,  3,  9, 9)
tetra10.addNode( 9,  3,  9,10)
tetra10.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(tetra10)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "tetra10")
obj.FemMesh = tetra10
obj.Placement.Base = FreeCAD.Vector(30, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Dodaj objętość z numerem elementu.


```python
elemtetra10 = Fem.FemMesh()
nodes = tetra10.Nodes
for n in nodes:
    elemtetra10.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtetra10.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemtetra10")
obj.FemMesh = elemtetra10
obj.Placement.Base = FreeCAD.Vector(230, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemtetra10.Volumes)
```



### Objętość, 8 węzłów prostopadłościan, hexa8 (liniowy) 


```python
import Fem

hexa8 = Fem.FemMesh()
hexa8.addNode( 0, 10, 10, 1)
hexa8.addNode( 0,  0, 10, 2)
hexa8.addNode(10,  0, 10, 3)
hexa8.addNode(10, 10, 10, 4)
hexa8.addNode( 0, 10,  0, 5)
hexa8.addNode( 0,  0,  0, 6)
hexa8.addNode(10,  0,  0, 7)
hexa8.addNode(10, 10,  0, 8)
hexa8.addVolume([1, 2, 3, 4, 5, 6, 7, 8])
print(hexa8)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "hexa8")
obj.FemMesh = hexa8
obj.Placement.Base = FreeCAD.Vector(60, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Dodaj objętość z numerem elementu.


```python
elemhexa8 = Fem.FemMesh()
nodes = hexa8.Nodes
for n in nodes:
    elemhexa8.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemhexa8.addVolume([1,  2,  3, 4, 5, 6, 7, 8], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemhexa8")
obj.FemMesh = elemhexa8
obj.Placement.Base = FreeCAD.Vector(260, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemhexa8.Volumes)
```



### Objętość, 20 węzłów prostopadłościan, hexa20 (kwadratowy) 


```python
import Fem

hexa20 = Fem.FemMesh()
hexa20.addNode( 0, 10, 10,  1)
hexa20.addNode( 0,  0, 10,  2)
hexa20.addNode(10,  0, 10,  3)
hexa20.addNode(10, 10, 10,  4)
hexa20.addNode( 0, 10,  0,  5)
hexa20.addNode( 0,  0,  0,  6)
hexa20.addNode(10,  0,  0,  7)
hexa20.addNode(10, 10,  0,  8)

hexa20.addNode( 0,  5, 10,  9)
hexa20.addNode( 5,  0, 10, 10)
hexa20.addNode(10,  5, 10, 11)
hexa20.addNode( 5, 10, 10, 12)

hexa20.addNode( 0,  5,  0, 13)
hexa20.addNode( 5,  0,  0, 14)
hexa20.addNode(10,  5,  0, 15)
hexa20.addNode( 5, 10,  0, 16)

hexa20.addNode( 0, 10,  5, 17)
hexa20.addNode( 0,  0,  5, 18)
hexa20.addNode(10,  0,  5, 19)
hexa20.addNode(10, 10,  5, 20)
hexa20.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(hexa20)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "hexa20")
obj.FemMesh = hexa20
obj.Placement.Base = FreeCAD.Vector(90, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Dodaj objętość z numerem elementu.


```python
elemhexa20 = Fem.FemMesh()
nodes = hexa20.Nodes
for n in nodes:
    elemhexa20.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemhexa20.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elemhexa20")
obj.FemMesh = elemhexa20
obj.Placement.Base = FreeCAD.Vector(290, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemhexa20.Volumes)
```



### Objętość, 6 węzłów pięciościan, penta6 (liniowy) 


```python
import Fem

penta6 = Fem.FemMesh()
penta6.addNode(10, 10, 10, 1)
penta6.addNode( 0,  0, 10, 2)
penta6.addNode(20,  0, 10, 3)
penta6.addNode(10, 10,  0, 4)
penta6.addNode( 0,  0,  0, 5)
penta6.addNode(20,  0,  0, 6)
penta6.addVolume([1, 2, 3, 4, 5, 6])
print(penta6)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "penta6")
obj.FemMesh = penta6
obj.Placement.Base = FreeCAD.Vector(0, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Dodaj objętość z numerem elementu.


```python
elempenta6 = Fem.FemMesh()
nodes = penta6.Nodes
for n in nodes:
    elempenta6.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempenta6.addVolume([ 1, 2, 3, 4, 5, 6], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elempenta6")
obj.FemMesh = elempenta6
obj.Placement.Base = FreeCAD.Vector(200, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempenta6.Volumes)
```



### Objętość, 15 węzłów pięciościan, penta15 (kwadratowy) 


```python
import Fem

penta15 = Fem.FemMesh()
penta15.addNode(10, 10, 10,  1)
penta15.addNode( 0,  0, 10,  2)
penta15.addNode(20,  0, 10,  3)
penta15.addNode(10, 10,  0,  4)
penta15.addNode( 0,  0,  0,  5)
penta15.addNode(20,  0,  0,  6)

penta15.addNode( 5,  5, 10,  7)
penta15.addNode(10,  0, 10,  8)
penta15.addNode(15,  5, 10,  9)

penta15.addNode( 5,  5,  0, 10)
penta15.addNode(10,  0,  0, 11)
penta15.addNode(15,  5,  0, 12)

penta15.addNode(10, 10,  5, 13)
penta15.addNode( 0,  0,  5, 14)
penta15.addNode(20,  0,  5, 15)
penta15.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(penta15)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "penta15")
obj.FemMesh = penta15
obj.Placement.Base = FreeCAD.Vector(40, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Dodaj objętość z numerem elementu.


```python
elempenta15 = Fem.FemMesh()
nodes = penta15.Nodes
for n in nodes:
    elempenta15.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempenta15.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elempenta15")
obj.FemMesh = elempenta15
obj.Placement.Base = FreeCAD.Vector(240, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempenta15.Volumes)
```



### Objętość, 5 węzłów piramidalny, pyra5 (liniowy) 


```python
import Fem

pyra5 = Fem.FemMesh()
pyra5.addNode( 0, 20,  0, 1)
pyra5.addNode(20, 20,  0, 2)
pyra5.addNode(20,  0,  0, 3)
pyra5.addNode( 0,  0,  0, 4)
pyra5.addNode(10, 10, 10, 5)
pyra5.addVolume([1, 2, 3, 4, 5])
print(pyra5)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "pyra5")
obj.FemMesh = pyra5
obj.Placement.Base = FreeCAD.Vector(80, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Dodaj objętość z numerem elementu.


```python
elempyra5 = Fem.FemMesh()
nodes = pyra5.Nodes
for n in nodes:
    elempyra5.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempyra5.addVolume([1, 2, 3, 4, 5], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elempyra5")
obj.FemMesh = elempyra5
obj.Placement.Base = FreeCAD.Vector(280, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempyra5.Volumes)
```



### Objętość, 13 węzłów piramidalny, pyra13 (kwadratowy) 


```python
import Fem

pyra13 = Fem.FemMesh()
pyra13.addNode( 0, 20,  0,  1)
pyra13.addNode(20, 20,  0,  2)
pyra13.addNode(20,  0,  0,  3)
pyra13.addNode( 0,  0,  0,  4)
pyra13.addNode(10, 10, 10,  5)

pyra13.addNode(10, 20,  0,  6)
pyra13.addNode(20, 10,  0,  7)
pyra13.addNode(10,  0,  0,  8)
pyra13.addNode( 0, 10,  0,  9)

pyra13.addNode( 5, 15,  5, 10)
pyra13.addNode(15, 15,  5, 11)
pyra13.addNode(15,  5,  5, 12)
pyra13.addNode( 5,  5,  5, 13)
pyra13.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(pyra13)

obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "pyra13")
obj.FemMesh = pyra13
obj.Placement.Base = FreeCAD.Vector(120, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Dodaj objętość z numerem elementu.


```python
elempyra13 = Fem.FemMesh()
nodes = pyra13.Nodes
for n in nodes:
    elempyra13.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempyra13.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 88)
obj = App.ActiveDocument.addObject("Fem::FemMeshObject", "elempyra13")
obj.FemMesh = elempyra13
obj.Placement.Base = FreeCAD.Vector(320, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempyra13.Volumes)
```



## Przykłady skryptów dla grup 

Zobacz np. <https://forum.freecadweb.org/viewtopic.php?f=18&t=37304&start=20#p318823>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Mesh/pl
