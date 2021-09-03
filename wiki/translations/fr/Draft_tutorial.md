


{{TutorialInfo/fr
|Topic= Drafting
|Level= Débutant
|Time= 30 minutes
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei] et vocx
|FCVersion=0.19
|Files=[https://forum.freecadweb.org/viewtopic.php?f=36&t=43651 Draft tutorial updated]
}}

## Introduction

Ce tutoriel a été écrit à l\'origine par Drei et a été écrit et illustré par vocx.

Ce tutoriel est destiné à présenter au lecteur le flux de travail de base de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Atelier Draft](Draft_Workbench/fr.md).

Le lecteur pratiquera:

-   création de lignes, d\'arcs et de polygones
-   l\'utilisation de plans de travail
-   la création de dimensions, de texte et de formes à partir de texte
-   la création d\'un dessin technique

Ce tutoriel utilise la notation {{Value|(x, y, z)}} pour désigner les coordonnées nécessaires pour définir des points dans un objet. L\'unité par défaut est le millimètre {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width:" height="400px;"> 
*Dessin final comprenant divers objets Draft.*

## Installation

1\. Ouvrez FreeCAD, créez un nouveau document vide avec **Fichier → <img src=images/Std_New.svg style="width:16px"> [Nouveau](Std_New/fr.md)**.

:   1.1. Basculez vers l\'<img src=images/Workbench_Draft.svg style="width:atelier Draft](Draft_Workbench/fr.md) depuis le [sélecteur d\'atelier](Std_Workbench/fr.md) ou le menu **Affichage → Atelier → [16px"> Draft**.
:   1.2. Assurez-vous de comprendre comment utiliser l\'[éditeur de propriétés](property_editor/fr.md), en particulier les onglets **Données** et **Affichage** pour modifier les propriétés. Lors de la modification des propriétés, vous devrez peut-être effectuer une action **<img src="images/Std_Refresh.svg" width=16px> [Std Rafraîchir](Std_Refresh/fr.md)** pour voir le résultat dans la [vue 3D](3D_view/fr.md).
:   1.3. Comme les objets Draft sont des formes planes, ils sont mieux vus du dessus. Utilisez **<img src=images/Std_ViewTop.svg style="width:16px"> [vue de dessus](Std_ViewTop/fr.md)** pour définir la [Vue 3D](3D_view/fr.md).
:   1.4. Bien qu\'elle ne soit pas utilisée dans ce tutoriel, la grille Draft est utile pour positionner des éléments géométriques. Utilisez **<img src=images/Draft_SelectPlane.svg style="width:16px"> <img src=images/Draft_ToggleGrid.svg style="width:Plan de travail](Draft_SelectPlane/fr.md)** pour définir à la fois le plan de travail et la grille, puis affichez et masquez la grille avec **[16px"> [Visibilité de la grille](Draft_ToggleGrid/fr.md)**.

## Verrouillage de la barre d\'outils 

2\. L\'[Draft Accrochage](Draft_Snap/fr.md) est normalement activée lorsque vous basculez vers [atelier Draft](Draft_Workbench/fr.md).

:   2.1. Pour vous assurer qu\'il est toujours là, allez dans [Draft Préférences](Draft_Preferences/fr.md), **Edition → Préférences → Draft → onglet: Grille et accrochage**.
:   2.2. Vérifiez que la barre d\'outils **Montrer la barre d\'outils d\'accrochage** est active.

Vous pouvez aussi changer la visibilité et les propriétés de la grille Draft dans cette même fenêtre.

## Plans de travail 

La plupart des objets Draft sont des formes planes, ils sont donc naturellement basés sur un **plan de travail**. Un plan de travail peut être l\'un des plans de coordonnées globaux principaux XY, XZ et YZ, ou il peut s\'agir d\'un plan qui leur est parallèle avec un décalage positif ou négatif, ou il peut s\'agir d\'un plan défini par la face d\'un objet solide.

3\. Appuyez sur **<img src=images/Draft_SelectPlane.svg style="width:16px"> <img src=images/Draft_SelectPlane.svg style="width:SelectPlane](Draft_SelectPlane/fr.md)** ou allez dans le menu **Utilities → [16px"> [Select plane](Draft_SelectPlane/fr.md)** pour ouvrir le plan de travail [Panneau des tâches](Task_panel/fr.md).

