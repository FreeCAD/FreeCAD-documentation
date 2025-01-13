---
 GuiCommand:
   Name: Part_Section
   Name/fr: Part Section
   MenuLocation: Part , Créer une section
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_CrossSections/fr
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
2.  Le premier objet sera la propriété **Base** de la section, mais l\'ordre de sélection n\'a aucune incidence sur le résultat.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **![](images/)_[Créer_une_section](Part_Section/fr.md)**.
    -   Sélectionnez l\'option **Part → ![](images/)_Créer_une_section**_du_menu.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet PartDesign Section est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Base}}

-    **Base|Link**: lien vers le premier objet.

-    **Tool|Link**: lien vers le deuxième objet.


{{Properties_Title|Boolean}}

-    **History|ShapeHistory|hidden**: \"historique de la forme\".

-    **Refine|Bool**: \"affiner la forme (nettoyer les arêtes redondantes) après cette opération booléenne\". La valeur par défaut est déterminée par la préférence **Affiner les modèles automatiquement après une opération sur une esquisse**. Voir [PartDesign Préférences](PartDesign_Preferences/fr#G.C3.A9n.C3.A9ral.md).


{{Properties_Title|Section}}

-    **Approximation|Bool**: approxime les arêtes générées.



## Liens

Pour créer des coupes depuis un plan de coupe, voir <img alt="" src=images/Part_CrossSections.svg  style="width:16px;"> [Part Coupes](Part_CrossSections/fr.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/fr
