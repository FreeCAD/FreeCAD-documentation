---
- GuiCommand:
   Name:FCGear InvoluteRack
   Name/fr:FCGear Engrenage à crémaillère
   MenuLocation:Gear - Involute Rack
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:v0.16
   SeeAlso:[FCGear Engrenage à développante](FCGear_InvoluteGear/fr.md)
---

# FCGear InvoluteRack/fr

## Description

Les crémaillères sont utilisées pour convertir un mouvement rotatif en un mouvement linéaire ou vice versa. Les exemples suivants présentent les différentes applications:

-   Une crémaillère avec un engrenage sur un barrage de retenue.
-   Divers systèmes de crémaillère de chemins de fer à crémaillère.
-   Direction à crémaillère dans un véhicule.
-   Treuil à crémaillère utilisé comme palan mécanique (par exemple, un cric de voiture).
-   Entraînements pneumatiques à crémaillère utilisés pour contrôler les vannes dans le transport par pipeline.

![](images/Involute-Rack_example.png ) 
*De gauche à droite : engrenage droit, engrenage hélicoïdal, engrenage hélicoïdal double.*

## Utilisation

1.  Passez à l\' <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur **[<img src=images/FCGear_InvoluteRack.svg style="width:16px"> [Involute Rack](FCGear_InvoluteRack/fr.md)** dans la barre d\'outils.
    -   Sélectionnez l\'option **Gear → [<img src=images/FCGear_InvoluteRack.svg style="width:16px"> Involute Rack** dans le menu.
3.  Modifiez le paramètre de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).

## Propriétés

Un objet FCGear InvoluteRack est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|base}}

-    **add_endings|Bool**: si {{True}} (valeur par défaut), alors la longueur totale de la crémaillère est égale à dents \* pas. Si {{False}}, alors la crémaillère commence par un front de dent.

-    **height|Length**: valeur par défaut à {{Value|5 mm}}. Valeur de la largeur de l\'engrenage.

-    **module|Length**: valeur par défaut à {{Value|1 mm}}. Module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir [Remarques](#Remarques.md)).

-    **teeth|Integer**: valeur par défaut à {{Value|15}}. Nombre de dents.

-    **thickness|Length**: valeur par défaut à {{Value|5}}. Hauteur de la racine de la dent à la face inférieure de la tige.


{{Properties_Title|computed}}

-    **transverse_pitch|Length**: (lecture seule) pas dans le plan transversal (voir [Remarques](#Remarques.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**: valeur par défaut à {{value|0 mm}}.

-    **root_fillet|Float**: valeur par défaut à {{value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: valeur par défaut à {{Value|0 °}}. Avec l\'angle d\'hélice β, un engrenage hélicoïdal est créé - valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche (voir [Remarques](#Remarques.md)).

-    **double_helix|Bool**: valeur par défaut à {{False}}, {{True}} crée un engrenage à double hélice (voir [Remarques](#Remarques.md)).

-    **properties_from_tool|Bool**: valeur par défaut à {{False}}. Si {{True}} et **beta** différente de zéro, les paramètres de l\'engrenage sont recalculés en interne pour l\'engrenage tourné.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: valeur par défaut à {{Value|20 °}} (voir [Remarques](#Remarques.md)).


{{Properties_Title|precision}}

-    **simplified|Bool**: valeur par défaut à {{False}}, {{True}} génère un affichage simplifié (sans dents).


{{Properties_Title|tolerance}}

-    **clearance|Float**: valeur par défaut à {{Value|0.25}} (voir [Remarques](#Remarques.md)).

-    **head|Float**: valeur par défaut à {{Value|0}}. Cette valeur est utilisée pour modifier la hauteur de la dent.


{{Properties_Title|version}}

-    **version|String**:

## Remarques

-    **transverse_pitch**: la valeur est le résultat de la multiplication de **module * pi**. Cela signifie que pour la crémaillère à développante standard de FCGear: 15 (**teeth**) \* 3.14 (**transverse_pitch**) est de 47,12 mm. Voir également **module** ci-dessous.

-    **clearance**: pour une paire d\'engrenages, le jeu est la distance entre l\'extrémité de la dent du premier engrenage et la racine de la dent du deuxième engrenage.

-    **double_helix**: pour utiliser l\'engrenage hélicoïdal double, l\'angle d\'hélice β (**beta**) pour l\'engrenage hélicoïdal doit d\'abord être saisi.

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes. Le résultat de la multiplication est affiché dans **transverse_pitch**

-    **pressure_parameter**: modifiez le paramètre uniquement si une connaissance suffisante de la géométrie de l\'engrenage est disponible.

## Formules utiles 

Voir [FCGear InvoluteGear](FCGear_InvoluteGear/fr#Formules_utiles.md).

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



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InvoluteRack/fr
