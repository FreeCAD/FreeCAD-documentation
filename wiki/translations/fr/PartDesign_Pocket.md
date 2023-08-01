---
- GuiCommand:
   Name:PartDesign_Pocket
   Name/fr:PartDesign Cavité
   MenuLocation:Part Design → Créer une fonction soustractive → Cavité
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Protrusion](PartDesign_Pad/fr.md)
---

# PartDesign Pocket/fr

## Description

L\'outil **Cavité** découpe des solides en extrudant une esquisse ou une face d\'un solide le long d\'une trajectoire droite.

![](images/PartDesign_Pocket_example.svg ) *Le profil d\'esquisse (A) a été appliqué sur la face de dessus du solide (B) ; le résultat après l\'opération de cavité est montré à droite.*

## Utilisation

1.  Sélectionnez l\'esquisse ou la face recevant la cavité. {{Version/fr|0.20}} : Vous pouvez également sélectionner plusieurs esquisses ou faces.
2.  Appuyez sur le bouton **<img src="images/PartDesign_Pocket.svg" width=16px> '''Cavité'''**.
3.  Définissez les paramètres de la cavité, voir les [Options](#Options.md) ci-dessous.
4.  Cliquez sur **OK**.

Lors de la sélection d\'une seule esquisse, celle-ci peut comporter plusieurs profils fermés à l\'intérieur d\'un profil plus grand, par exemple un rectangle contenant deux cercles. Mais les profils ne peuvent pas se croiser. {{Version/fr|0.20}}

## Options

Lors de la création de la protrusion, la boîte de dialogue **Paramètres de la cavité** s\'affiche. Elle offre les paramètres suivants :

![](images/pocket_parameters_cropped.png )

### Type

Type offre cinq façons différentes de spécifier la longueur à laquelle la cavité sera extrudée :

#### Dimension

Entrez une valeur numérique pour la longueur de la cavité. La direction par défaut de l\'extrusion est vers le support, mais elle peut être modifiée en cochant l\'option **Inversé**. Les extrusions se produisent par défaut selon la [normale](https://fr.wikipedia.org/wiki/Normale_(g%C3%A9om%C3%A9trie)) au plan d\'esquisse de définition. Cela peut être modifié en spécifiant une autre **Direction** {{Version/fr|0.20}}. Avec l\'option **Symétrique au plan**, la cavité s\'étendra sur la moitié de la longueur donnée de chaque côté du plan. Les dimensions négatives ne sont pas possibles. Utilisez plutôt l\'option **Inversé**.

#### À travers tout 

La cavité sera extrudée à travers tous les objets dans le sens de l\'extrusion. Avec l\'option **Symétrique au plan**, la cavité traversera tous les matériaux dans les deux sens.**Remarque :** Pour des raisons techniques, **À travers tout** est en fait une cavité de 10 mètres de profondeur. Si vous avez besoin de cavités plus profondes, utilisez le type **Dimension**.

#### Au premier 

La cavité sera extrudée jusqu\'à la première face du support dans le sens de l\'extrusion. En d\'autres termes, elle coupera tout le matériau jusqu\'à ce qu\'elle atteigne un espace vide.

#### Jusqu\'à la face 

La cavité sera extrudée jusqu\'à une face du modèle qui peut être choisie en cliquant dessus.

#### Deux dimensions 

Permet de saisir une seconde valeur de longueur pour prolonger la cavité dans la direction opposée (à travers le support). Les directions peuvent être inversées en cochant l\'option *Inversé*.

### Longueur

Définit la longueur de la cavité. Plusieurs unités peuvent être utilisées, indépendamment des préférences de l\'utilisateur (m, cm, mm, nm, ft ou \' pour pieds, in ou \" pour pouces). Cette option n\'est disponible que lorsque **Type** est soit **Dimension** soit **Deux dimensions**.

### Décalage par rapport à la surface 

Décalage de la surface à laquelle la cavité se terminera. Cette option n\'est disponible que lorsque le *Type* est soit **À travers tout**, **Au premier** ou **Jusqu\'à la face**.

### Direction


{{Version/fr|0.20}}

#### Direction/arête

Vous pouvez sélectionner la direction de la protrusion :

-   **Normale à l\'esquisse** L\'esquisse ou la face est extrudée le long de sa normale. Si vous avez sélectionné plusieurs esquisses ou faces à extruder, la normale de la première sera utilisée. {{Version/fr|0.20}}
-   **Sélectionnez une reference\...** L\'esquisse est extrudée le long d\'une arête du modèle 3D. Lorsque cette méthode est sélectionnée, vous pouvez cliquer sur n\'importe quelle arête du modèle 3D. Celle-ci devient alors le vecteur de direction pour la protrusion.
-   **Direction personnalisée** L\'esquisse est extrudée selon une direction qui peut être spécifiée par des valeurs vectorielles.

#### Afficher la direction 

Si cette case est cochée, la direction de la cavité sera affichée. Si la cavité utilise une **direction personnalisée**, elle peut être modifiée.

#### Longueur le long de la normale à l\'esquisse 

Si cette case est cochée, la longueur de la cavité est mesurée le long de la normale à l\'esquisse, sinon le long de la direction personnalisée.

### Symétrique au plan 

Cochez la case pour extruder la moitié de la longueur donnée de chaque côté de l\'esquisse ou du plan.

### Inversé

Inverse la direction de la cavité.

### Angle de dépouille/contre dépouille 


{{Version/fr|0.20}}

Génère la cavité dans le sens de l\'extrusion selon l\'angle donné. Un angle positif signifie que le bord extérieur de la cavité s\'élargit. Cette option n\'est disponible que si le **Type** est mis soit à **Dimension** soit à **Deux dimensions**. Notez que les structures internes reçoivent l\'angle d\'inclinaison opposée. Ceci est fait pour faciliter la conception de moules et de pièces moulées.

Limitations :

-   Les esquisses contenant des [B-splines](B-Splines/fr.md) ne peuvent souvent pas être correctement formées. Il s\'agit d\'une limitation du noyau [OpenCASCADE](OpenCASCADE/fr.md) que FreeCAD utilise.
-   Pour des angles plus importants, le cône échouera si la dernière face de la cavité a moins d\'arêtes que la face/esquisse de départ.

### 2ème longueur 

Définit la longueur de la cavité dans le sens d\'extrusion opposé. Plusieurs unités peuvent être utilisées indépendamment des préférences de l\'utilisateur (m, cm, mm, nm, ft ou \', in ou \"). Cette option n\'est disponible que si le **Type** est à **Deux dimensions**.

### 2ème angle de dépouille/contre dépouille 


{{Version/fr|0.20}}

Génère la cavité dans le sens opposé de l\'extrusion selon l\'angle donné. Un angle positif signifie que le bord extérieur de la protrusion s\'élargit. Cette option n\'est disponible que si le **Type** est à **Deux dimensions**. Notez que les structures internes reçoivent l\'angle d\'inclinaison opposé. Ceci est fait pour faciliter la conception de moules et de pièces moulées.

## Propriétés

-    **Type**: Type de manière dont la cavité sera extrudée, voir [Options](#Options.md).

-    **Length**: Définit la longueur de la cavité, voir [Options](#Options.md).

-    **Length2**: Deuxième longueur de la cavité si le **Type** est **TwoLengths**, voir [Options](#Options.md).

-    **Use Custom Vector**: {{Version/fr|0.20}}. Si coché, la direction de la cavité ne sera pas le vecteur normal de l\'esquisse mais le vecteur donné, voir [Options](#Options.md).

-    **Direction**: {{Version/fr|0.20}} Vecteur de la direction de la cavité si **Use Custom Vector** est utilisé.

-    **Along Sketch Normal**: {{Version/fr|0.20}} Si *true*, la longueur de la cavité est mesurée le long de la normale à l\'esquisse. Sinon et si **Use Custom Vector** est utilisé, elle est mesurée le long de la direction personnalisée.

-    **Up To Face**: La face vers laquelle la cavité sera extrudée, voir [Options](#Options.md).

-    **Refine**: True ou false. Nettoie les bords résiduels laissés après l\'opération. Cette propriété est initialement définie en fonction des paramètres de l\'utilisateur (trouvés dans **Préférences → Conception de la pièce → Général → Paramètres du modèle**). Elle peut être modifiée manuellement par la suite. Cette propriété sera enregistrée avec le document FreeCAD.

## Limitations

-   Utilisez le type **Dimension** ou **À travers tout** dans la mesure du possible, car les autres types peuvent parfois causer problème lorsque la cavité est utilisée pour une répétition linéaire ou circulaire.
-   La fonction cavité partage les mêmes [limitations](PartDesign_Pad/fr#Limitations.md) que la fonction protrusion.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/fr
