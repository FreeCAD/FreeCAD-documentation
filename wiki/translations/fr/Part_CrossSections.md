---
 GuiCommand:
   Name: Part CrossSections
   Name/fr: Part Coupes
   Icon: Part_CrossSections.svg
   MenuLocation: Part , Coupes...
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_Section/fr
---

# Part CrossSections/fr

## Description

L\'utilitaire **Coupes** crée une ou plusieurs coupes transversales à travers la forme sélectionnée, parallèlement à l\'un des plans globaux par défaut (XY, XZ ou YZ).



## Utilisation

1.  Sélectionnez une forme.
2.  Cliquez sur le bouton **[24px|link=Part_CrossSections/fr](File:Part_CrossSections.svg.md) '''Coupes...'''**.
3.  Définissez le plan guide.
4.  Définissez la position (hauteur de la section transversale).
5.  Vous pouvez cocher **Sections** pour créer plus d\'une section transversale :
    -   Cochez *Des deux côtés* pour répartir les sections transversales de chaque côté de l\'emplacement du plan de guidage.
    -   Définissez le nombre.
6.  Cliquez sur **OK**.



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être utilisés comme objets sources. {{Version/fr|0.20}}
-   L\'objet résultant n\'est pas paramétrique, c\'est-à-dire qu\'il n\'est pas lié à la forme originale.
-   Un seul objet est créé, même pour plusieurs coupes.



## Exemple

![Sélectionner un objet](images/SectionCross1.png )

![Fenêtre de dialogue](images/SectionCross2.png )

![Résultat](images/SectionCross3.png )



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CrossSections/fr
