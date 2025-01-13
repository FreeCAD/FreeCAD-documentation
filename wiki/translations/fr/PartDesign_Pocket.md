---
 GuiCommand:
   Name: PartDesign_Pocket
   Name/fr: PartDesign Cavité
   MenuLocation: PartDesign , Créer une fonction soustractive , Cavité
   Workbenches: PartDesign_Workbench/fr
   SeeAlso: PartDesign_Pad/fr
---

# PartDesign Pocket/fr

## Description

L\'outil **Cavité** découpe des solides en extrudant une esquisse ou une face d\'un solide le long d\'une trajectoire droite.

![](images/PartDesign_Pocket_example.svg ) *Le profil d\'esquisse (A) a été appliqué sur la face de dessus du solide (B) ; le résultat après l\'opération de cavité est montré à droite.*



## Utilisation

1.  Sélectionnez une seule esquisse ou une ou plusieurs faces du corps.
2.  Appuyez sur le bouton **<img src="images/PartDesign_Pocket.svg" width=16px> [Cavité](PartDesign_Pocket/fr.md)**.
3.  Définissez les paramètres de la cavité, voir les [Options](#Options.md) ci-dessous.
4.  Appuyez sur le bouton **OK**.

## Options

Lors de la création d\'une cavité, ou après avoir double-cliqué sur une cavité existante dans la [vue en arborescence](Tree_view/fr.md), le panneau de tâches **Paramètres de la cavité** s\'affiche. Il propose les paramètres suivants :

![](images/PartDesign_Pocket_Taskpanel.png )

### Type

Type offre cinq façons différentes de spécifier la longueur de la cavité :

#### Dimension

Entrez une valeur numérique pour la **longueur** de la cavité. Avec l\'option **Symétrique au plan**, la cavité s\'étendra à la moitié de la longueur donnée de chaque côté de l\'esquisse ou de la face.



#### À travers tout 

La cavité s\'étendra jusqu\'à la dernière face du support qu\'elle rencontre dans sa direction. Avec l\'option **Symétrique au plan**, la cavité traversera tous les matériaux dans les deux directions. Remarquez que pour des raisons techniques, *A travers tout* est en fait une cavité de 10 mètres de profondeur. Si vous avez besoin de cavités plus profondes, utilisez le type **Dimension**.



#### La plus proche 

La cavité sera prolongée jusqu\'à la première face du support qu\'elle rencontrera dans sa direction.



#### Jusqu\'à une face 

La cavité sera prolongée jusqu\'à une face. Appuyez sur le bouton **Sélectionner une face** et sélectionnez une face ou un [plan de référence](PartDesign_Plane/fr.md) du corps.



#### Deux dimensions 

Cela permet d\'entrer une deuxième longueur pour laquelle la cavité doit s\'étendre dans la direction opposée. Les directions peuvent être inversées en cochant l\'option **Inversé**.



#### Jusqu\'à une forme 


{{Version/fr|1.0}}

: la cavité s\'étend jusqu\'à la forme sélectionnée. Vous pouvez appuyer sur le bouton **Sélectionner une forme** et sélectionnez une forme. Laissez la case **Sélectionner toutes les faces** activée ou désactivez-la, appuyez sur le bouton **Sélectionner des faces** et sélectionnez les faces jusqu\'où la cavité doit aller.



### Décalage par rapport à la surface 

Décalage par rapport à la face à laquelle la cavité se terminera. Cette option n\'est disponible que si **Type** est soit **À travers tout**, **La plus proche** ou **Jusqu\'à une face**.



### Longueur

Définit la longueur de la cavité. Cette option n\'est disponible que si **Type** est **Dimension** ou **Deux dimensions**. La longueur est mesurée le long du vecteur de direction, ou le long de la normale de l\'esquisse ou de la face. Les valeurs négatives ne sont pas possibles. Utilisez plutôt l\'option **Inverser**.



### 2ème longueur 

Définit la longueur de la cavité dans le sens opposé. Cette option n\'est disponible que si **Type** est sur **Deux dimensions**.



### Symétrique au plan 

Cochez cette option pour étendre la cavité de la moitié de la longueur donnée de chaque côté de l\'esquisse ou de la face, si **Type** est sur **Dimension**, ou **À travers tout** si c\'est **Type**.



### Inverser

Inverse la direction de la cavité.



### Direction



#### Direction/arête

Vous pouvez sélectionner la direction de la protrusion :

-   **Normale à l\'esquisse** ou **Normale à la face** : l\'esquisse ou la face est extrudée dans la direction de sa normale. Si vous avez sélectionné plusieurs esquisses ou faces à extruder, c\'est la normale de la première qui sera utilisée.
-   **Sélectionner une référence\...** : l\'esquisse ou la face est extrudée dans la direction d\'une ligne droite ou d\'une [ligne de référence](PartDesign_Line/fr.md) sélectionnée du corps.
-   **Direction personnalisée** : l\'esquisse ou la face est extrudée dans la direction du vecteur spécifié.



#### Afficher la direction 

Si cette case est cochée, la direction de la cavité sera affichée. Si la cavité utilise **Direction personnalisée**, elle peut être modifiée.



#### Longueur le long de la normale à l\'esquisse 

Si cette case est cochée, la longueur de la cavité est mesurée le long de la normale de l\'esquisse ou de la face, sinon le long de la direction personnalisée.



### Angle de dépouille 

Génère la cavité dans le sens de l\'extrusion selon l\'angle donné. Un angle positif signifie que le bord extérieur de la cavité s\'élargit. Remarquez que les structures internes reçoivent l\'angle d\'inclinaison opposé. Ceci est fait pour faciliter la conception de moules et de pièces moulées. Cette option n\'est disponible que si le **Type** est sur **Dimension** ou **Deux dimensions**.



### 2ème angle de dépouille 

Génère la cavité dans le sens opposé de l\'extrusion selon l\'angle donné. Voir **Angle de dépouille**. Cette option n\'est disponible que si **Type** est sur **Deux dimensions**.



## Propriétés



### Données


{{TitleProperty|Part Design}}

-    **Refine|Bool**: vrai ou faux. Nettoie les arêtes résiduelles laissées après l\'opération. Cette propriété est initialement définie en fonction des paramètres de l\'utilisateur (dans **Préférences → PartDesign → Général → Paramètres des modèles**).


{{TitleProperty|Pocket}}

-    **Type|Enumeration**: définit la manière dont la cavité sera extrudée, voir [Options](#Options.md).

-    **Length|Length**: définit la longueur de la cavité, voir [Options](#Options.md).

-    **Length2|Length**: deuxième longueur de la cavité si **Type** est **TwoLengths**, voir [Options](#Options.md).

-    **Use Custom Vector|Bool**: si cette option est cochée, la direction de la cavité ne sera pas le vecteur normal de l\'esquisse mais le vecteur donné, voir [Options](#Options.md).

-    **Direction|Vector**: vecteur de la direction de la cavité si **Use Custom Vector** est utilisé.

-    **Reference Axis|LinkSub**
    

-    **Along Sketch Normal|Bool**: si *True*, la longueur de la cavité est mesurée le long de la normale de l\'esquisse. Sinon, et si **Use Custom Vector** est utilisé, elle est mesurée le long de la direction personnalisée.

-    **Up To Face|LinkSub**: une face vers laquelle la cavité sera extrudée, voir [Options](#Options.md).

-    **Offset|Length**
    

-    **Angle|Angle**
    

-    **Angle2|Angle**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Limitations

-   Utilisez le type **Dimension** ou **À travers tout** dans la mesure du possible, car les autres types peuvent parfois causer problème lorsque la cavité est utilisée pour une répétition linéaire ou circulaire.
-   La fonction cavité partage les mêmes [limitations](PartDesign_Pad/fr#Limitations.md) que la fonction protrusion.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/fr
