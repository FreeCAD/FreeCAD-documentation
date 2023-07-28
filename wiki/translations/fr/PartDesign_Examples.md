# PartDesign Examples/fr
{{TOCright}}

## Introduction

Parfois, vous avez besoin d\'un indice de la puissance d\'un outil, sans trop d\'explications.

Il s\'agit d\'une série d\'exemples qui peuvent être réalisés avec certains outils. Pour des explications détaillées, consultez les descriptions des outils et cherchez des tutoriels sur le web.



## Protrusion

<img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) est un outil permettant de créer des objets Protrusion, qui sont des objets prismatiques tels que des objets d\'extrusion, des cylindres, des cônes, des cubes, des coins \...

Chaque objet est basé sur un contour (jaune), qui définit la forme de la section transversale (de préférence réalisé avec l\'[atelier Sketcher](Sketcher_Workbench/fr.md)).

Le contour est tiré le long d\'une direction (extrudé) pour donner à l\'objet une épaisseur ou une longueur.
Par défaut, il s\'agit de la direction normale du plan contenant le contour (plan d\'esquisse). Il est possible, en option, de modifier la direction en éditant les paramètres dans le panneau des propriétés ou en sélectionnant une ligne droite séparée (blanche).


<div class="mw-collapsible mw-collapsed">

**Galerie**


<div class="mw-collapsible-content toccolours">



### Primitives prismatiques 

++++
| **Cylindre**          | <img alt="Cylinder/fr" src=images/PartDesign_ExamplePad-01.png  style="width:200px;">           | -   Contour : **cercle**.                                         |
++++
| **Cube**              | <img alt="Cube/fr" src=images/PartDesign_ExamplePad-02.png  style="width:200px;">                   | -   Contour : **carré**.                                          |
|                       |                                                                                   | -   Longueur d\'extrusion : égale à la longueur des bords carrés. |
++++
| **Cuboïde**           | <img alt="Cuboid/fr" src=images/PartDesign_ExamplePad-03.png  style="width:200px;">               | -   Contour : **rectangle**.                                      |
++++
| **Prisme régulier**   | <img alt="Regular Prism/fr" src=images/PartDesign_ExamplePad-04.png  style="width:200px;"> | -   Contour : **hexagone**.                                       |
++++
| **‎Pyramide            | <img alt="Wedge/fr" src=images/PartDesign_ExamplePad-05.png  style="width:200px;">                 | -   Contour : **triangle**.                                       |
| tronquée**            |                                                                                   |                                                                   |
++++



### Profils prismatiques 

++++
| **Profil en L** | <img alt="Profil en L" src=images/PartDesign_ExamplePad-06.png  style="width:200px;"> | -   Contour : forme en **L**.                                          |
|                 |                                                                         |                                                                        |
|                 |                                                                         | :                                                                      |
++++
| **Profil en C** | <img alt="Profil en C" src=images/PartDesign_ExamplePad-07.png  style="width:200px;"> | -   Contour : forme en **C**.                                          |
++++
| **Profil en Z** | <img alt="Profil en Z" src=images/PartDesign_ExamplePad-11.png  style="width:200px;"> | -   Contour : forme en **Z**.                                          |
++++
| **Profil en T** | <img alt="Profil en T" src=images/PartDesign_ExamplePad-09.png  style="width:200px;"> | -   Contour : forme en **T**.                                          |
++++
| **Profil en I** | <img alt="Profil en I" src=images/PartDesign_ExamplePad-10.png  style="width:200px;"> | -   Contour : forme en **I**, avec la largeur de la semelle \< l\'âme. |
++++
| **Profil en H** | <img alt="Profil en H" src=images/PartDesign_ExamplePad-08.png  style="width:200px;"> | -   Contour : forme en **H**, avec la largeur = la hauteur.            |
++++


</div>


</div>



## Balayage additif 

<img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:24px;"> [PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md) est un outil permettant de créer des objets AdditivePipe tels que des objets de balayage, des objets d\'extrusion, des objets de rotation, des cylindres, des cônes, des cubes, des pyramides, des sphères\...

Chaque objet est basé sur au moins deux lignes (réalisées de préférence avec l\'[atelier Sketcher](Sketcher_Workbench/fr.md)) :

-   Un contour (jaune), pour définir la forme de la section transversale.
-   Un chemin (blanc), pour le balayer.

Il n\'est pas difficile de réaliser que certains objets peuvent également être créés avec d\'autres outils, mais auriez-vous deviné la polyvalence de cet outil sans ces exemples ?


<div class="mw-collapsible mw-collapsed">

**Galerie**


<div class="mw-collapsible-content toccolours">



### Objets à balayage circulaire 

++++
| **Sphère**           | <img alt="Sphère" src=images/PartDesign_ExampleSphere-01.png  style="width:200px;">                                      | -   Contour : un **arc de 180°** et une **ligne** reliant les points d\'extrémité.                                                                                                  |
|                      |                                                                                                       | -   Trajectoire : **cercle** complet.                                                                                                                                               |
++++
| **Partie de sphère** | <img alt="Partie de sphère de 240°" src=images/PartDesign_ExampleSphere-02.png  style="width:200px;">  | -   Contour : un **arc de 180°** et une **ligne** reliant les points d\'extrémité.                                                                                                  |
|                      |                                                                                                       | -   Trajectoire : un **arc de cercle de 240°**.                                                                                                                                     |
|                      |                                                                                                       |                                                                                                                                                                                     |
|                      |                                                                                                       | :   Cette fonction peut créer des segments de n\'importe quel angle sauf 180° exactement, car elle a un problème avec le plan de départ et le plan d\'arrivée qui sont coplanaires. |
++++
| **Hémisphère**       | <img alt="Hémisphère" src=images/PartDesign_ExampleSphere-03.png  style="width:200px;">                              | -   Contour : un **arc de 90°** et deux **lignes** perpendiculaires reliant les points d\'extrémité.                                                                                |
|                      |                                                                                                       | -   Trajectoire : un **cercle** complet.                                                                                                                                            |
++++
| **Tore**             | <img alt="Tore" src=images/PartDesign_ExampleTorus-01.png  style="width:200px;">                                           | -   Contour : **cercle** complet.                                                                                                                                                   |
|                      |                                                                                                       | -   Trajectoire : **cercle** complet.                                                                                                                                               |
++++
| **Cône**             | <img alt="Cône" src=images/PartDesign_ExampleTorus-04.png  style="width:200px;">                                           | -   Contour : **triangle** dont une arête est située sur la ligne médiane.                                                                                                          |
|                      |                                                                                                       | -   Trajectoire : **cercle** complet.                                                                                                                                               |
++++
| **Cylindre**         | <img alt="Cylindre" src=images/PartDesign_ExampleTorus-02.png  style="width:200px;">                                   | -   Contour : **rectangle** avec un bord situé sur la ligne médiane.                                                                                                                |
|                      |                                                                                                       | -   Trajectoire : **cercle** complet.                                                                                                                                               |
++++
| **Balayage**         | <img alt="Balayage (Cylindre creux)" src=images/PartDesign_ExampleTorus-03.png  style="width:200px;"> | -   Contour : **rectangle**.                                                                                                                                                        |
| Cylindre creux       |                                                                                                       | -   Trajectoire : **cercle** complet                                                                                                                                                |
++++



### Objets prismatiques 

Objets à balayage droit

++++
| **Cylindre**              | <img alt="Cylindre" src=images/PartDesign_ExamplePrism-01.png  style="width:200px;">                                  | -   Contour : **cercle**.                                                       |
|                           |                                                                                                      | -   Chemin : **ligne** droite.                                                  |
++++
| **Cube**                  | <img alt="Cube" src=images/PartDesign_ExamplePrism-02.png  style="width:200px;">                                          | -   Contour : **carré**.                                                        |
|                           |                                                                                                      | -   Trajectoire : **ligne** droite, de la même longueur que les bords du carré. |
++++
| **Cuboïde**               | <img alt="Cuboïde" src=images/PartDesign_ExamplePrism-03.png  style="width:200px;">                                    | -   Contour : **rectangle**.                                                    |
|                           |                                                                                                      | -   Trajectoire : **ligne** droite.                                             |
++++
| **Pyramide tronquée**     | <img alt="Pyramide tronquée" src=images/PartDesign_ExamplePrism-04.png  style="width:200px;">                | -   Contour : **triangle**.                                                     |
|                           |                                                                                                      | -   Trajectoire : **ligne** droite.                                             |
++++
| **Prisme** régulier       | <img alt="Prisme régulier" src=images/PartDesign_ExamplePrism-05.png  style="width:200px;">                    | -   Contour : **hexagone** régulier.                                            |
|                           |                                                                                                      | -   Trajectoire : **ligne** droite.                                             |
++++
| Prisme en forme d\'étoile | <img alt="Prisme en forme d\'étoile" src=images/PartDesign_ExamplePrism-06.png  style="width:200px;"> | -   Contour : **forme régulière d\'étoile**.                                    |
|                           |                                                                                                      | -   Trajectoire : **ligne** droite.                                             |
++++
| Poutre en I               | <img alt="Poutre en I" src=images/PartDesign_ExamplePrism-07.png  style="width:200px;">                            | -   Contour : **section de poutre**                                             |
|                           |                                                                                                      | -   Trajectoire : **ligne** droite.                                             |
++++



### Objets coniques 

++++
| **Cône**          | <img alt="Cône" src=images/PartDesign_ExampleConic-01.png  style="width:200px;">                           | -   Contours : la base : **cercle** complet, le sommet : **point**.    |
|                   |                                                                                       | -   Trajectoire : **ligne** droite.                                    |
|                   |                                                                                       |                                                                        |
|                   |                                                                                       | :   (Le point d\'extrémité est un point final d\'une ligne auxiliaire) |
++++
| **Pyramide**      | <img alt="Pyramide" src=images/PartDesign_ExampleConic-02.png  style="width:200px;">                   | -   Contours : la base : **carré**, le dessus : **point**.             |
|                   |                                                                                       | -   Trajectoire : **ligne** droite.                                    |
|                   |                                                                                       |                                                                        |
|                   |                                                                                       | :   (Le point d\'extrémité est un point final d\'une ligne auxiliaire) |
++++
| Pyramide inclinée | <img alt="Pyramide inclinée" src=images/PartDesign_ExampleConic-03.png  style="width:200px;"> | -   Contours : la base : **carré**, le dessus : **point**.             |
|                   |                                                                                       | -   Trajectoire : **ligne** droite.                                    |
|                   |                                                                                       |                                                                        |
|                   |                                                                                       | :   (Le point d\'extrémité est le point final de la trajectoire)       |
++++



### Objets à balayage courbe 

++++
| **Tuyau**                | <img alt="Tuyau" src=images/PartDesign_ExampleSweep-01.png  style="width:200px;">                 | -   Contour : 2 **cercles** concentriques.                                |
| (Tube)                   |                                                                               | -   Trajectoire : une **ligne** courbe.                                   |
++++
| **Tuyau** carré          | <img alt="**Tuyau** carré" src=images/PartDesign_ExampleSweep-02.png  style="width:200px;"> | -   Contour : 2 **carrés** concentriques.                                 |
|                          |                                                                               | -   Trajectoire : une **ligne** courbe.                                   |
++++
| **Ligne**                | <img alt="Ligne" src=images/PartDesign_ExampleSweep-04.png  style="width:200px;">                 | -   Contour : **cercle**.                                                 |
|                          |                                                                               | -   Trajectoire : une **ligne** courbe.                                   |
++++
| Cornet                   | <img alt="Cornet" src=images/PartDesign_ExampleSweep-03.png  style="width:200px;">               | -   Contours : la base : **cercle**, le dessus : **cercle** (plus petit). |
|                          |                                                                               | -   Trajectoire : une **ligne** courbe.                                   |
++++
| Légendaire **clé Allen** | <img alt="Clé Allen" src=images/PartDesign_ExampleSweep-05.png  style="width:200px;">         | -   Contours : **hexagone**.                                              |
|                          |                                                                               | -   Trajectoire : une **ligne** courbe.                                   |
++++



### Objets spiralés et hélicoïdaux 

++++
| Ressort hélicoïdal     | <img alt="Ressort" src=images/PartDesign_ExampleSpring-01.png  style="width:200px;">                           | -   Contour : **cercle**.                                                                                                 |
|                        |                                                                                              | -   Trajectoire : <img alt="" src=images/Part_Helix.svg  style="width:16px;"> [Part Hélice](Part_Helix/fr.md).               |
++++
| Spirale                | <img alt="Ressort de balancier" src=images/PartDesign_ExampleSpring-03.png  style="width:200px;"> | -   Contour : **rectangle**.                                                                                              |
| Ressort de balancier   |                                                                                              | -   Trajectoire : <img alt="" src=images/Part_Spiral.svg  style="width:16px;"> [Part Spirale](Part_Spiral/fr.md).           |
++++
| **Ressort de volute**, | <img alt="Ressort de volute" src=images/PartDesign_ExampleSpring-04.png  style="width:200px;">       | -   Contour : **rectangle**.                                                                                              |
| Ressort conique        |                                                                                              | -   Trajectoire : <img alt="" src=images/Part_Helix.svg  style="width:16px;"> [Part Hélice](Part_Helix/fr.md) avec un angle. |
++++



### Objets de transition 

++++
| De carré à cercle en passant par la trajectoire | <img alt="Objet de transition incurvé" src=images/PartDesign_ExampleTrans-01.png  style="width:200px;"> | -   Contours : la base : **carré**, le dessus : **cercle**.     |
|                                                 |                                                                                                           | -   Trajectoire : **ligne** courbée.                            |
++++
| De carré à cercle directement                   | <img alt="Objet de transition droit" src=images/PartDesign_ExampleTrans-02.png  style="width:200px;">     | -   Contours : la base : **carré**, le dessus : **cercle**.     |
|                                                 |                                                                                                           | -   Trajectoire : **ligne** droite.                             |
++++
| De polygone à étoile                            | <img alt="De polygone à étoile" src=images/PartDesign_ExampleTrans-03.png  style="width:200px;">               | -   Contours : la base : **pentagone**, le dessus : **étoile**. |
|                                                 |                                                                                                           | -   Trajectoire : **ligne** droite.                             |
++++

### Options



#### Transition d\'angle 

Une polyligne peut être utilisée comme chemin, et la propriété **Transition** influence la forme des coins.

La transformation nécessite une attention particulière car elle peut produire des zones plates où l\'épaisseur est de 0.

++++
| Paramètre         | Vue iso                                                                                                     | Vue de dessus                                                                                                           |
+===================+=============================================================================================================+=========================================================================================================================+
| **Transformé**    | <img alt="Vue iso de la transformée" src=images/PartDesign_ExampleProperty-01.png  style="width:200px;">    | <img alt="Vue de dessus de la transformée" src=images/PartDesign_ExampleProperty-02.png  style="width:200px;">    |
|                   |                                                                                                             |                                                                                                                         |
|                   | :   Les coins intérieurs et extérieurs sont des bords.                                                      | :   La forme de base ne suit pas l\'orientation de la ligne.                                                            |
++++
| **Angle droit**   | <img alt="Vue iso de l\'angle droit" src=images/PartDesign_ExampleProperty-03.png  style="width:200px;">     | <img alt="Vue de dessus de l\'angle droit" src=images/PartDesign_ExampleProperty-04.png  style="width:200px;">     |
|                   |                                                                                                             |                                                                                                                         |
|                   | :   Les coins intérieurs et extérieurs sont des bords.                                                      | :   La forme de base suit l\'orientation de la ligne.                                                                   |
++++
| **Angle arrondi** | <img alt="Vue iso de l\'angle arrondi" src=images/PartDesign_ExampleProperty-05.png  style="width:200px;"> | <img alt="Vue de dessus de l\'angle arrondi" src=images/PartDesign_ExampleProperty-06.png  style="width:200px;"> |
|                   |                                                                                                             |                                                                                                                         |
|                   | :   Les coins situés en dehors de la trajectoire sont arrondis.                                             | :   La forme de base suit l\'orientation de la ligne.                                                                   |
++++



#### Mode d\'orientation 

++++
| Paramètre      | Vue iso                                                                                                          | Vue de dessus                                                                                                           |
+================+==================================================================================================================+=========================================================================================================================+
| **Standard**   | <img alt="Vue iso standard" src=images/PartDesign_ExampleProperty-07.png  style="width:200px;">                           | <img alt="Vue de dessus standard" src=images/PartDesign_ExampleProperty-08.png  style="width:200px;">                      |
|                |                                                                                                                  |                                                                                                                         |
|                | :   L\'emplacement et l\'orientation suivent la trajectoire.                                                     | :   (Si l\'objet est tordu d\'une manière inattendue, essayez Frenet)                                                   |
++++
| **Figé**       | <img alt="Vue iso figée" src=images/PartDesign_ExampleProperty-09.png  style="width:200px;">                                 | <img alt="Vue de dessus figée" src=images/PartDesign_ExampleProperty-10.png  style="width:200px;">                            |
|                |                                                                                                                  |                                                                                                                         |
|                | :   L\'emplacement suit la trajectoire et l\'orientation reste la même que la forme de base.                     | :   Cela a tendance à provoquer des auto-intersections qui entraînent d\'autres erreurs : une face fantôme dans ce cas. |
++++
| **Frenet**     | <img alt="Vue iso de Frenet" src=images/PartDesign_ExampleProperty-07.png  style="width:200px;">                         | <img alt="Vue de dessus de Frenet" src=images/PartDesign_ExampleProperty-08.png  style="width:200px;">                    |
|                |                                                                                                                  |                                                                                                                         |
|                | :   L\'emplacement et l\'orientation suivent la trajectoire, sur la base d\'un algorithme différent du standard. | :   La forme de base suit l\'orientation de la ligne.                                                                   |
++++
| **Auxiliaire** |                                                                                                                  |                                                                                                                         |
++++
| **Binormale**  |                                                                                                                  |                                                                                                                         |
++++


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Examples/fr