:   3.1. Appuyez sur **<img src=images/Std_ViewTop.svg style="width:16px"> Top (XY)**.

Avant d\'appuyer sur le bouton, vous pouvez également modifier la valeur du décalage en millimètres, ainsi que l\'espacement de la grille, les lignes principales et le rayon d\'accrochage.

## Lignes et arcs 

4\. Nous allons créer des arcs et des lignes.

:   4.1. Appuyez sur **<img src=images/Draft_Arc.svg style="width:16px"> [Arc](Draft_Arc/fr.md)**.
:   4.2. Définissez **Center** sur {{Value|(0, 0, 0)}} et appuyez sur **Validez**.
:   4.3. Réglez **Radius** sur {{Value|30 mm}} et appuyez sur **Validez**.
:   4.4. Réglez **Start angle** sur {{Value|60.0°}} et appuyez sur **Validez**.
:   4.5. Réglez **Aperture angle** sur {{Value|60.0°}} et appuyez sur **Validez**.
:   4.6. Répétez la même procédure pour un deuxième arc avec un rayon de {{Value|25 mm}}, les autres propriétés sont les mêmes.

5\. Nous allons maintenant créer un profil fermé en liant les arcs avec des lignes.

:   5.1. Appuyez sur **<img src=images/Draft_Line.svg style="width:16px"> [Ligne](Draft_Line/fr.md)**.
:   5.2. Dans la <img src=images/Draft_Snap_Lock.svg style="width:Barre d\'outils Accrochage](Draft_Snap/fr.md), assurez-vous que **[16px"> <img src=images/Draft_Snap_Endpoint.svg style="width:Activer/désactiver l'accrochage](Draft_Snap_Lock/fr.md)** est actif et que **[16px"> [Terminaison](Draft_Snap_Endpoint/fr.md)** également. Lorsque vous déplacez le pointeur sur l\'arc et à proximité de l\'un de ses extrémités, l\'icône <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> [Terminaison](Draft_Snap_Endpoint/fr.md) doit apparaître. De plus, le point cible est mis en valeur par un grand point blanc. Cliquez pour sélectionner ce point.
:   5.3. Déplacez le pointeur vers l\'extrémité la plus proche de l\'autre arc pour lier les deux arcs ensemble.
:   5.4. Répétez le processus pour l\'autre côté de l\'arc pour fermer le profil.

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width:" height="400px;"> 
*Profil fermé créé par deux arcs et deux lignes.*

## Fusion ou composition 

Nous avons maintenant plusieurs objets dans la [Vue en arborescence](Tree_view/fr.md) qui forment un profil fermé. Cependant, ce profil est toujours composé d\'objets déconnectés. Chacun d\'eux peut être édité et déplacé indépendamment des autres. Il est possible de continuer à travailler avec les éléments de cette manière mais il est également possible de les fusionner en un seul objet.

6a. Notez que fusionner les objets en un seul objet créera un objet qui n\'est plus paramétrique, de sorte que leurs propriétés ne peuvent plus être modifiées.

:   6a.1. Sélectionnez les quatre objets dans la [Vue en arborescence](Tree_view/fr.md) ou en maintenant **Ctrl** et en les sélectionnant dans la [Vue 3D](3D_view/fr.md).
:   6a.2. Une fois ces objets sélectionnés, cliquez sur **<img src=images/Draft_Upgrade.svg style="width:16px"> [Mettre à niveau](Draft_Upgrade/fr.md)**.
:   6a.3. Cela mettra à niveau les quatre objets en un seul {{Value|Wire}}.

6b. Si vous souhaitez conserver la nature paramétrique des objets, vous pouvez créer un composé à la place.

:   6b.1. Basculez vers <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md).
:   6b.2. Une fois ces objets sélectionnés, cliquez sur **<img src=images/Part_Compound.svg style="width:16px"> [Part Composé](Part_Compound/fr.md)**.

## Rectangles, cercles et polygones 

