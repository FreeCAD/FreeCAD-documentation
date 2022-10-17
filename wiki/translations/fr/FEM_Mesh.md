# FEM Mesh/fr
{{TOCright}}

## Créer un maillage à éléments finis 

L\'analyse par éléments finis (FEA) est effectuée sur un maillage composé de multiples éléments triangulaires et quadrilatéraux qui subdivisent le corps d\'origine. Plus le maillage est raffiné, plus les résultats numériques seront précis, mais le temps de calcul sera également plus long. Un équilibre entre la taille du maillage, le temps de calcul et la précision des résultats est une caractéristique importante d\'une analyse par éléments finis bien définie.

Il existe différentes possibilités pour configurer un maillage dans l\'[atelier FEM](FEM_Workbench/fr.md)    *

-   L\'[outil Gmsh](FEM_MeshGmshFromShape/fr.md) de l\'interface utilisateur graphique.
-   L\'[outil Netgen](FEM_MeshNetgenFromShape/fr.md) à partir de l\'interface graphique.
-   Importer un maillage depuis un autre programme. En particulier, Gmsh et Netgen peuvent être utilisés seuls en dehors de FreeCAD pour mailler des corps solides tels que des fichiers Step.
-   Créer manuellement le maillage à l\'aide de scripts [Python](Python/fr.md).

Les outils Gmsh et Netgen prennent en charge les corps de maillage créés avec les ateliers [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md), ainsi que les copies simples de ces solides. En général, tout atelier générant des objets solides, tel que l\'[atelier Arch](Arch_Workbench/fr.md), peut être utilisé comme base de création de maillages. Notez qu\'un maillage utilisé pour FEA est différent d\'un maillage créé ou importé à partir de l\'[atelier Mesh](Mesh_Workbench/fr.md).

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width   *600px;"> 
*L'atelier FEM appelle l'outil externe Gmsh pour obtenir un maillage à partir d'un corps solide créé avec n'importe quel atelier dans FreeCAD ; il peut aussi importer un maillage créé en externe*

<img alt="" src=images/FEM_Mesh.png  style="width   *600px;"> 
*(1) Corps solide créé avec PartDesign ; (2) maillage produit par l'outil Gmsh à l'intérieur de l'atelier FEM (tous les triangles) ; et (3) un maillage produit en externe par Gmsh, exporté au format Abaqus **.inp*, puis importé dans FreeCAD (tous les quadrangles).**

Les outils [Gmsh](FEM_MeshGmshFromShape/fr.md) et [Netgen](FEM_MeshNetgenFromShape/fr.md) sont des outils pratiques pour rapidement mailler un corps et ne pas exposer ainsi toutes les capacités de ces programmes. ils créent normalement des maillages triangulaires, ce qui peut ne pas être idéal pour certains types d\'analyse. Si vous souhaitez mieux contrôler le maillage créé (utilisez uniquement des quadrilatères, un nombre et une taille d\'élément précis, une résolution variable du maillage, etc.), vous devez utiliser ces programmes en externe, créez un fichier de maillage dans un format pris en charge (**.inp**, **.unv**, **.vtk**, **.z88**), et importez ce fichier dans FreeCAD.

Auparavant, Netgen était inclus dans FreeCAD et pouvait être utilisé immédiatement. Maintenant, Netgen et Gmsh doivent être installés avant de pouvoir être utilisés par l\'[atelier FEM](FEM_Workbench/fr.md). Reportez-vous à [Installation FEM](FEM_Install/fr.md) pour les instructions.

## Logiciels de maillage 

Les logiciels de maillage opèrent sur des corps solides qui peuvent être dans différents formats, comme Step et Brep. Ces programmes peuvent être utilisés indépendamment de FreeCAD, et disposent généralement de nombreuses options pour contrôler les algorithmes de maillage, la taille des éléments et les conditions aux limites.

L\'[atelier FEM](FEM_Workbench/fr.md) a développé des interfaces de communication simples pour utiliser Gmsh et Netgen directement dans FreeCAD. D\'autres programmes n\'ont pas d\'interface, mais cela pourrait changer à l\'avenir si la communauté suscite de l\'intérêt et si ces applications sont faciles à intégrer. Le logiciel de maillage peut être compilé et distribué avec FreeCAD seulement si sa licence est compatible avec les licences GPL2 ou LGPL2 ; sinon le programme doit être utilisé comme un binaire externe, comme Gmsh (GPL2).

