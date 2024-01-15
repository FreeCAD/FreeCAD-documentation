---
 GuiCommand:
   Name: Draft SelectPlane
   Name/fr: Draft Plan de travail
   MenuLocation: Utilitaires , Sélectionner un plan
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   Shortcut: **W** **P**
   SeeAlso: Draft_WorkingPlaneProxy/fr
---

# Draft SelectPlane/fr

## Description

La commande <img alt="" src=images/Draft_SelectPlane.svg  style="width:24px;"> **Draft Plan de travail** définit le plan de travail en cours sous Draft. C\'est le plan dans la [vue 3D](3D_view/fr.md) où les nouveaux objets de [Draft](Draft_Workbench/fr.md) sont créés. Un nouveau plan de travail peut être basé sur l\'une des nombreuses [présélections](#Utilisation_avec_les_pr.C3.A9s.C3.A9lections.md) ou sur une sélection. La sélection peut être créée avant ([présélection](#Utilisation_avec_pr.C3.A9s.C3.A9lection.md)) ou après ([post-sélection](#Utilisation_avec_post-s.C3.A9lection.md)) le lancement de la commande.


<small>(v0.22)</small> 

: pour chaque vue 3D, un plan de travail distinct est enregistré.

Le bouton ![](images/Draft_tray_button_plane.png ) dans [Draft La barre](Draft_Tray/fr.md) change en fonction du plan de travail courant. {{Version/fr|0.22}} : si le plan de travail n\'est pas réglé sur **Automatique**, un astérisque (*****) est ajouté à l\'étiquette du bouton si l\'origine du plan de travail ne correspond pas à l\'origine globale.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Formes créées sur différents plans de travail*



