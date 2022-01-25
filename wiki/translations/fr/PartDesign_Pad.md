---
- GuiCommand:/fr
   Name:PartDesign Pad
   Name/fr:PartDesign Protrusion 
   MenuLocation:Conception de pièces → Créer une fonction additive → Protrusion
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Cavité](PartDesign_Pocket/fr.md)
---

# PartDesign Pad/fr

## Description

L\'outil *Protrusion* extrude une esquisse ou une face d\'un solide le long d\'une trajectoire droite.

![](images/PartDesign_Pad_example.svg )

*L\'esquisse (A) est montrée à gauche ; le solide résultant de l\'opération de protrusion (B) est à droite.*

## Utilisation

1.  Sélectionnez une esquisse ou une face à extruder. {{Version/fr|0.20}} Vous pouvez également sélectionner plusieurs esquisses ou faces.
2.  Cliquer sur le bouton **<img src="images/PartDesign_Pad.svg" width=16px> '''Protrusion'''**.
3.  Définir les paramètres de protrusion, voir [Options](#Options.md) ci-dessous.
4.  Cliquer sur **OK**.

## Options

Lors de la création de la protrusion, la boîte de dialogue **Paramètres de protrusion** s\'affiche. Elle offre les paramètres suivants :

![](images/Pad_parameters_cropped_fr.png )

### Type

Type offre 5 différentes façons de définir la longueur de la protrusion:

#### Dimension

Permet de saisir une valeur numérique pour la longueur de la protrusion. La direction par défaut de la protrusion est vers le haut du plan d\'esquisse, mais cela peut être changé en cochant la case **Inversé**. La protrusion s\'effectue par défaut [normale](http://fr.wikipedia.org/wiki/Normale_%C3%A0_une_surface) au plan de l\'esquisse. Ceci peut être modifié en spécifiant une autre *Direction*. L\'option **Symétrique au plan** étendra la protrusion à la moitié de la longueur saisie de chaque côté du plan d\'esquisse. Les dimensions négatives ne sont pas permises, utilisez plutôt l\'option **Inversé**.

#### Deux dimensions 

Permet de saisir une seconde valeur de longueur pour prolonger la protrusion dans la direction opposée (à travers le support). Les directions peuvent être inversées en cochant l\'option *Inversé*.

#### Au dernier 

La protrusion sera prolongée jusqu\'à la dernière face rencontrée dans la direction d\'extrusion. S\'il n\'y a aucun support rencontré, un message d\'erreur apparaîtra.

#### Au premier 

La protrusion sera prolongée jusqu\'à la première face rencontrée dans la direction d\'extrusion. S\'il n\'y a aucun support rencontré, un message d\'erreur apparaîtra.

#### Jusqu\'à la face 

La protrusion sera prolongée jusqu\'à une face du modèle qui peut être choisie en cliquant dessus.

### Longueur

Définit la longueur de la protrusion. Plusieurs unités peuvent être utilisées, indépendamment des préférences de l\'utilisateur (m, cm, mm, nm, ft ou \' pour pieds, in ou \" pour pouces). Cette option n\'est disponible que lorsque **Type** est soit **Dimension** soit **Deux dimensions**.

### Décalage par rapport à la surface 

Décalage de la surface à laquelle la protrusion se terminera. Cette option n\'est disponible que lorsque le *Type* est soit *En dernier*, *En premier* ou *Jusqu\'à la face*.

### Direction

#### Direction/bord

Vous pouvez sélectionner la direction de la protrusion :

-   **Face/Sketch normal** L\'esquisse ou la face est extrudée le long de sa normale. Si vous avez sélectionné plusieurs esquisses ou faces à extruder, la normale de la première sera utilisée. {{Version/fr|0.20}}
-   **Select reference\...** L\'esquisse est extrudée le long d\'une arête du modèle 3D. Lorsque cette méthode est sélectionnée, vous pouvez cliquer sur n\'importe quelle arête du modèle 3D. Celle-ci devient alors le vecteur de direction pour la protrusion. {{Version/fr|0.20}}
-   **Custom direction** L\'esquisse est extrudée selon une direction qui peut être spécifiée par des valeurs vectorielles. {{Version/fr|0.19}}

#### Afficher la direction 

Si cette case est cochée, la direction du pad sera affichée. Si la protrusion utilise une **direction personnalisée**, elle peut être modifiée. {{Version/fr|0.20}}

#### Longueur le long de la normale à l\'esquisse 

Si cette case est cochée, la longueur de la protrusion est mesurée le long de la normale à l\'esquisse, sinon le long de la direction personnalisée. {{Version/fr|0.20}}

### Symétrique au plan 

Cochez la case pour extruder la moitié de la longueur donnée de chaque côté de l\'esquisse ou du plan.

### Inversé

Inverse la direction de la protrusion.

## Propriétés

-    **Type**: Type de façons dont la protrusion sera extrudée, voir [Options](#Options.md).

-    **Length**: Définit la longueur de la protrusion, voir [Options](#Options.md).

-    **Length2**: Deuxième longueur de la protrusion dans le cas où l\'option **Type** est à **TwoLengths**, voir [Options](#Options.md).

-    **Use Custom Vector**: {{Version/fr|0.19}} Si coché, la direction de la protrusion ne sera pas le vecteur normal de l\'esquisse mais le vecteur donné, voir [Options](#Options.md).

-    **Direction**: {{Version/fr|0.19}} Vecteur de la direction de la protrusion si **Use Custom Vector** est utilisé.

-    **Along Sketch Normal**: {{Version/fr|0.20}} Si *True*, la longueur de la protrusion est mesurée le long de la normale à l\'esquisse. Sinon et si **Use Custom Vector** est utilisé, elle est mesurée le long de la direction personnalisée.

-    **Up To Face**: Une face vers laquelle la protrusion va extruder, voir [Options](#Options.md).

-    **Offset**: Décalage par rapport à la face dans laquelle la protrusion se terminera. Ceci n\'est pris en compte que si l\'option **Type** **UpToLast**, **UpToFirst** ou **UpToFace** est utilisée.

-    **Refine**: True ou false. Nettoie les bords résiduels laissés après l\'opération. Cette propriété est initialement définie en fonction des paramètres de l\'utilisateur (trouvés dans **Préférences → Conception de la pièce → Général → Paramètres du modèle**). Il peut être modifié manuellement par la suite. Cette propriété sera enregistrée avec le document FreeCAD.

## Limitations

-   Comme toutes les fonctions Part Design, la Protrusion créé un solide, l\'esquisse doit par conséquent inclure un profil fermé ou elle échouera. Il peut y avoir plusieurs profils fermés à l\'intérieur d\'un profil fermé plus grand, pourvu qu\'aucun des profils ne s\'entrecroise (par exemple, un rectangle avec deux cercles à l\'intérieur sera valide).
-   L\'algorithme utilisé pour **Au premier** et **Au dernier** fonctionne ainsi :
    -   Il crée une ligne passant par le centre de gravité de l\'esquisse ;
    -   Il trouve toutes les faces du support coupées par cette ligne ;
    -   Il choisit la face la plus près/la plus loin du point d\'intersection de l\'esquisse.
-   Cela veut dire que la face trouvée pourrait ne pas être celle attendue. Si vous faites face à ce problème, utilisez plutôt le type **Jusqu\'à la face** et sélectionnez la face désirée.
-   Dans le cas très spécifique d\'une protrusion sur une surface concave, où l\'esquisse est plus grande que cette surface, la protrusion échouera. Il s\'agit d\'un bogue non-résolu.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/fr
