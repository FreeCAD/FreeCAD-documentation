---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ElementFluid1D
   Name/fr: FEM Section fluide 1D
   MenuLocation: Modèle , Géométrie de l'élement , Section de fluide pour un écoulement 1D
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM ElementFluid1D/fr

## Description

Crée un élément FEM de section fluide pour les réseaux pneumatiques et hydrauliques résolus avec CalculiX.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ElementFluid1D.svg" width=16px> [Section de fluide pour un écoulement 1D](FEM_ElementFluid1D/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Géométrie de l'élement → <img src="images/FEM_ElementFluid1D.svg" width=16px> Section de fluide pour un écoulement 1D** du menu.
2.  Sélectionnez le type de fluide : Liquid, Gas ou Open Channel
3.  Sélectionnez le type de section : Pipe Manning, Pipe Inlet etc.
4.  Entrez les paramètres du type de section.
5.  Sélectionnez et ajoutez une arête.

## Limitations

1.  Le jeu de paramètres ne fonctionne qu\'avec un type d\'élément de réseau à 3 nœuds. Les informations peuvent être trouvées ici : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node54.html>



## Remarques

1.  Un exemple de la mise en place d\'un réseau hydraulique peut être trouvé ici : <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node13.html>
2.  Le [jeu de paramètres \*FLUID SECTION](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node205.html) est utilisé pour modéliser les éléments fluides pour un écoulement 1D.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementFluid1D/fr
