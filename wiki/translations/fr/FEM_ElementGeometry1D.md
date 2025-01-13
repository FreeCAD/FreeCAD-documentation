---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ElementGeometry1D
   Name/fr: FEM Coupe transversale d'un élément 1D
   MenuLocation: Modèle , Géométrie de l'élement , Coupe transversale d'un élément 1D
   Workbenches: FEM_Workbench/fr
   Shortcut: **C** **B**
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX, Mystran, Z88
}}
---

# FEM ElementGeometry1D/fr

## Description

**Coupe transversale d\'un élément 1D** est utilisé pour définir les sections transversales d\'éléments de type poutre. Pour l\'instant, les types de sections transversales suivantes disponibles sections : rectangulaire, circulaire et tube.

Les sections transversales de poutres-caissons et elliptiques sont également disponibles. {{VersionPlus/fr|1.1}}



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [Coupe transversale d'un élément 1D](FEM_ElementGeometry1D/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Géométrie de l'élément → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Coupe transversale d'un élément 1D** du menu.
2.  Choisissez le type de section transversale et spécifiez les dimensions nécessaires :
    -   Rectangulaire : largeur et hauteur,
    -   Circulaire : diamètre,
    -   Tube : diamètre extérieur et épaisseur,
    -   Elliptique : longueur de l\'axe 1 et longueur de l\'axe 2. {{VersionPlus/fr|1.1}}
    -   Poutre-caisson : hauteur, largeur, épaisseur T1 - T4. {{VersionPlus/fr|1.1}}
3.  Vous pouvez appuyer sur le bouton **Ajouter** dans le panneau des tâches, puis cliquer sur l\'arête à laquelle vous voulez donner une section transversale prescrite. Si la sélection de l\'arête est libre, toutes les arêtes restantes (dont la section transversale n\'est pas définie par d\'autres objets [Coupe transversale d\'un élément 1D](FEM_ElementGeometry1D/fr.md)) seront automatiquement attribuées.



## Propriétés

-    **Section Type**: spécifie le type de section de la poutre (*Rectangulaire*, *Circulaire*, *Tube*, {{VersionPlus/fr|1.1}} : *Elliptique* et *Boîte*)

-    **Box Height**: hauteur de la section de la poutre-caisson, utilisée si **Section Type** est *Box*. {{VersionPlus/fr|1.1}}

-    **Box T1**: épaisseur T1 de la section de la poutre-caisson, utilisé si **Section Type** est *Box*. {{VersionPlus/fr|1.1}}

-    **Box T2**: épaisseur T2 de la section de la poutre-caisson, utilisée si **Section Type** est *Box*. {{VersionPlus/fr|1.1}}

-    **Box T3**: épaisseur T3 de la section de la poutre-caisson, utilisée si **Section Type** est *Box*. {{VersionPlus/fr|1.1}}

-    **Box T4**: épaisseur T4 de la section de la poutre-caisson, utilisée si **Section Type** est *Box*. {{VersionPlus/fr|1.1}}

-    **Box Width**: largeur de la section de la poutre-caisson, utilisée si **Section Type** est *Box*. {{VersionPlus/fr|1.1}}

-    **Circ Diameter**: diamètre de la section circulaire, utilisé si **Section Type** est *Circular*

-    **Axis 1 Length**: longueur de l\'axe 1 de la section elliptique, utilisé si **Section Type** est *Elliptical*. {{VersionPlus/fr|1.1}}

-    **Axis 2 Length**: longueur de l\'axe 2 de la section elliptique, utilisée si **Section Type** est *Elliptical*. {{VersionPlus/fr|1.1}}

-    **Pipe Diameter**: diamètre extérieur de la section de tube, utilisé si **Section Type** est *Pipe*

-    **Pipe Thickness**: épaisseur de la section de tube, utilisée si **Section Type** est *Pipe*

-    **Rect Height**: hauteur de la section rectangulaire, utilisée si **Section Type** est *Rectangular*

-    **Rect Width**: hauteur de la section rectangulaire, utilisée si **Type de section** est *Rectangular*

## Limitations

-    {{VersionMinus/fr|1.0}}: les autres types de sections transversales disponibles dans CalculiX (elliptique, boîte et générale) ne sont pas pris en charge pour l\'instant. Il est possible de modifier le fichier d\'entrée pour les utiliser.

-    {{VersionPlus/fr|1.1}}: la section générale des poutres n\'est pas prise en charge pour le moment. Il est possible de modifier le fichier d\'entrée pour l\'utiliser.



## Remarques

-   Pour visualiser les résultats du solveur CalculiX sur le maillage étendu à la section transversale prescrite, la propriété `Beam Shell Result Output 3D` du [FEM Solveur CalculiX standard](FEM_SolverCalculixCxxtools/fr.md) doit être définie à `True`.
-   Certaines sections nécessitent des types d\'éléments spécifiques :
    -   section circulaire : éléments de 2ème ordre
    -   section de tube : éléments du 2ème ordre avec intégration réduite ({{Version/fr|1.0}} : l\'intégration réduite est activée par défaut pour les éléments de type poutre et peut être commutée en utilisant la propriété *Beam Reduced Integration* du [solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md)).
    -   section elliptique : éléments du 2ème ordre. {{VersionPlus/fr|1.1}}
    -   section poutre-caisson : éléments du 2ème ordre avec intégration réduite (comme expliqué ci-dessus). {{VersionPlus/fr|1.1}}
-   Cette fonction utilise le [jeu de paramètres \*BEAM SECTION de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry1D/fr