7\. Nous allons dessiner un cadre rectangulaire. (retournez vers l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md).)

:   7.1. Appuyez sur **<img src=images/Draft_Rectangle.svg style="width:16px"> [Rectangle](Draft_Rectangle/fr.md)**.
:   7.2. Entrez les valeurs du premier point {{Value|(-100, -60, 0)}} et appuyez sur **Validez**.
:   7.3. Assurez-vous que l\'option **Relative** n\'est pas cochée, car nous utiliserons des unités absolues. Vous pouvez appuyer sur **R** sur le clavier pour activer et désactiver rapidement cette option.
:   7.4. Entrez les valeurs du deuxième point {{Value|(140, 90, 0)}} et appuyez sur **Validez**.

Un rectangle est créé. Allez dans l\'[Éditeur de propriétés](Property_editor/fr.md) pour modifier ses propriétés. Si vous ne voulez pas que le rectangle crée une face, définissez {{PropertyData/fr|Make Face}} sur `False`. Si vous voulez créer une face mais ne voyez que les fils de cet objet, conservez {{PropertyData/fr|Make Face}} sur `True` mais réglez {{PropertyView/fr|Display Mode}} sur {{Value|Wireframe}}.

8\. Nous allons dessiner un cercle.

:   8.1. Appuyez sur **<img src=images/Draft_Circle.svg style="width:16px"> [Cercle](Draft_Circle/fr.md)**.
:   8.2. Entrez les valeurs du centre {{Value|(0, 0, 0)}} et appuyez sur **Validez**.
:   8.3. Définissez le rayon sur {{value|15 mm}} et appuyez sur **Validez**.

9\. Nous allons dessiner un polygone régulier.

:   9.1. Appuyez sur **<img src=images/Draft_Polygon.svg style="width:16px"> [Polygone](Draft_Polygon/fr.md)**.
:   9.2. Entrez les valeurs du centre {{Value|(0, 0, 0)}} et appuyez sur **Validez**.
:   9.3. Définissez le nombre de côtés sur {{Value|6}} et appuyez sur **Validez**.
:   9.4. Définissez le rayon sur {{Value|50 mm}} et appuyez sur **Validez**.

Encore une fois, vous pouvez modifier les propriétés {{PropertyData/fr|Make Face}} et {{PropertyView/fr|Display Mode}} dans l\'[Éditeur de propriétés](Property_editor/fr.md) si vous le souhaitez.

Le rectangle, le cercle, le polygone et la plupart des autres objets créés avec l\'[atelier Draft](Draft_Workbench/fr.md) partagent de nombreuses données et propriétés d\'affichage car ils sont dérivés de la même classe de base, [Part Part2DObject](Part_Part2DObject/fr.md).

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width:" height="400px;"> 
*Rectangle, cercle et polygone ajoutés.*

## Réseaux

Les réseaux sont utilisés pour répliquer un objet plusieurs fois dans une direction orthogonale (X, Y, Z) autour d\'un axe de révolution ou le long d\'une trajectoire.

10\. Nous allons créer un réseau polaire.

:   10.1. Sélectionnez l\'objet {{Value|Wire}} qui a été précédemment créé avec l\'outil **<img src=images/Draft_Upgrade.svg style="width:16px"> <img src=images/Part_Compound.svg style="width:Mettre à niveau](Draft_Upgrade/fr.md)** ou {{Value|Compound}} créé avec l\'outil **[16px"> [Part Composé](Part_Compound/fr.md)**.
:   10.2. Appuyez sur **<img src=images/Draft_PolarArray.svg style="width:16px"> [Réseau polaire](Draft_PolarArray/fr.md)**.
:   10.3. Ajustez l\'angle polaire sur {{Value|360°}}.
:   10.4. Définissez le nombre d\'éléments sur {{Value|4}}.
:   10.5. Saisissez les valeurs du centre de rotation {{Value|(0, 0, 0)}} et appuyez sur **Validez**.

L\'objet réseau montre des copies de l\'objet autour de l\'origine.

<img alt="" src=images/03_Dr01_Draft_PolarArray.png  style="width:" height="400px;"> 
*Réseau polaire du petit profil centré autour de l'origine.*

