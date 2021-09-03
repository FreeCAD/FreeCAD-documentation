---
- GuiCommand:/fr
   Name:PartDesign Pad
   Name/fr:PartDesign Protrusion 
   MenuLocation:Conception de pièces → Créer une fonction additive → Protrusion
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Cavité](PartDesign_Pocket/fr.md)
---

## Description

L\'outil **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Protrusion](PartDesign_Pad/fr.md)** extrude une esquisse sélectionnée dans une direction normale au plan de l\'esquisse. À partir de la {{VersionPlus/fr|0.17}} les faces sur un solide peuvent également être utilisées.

![](images/PartDesign_Pad_example.svg )

*L\'esquisse (A) est montrée à gauche ; le solide résultant de l\'opération de protrusion (B) est à droite.*

**Remarque:** {{VersionMinus/fr|0.16}} Si l\'esquisse sélectionnée est appliquée sur la face d\'une solide existant ou d\'une autre fonction Part Design, la protrusion sera fusionnée au solide.

## Utilisation

1.  Sélectionner une esquisse. **Remarque:** à partir de {{VersionPlus/fr|0.17}}, une face du solide peut également être utilisée.
2.  Cliquer sur le bouton **<img src="images/PartDesign_Pad.svg" width=16px> '''Protrusion'''**.
3.  Définir les paramètres de protrusion, voir [Options](#Options.md) ci-dessous.
4.  Cliquer sur **OK**.

## Options

Lors de la création de la protrusion, la vue combinée bascule automatiquement à l\'onglet Tâches, qui affiche la boîte de dialogue **Paramètres de protrusion**.

![](images/Pad_parameters_cropped_fr.png )

### Type

Offre 5 différentes façons de définir la longueur de la protrusion.

#### Dimension

Permet de saisir une valeur numérique pour la longueur de la protrusion. La direction par défaut de la protrusion est vers le haut du plan d\'esquisse, mais cela peut être changé en cochant la case **Inversé**. La protrusion s\'effectue [normale](http://fr.wikipedia.org/wiki/Normale_%C3%A0_une_surface) au plan de l\'esquisse. L\'option **Symétrique au plan** étendra la protrusion à la moitié de la longueur saisie de chaque côté du plan d\'esquisse. Les dimensions négatives ne sont pas permises, utilisez plutôt l\'option **Inversé**.

#### Deux dimensions 

Permet de saisir une seconde valeur de longueur pour prolonger la protrusion dans la direction opposée (à travers le support). La direction peut également être changée avec l\'option **Inversé**.

#### Au dernier 

La protrusion sera prolongée jusqu\'à la dernière face rencontrée dans la direction d\'extrusion. S\'il n\'y a aucun support rencontré, un message d\'erreur apparaîtra.

#### Au premier 

La protrusion sera prolongée jusqu\'à la première face rencontrée dans la direction d\'extrusion. S\'il n\'y a aucun support rencontré, un message d\'erreur apparaîtra.

#### Jusqu\'à la face 

La protrusion sera prolongée jusqu\'à la face sélectionnée du support. La face est sélectionnée en cliquant sur le bouton *Face*, puis en cliquant sur la face désirée dans la vue modèle. S\'il n\'y a aucun support, aucune sélection ne sera allouée.

### Longueur

Définit la longueur de la protrusion. Plusieurs unités peuvent être utilisées, indépendamment des préférences de l\'utilisateur (m, cm, mm, nm, ft ou \' pour pieds, in ou \" pour pouces).

### Utiliser une direction personnalisée 


{{Version/fr|0.19}}

Si coché, la direction de la protrusion ne sera pas le vecteur normal de l\'esquisse mais le vecteur donné. La longueur de la protrusion est cependant réglée selon la direction normale du vecteur.

### Longueur le long de la normale à l\'esquisse 

Si cette case est cochée, la longueur de la protrusion est mesurée le long de la normale à l\'esquisse, sinon le long de la direction personnalisée. {{Version/fr|0.20}}

### Décalage par rapport à la surface 

Décalage de la surface dans laquelle la protrusion se terminera. Cette option n\'est disponible que lorsque le *Type* est soit *En dernier*, *En premier* ou *Jusqu\'à la face*.

### Symétrique au plan 

Cocher la case pour prolonger la moitié de la longueur définie de chaque côté du plan d\'esquisse.

### Inversé

Inverse la direction de la protrusion.

## Propriétés

-    {{PropertyData/fr|Type}}: Type de façons dont la protrusion sera extrudée, voir [Options](#Options.md).

-    {{PropertyData/fr|Length}}: définit la longueur de la protrusion, voir [Options](#Options.md).

-    {{PropertyData/fr|Length2}}: Deuxième longueur de remplissage au cas où l\'option {{PropertyData/fr|Type}} **TwoLengths** est utilisée, voir [Options](#Options.md).

-    {{PropertyData/fr|Use Custom Vector}}: {{Version/fr|0.19}} Si coché, la direction de la protrusion ne sera pas le vecteur normal de l\'esquisse mais le vecteur donné, voir [Options](#Options.md).

-    {{PropertyData/fr|Direction}}: {{Version/fr|0.19}} Vecteur de la direction de la protrusion si {{PropertyData/fr|Use Custom Vector}} est utilisé.

-    {{PropertyData/fr|Along Sketch Normal}}: {{Version/fr|0.20}} Si *true*, la longueur de la protrusion est mesurée le long de la normale à l\'esquisse. Sinon et si {{PropertyData/fr|Use Custom Vector}} est utilisé, elle est mesurée le long de la direction personnalisée.

-    {{PropertyData/fr|Up To Face}}: Une face vers laquelle la protrusion va extruder, voir [Options](#Options.md).

-    {{PropertyData/fr|Offset}}: Décalage par rapport à la face dans laquelle la protrusion se terminera. Ceci n\'est pris en compte que si l\'option {{PropertyData/fr|Type}} **UpToLast**, **UpToFirst** ou **UpToFace** est utilisée.

-    {{PropertyData/fr|Refine}}: {{VersionPlus/fr|0.17}} true ou false. Nettoie les bords résiduels laissés après l\'opération. Cette propriété est initialement définie en fonction des paramètres de l\'utilisateur (trouvés dans *Préférences → Conception de la pièce → Général → Paramètres du modèle*). Il peut être modifié manuellement par la suite. Cette propriété sera enregistrée avec le document FreeCAD.

## Limitations


<div class="mw-translate-fuzzy">

-   Comme toutes les fonctions Part Design, la Protrusion créé un solide, l\'esquisse doit par conséquent inclure un profil fermé ou elle échouera. Il peut y avoir plusieurs profils fermés à l\'intérieur d\'un profil fermé plus grand, pourvu qu\'aucun des profils ne s\'entrecroise (par exemple, un rectangle avec deux cercles à l\'intérieur sera valide).

-   L\'algorithme utilisé pour **Au premier** et **Au dernier** fonctionne ainsi :
    -   Il crée une ligne passant par le centre de gravité de l\'esquisse ;
    -   Il trouve toutes les faces du support coupées par cette ligne ;
    -   Il choisit la face la plus près/la plus loin du point d\'intersection de l\'esquisse.

-   Cela veut dire que la face trouvée pourrait ne pas être celle attendue. Si vous faites face à ce problème, utilisez plutôt le type **Jusqu\'à la face** et sélectionnez la face désirée.

-   Dans le cas très spécifique d\'une protrusion sur une surface concave, où l\'esquisse est plus grande que cette surface, la protrusion échouera. Il s\'agit d\'un bogue non-résolu.

-    {{VersionMinus/fr|0.16}}Il n\'y a pas de nettoyage automatique, par ex. des surfaces planes adjacentes en une seule surface. Vous pouvez résoudre ce problème manuellement dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Atelier Part](Part_Workbench.md) avec **<img src="images/Part_RefineShape.svg" width=16px> [Part Affiner la forme](Part_RefineShape/fr.md)** (qui crée un solide non paramétrique non lié) ou avec le **<img src="images/OpenSCAD_RefineShapeFeature.svg" width=16px> [OpenSCAD Affinage de la forme](OpenSCAD_RefineShapeFeature/fr.md)** à partir de <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:16px;"> [Atelier OpenSCAD](OpenSCAD_Workbench/fr.md) qui crée une fonction paramétrique.


</div>





{{PartDesign Tools navi

}} 
