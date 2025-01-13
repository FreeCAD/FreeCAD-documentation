---
 GuiCommand:
   Name: Std_Paste
   Name/fr: Std Coller
   MenuLocation: Édition , Coller
   Workbenches: Tous
   Shortcut: **Ctrl** + **V**
   SeeAlso: Std_Cut/fr, Std_Copy/fr, Std_DuplicateSelection/fr
---

# Std Paste/fr

## Description

La commande **Std Coller** colle les objets du Presse-papiers dans le document actif.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Std_Paste.svg" width=16px> [Coller](Std_Paste/fr.md)**.
    -   Sélectionnez l\'option **Édition → <img src="images/Std_Paste.svg" width=16px> Coller** du menu.
    -   Sélectionnez l\'option **<img src="images/Std_Paste.svg" width=16px> Coller** dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md). Notez que cette option n\'est disponible que lorsqu\'un objet sortant a été sélectionné.
    -   Utilisez le raccourci clavier: **Ctrl**+**V**.



## Remarques

-   FreeCAD changera automatiquement les noms internes et, selon les préférences, les étiquettes des objets pour éviter les conflits de noms.
-   Un alias de cellule de feuille de calcul qui existe déjà dans la feuille de calcul ne sera pas collé.
-   Lorsque vous travaillez dans une fenêtre de texte FreeCAD, une zone de saisie ou une feuille de calcul, le raccourci clavier standard **Ctrl**+**V**, dans presque tous les cas, n\'appelle pas cette commande mais utilise la fonction Coller du système d\'exploitation à la place.
-   Il n\'est pas possible de copier-coller des objets natifs entre FreeCAD et d\'autres applications.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md).

-   Pour autoriser les étiquettes en double, cochez l\'option **Édition → Préférences... → Général → Document → Autoriser la duplication des étiquettes dans un document**. Mais cela n\'est pas recommandé.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Paste/fr