## Cotes

Les cotes linéaires fonctionnent mieux lorsque vous utilisez les méthodes d\'[Accrochage](Draft_Snap/fr.md) appropriées pour sélectionner les points et les arêtes à mesurer. Cependant, ils peuvent également être créés en spécifiant des coordonnées absolues.

11\. Créez des dimensions pour les différents objets.

:   11.1. Appuyez sur **<img src=images/Draft_Dimension.svg style="width:16px"> [Dimension](Draft_Dimension/fr.md)**.
:   11.2. Choisissez le premier point. Dans ce tutoriel, le premier point sera toujours l\'origine {{Value|(0, 0, 0)}}.
:   11.3. Dans la <img src=images/Draft_Snap_Lock.svg style="width:Barre d\'outils Accrochage](Draft_Snap/fr.md), assurez-vous que **[16px"> <img src=images/Draft_Snap_Midpoint.svg style="width:Bascule l'accrochage](Draft_Snap_Lock/fr.md)** est actif et que **[16px"> [Milieu](Draft_Snap_Midpoint/fr.md)** également. Lorsque vous déplacez le pointeur vers le bord supérieur du polygone, l\'icône <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Milieu](Draft_Snap_Midpoint/fr.md) doit apparaître; cliquez pour sélectionner ce point.
:   11.4. Déplacez le curseur vers la droite pour spécifier l\'emplacement de la dimension, puis cliquez pour définir la position finale, autour de {{Value|(100, 20, 0)}}. La cote affichera automatiquement la valeur de longueur mesurée entre les deux points.
:   11,5. Sélectionnez l\'objet dimension dans la [Vue en arborescence](Tree_view/fr.md) et dans l\'[Éditeur de propriétés](Property_editor/fr.md) remplacez {{PropertyView/fr|Font Size}} par {{Value|6 mm}}, définissez {{PropertyView/fr|Ext Lines}} à {{Value|45 mm}} et {{PropertyView/fr|Show Unit}} à `False`.

12\. Répétez le processus pour les deux arcs du profil fermé. Le premier point de la mesure sera toujours l\'origine et le second point utilisera le <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Milieu](Draft_Snap_Midpoint/fr.md) de l\'arc.

13\. Répétez le processus pour le cercle situé au centre. Le premier point de la mesure sera toujours l\'origine. Pour sélectionner le deuxième point, assurez-vous que **<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Bascule de l'accrochage](Draft_Snap_Lock/fr.md)** est actif et que seul **[16px ](File:Draft_Snap_Angle.svg.md) [Angle](Draft_Snap_Angle/fr.md)** également. Lorsque vous déplacez le pointeur vers le haut du cercle, l\'icône <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> [Angle](Draft_Snap_Angle/fr.md) doit apparaître. Cliquez pour sélectionner ce point. Déplacez ensuite le curseur vers la droite et cliquez pour fixer la cote.

N\'oubliez pas d\'ajuster {{PropertyView/fr|Font Size}} et d\'autres propriétés pour voir correctement la dimension.

<img alt="" src=images/04_Dr01_Draft_Dimension.png  style="width:" height="400px;"> 
*Cotes qui mesurent la distance verticale entre l'origine et le haut du cercle, des arcs et du polygone.*

## Textes et Formes à partir de texte 

14\. Les objets texte sont de simples figures planes qui sont créées dans la [Vue 3D](3D_view/fr.md) mais qui n\'ont pas de véritable \"[Forme](Shape/fr.md)\" sous jacente. Cela signifie qu\'ils ne peuvent pas être utilisés dans des opérations complexes avec des formes telles que des extrusions ou des opérations booléennes.