### Interface implémenté dans FreeCAD 

-   Gmsh    * [site web principal](http   *//gmsh.info/), [dépôt du code](https   *//gitlab.onelab.info/gmsh/gmsh)
-   Netgen    * [site web principal](https   *//ngsolve.org/), [dépôt du code](https   *//github.com/NGSolve/netgen)

### Sans interface dans FreeCAD 

-   ENigMA, [fil du forum](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=33048), [dépôt du code](https   *//github.com/bjaraujo/ENigMA)
-   libMesh, [site web principal](http   *//libmesh.github.io/), [dépôt du code](https   *//github.com/libMesh/libmesh), [fil du forum](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=33621) ; c\'est un projet très actif seulement en C++
-   PythonOCC, [site web principal](http   *//www.pythonocc.org/)
-   SnappyHexMesh, [site web principal](https   *//openfoamwiki.net/index.php/SnappyHexMesh)
-   Tetgen, [site web principal](http   *//wias-berlin.de/software/tetgen/)

## Éléments de maillage dans FreeCAD 

FreeCAD supporte différents types d\'éléments. L\'article suivant explique la différence qui existe entre eux et quand vous pouvez les utiliser    * [Maillage de votre géométrie    * quand utiliser les différents types d\'élément](https   *//www.comsol.com/blogs/meshing-your-geometry-various-element-types/).

<table>
<caption>Importation et exportation d'éléments de maillage</caption>
<thead>
<tr class="header">
<th><p>Elément</p></th>
<th><p>Elément</p></th>
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
<td><p>Maillage FEM</p></td>
<td><p>SMESH</p></td>
<td><p>IDEAS/FreeCAD</p></td>
<td><p>Abaqus/CalculiX</p></td>
<td><p>Résultat de Mesh</p></td>
<td><p>Z88</p></td>
<td><p>FEniCS</p></td>
</tr>
<tr class="even">
<td><p>Nom</p></td>
<td><p>Nom</p></td>
<td><p>Créer des éléments</p></td>
<td><p>Éléments d'affichage</p></td>
<td><p>Importer/exporter</p></td>
<td><p>Importer/exporter</p></td>
<td><p>Importer/exporter</p></td>
<td><p>Importer</p></td>
<td><p>Importer/exporter</p></td>
<td><p>Importer/exporter</p></td>
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
<td><p>(<img src="Edit_Cancel.svg" title="Edit_Cancel.svg" width="20" alt="Edit_Cancel.svg" />) le format le permet,<br />
mais il n'est pas lisible<br />
ou modifiable par FEniCS.</p></td>
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

   * Importation et exportation d\'éléments de maillage

-   \"NI\" signifie que le type d\'élément n\'est pas implémenté dans FreeCAD, mais le format est supporté.
-   <img alt="" src=images/Edit_Cancel.svg  style="width   *20px;"> signifie que la spécification de format ne supporte pas ce type d\'élément, et qu\'il ne sera pas accepté par FreeCAD.
-   \"?\" signifie qu\'on ne sait pas si ce type d\'élément est supporté.

## Types d\'éléments FEM 

Vous trouverez plus d\'informations sur les éléments et leur structure de données dans FreeCAD dans [Types d\'élément FEM](FEM_Element_Types/fr.md).

### Les segments 

<img alt="" src=images/FEM_mesh_elements_1_segment.svg  style="width   *600px;">

### Les triangles 

<img alt="" src=images/FEM_mesh_elements_2_triangle.svg  style="width   *600px;">

### Les quadrangles 

<img alt="" src=images/FEM_mesh_elements_3_quadrangle.svg  style="width   *600px;">

### Les tétraèdres 

<img alt="" src=images/FEM_mesh_elements_4_tetrahedron.svg  style="width   *600px;">

### Les hexaèdres 

<img alt="" src=images/FEM_mesh_elements_5_hexahedron.svg  style="width   *600px;">

### Les pentaèdres (prismes) 

<img alt="" src=images/FEM_mesh_elements_6_pentahedron.svg  style="width   *600px;">

### Les pyramides 

<img alt="" src=images/FEM_mesh_elements_7_pyramid.svg  style="width   *600px;">

## Script

### Créez un maillage FEM entièrement en Python 


**Voir aussi   ***

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'API Python permet à l\'utilisateur de définir un maillage d\'éléments finis en ajoutant directement des nœuds individuels et en définissant des arêtes, des faces et des volumes.

Le maillage lui-même est de type `Fem   *   *FemMesh`, qui doit être attaché à un objet approprié du document de type `Fem   *   *FemMeshObject`.


```python
App.ActiveDocument.Mesh_object.TypeId = Fem   *   *FemMeshObject
                              .
                              .
                              .FemMesh.TypeId = Fem   *   *FemMesh
```

#### Création d\'un maillage avec un élément Tet-10 

Créez un FemMesh vide, remplissez-le avec des nœuds, créez le volume et appelez enfin `Fem.show()` pour créer l\'objet du document avec le maillage correspondant.


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

Si vous souhaitez une numérotation prédéfinie des noeuds et des éléments, transmettez l\'ID approprié aux méthodes de noeud et de volume.

Pour créer un objet document réel, au lieu de `Fem.show()` vous pouvez utiliser la méthode `addObject()` ; attachez ensuite le maillage créé à l\'attribut `FemMesh` de cet objet.


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
obj_2 = FreeCAD.ActiveDocument.addObject("Fem   *   *FemMeshObject")
obj_2.Placement.Base = FreeCAD.Vector(2, 0, 0)
obj_2.FemMesh = a
```

#### Propriétés visuelles 

Une fois qu\'un objet FemMesh a été créé avec `Fem.show()` , certaines de ses propriétés visuelles peuvent être modifiées en modifiant les différents attributs de son `ViewObject`. Cela peut être utile pour post-traiter le maillage après avoir obtenu une solution d\'éléments finis.

Mettez en surbrillance certains nœuds dans le maillage 
```python
Fem.show(m)
obj = FreeCAD.ActiveDocument.ActiveObject

obj.ViewObject.HighlightedNodes = [1, 2, 3]
```

Les éléments individuels d\'un maillage peuvent être modifiés en passant un dictionnaire avec les paires `key   *value` appropriées.

Réglez le volume 1 sur rouge


```python
obj.ViewObject.ElementColor = {1   *(1,0,0)}
```

Définissez les nœuds 1, 2 et 3 sur une certaine couleur; les faces entre les nœuds acquièrent une couleur interpolée.


```python
obj.ViewObject.NodeColor = {1   *(1,0,0), 2   *(0,1,0), 3   *(0,0,1)}
```

Déplacer les nœuds 1 et 2 par le sens et la direction définies par un vecteur.


```python
obj.ViewObject.NodeDisplacement = {1   *FreeCAD.Vector(0,1,0), 2   *FreeCAD.Vector(1,0,0)}
```

Doubler le facteur de déplacement indiqué. (**Note aux éditeurs    * supprimé dans les nouvelles versions ?)**


```python
obj.ViewObject.animate(2.0)
```

## Exemples de script de chaque type d\'élément supporté 

### Poutre, ligne à 2 nœuds, seg2 (linéaire) 


```python
import Fem

seg2 = Fem.FemMesh()
seg2.addNode( 0, 0, 0, 1)
seg2.addNode(10, 0, 0, 2)
seg2.addEdge(1, 2)
print(seg2)

obj = FreeCAD.ActiveDocument.addObject("Fem   *   *FemMeshObject", "seg2")
obj.FemMesh = seg2
obj.Placement.Base = FreeCAD.Vector(0, 110, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

### Poutre, ligne à 3 nœuds, seg3 (quadratique) 


```python
import Fem

seg3 = Fem.FemMesh()
seg3.addNode( 0, 0, 0, 1)
seg3.addNode(10, 0, 0, 2)
seg3.addNode( 5, 0, 0, 3)
seg3.addEdge([1, 2, 3])
print(seg3)

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "seg3")
obj.FemMesh = seg3
obj.Placement.Base = FreeCAD.Vector(30, 110, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

### Coque, triangle à 3 nœuds, tria3 (linéaire) 


```python
import Fem

tria3 = Fem.FemMesh()
tria3.addNode( 0,  0, 0, 1)
tria3.addNode( 6, 12, 0, 2)
tria3.addNode(12,  0, 0, 3)
tria3.addFace([1, 2, 3])
print(tria3)

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "tria3")
obj.FemMesh = tria3
obj.Placement.Base = FreeCAD.Vector(0, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Ajoutez une face avec le numéro d\'élément.


```python
elemtria3 = Fem.FemMesh()
nodes = tria3.Nodes
for n in nodes   *
    elemtria3.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtria3.addFace([1, 2, 3], 88)

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elemtria3")
obj.FemMesh = elemtria3
obj.Placement.Base = FreeCAD.Vector(200, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemtria3.Faces)
```

### Coque, triangle à 6 nœuds, tria6 (quadratique) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "tria6")
obj.FemMesh = tria6
obj.Placement.Base = FreeCAD.Vector(30, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Ajoutez une face avec le numéro d\'élément.


```python
elemtria6 = Fem.FemMesh()
nodes = tria6.Nodes
for n in nodes   *
    elemtria6.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtria6.addFace([1, 2, 3, 4, 5, 6], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elemtria6")
obj.FemMesh = elemtria6
obj.Placement.Base = FreeCAD.Vector(230, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemtria6.Faces)
```

### Coque, quadrilatère à 4 nœuds, quad4 (linéaire) 


```python
import Fem

quad4 = Fem.FemMesh()
quad4.addNode( 0, 10, 0, 1)
quad4.addNode(10, 10, 0, 2)
quad4.addNode(10,  0, 0, 3)
quad4.addNode( 0,  0, 0, 4)
quad4.addFace([1, 2, 3, 4])
print(quad4)

obj = FreeCAD.ActiveDocument.addObject("Fem   *   *FemMeshObject", "quad4")
obj.FemMesh = quad4
obj.Placement.Base = FreeCAD.Vector(60, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Ajoutez une face avec le numéro d\'élément.


```python
elemquad4 = Fem.FemMesh()
nodes = quad4.Nodes
for n in nodes   *
    elemquad4.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemquad4.addFace([1, 2, 3, 4], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elemquad4")
obj.FemMesh = elemquad4
obj.Placement.Base = FreeCAD.Vector(260, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemquad4.Faces)
```

### Coque, quadrilatère à 8 nœuds, quad8 (quadratique) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "quad8")
obj.FemMesh = quad8
obj.Placement.Base = FreeCAD.Vector(90, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
```

Ajoutez une face avec le numéro d\'élément.


```python
elemquad8 = Fem.FemMesh()
nodes = quad8.Nodes
for n in nodes   *
    elemquad8.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemquad8.addFace([1, 2, 3, 4, 5, 6, 7, 8], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elemquad8")
obj.FemMesh = elemquad8
obj.Placement.Base = FreeCAD.Vector(290, 80, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
obj.ViewObject.BackfaceCulling = False
print(elemquad8.Faces)
```

### Volume, tétraèdre à 4 nœuds, tétra4 (linéaire) 


```python
import Fem

tetra4 = Fem.FemMesh()
tetra4.addNode( 6, 12, 18, 1)
tetra4.addNode( 0,  0, 18, 2)
tetra4.addNode(12,  0, 18, 3)
tetra4.addNode( 6,  6,  0, 4)
tetra4.addVolume([1, 2, 3, 4])
print(tetra4)

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "tetra4")
obj.FemMesh = tetra4
obj.Placement.Base = FreeCAD.Vector(0, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Ajoutez un volume avec le numéro d\'élément.


```python
elemtetra4 = Fem.FemMesh()
nodes = tetra4.Nodes
for n in nodes   *
    elemtetra4.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtetra4.addVolume([1, 2, 3, 4], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elemtetra4")
obj.FemMesh = elemtetra4
obj.Placement.Base = FreeCAD.Vector(200, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemtetra4.Volumes)
```

### Volume, tétraèdre à 10 nœuds, tétra10 (quadratique) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "tetra10")
obj.FemMesh = tetra10
obj.Placement.Base = FreeCAD.Vector(30, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Ajoutez un volume avec le numéro d\'élément.


```python
elemtetra10 = Fem.FemMesh()
nodes = tetra10.Nodes
for n in nodes   *
    elemtetra10.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemtetra10.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elemtetra10")
obj.FemMesh = elemtetra10
obj.Placement.Base = FreeCAD.Vector(230, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemtetra10.Volumes)
```

### Volume, hexaèdre à 8 nœuds, hexa8 (linéaire) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "hexa8")
obj.FemMesh = hexa8
obj.Placement.Base = FreeCAD.Vector(60, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Ajoutez un volume avec le numéro d\'élément.


```python
elemhexa8 = Fem.FemMesh()
nodes = hexa8.Nodes
for n in nodes   *
    elemhexa8.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemhexa8.addVolume([1,  2,  3, 4, 5, 6, 7, 8], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elemhexa8")
obj.FemMesh = elemhexa8
obj.Placement.Base = FreeCAD.Vector(260, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemhexa8.Volumes)
```

### Volume, hexaèdre à 20 noeuds, hexa20 (quadratique) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "hexa20")
obj.FemMesh = hexa20
obj.Placement.Base = FreeCAD.Vector(90, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Ajoutez un volume avec le numéro d\'élément.


```python
elemhexa20 = Fem.FemMesh()
nodes = hexa20.Nodes
for n in nodes   *
    elemhexa20.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elemhexa20.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elemhexa20")
obj.FemMesh = elemhexa20
obj.Placement.Base = FreeCAD.Vector(290, 50, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elemhexa20.Volumes)
```

### Volume, pentaèdre à 6 nœuds, penta6 (linéaire) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "penta6")
obj.FemMesh = penta6
obj.Placement.Base = FreeCAD.Vector(0, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Ajoutez un volume avec le numéro d\'élément.


```python
elempenta6 = Fem.FemMesh()
nodes = penta6.Nodes
for n in nodes   *
    elempenta6.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempenta6.addVolume([ 1, 2, 3, 4, 5, 6], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elempenta6")
obj.FemMesh = elempenta6
obj.Placement.Base = FreeCAD.Vector(200, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempenta6.Volumes)
```

### Volume, pentaèdre à 15 noeuds, penta15 (quadratique) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "penta15")
obj.FemMesh = penta15
obj.Placement.Base = FreeCAD.Vector(40, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Ajoutez un volume avec le numéro d\'élément.


```python
elempenta15 = Fem.FemMesh()
nodes = penta15.Nodes
for n in nodes   *
    elempenta15.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempenta15.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elempenta15")
obj.FemMesh = elempenta15
obj.Placement.Base = FreeCAD.Vector(240, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempenta15.Volumes)
```

### Volume, pyramide à 5 nœuds, pyra5 (linéaire) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "pyra5")
obj.FemMesh = pyra5
obj.Placement.Base = FreeCAD.Vector(80, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Ajoutez un volume avec le numéro d\'élément.


```python
elempyra5 = Fem.FemMesh()
nodes = pyra5.Nodes
for n in nodes   *
    elempyra5.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempyra5.addVolume([1, 2, 3, 4, 5], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elempyra5")
obj.FemMesh = elempyra5
obj.Placement.Base = FreeCAD.Vector(280, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempyra5.Volumes)
```

### Volume, pyramide à 13 nœuds, pyra13 (quadratique) 


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

obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "pyra13")
obj.FemMesh = pyra13
obj.Placement.Base = FreeCAD.Vector(120, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
```

Ajoutez un volume avec le numéro d\'élément.


```python
elempyra13 = Fem.FemMesh()
nodes = pyra13.Nodes
for n in nodes   *
    elempyra13.addNode(nodes[n].x, nodes[n].y, nodes[n].z, n)

elempyra13.addVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 88)
obj = App.ActiveDocument.addObject("Fem   *   *FemMeshObject", "elempyra13")
obj.FemMesh = elempyra13
obj.Placement.Base = FreeCAD.Vector(320, 0, 0)
obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
print(elempyra13.Volumes)
```

## Exemples de script pour les groupes 

Voir par exemple <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=37304&start=20#p318823>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Mesh/fr
