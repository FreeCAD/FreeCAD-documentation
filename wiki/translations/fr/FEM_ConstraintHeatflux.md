---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintHeatflux
   Name/fr: FEM Charge de flux de chaleur
   MenuLocation: Modèle , Conditions limites et charges thermiques , Charge de flux de chaleur
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintHeatflux/fr

## Description

Par défaut, définit une charge de flux de chaleur convective sur une surface à une température $T$ avec un coefficient de film $h$ et avec la température de l\'environnement (puits/ambiant) $T_{0}$. Le flux de chaleur convectif $q$ répondra à la condition suivante : $q=h(T-T_{0})$. En outre, il est possible de définir une charge de flux thermique de surface régulière.


{{Version/fr|1.0}}

: peut également être utilisé pour définir un flux de chaleur par rayonnement sur une surface. Cela correspond à : $q=\epsilon \sigma(T^{4}-T_{0}^{4})$ où $\epsilon$ est l\'émissivité de la surface et $\sigma$ est la constante de Stefan-Boltzmann.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Charge de flux de chaleur](FEM_ConstraintHeatflux/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges thermiques → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Charge de flux de chaleur** du menu.
2.  Cliquez sur le bouton **Ajouter**. Dans la [vue 3D](3D_view/fr.md), sélectionnez la ou les faces sur lesquelles la charge de flux thermique doit être appliquée. Si vous le souhaitez, cliquez sur le bouton **Supprimer** pour supprimer les faces sélectionnées de la liste de sélection.
3.  Choisissez le type de flux thermique et spécifiez ses paramètres :
    -   *Convection de surface* : valeur par défaut, flux de chaleur convectif, entrez le *Coefficient de film* et la *Température ambiante* souhaités.
    -   *Rayonnement de surface* : flux de chaleur par rayonnement, entrez l*\'Émissivité* de la surface et la *Température ambiante*. {{Version/fr|1.0}}
    -   *Flux de chaleur de surface* : flux de chaleur général, entrez le *Flux de chaleur de surface* en Watts par surface (W/m\^2).



## Remarques

-   La charge de flux de chaleur utilise les jeux de paramètres de CalculiX suivants en fonction du mode sélectionné :
    -   [\*FILM](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html) pour *Convection de surface*
    -   [\*RADIATE](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node234.html) pour *Rayonnement de surface*, {{Version/fr|1.0}}
    -   [\*DFLUX](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html) pour *Flux de chaleur en surface*





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/fr