:   14.1. Appuyez sur **<img src=images/Draft_Text.svg style="width:16px"> [Texte](Draft_Text/fr.md)**.
:   14.2. Sélectionnez le point de référence dans la <img src=images/Draft_Snap_Lock.svg style="width:Vue 3D](3D_view/fr.md). Dans la [Barre d\'outils d\'accrochage](Draft_Snap/fr.md), assurez-vous que **[16px"> <img src=images/Draft_Snap_Midpoint.svg style="width:Bascule l'accrochage](Draft_Snap_Lock/fr.md)** est actif et que **[16px"> [Milieu](Draft_Snap_Midpoint/fr.md)** également. Déplacez le pointeur vers le bord supérieur de l\'arc le plus élevé, de sorte que l\'icône <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Milieu](Draft_Snap_Midpoint/fr.md) s\'affiche. Cliquez pour sélectionner ce point.
:   14.3. Entrez le **Text** souhaité et appuyez une fois sur **Validez** pour commencer une nouvelle ligne; ajoutez plus de lignes de texte au besoin.
:   14.4. Lorsque vous êtes prêt à terminer l\'édition, appuyez deux fois sur **Validez**.
:   14,5. Sélectionnez l\'objet texte dans [tree view](tree_view.md), et dans l\'[Éditeur de propriétés](Property_editor/fr.md) remplacez {{PropertyView/fr|Font Size}} par {{Value|6 mm}} et {{PropertyView/fr|Justification}} à {{Value|Center}}.

15\. Les objets ShapeString sont des formes constituées de fils primitifs qui suivent les lignes indiquées par une certaine police. Cela signifie que ces objets ont une vraie \"[Forme](Shape/fr.md)\" sous jacente et peuvent donc être utilisés dans des opérations complexes comme les extrusions et les opérations booléennes.

:   15.1. Appuyez sur **<img src=images/Draft_ShapeString.svg style="width:16px"> [Forme à partir de texte](Draft_ShapeString/fr.md)**.
:   15.2. Déplacez le pointeur vers l\'emplacement souhaité dans la [Vue 3D](3D_view/fr.md) au-dessus du polygone régulier, et cliquez une fois. Cela corrigera le point de base du ShapeString. Les coordonnées peuvent également être entrées manuellement, par exemple, {{Value|(-20, 65, 0)}}.
:   15.3. Entrez la **String** (chaîne de caractère)souhaitée et choisissez la **Height** (hauteur) souhaitée.
:   15.4. S\'il n\'y a pas de fichier de police par défaut, vous devez cliquer sur les points de suspension **...** pour ouvrir une boîte de dialogue pour choisir l\'emplacement de la police dans le système.
:   15.5. Lorsqu\'un fichier de police valide a été spécifié, vous pouvez cliquer sur **OK** ou appuyer sur **Validez**.

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:" height="400px;"> 
*Objets Text et ShapeString ajoutés.*

Pour extruder des lettres et les graver sur des solides, voir le [Draft Tutoriel Forme à partir de texte](Draft_ShapeString_tutorial/fr.md).

## Création de dessins techniques 

Dans l\'état actuel des choses, les objets que nous avons créés peuvent être sauvegardés, exportés vers d\'autres formats [SVG](SVG/fr.md) ou [DXF](DXF/fr.md) ou imprimés.

Si vous le souhaitez, vous pouvez créer un dessin technique pour afficher ces objets avec des informations supplémentaires comme un cadre.

Avant de faire quoi que ce soit, masquez la grille Draft en appuyant sur **<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Bascule de la grille](Draft_ToggleGrid/fr.md)**.

16\. Basculez vers l\' <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md).

:   16.1. Créez une page standard en appuyant sur **<img src=images/TechDraw_PageDefault.svg style="width:16px"> [TechDraw Page par défaut](TechDraw_PageDefault/fr.md)**.
:   16.2. Dans la <img src=images/TechDraw_ActiveView.svg style="width:Vue en arborescence](Tree_view/fr.md), sélectionnez tous les objets créés, à l\'exception de la page, puis appuyez sur **[16px"> [TechDraw Vue active](TechDraw_ActiveView/fr.md)**. Appuyez sur **OK** avec les options par défaut; la création de la vue dans la page peut prendre quelques secondes.
:   16.3. La sélection de l\'objet Page dans la [Vue en arborescence](Tree_view/fr.md) affichera automatiquement la page dans la fenêtre principale. Avec la page sélectionnée, allez dans l\'[Éditeur de propriétés](Property_editor/fr.md) et changez {{PropertyData/fr|Scale}} en {{Value|0.75}}.
:   16.4. Développez l\'objet Page dans la [Vue en arborescence](Tree_view/fr.md) pour sélectionner l\'objet ActiveView. Avec cette vue sélectionnée, allez dans [property editor](Property_editor.md) et changez {{PropertyData/fr|Scale Type}} en {{Value|Page}}.
:   16.5. Recalculez le modèle en utilisant **<img src=images/Std_Refresh.svg style="width:16px"> [Rafraîchir](Std_Refresh/fr.md)** ou en appuyant sur **F5**.
:   16.6. Cachez les cadres des objets en appuyant sur **<img src=images/TechDraw_ToggleFrame.svg style="width:16px"> [TechDraw Bascule des cadres](TechDraw_ToggleFrame/fr.md)**.

