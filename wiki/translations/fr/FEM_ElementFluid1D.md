---
- GuiCommand:/fr
   Name:FEM ElementFluid1D
   Name/fr:FEM Section fluide 1D
   MenuLocation:Modèle → Géométrie de l'élement → Section de fluide pour écoulement 1D
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM ElementFluid1D/fr

## Description

Crée un élément FEM de section de fluide pour les réseaux pneumatiques et hydrauliques.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/FEM_ElementFluid1D.svg" width=16px> [Section de fluide pour écoulement 1D](FEM_ElementFluid1D/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Géométrie de l'élement → <img src="images/FEM_ElementFluid1D.svg" width=16px> Section de fluide pour écoulement 1D** dans le menu.
2.  Sélectionnez le type de fluide: Liquid, Gas ou Open Channel
3.  Sélectionnez le type de section: Pipe Manning, Pipe Inlet etc.
4.  Entrez les paramètres du type de section.
5.  Sélectionnez et ajoutez un bord.

## Limitations

1.  La carte ne fonctionne qu\'avec un type d\'élément de réseau à 3 nœuds. Les informations peuvent être trouvées ici:<http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node54.html>

## Remarques

1.  Un exemple de la mise en place d\'un réseau hydraulique peut être trouvé ici:<http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node13.html>
2.  La fonction \*FLUID SECTION est utilisée pour modéliser les éléments fluides pour un écoulement 1D. Des informations sur la fonction sont disponibles ici : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node205.html>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementFluid1D/fr
