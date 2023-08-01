---
- GuiCommand:/fr
   Name:Surface CurveOnMesh
   Name/fr:Surface Courbe sur maillage
   MenuLocation:Surface → Curve on mesh...
   Workbenches:[Surface](Surface_Workbench/fr.md)
   Version:0.17
---

# Surface CurveOnMesh/fr

## Description


**[<img src=images/Surface_CurveOnMesh.svg style="width:16px"> [Surface Courbe sur maillage](Surface_CurveOnMesh/fr.md)**

crée des segments de spline approximatifs par dessus un [maillage](Mesh_Workbench/fr.md) sélectionné.

Si l\'objet n\'est pas un [maillage](Mesh/fr.md), mais une [Forme](Shape/fr.md) ou une surface paramétrique, il doit d\'abord être converti en un maillage à l\'aide de **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Mesh Créer un maillage](Mesh_FromPartShape/fr.md)**.

Ces arêtes créées par dessus le maillage peuvent être utilisées pour recréer la surface de manière paramétrique en utilisant des outils tels que **[<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [Remplir entre les courbes limites](Surface_GeomFillSurface/fr.md)** et **[<img src=images/Surface_Sections.svg style="width:16px"> [Sections](Surface_Sections/fr.md)**.

![](images/Surface_CurveOnMesh_mesh_example.png ) ![](images/Surface_CurveOnMesh_example.png )

![](images/Surface_CurveOnMesh_surface_example.png )



*En haut à gauche: objet maillé avec des points sélectionnés sur la surface.<br/>En haut à droite: splines créées en sélectionnant plusieurs points sur le maillage.<br/>En bas à gauche: une surface paramétrique reconstruite à partir des splines approximées en utilisant [Surface Sections](Surface_Sections/fr.md).*



## Utilisation

1.  Assurez-vous d\'avoir un [objet maillé](Mesh/fr.md). Cela peut être créé par l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [atelier Mesh](Mesh_Workbench/fr.md) ou en important un type de fichier de maillage, comme STL, [OBJ](Arch_OBJ/fr.md) ou [DAE](Arch_DAE/fr.md). Si un objet solide ou un type de fichier solide (STEP) est utilisé, il peut être converti en un maillage à l\'aide de **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Mesh Tesselation](Mesh_FromPartShape/fr.md)**.
2.  Appuyez sur **[<img src=images/Surface_CurveOnMesh.svg style="width:16px"> [Courbe sur maillage](Surface_CurveOnMesh/fr.md)**.
3.  Appuyez sur **Start**.
4.  À l\'aide du pointeur de la souris, choisissez des points sur la surface du maillage dans la [Vue 3D](3D_view/fr.md). Choisissez autant de points que nécessaire pour dessiner une ligne d\'aperçu lisse.
5.  Quand suffisamment de points ont été ajoutés, faites un clic droit sur la [Vue 3D](3D_view/fr.md) pour ouvrir le menu contextuel et sélectionnez **Create**. En fonction de la fluidité du maillage d\'origine, une spline ou plusieurs splines seront créées dans la [Vue en arborescence](Tree_view/fr.md).
6.  Répétez la séquence **Start** → Pick → **Create**, pour ajouter d\'autres splines approchées.
7.  La nouvelle spline sera créée et apparaîtra dans la [Vue en arborescence](Tree_view/fr.md) immédiatement après avoir choisi **Create**. Le [Panneau des tâches](Task_panel/fr.md) restera actif.
8.  Appuyez sur **Close** pour fermer le [Panneau des tâches](Task_panel/fr.md) et terminer complètement la commande.

Après avoir appuyé sur **Start**, le menu contextuel (clic droit) dans la [vue 3D](3D_view/fr.md) affiche diverses options à côté de **Create**.

-    **Close wire**: si au moins trois points ont été choisis, cette option sera disponible pour joindre le dernier point au premier point par une ligne.

-    **Clear**: cela effacera les points provisoires qui ont été choisis sur le maillage, et vous permettra d\'en choisir de nouveaux.

-    **Cancel**: cela effacera les points provisoires qui ont été choisis, et arrêtera l\'opération de prélèvement. Appuyez à nouveau sur **Start** pour sélectionner à nouveau des points.

## Options


**(Editeur : ces informations doivent être vérifiées)**

Section **Wire** :

-    **Snap tolerances to vertices**: par défaut {{Value|10 px}}. Indique la distance minimale entre un point et un autre lors du prélèvement avec le pointeur.

-    **Split threshold**: par défaut {{Value|45 deg}}. Indique l\'écart angulaire d\'un point du maillage à un autre point nécessaire pour créer une nouvelle spline au lieu d\'étendre la spline précédente.


**Spline approximation**

, si {{CheckBox|TRUE|coché}}, cela créera des objets spline sinon créera de simples objets de ligne droite (polyligne).

-    **Tolerance to mesh**: par défaut {{Value|0.2}}. C\'est un paramètre qui prend en compte les imperfections du maillage. Plus ce nombre est petit, plus il considérera le maillage avec précision, surtout s\'il s\'agit d\'un maillage très fin.

-    **Continuity**: par défaut {{Value|C2}}. Détermine la continuité de la spline. Il peut s\'agir de {{Value|C0}} (toucher), {{Value|C1}} (tangente), {{Value|C2}} (courbure) et {{Value|C3}} (courbure d\'accélération).

-    **Maximum curve degree**: par défaut {{Value|5}}. Détermine le degré maximum de la spline pour se rapprocher de la surface. Il peut s\'agir d\'une valeur comprise entre {{Value|1}} et {{Value|8}}.



## Propriétés

Si {{CheckBox|FALSE|Spline approximation}} n\'est pas cochée, l\'outil [Courbe sur maillage](Surface_CurveOnMesh/fr.md) crée une [Part Feature](Part_Feature/fr.md) de base.

Si {{CheckBox|TRUE|Spline approximation}} est coché, l\'outil [Courbe sur maillage](Surface_CurveOnMesh/fr.md) crée une **[<img src=images/Part_Spline.svg style="width:16px"> [Part Spline](Part_Spline/fr.md) ** (classe `Part::Spline`) qui est dérivée de la classe de base [Part Feature](Part_Feature/fr.md) (classe `Part::Feature`). Elle partage donc toutes les propriétés de cette dernière.

Outre les propriétés décrites dans [Part Feature](Part_Feature/fr.md), Part Spline a les propriétés suivantes dans l\'[éditeur de propriétés](Property_editor/fr.md).



### Vue


{{TitleProperty|Base}}

-    {{PropertyView/fr|Control Points|Bool}}: par défaut `False`. Mis à `True`, elle affichera une superposition avec les points de contrôle de la surface.





{{Surface Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface CurveOnMesh/fr
