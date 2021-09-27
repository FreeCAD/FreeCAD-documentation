---
- GuiCommand:/fr
   Name:FCGear InvoluteRack
   Name/fr:FCGear InvoluteRack
   MenuLocation:FCGear → Create an Involute rack
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Version:v0.16
   SeeAlso:[FCGear Engrenage à développante](FCGear_InvoluteGear/fr.md)
---

# FCGear InvoluteRack/fr

## Description

Les crémaillères sont utilisées pour convertir un mouvement rotatif en un mouvement linéaire ou vice versa. Les exemples suivants présentent les différentes applications:

-   Une crémaillère avec équipement sur un déversoir de retenue.
-   Divers systèmes de crémaillères de chemins de fer à crémaillère.
-   Direction à pignon et crémaillère dans un véhicule.
-   Treuil à crémaillère et pignon comme palan mécanique (par exemple cric de voiture).
-   Entraînements pneumatiques à crémaillère et pignon utilisés pour contrôler les vannes dans le transport par pipeline.

:   ![](images/Involute-Rack_example.png )
:   
    *De gauche à droite: Engrenage droit, engrenage hélicoïdal, engrenage double hélicoïdal*
    

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Lancez la commande d\'une de ces manières :
    -   Appuyez sur le bouton <img alt="" src=images/FCGear_InvoluteRack.svg  style="width:22px;"> [Create an Involute rack](FCGear_InvoluteRack/fr.md) dans la barre d\'outils.
    -   Utilisez **Gear Menu → Involute rack**.
3.  Modifiez le paramètre de démultiplication aux conditions requises (voir **Propriétés → Données** ci-dessous).

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: [Placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    {{PropertyData/fr|Label}}: nom d\'utilisateur de l\'objet dans [vue en arborescence](tree_view/fr.md).


{{Properties_Title|computed}}

-    **transverse_pitch**: Pas dans le plan transversal - non modifiable, est calculé automatiquement (voir aussi les informations dans les {{Emphasis |Remarques}}).


{{Properties_Title|gear_parameter}}

-    {{PropertyData/fr|add_endings}}: si **True** alors la longueur totale de la crémaillère est dents \* pas, sinon la crémaillère commence avec un flanc de dent.

-    {{PropertyData/fr|beta}}: avec l\'angle d\'hélice β, un engrenage hélicoïdal est créé (valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche).

-    {{PropertyData/fr|clearance}}: La valeur par défaut est 0,25 (voir aussi les informations dans les **Remarques**).

-    {{PropertyData/fr|double_helix}}: **True** crée un engrenage à double hélice (voir aussi les informations dans les **Remarques**).

-    {{PropertyData/fr|head}}: valeur par défaut est 0,00. Cette valeur est utilisée pour modifier la hauteur des dents.

-    {{PropertyData/fr|height}}: valeur de la largeur de l\'engrenage.

-    {{PropertyData/fr|module}}: module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir aussi les informations dans les **Remarques**).

-    {{PropertyData/fr|properties_from_tool}}: si l\'angle d\'hélice β est donné et que **properties_from-tool** est activé, les paramètres d\'engrenage sont recalculés en interne pour l\'engrenage tourné.

-    {{PropertyData/fr|simplified}}: **True** génère un affichage simplifié (sans dents).

-    {{PropertyData/fr|teeth}}: nombre de dents.

-    {{PropertyData/fr|thickness}}: hauteur de la racine de la dent juqu\'au côté inférieur de la tige.


{{Properties_Title|involute_parameter}}

-    {{PropertyData/fr|pressure_parameter}}: valeur par défaut 20 (voir aussi les informations dans les **Remarques**).

### Vue

La description des paramètres de l\'onglet **View** se trouve dans l\'[Éditeur de propriétés](Property_editor/fr.md) dans **Exemple de propriétés d'un objet PartDesign**.

## Remarques

-    **transverse_pitch**: la valeur est le résultat de la multiplication de **module * pi**. Cela signifie que pour la crémaillère à développante standard de FCGear: 15 (**teeth**) \* 3,14 (**transverse_pitch**) est de 47,12 mm. Voir également **module** ci-dessous.

-    **clearance**: pour une paire d\'engrenages, le jeu est la distance entre l\'extrémité de la dent du premier engrenage et la racine de la dent du deuxième engrenage.

-    **double_helix**: pour utiliser l\'engrenage hélicoïdal double, l\'angle d\'hélice β (**beta**) pour l\'engrenage hélicoïdal doit d\'abord être saisi.

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes. Le résultat de la multiplication est affiché dans **transverse_pitch**

-    **pressure_parameter**: modifiez le paramètre uniquement si une connaissance suffisante de la géométrie de l\'engrenage est disponible.

## Limitations

Aucune limitation n\'est connue.

## Formules utiles 

Pour plus d\'informations, voir <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:22px;"> [Engrenage à développante](FCGear_InvoluteGear/fr.md).

## Script

Utilisez la puissance de Python pour automatiser la modélisation de votre engrenage: 
```python
import FreeCAD as App
import freecad.gears.commands
gear = freecad.gears.commands.CreateInvoluteRack.create()
gear.teeth = 20
gear.beta = 20
gear.height = 10
gear.double_helix = True
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
``` 

_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear InvoluteRack/fr