## Utilisation avec présélection 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez un seul objet. Les objets suivants sont pris en charge :
        -   [Draft Proxy pour plan de travail](Draft_WorkingPlaneProxy/fr.md) : la **View Data** (position de la caméra) et la **Visibility Map** (la visibilité enregistrée des objets) du proxy plan de travail sont également restaurées.
        -   [Arch Axes](Arch_Axis/fr.md) ({{Version/fr|0.22}})
        -   [Arch Système d\'axes](Arch_AxisSystem/fr.md) ({{Version/fr|0.22}})
        -   [Arch Partie de bâtiment](Arch_BuildingPart/fr.md).
        -   [Arch Plan de coupe](Arch_SectionPlane/fr.md).
        -   Les objets [Std Parts](Std_Part/fr.md) : pour éviter de sélectionner des sous-éléments, il est conseillé de les sélectionner dans la [vue en arborescence](Tree_view/fr.md).
        -   Les objets non solides constitués d\'une seule face plane ou d\'une seule arête courbe, ou ({{Version/fr|0.22}}) qui ont trois sommets ou plus.
        -   Les objets solides ou objets sans forme ayant une propriété **Placement**. ({{Version/fr|0.22}})
    -   Sélectionnez un ou plusieurs sous-éléments. Vous pouvez sélectionner :
        -   Une face plane.
        -   Une arête incurvée.
        -   Trois sommets.
        -   Une arête et un sommet, ou deux arêtes. Les sommets combinés doivent définir un plan. ({{Version/fr|0.22}})
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton ![](images/Draft_tray_button_plane.png ) de [Draft La barre](Draft_Tray/fr.md).
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SelectPlane.svg" width=16px> Sélectionner un plan** du menu.
    -   Utilisez le raccourci clavier : **W** puis **P**.
3.  Le plan de travail et le bouton de [Draft La barre](Draft_Tray/fr.md) sont mis à jour.



## Utilisation avec post-sélection 

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton ![](images/Draft_tray_button_plane.png ) de [Draft La barre](Draft_Tray/fr.md).
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SelectPlane.svg" width=16px> Sélectionner un plan** du menu.
    -   Utilisez le raccourci clavier : **W** puis **P**.
2.  Le panneau de tâches **Configuration du plan de travail** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez un seul objet. Voir le [paragraphe précédent](#Utilisation_avec_présélection.md) pour les objets pris en charge.
    -   Sélectionner un ou plusieurs sous-éléments. Voir le [paragraphe précédent](#Utilisation_avec_présélection.md).
4.  Cliquez n\'importe où dans la [vue 3D](3D_view/fr.md) pour confirmer la sélection et terminer la commande.
5.  Le plan de travail et le bouton de [Draft La barre](Draft_Tray/fr.md) sont mis à jour.



## Utilisation avec les présélections 

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton ![](images/Draft_tray_button_plane.png ) de [Draft La barre](Draft_Tray/fr.md).
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SelectPlane.svg" width=16px> Sélectionner un plan** dans le menu.
    -   Utilisez le raccourci clavier : **W** puis **P**.
2.  Le panneau de tâches **Configuration du plan de travail** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Appuyez sur l\'un des boutons pour terminer la commande.
4.  Le plan de travail et le bouton de [Draft La barre](Draft_Tray/fr.md) sont mis à jour.

## Options

-   Appuyez sur le bouton **<img src="images/View-top.svg" width=16px> Haut (XY)** pour aligner le plan de travail avec le plan XY du système de coordonnées global.

-   Appuyez sur le bouton **<img src="images/View-front.svg" width=16px> Face (XZ)** pour aligner le plan de travail sur le plan XZ du système de coordonnées global.

-   Appuyez sur le bouton **<img src="images/View-right.svg" width=16px> Côté (YZ)** pour aligner le plan de travail sur le plan YZ du système de coordonnées global.

-   Appuyez sur le bouton **<img src="images/View-isometric.svg" width=16px> Aligner selon la vue** pour aligner le plan de travail sur la [vue 3D](3D_view/fr.md) en cours. Si la case **Centrer le plan dans la vue** n\'est pas cochée, l\'origine du plan de travail correspondra à l\'origine du système de coordonnées global, sinon elle correspondra au centre de la [vue 3D](3D_view/fr.md) en cours.

-   Appuyez sur le bouton **<img src="images/View-axonometric.svg" width=16px> Automatique** pour régler le plan de travail en **Automatique**. Un plan de travail réglé sur **Automatique** s\'alignera automatiquement sur la [vue 3D](3D_view/fr.md) en cours chaque fois qu\'une commande de Draft ou de [Arch](Arch_Workbench/fr.md) nécessitant l\'entrée de points est lancée. Cela équivaut à appuyer sur le bouton **<img src="images/View-isometric.svg" width=16px> Aligner selon la vue** avant d\'utiliser la commande. De plus, le plan de travail s\'alignera sur les faces planes qui ont été sélectionnées avant de lancer la commande, ou lorsque des points sur des faces planes sont sélectionnés pendant la commande.

-    **Décalage**définit la distance perpendiculaire entre le plan calculé et le plan de travail réel en cours.

-   Cochez la case **Centrer le plan dans la vue** pour placer l\'origine du plan de travail au centre de la [vue 3D](3D_view/fr.md) en cours. Cette option peut être utile en combinaison avec le bouton **<img src="images/View-isometric.svg" width=16px> Aligner selon la vue**.

-   Sélectionnez un sommet dans la [vue 3D](3D_view/fr.md) et appuyez sur le bouton **<img src="images/Draft_Move.svg" width=16px> Déplacer le plan de travail** pour déplacer le plan de travail afin que son origine corresponde à la position du sommet sélectionné.

-    **Espacement de la grille**définit la distance entre les lignes de la grille.

-   La valeur de **Ligne principale tous les** détermine l\'endroit où les lignes de grille principales sont dessinées. Les lignes de grille principales sont légèrement plus épaisses que les lignes de grille normales. Par exemple, si l\'espacement de la grille est de {{Value|0.5 m}} et qu\'une ligne principale est tracée toutes les {{Value|10 lignes}}, une telle ligne sera tracée tous les {{Value|5 m}}.

-   La valeur de **Extension de la grille** détermine le nombre de lignes de grille dans les directions X et Y de la grille.

-    **Rayon d'aimantation**est la distance maximale à laquelle [Draft Aimantation Grille](Draft_Snap_Grid/fr.md) détecte les intersections des lignes de la grille.

-   Appuyez sur le bouton **<img src="images/view-fullscreen.svg" width=16px> Centrer la vue** pour aligner la [vue 3D](3D_view/fr.md) sur le plan de travail en cours.

-   Appuyez sur le bouton **<img src="images/sel-back.svg" width=16px> Précédent** pour réinitialiser le plan de travail à sa position précédente.

-   Appuyez sur le bouton **Suivant <img src="images/sel-forward.svg" width=16px>** pour réinitialiser le plan de travail à sa position suivante. {{Version/fr|0.22}}

-   Appuyez sur **Échap** ou sur le bouton **Fermer** pour abandonner la commande.



## Remarques

-   Il peut être utile d\'aligner la [vue 3D](3D_view/fr.md) avec le plan de travail Draft sélectionné. Par exemple, après avoir changé le plan de travail en vue de face, vous pouvez vouloir passer à la [vue de face](Std_ViewFront/fr.md) également.
-   La grille peut être basculée avec la commande [Draft Visibilité de la grille](Draft_ToggleGrid/fr.md).
-   En double-cliquant sur [Draft Proxy pour plan de travail](Draft_WorkingPlaneProxy/fr.md) dans la [vue en arborescence](Tree_view/fr.md), vous pouvez rapidement passer d\'un plan de travail à un autre.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Les paramètres de la grille dans le panneau des tâches ainsi que plusieurs autres paramètres de la grille sont disponibles en tant que préférences : **Édition → Préférences... → Draft → Grille et aimantation**.
-   Le rayon d\'aimantation peut également être modifié à la volée (voir [Draft Aimantation](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)) ou en modifiant : **Outils → Éditer les paramètres... → BaseApp → Preferences → Mod → Draft → snapRange**.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).


{{Version/fr|0.22}}

Le module WorkingPlane propose deux classes pour créer des objets plan de travail : la classe `PlaneBase` et la classe `PlaneGui`. La seconde classe hérite de la première. Les objets de la classe `PlaneGui` interagissent avec l\'interface graphique (le bouton de [Draft La barre](Draft_Tray/fr.md)), la [vue 3D](3D_view/fr.md) et la [grille](Draft_Snap_Grid/fr.md). Les objets `PlaneBase` ne le sont pas.

Utilisez la méthode `get_working_plane()` du module WorkingPlane pour obtenir une instance de la classe `PlaneGui` liée à la vue 3D en cours. La méthode renvoie le plan de travail existant lié à la vue ou crée un nouveau plan de travail si nécessaire.


```python
import FreeCAD as App
import WorkingPlane

wp = WorkingPlane.get_working_plane()

origin = App.Vector(0, 0, 0)
normal = App.Vector(1, 1, 1).normalize()
offset = 17
wp.align_to_point_and_axis(origin, normal, offset)

point = App.Vector(10, 15, 2)
projection = wp.project_point(point)
print(projection)
```

La classe `PlaneBase` peut être utilisée pour créer des plans de travail indépendants de l\'interface graphique :


```python
import WorkingPlane

wp = WorkingPlane.PlaneBase()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/fr
