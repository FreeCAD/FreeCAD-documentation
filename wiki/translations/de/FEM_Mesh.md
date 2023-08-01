# FEM Mesh/de
{{TOCright}}

## Ein Finite-Elemente-Netz erstellen 

Die Finite-Elemente-Analyse (FEA) wird auf einem Polygonnetz durchgeführt, das aus mehreren drei- und vierseitigen finiten Elementen besteht, die einen Originalkörper unterteilen. Je feiner das Netz ist, desto genauer sind die numerischen Ergebnisse, aber desto größer ist auch die Berechnungszeit. Ein Gleichgewicht zwischen der Größe des Netzes, der Berechnungszeit und der Genauigkeit der Ergebnisse ist ein wichtiges Merkmal einer gut definierten Finite-Elemente-Analyse.

Es gibt verschiedene Möglichkeiten, ein Polygonnetz im Arbeitsbereich [FEM](FEM_Workbench/de.md) einzurichten:

-   Das Werkzeug [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape/de.md) aus der grafischen Benutzeroberfläche.
-   Das Werkzeug [FEM mesh from shape by Netgen](FEM_MeshGmshFromShape/de.md) aus der grafischen Benutzeroberfläche.
-   Importieren eines Polygonnetzes aus einem anderen Programm. Insbesondere können Gmsh und Netgen außerhalb von FreeCAD allein verwendet werden, um Volumenkörper wie Step Dateien zu vernetzen.
-   Manuelle Erstellung des Netzes durch [Python](Python/de.md)-Skripte.

Die Gmsh und Netgen Werkzeuge unterstützen die Vernetzung von Körpern, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md) und [PartDesign](PartDesign_Workbench/de.md) erstellt wurden, sowie einfache Kopien dieser Körper. Im Allgemeinen kann jeder Arbeitsbereich, der Volumenkörper erzeugt, wie z.B. der Arbeitsbereich [Arch](Arch_Workbench/de.md), als Grundlage für die Erstellung von Polygonnetzen verwendet werden. Beachte, dass sich ein für die FEA verwendetes Netz von einem Netz unterscheidet, das mit dem Arbeitsbereich [Mesh](Mesh_Workbench/de.md) erstellt oder importiert wurde.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;"> 
*Der Arbeitsbereich FEM ruft das externe Werkzeug Gmsh auf, um ein Netz aus einem Volumenkörper zu erhalten, der mit einem beliebigen Arbeitsbereich in FreeCAD erstellt wurde; es kann auch ein extern erstelltes Netz importieren*

<img alt="" src=images/FEM_Mesh.png  style="width:600px;"> 
*(1) Festkörper, der mit PartDesign erzeugt wurde; (2) Netz, das mit dem Gmsh Werkzeug innerhalb des FEM Arbeitsbereich erzeugt wurde (alle Dreiecke); und (3) Netz, das extern mit Gmsh erzeugt wurde, in das Abaqus Format **.inp* exportiert und dann in FreeCAD importiert wurde (alle Vierecke)**

Die [Gmsh-](FEM_MeshGmshFromShape/de.md) und [Netgen-Werkzeuge](FEM_MeshNetgenFromShape/de.md) sind einfach anzuwendende Werkzeuge, um einen Körper schnell zu vernetzen, und besitzen nicht den vollen Funktionsumfang dieser Programme; sie erzeugen normalerweise Dreiecksnetze, die für manche Arten von Analysen nicht ideal sind. Wird mehr Kontrolle über das erstellte Netz gebraucht (nur Vierecke verwenden, genaue Elementanzahl und -Größe, variable Auflösung des Netzes, usw.), sollten diese Programme extern verwendet, eine Netzdatei in einem unterstützten Format (**.inp**, **.unv**, **.vtk**, **.z88**) erzeugt und diese Datei in FreeCAD importiert werden.

Zuvor war Netgen in FreeCAD enthalten und konnte sofort verwendet werden. Nun sollten sowohl Netgen als auch Gmsh installiert werden, bevor sie vom Arbeitsbereich [FEM](FEM_Workbench/de.md) verwendet werden können. Siehe [FEM Installation](FEM_Install/de.md) für Anleitungen.

## Netzerstellungssoftware

Netzerstellungssoftware arbeitet mit Festkörpern, die in verschiedenen Formaten vorliegen können, wie Step und Brep. Diese Programme können unabhängig von FreeCAD verwendet werden und verfügen typischerweise Über viele Optionen zur Steuerung der Vernetzungsalgorithmen, der Elementgröße und der Randbedingungen.

