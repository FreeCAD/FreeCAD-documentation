---
- GuiCommand:
   Name: Path Custom
   Name/fr: Path Personnaliser
   MenuLocation: Path -> Autres commandes -> Personnaliser
   Workbenches: Path_Workbench/fr
---

# Path Custom/fr

## Description

L\'outil <img alt="" src=images/Path_Custom.svg  style="width:24px;"> [Personnaliser](Path_Custom/fr.md) insère un objet chemin créé à partir de G-code personnalisé codé à la main.

Comme la commande de G-code personnalisé ne fournit aucun lien avec un contrôleur d\'outil, si un outil est utilisé par le G-code personnalisé, l\'index de l\'outil doit être écrit, ainsi que le M-code de démarrage de la broche, afin qu\'il soit transmis au post-processeur. Cela garantit que les changements et les démarrages d\'outils seront correctement générés.

Par exemple, pour indiquer au post-processeur que l\'outil utilisé dans l\'opération du G-code personnalisé a l\'indice d\'outil 6 et une vitesse de broche de 10 000, insérez le code suivant au début de l\'opération du G-code personnalisé :

(T6 : 4mm Endmill)

M6 T6

M3 S10000

Notez que les vitesses d\'avance ne seront correctement générées par le post-processeur que si les vitesses d\'avance du G-code personnalisé sont écrites en unités/seconde.



## Utilisation

1.  Pressez le bouton **<img src="images/Path_Custom.svg" width=16px>  [Personnaliser](Path_Custom/fr.md)
**
2.  Écrivez le G-code adapté dans la propriété **G Code** de l\'objet juste créé. Voir la page [Path Script](Path_scripting/fr.md) pour les commandes G-code acceptées.



## Propriétés

-    **G Code**: commandes G-code personnalisées pour programmer le parcours.





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Custom/fr
