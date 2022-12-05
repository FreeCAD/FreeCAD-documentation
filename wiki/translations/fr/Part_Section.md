---
- GuiCommand:/fr
   Name:Part_Section
   Name/fr:Part Section
   MenuLocation:Part → Section
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Coupes](Part_CrossSections/fr.md)
---

# Part Section/fr

## Description

La commande <img alt="" src=images/Part_Section.svg  style="width:24px;"> **Part Section** crée une géométrie filaire aux intersections de deux objets. Le résultat est entièrement paramétrique.

-   Une intersection de deux solides/faces donne lieu à une ou plusieurs lignes de section.
-   L\'intersection de deux lignes, ou d\'une ligne et d\'un solide/face, donne un ou plusieurs points.

![](images/PartSection1_it.png ) 
*Un cube sectionné avec un cylindre*

## Utilisation

1.  Sélectionnez deux objets.
2.  Le premier objet sera la **Base** de la section, mais l\'ordre de sélection n\'a aucune incidence sur le résultat.
3.  Il existe plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le bouton **![](images/)_[Section](Part_Section/fr.md)**.
    -   Sélectionnez l\'option **Part → ![](images/)_Section**_dans_le_menu.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Part Section est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    **Base|Link**: Lien vers le premier objet.

-    **Tool|Link**: Lien vers le deuxième objet.


{{Properties_Title|Boolean}}

-    **History|ShapeHistory|hidden**: \"Historique de la forme\".

-    **Refine|Bool**: \"Affiner la forme (nettoyer les bords redondants) après cette opération booléenne\". La valeur par défaut est déterminée par la préférence **Affiner automatiquement le modèle après une opération d'esquisse**. Voir [PartDesign Préférences](PartDesign_Preferences/fr#G.C3.A9n.C3.A9ral.md).


{{Properties_Title|Section}}

-    **Approximation|Bool**: Approximation des bords de sortie.

## Liens

Pour créer des coupes depuis un plan de coupe, voir <img alt="" src=images/Part_CrossSections.svg  style="width:16px;"> [Part Coupes](Part_CrossSections/fr.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/fr