Der Arbeitsbereich [FEM](FEM_Workbench/de.md) hat einfache Kommunikationsoberflächen entwickelt, um Gmsh und Netgen direkt in FreeCAD zu verwenden. Andere Programme haben keine Oberfläche, aber das könnte sich in Zukunft ändern, wenn Interesse in der Gemeinschaft besteht und wenn diese Anwendungen leicht zu integrieren sind. Die Netzerstellungssoftware darf nur dann zusammen mit FreeCAD kompiliert und verteilt werden, wenn ihre Lizenz mit der LGPL2-Lizenz kompatibel ist; andernfalls muss das Programm als externe Binärdatei verwendet werden, wie z.B. Gmsh (GPL2).

### Oberfläche in FreeCAD implementiert 

-   Gmsh: [Hauptwebseite](http://gmsh.info/), [Code Repositorium](https://gitlab.onelab.info/gmsh/gmsh)
-   Netgen: [Hauptwebseite](https://ngsolve.org/), [Code Repositorium](https://github.com/NGSolve/netgen)

### Keine Oberfläche in FreeCAD 

-   ENigMA, [1](https://forum.freecadweb.org/viewtopic.php?f=18&t=33048beitrag), [Code Repositorium](https://github.com/bjaraujo/ENigMA)
-   libMesh, [Hauptwebseite](http://libmesh.github.io/), [Code Repositorium](https://github.com/libMesh/libmesh), [Forumsbeitrag](https://forum.freecadweb.org/viewtopic.php?f=18&t=33621); es ist ein sehr aktives Projekt, und es ist nur C++
-   PythonOCC, [Haupt-Webseite](http://www.pythonocc.org/)
-   SnappyHexMesh, [Hauptwebseite](https://openfoamwiki.net/index.php/SnappyHexMesh)
-   Tetgen, [Hauptwebseite](http://wias-berlin.de/software/tetgen/)

## Netzelemente in FreeCAD 

FreeCAD unterstützt verschiedene Elementtypen. Der folgende Artikel erklärt den Unterschied zwischen ihnen und wann sie verwendet werden sollten (engl.): [Meshing Your Geometry: When to Use the Various Element Types](https://www.comsol.com/blogs/meshing-your-geometry-various-element-types/).

<table>
<caption>Import and export of mesh elements</caption>
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
<td><p>Result Mesh</p></td>
<td><p>Z88</p></td>
<td><p>FEniCS</p></td>
</tr>
<tr class="even">
<td><p>Name</p></td>
<td><p>Name</p></td>
<td><p>create elements</p></td>
<td><p>view elements</p></td>
<td><p>import/export</p></td>
<td><p>import/export</p></td>
<td><p>import/export</p></td>
<td><p>import</p></td>
<td><p>import/export</p></td>
<td><p>import/export</p></td>
</tr>
<tr class="odd">
<td><p>seg 2</p></td>
<td><p>B31</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>seg 3</p></td>
<td><p>B32</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><p>NI</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>tria 3</p></td>
<td><p>S3</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>tria 6</p></td>
<td><p>S6</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>quad 4</p></td>
<td><p>S4</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>quad 8</p></td>
<td><p>S8</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>tetra 4</p></td>
<td><p>C3D4</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>tetra 10</p></td>
<td><p>C3D10</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>hexa 8</p></td>
<td><p>C3D8</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><p>(<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />) the format allows it,<br />
but it's not readable or writable by FEniCS</p></td>
</tr>
<tr class="even">
<td><p>hexa 20</p></td>
<td><p>C3D20</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>penta 6</p></td>
<td><p>C3D6</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><p>?</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>penta 15</p></td>
<td><p>C3D15</p></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><p>?</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="odd">
<td><p>pyra 5</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>pyra 13</p></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_OK.svg" title="Edit_OK.svg" width="20" alt="Edit_OK.svg" />
<figcaption aria-hidden="true">Edit_OK.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
<td><figure>
<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />
<figcaption aria-hidden="true">Edit_Cancel.svg</figcaption>
</figure></td>
</tr>
</tbody>
</table>

: Import and export of mesh elements

-   NI\" bedeutet, dass der Elementtyp in FreeCAD nicht implementiert ist, aber das Format ihn unterstützen würde.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:20px;"> bedeutet, dass die Formatspezifikation diesen Elementtyp nicht unterstützt, so dass FreeCAD ihn nicht unterstützen kann.
-   \"?\" bedeutet, dass es nicht bekannt ist, ob das Format diesen Elementtyp unterstützt.

## FEM Elementtypen 

Mehr Informationen über die Elemente und ihre Datenstruktur in FreeCAD kann in [FEM Elementtypen](FEM_Element_Types/de.md) gefunden werden.

### Segmentelement

<img alt="" src=images/FEM_mesh_elements_1_segment.svg  style="width:600px;">

### Dreieckelement

<img alt="" src=images/FEM_mesh_elements_2_triangle.svg  style="width:600px;">

### Viereckelement

<img alt="" src=images/FEM_mesh_elements_3_quadrangle.svg  style="width:600px;">

### Tetraederelement

<img alt="" src=images/FEM_mesh_elements_4_tetrahedron.svg  style="width:600px;">

### Hexaederelement

<img alt="" src=images/FEM_mesh_elements_5_hexahedron.svg  style="width:600px;">

### Pentaederelement (Prisma) 

<img alt="" src=images/FEM_mesh_elements_6_pentahedron.svg  style="width:600px;">

### Pyramidenelement

<img alt="" src=images/FEM_mesh_elements_7_pyramid.svg  style="width:600px;">

## Skripten

### Ein FEM-Netz komplett in Python erstellen 


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Die Python API ermöglicht dem Benutzer ein Finite Element Netz festzulegen, durch direktes hinzufügen einzelner Knoten und festlegen von Kanten, Flächen und Volumen.

Das Netz selbst ist vom Typ `Fem::FemMesh`, das an ein entsprechendes Dokumentobjekt vom Typ `Fem::FemMeshObject` angehängt werden muss .


```python
App.ActiveDocument.Mesh_object.TypeId = Fem::FemMeshObject
                              .
                              .
                              .FemMesh.TypeId = Fem::FemMesh
```

#### Erstellen eines Netzes mit einem Tet-10 Element 

Erstelle ein leeres FemMesh, bestücke es mit Knoten, erstelle das Volumen und rufe schließlich `Fem.show()` auf, um das Dokumentobjekt mit dem zugehörigen Netz zu erstellen.


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

Wenn du eine vordefinierte Knoten- und Elementnummerierung wünschst, übergib die entsprechende ID an die Knoten- und Volumen Methoden

Um ein aktuelles Dokumentobjekt zu erstellen, kannst du anstelle von `Fem.show()` auch die Methode document `addObject()` verwenden; hänge dann das erstellte Netz an das `FemMesh` Attribut dieses Objekts an.


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

#### Visuelle Eigenschaften 

Sobald ein FemMesh Objekt mit `Fem.show()` erstellt wurde, können einige seiner visuellen Eigenschaften durch Ändern der verschiedenen Attribute seines `ViewObject` geändert werden. Dies kann nützlich sein, um das Netz nach einer Finite Elemente Lösung nachzubearbeiten.

Heben Sie einige Knoten im Netz hervor 
```python
Fem.show(m)
obj = FreeCAD.ActiveDocument.ActiveObject

obj.ViewObject.HighlightedNodes = [1, 2, 3]
```

Die einzelnen Elemente eines Netzes können durch die Übergabe eines Wörterbuchs mit den entsprechenden `key:value` Paaren modifiziert werden

Setze das Volumen 1 auf rot


```python
obj.ViewObject.ElementColor = {1:(1,0,0)}
```

Setzt man die Knoten 1, 2 und 3 auf unterschiedliche Farben, erhält die Fläche dazwischen eine daraus errechnete Farbe.


```python
obj.ViewObject.NodeColor = {1:(1,0,0), 2:(0,1,0), 3:(0,0,1)}
```

Displace the nodes 1 and 2 by the magnitude and direction defined by a vector.


```python
obj.ViewObject.NodeDisplacement = {1:FreeCAD.Vector(0,1,0), 2:FreeCAD.Vector(1,0,0)}
```

Double the factor of the displacement shown. (**Note to editors: removed in newer versions?**)


```python
obj.ViewObject.animate(2.0)
```

## Skripten Beispiele für jeden unterstützten Elementtyp 

### Träger, 2 Knoten Linie, seg2 (linear) 


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

### Träger, 3 Knoten Linie, seg3 (quadratisch) 


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

### Shell, 3 node triangle, tria3 (linear) 


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

Add a face with the element number.


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

### Shell, 6 node triangle, tria6 (quadratic) 


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

Add a face with the element number.


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

### Shell, 4 node quadrangle, quad4 (linear) 


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

Add a face with the element number.


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

### Shell, 8 node quadrangle, quad8 (quadratic) 


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

Add a face with the element number.


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

### Volume, 4 node tetrahedron, tetra4 (linear) 


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

Add a volume with the element number.


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

### Volume, 10 node tetrahedron, tetra10 (quadratic) 


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

Add a volume with the element number.


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

### Volume, 8 node hexahedron, hexa8 (linear) 


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

Add a volume with the element number.


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

### Volume, 20 node hexahedron, hexa20 (quadratic) 


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

Add a volume with the element number.


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

### Volume, 6 node pentahedron, penta6 (linear) 


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

Add a volume with the element number.


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

### Volume, 15 node pentahedron, penta15 (quadratic) 


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

Add a volume with the element number.


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

### Volume, 5 node pyramid, pyra5 (linear) 


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

Add a volume with the element number.


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

### Volume, 13 node pyramid, pyra13 (quadratic) 


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

Füge ein Volumen mit der Elementnummer hinzu.


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

## Scripting examples for groups 

See for example <https://forum.freecadweb.org/viewtopic.php?f=18&t=37304&start=20#p318823>


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Mesh/de