En savoir plus sur l\'[atelier TechDraw](TechDraw_Workbench/fr.md) en lisant le [TechDraw: Tutoriel d\'introduction](Basic_TechDraw_Tutorial/fr.md).

<img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:" height="400px;"> 
*Page TechDraw avec une projection des formes créées avec l'atelier Draft.*

TechDraw fonctionne mieux avec les objets qui ont une [Part TopoShape](Part_TopoShape/fr.md). Étant donné que certains objets de Draft, tels que [Draft Textes](Draft_Text/fr.md) et [Draft Dimensions](Draft_Dimension/fr.md), n\'ont pas de telles \"[formes](Shape/fr.md)\", certaines opérations de TechDraw ne fonctionnent pas avec ces éléments.

Les outils tels que **<img src=images/TechDraw_ActiveView.svg style="width:16px"> <img src=images/TechDraw_DraftView.svg style="width:TechDraw Vue active](TechDraw_ActiveView/fr.md)**, **[16px"> <img src=images/TechDraw_ArchView.svg style="width:TechDraw Vue Draft](TechDraw_DraftView/fr.md)** et **[16px"> [TechDraw Vue architecturale](TechDraw_ArchView/fr.md)** fonctionnent en recevant une image SVG interne générée par les fonctions Draft internes; par conséquent, TechDraw n\'a pas beaucoup de contrôle sur la façon dont ces vues sont affichées. Une plus grande intégration de Draft et TechDraw est un travail en cours.

## Remarques finales 

L\'[atelier Draft](Draft_Workbench/fr.md) est à bien des égards similaire au [atelier Sketcher](Sketcher_Workbench/fr.md), car tous deux sont destinés à produire des formes 2D. La principale différence réside dans la façon dont chaque atelier gère les systèmes de coordonnées et la façon dont les objets sont positionnés. Dans Draft, les objets sont librement positionnés dans le système de coordonnées global, en alignant généralement leurs points sur une grille ou sur d\'autres objets. Dans Sketcher, un \"[objet sketch](Sketch/fr.md)\" définit un système de coordonnées local qui sert de référence pour tous les éléments géométriques de cette esquisse. De plus, l\'esquisse s\'appuie sur des «contraintes» pour définir la position finale de ses points.

-   L\'[atelier Draft](Draft_Workbench/fr.md) est destiné aux dessins 2D qui peuvent être dessinés sur une grille. L\'[atelier Arch](Arch_Workbench/fr.md) s\'appuie principalement sur les outils définis dans l\'[atelier Draft](Draft_Workbench/fr.md).

-   L\'[atelier Sketcher](Sketcher_Workbench/fr.md) est destiné aux dessins 2D qui nécessitent des relations précises entre ses points. Il ne s\'appuie pas sur une grille mais sur des règles de positionnement (contraintes) pour déterminer où seront placés les points et les arêtes. L\'[atelier Sketcher](Sketcher_Workbench/fr.md) est principalement utilisé avec l\'[atelier PartDesign](PartDesign_Workbench/fr.md) pour la création de solides [corps](Body/fr.md).

-   Il est possible de transformer un objet Draft en <img src=images/Draft_Draft2Sketch.svg style="width:Esquisse](Sketch/fr.md) et inversement en utilisant l\'outil **[16px"> [Draft Draft vers esquisse](Draft_Draft2Sketch/fr.md)**.


{{Tutorials navi

}}  
