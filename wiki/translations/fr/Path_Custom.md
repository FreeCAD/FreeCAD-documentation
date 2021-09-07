---
- GuiCommand:/fr
   Name:Path Custom
   Name/fr:Path Personnaliser
   MenuLocation:Path → Supplemental Commands → Personnalisée
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:
   SeeAlso:
---


</div>

## Description

Cet outil insère un objet chemin créé à partir de G-code personnalisé codé à la main.

Etant donné que la commande Code G personnalisé ne fournit aucun lien vers un contrôleur d'outil, si un outil est utilisé par le code G personnalisé, vous devez écrire l'index de l\'outil, ainsi que le code M de démarrage de la broche, afin qu\'il soit transmis au post-processeur. Cela garantit que les changements d'outil et les démarrages seront correctement générés.

Par exemple, pour indiquer au postprocesseur que l\'outil utilisé dans l\'opération Custom G-Code a l\'index 6 et une vitesse de rotation de 10 000, insérez le code suivant au début de l\'opération Custom G-Code:

(T6: 4mm Endmill)

M6 T6

M3 S10000

Notez que les taux d'alimentation seront correctement générés par le post-processeur, uniquement si les taux d'alimentation personnalisés du code G sont écrits en unités / seconde.

## Utilisation

1.  Pressez le bouton **<img src="images/Path_Custom.svg" width=16px>  [Personnalisée](Path_Custom/fr.md)
**
2.  Écrivez le G-Code adapté dans la propriété **G Code** de l\'objet nouvellement créé. Voyez la page [Path Programmer](Path_scripting/fr.md) pour les commandes G-Code acceptées.

## Propriétés

-    **G Code**: Les commandes G-Code sur lequelles sont construites le chemin.


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 