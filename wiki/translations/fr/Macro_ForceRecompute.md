# Macro ForceRecompute/fr
{{Macro/fr
|Name=Macro Force Recompute
|Icon=Force_Recompute.png
|Description=Cette petite macro force un recalcul manuel du modèle. <br> Parfois, l'utilisateur applique des modifications au modèle dans FreeCAD. <br> Mais FreeCAD ne semble pas les reconnaître. <br> ({{Version/fr|0.17}}, l'effet de cette macro peut être obtenu via l'interface graphique. Cliquez avec le bouton droit sur le projet dans l'arborescence du modèle et choisissez "Marquer pour recalculer" dans le menu contextuel. Ensuite, appuyez sur le bouton Recalculer.)
|Author=shoogen
|Version=1.0
|Date=2014-09-01
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/8/88/Force_Recompute.png Icône de la barre d'outils]
}}

## Description

Parfois, lorsqu\'un utilisateur applique des modifications au modèle, FreeCAD ne semble pas les reconnaître/les intégrer. En outre, le bouton bleu **<img src="images/Std_Refresh.svg" width=24px> [Std Rafraîchir](Std_Refresh/fr.md)** reste grisé. Cette petite macro a donc été conçue pour forcer un recalcul manuel du modèle.

**Remarque:** a partir de {{VersionPlus/fr|0.17}}, l\'effet de cette macro peut être obtenu via l\'interface graphique. Cliquez avec le bouton droit sur le projet dans la [vue en arborescence du modèle](Tree_view/fr.md) et choisissez **Mark to recompute** dans le menu contextuel. Cela revient à réactiver l\'icône Actualiser/Recalculer. Appuyez maintenant sur le bouton <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Std Rafraîchir](Std_Refresh/fr.md) pour déclencher un recalcul.

## Utilisation

Lancer la macro au moment voulu.

## Script

Icône de la barre d\'outils <img alt="" src=images/Force_Recompute.png  style="width:24px;">

**Macro Force_Recompute.py**


{{MacroCode|code=
# -*- coding: utf-8 -*-
# Force Recompute
# macro provided by shoogen

import FreeCAD
for obj in FreeCAD.ActiveDocument.Objects:
 obj.touch()
FreeCAD.ActiveDocument.recompute()

}}



---
⏵ [documentation index](../README.md) > Macro ForceRecompute/fr
