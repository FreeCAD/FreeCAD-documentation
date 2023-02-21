---
- GuiCommand:/fr
   Name:Arch Structure
   Name/fr:Arch Structure
   MenuLocation:Arch → Outils pour les strutures → Structure
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**S** **T**
   SeeAlso:[Arch Mur](Arch_Wall/fr.md), [Arch Armature personnalisée](Arch_Rebar/fr.md)
---

# Arch Structure/fr

## Description

L\'outil [Arch Structure](Arch_Structure/fr.md) vous permet de construire les éléments structurels, tels que des colonnes ou des poutres, en précisant leur largeur, longueur et hauteur ou en les basant sur un profil 2D (face, polyligne ou esquisse).

Si aucun profil n\'est fourni, un ensemble de préréglages est disponible pour construire rapidement un élément structurel à partir d\'un profil standard prédéfini.

![](images/Arch_Structure_example.jpg ) 
*Colonne basée sur un profil de base 2D ; une colonne et une poutre définies par leur hauteur, leur longueur et leur largeur, sans profil de base ; une structure métallique basée sur une face 2D*



## Utilisation

-   Sélectionnez une forme 2D (objet Draft, une face ou une esquisse) (en option).
-   Appuyez sur le bouton **<img src="images/Arch_Structure.svg" width=16px> [Structure](Arch_Structure/fr.md)** ou appuyez sur les touches **S** puis **T**.
-   Réglez les propriétés désirées.

## Options

-   Lorsqu\'aucun objet 2D de base n\'est sélectionné, l\'outil Structure dispose de 2 modes de dessin: colonne et poutre :
    -   En mode colonne, il vous est demandé de choisir un point à l\'écran ou en entrant les coordonnées. Le nouvel objet de structure sera placé à cet endroit.
    -   En mode poutre, il vous est demandé de choisir deux points à l\'écran ou en entrant les coordonnées. Le nouvel objet structurel s\'étendra entre ces deux points.
-   Les éléments structurels partagent les propriétés communes et les comportements de tous les [Arch Composants](Arch_Component/fr.md)
-   La hauteur, la largeur et la longueur d\'une structure peuvent être modifiées après création.
-   Appuyez sur les touches **Echap** ou le bouton **Annuler** pour annuler la commande en cours.
-   Double-cliquer sur la structure dans l\'arborescence après sa création vous permet d\'entrer dans le mode édition pour accéder et modifier ses ajouts et retraits.
-   En mode édition, il est également possible d\'ajouter un [système d\'axes](Arch_Axis/fr.md) à l\'élément structurel. Lors de l\'ajout d\'un système d\'axes, l\'élément structurel sera copié une fois sur chaque axe du système. Lors de l\'ajout de deux systèmes d\'axes, l\'élément structurel sera copié une fois sur chaque point d\'intersection des deux systèmes.



## Propriétés



### Données

-    **Tool**: un chemin d\'extrusion facultatif, qui peut être n\'importe quel type de fil. Si cette propriété est vide, l\'extrusion sera droite et se déroulera dans le sens indiqué par la propriété Normal.

-    **Normal**: spécifie la direction dans laquelle la face de base de cette structure sera extrudée. Si cette propriété est maintenue à (0,0,0), la direction sera automatiquement définie sur la direction normale de la face de base.

-    **Face Maker**: spécifie le type d\'algorithme de génération de face à utiliser pour créer le profil. Les choix sont None, Simple, Cheese and Bullseye.

-    **Length**: spécifie la longueur de la structure. Ceci n\'est utilisé que si la structure n\'est pas basée sur un profil.

-    **Width**: spécifie la largeur de la structure. Ceci n\'est utilisé que si la structure n\'est pas basée sur un profil.

-    **Height**: spécifie la hauteur de la structure ou la longueur d\'extrusion lorsqu\'elle est basée sur un profil. Si aucune hauteur n\'est donnée et que la structure est à l\'intérieur d\'un objet [Arch Niveaux](Arch_Floor/fr.md) avec sa hauteur définie, la structure prendra automatiquement la valeur de la hauteur du sol.

-    **Nodes Offset**: spécifie un décalage facultatif entre la ligne médiane et la ligne des nœuds.



### Vues

-    **Nodes Type**: type de nœuds structurels de cet objet, linéaire ou zone.

-    **Show Nodes**: affiche ou masque les nœuds structurels.



## Prérequis

L\'outil Structure dispose aussi d\'une série de préréglages qui permettent de construire rapidement des profils métalliques standard ou d\'éléments préfabriqués en béton.

![](images/Arch_presets_example.jpg ) 
*Quelques préréglages pour les structures en acier*

Les présélections sont obtenues en choisissant une **Catégorie** à partir du panneau d\'options de structure. Les catégories disponibles sont **Béton préfabriqué** ou un des profilés métalliques standard de l\'industrie tels que **HEA**, **HEB** ou **INP**. Pour chacune de ces catégories, un certain nombre de préréglages est disponible. Une fois qu\'une présélection est choisie, ses propres paramètres tels que **Longueur**, **Largeur** ou **Hauteur** peuvent être ajustés. Cependant, pour des profilés métalliques, la taille du profil est définie par le préréglage et ne peut pas être modifiée.

Le bouton **Commutateur L/H** peut être utilisé pour intervertir les valeurs de longueur et de hauteur, et ainsi construire une poutre horizontale plutôt qu\'une colonne verticale.

<img alt="" src=images/Arch_precast_example.jpg  style="width:960px;"> 
*Quelques préréglages pour les structures préfabriquées en béton*



## Structure des nœuds 

L\'objet structurel a également la possibilité d\'afficher les nœuds structurels. les nœuds structurels sont une séquence de points 3D stockés dans la propriété \"nœuds\". Dans propriété \"Afficher les nœuds\" sélectionnez on/off, on peut voir les nœuds structurels d\'un élément de structure :

<img alt="" src=images/Arch_structural_nodes.jpg  style="width:960px;"> 
*Nœuds structurels rendus visibles pour un ensemble de structures*

-   Les nœuds sont calculés et mis à jour automatiquement, tant que vous ne les modifiez pas manuellement. Si vous le faites manuellement, et que la forme de l\'objet change sa structure ils ne seront pas mis à jour, à moins que vous n\'utilisiez l\'outil « Reset nœuds » ci-dessous.
-   Les structures Arch peuvent avoir non seulement des nœuds linéaires, mais aussi des nœuds planaires. Pour cela, 1- Il doit y avoir au moins 3 vecteurs dans la propriété \"Nodes\" de l\'objet, 2- la propriété \"NodesType\" de leur ViewObject doit être réglée sur \"Surface\".
-   Lorsque le calcul des nœuds est automatique (d\'office, si vous ne les touchez pas manuellement), lors de la création de la propriété Rôle d\'une structure à \"Slab\", il deviendra automatiquement un nœud plat (il y aura plus de 3 vecteurs et NodesType sera réglé sur \"Surface\").
-   Lors de la modification d\'un objet de structure (double-clic), une série d\'outils pour les nœuds est disponible dans la vue \"Tâche\" :
    -   Réinitialiser les nœuds lancera le calcul automatique, dans le cas où vous les modifiez manuellement.
    -   Modifier les nœuds graphiquement, fonctionne de la même manière que dans [Draft Éditer](Draft_Edit/fr.md).
    -   Étendre les nœuds de l\'objet modifié jusqu\'à ce qu\'il touchent le nœud d\'un autre objet.
    -   Construire le nœud de cet objet et le rendre coïncidant à un autre.
    -   Activer/désactiver l\'affichage de tous les nœuds de tous les objets structurels du document



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Structure peut être utilisé dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Structure = makeStructure(baseobj=None, height=None)
Structure = makeStructure(baseobj=None, length=None, width=None, height=None, name="Structure")
```

-   Créer un objet `Structure` à partir du `baseobj` donné, qui est un profil fermé, et de l\'extrusion donnée `height`.
    -   Si aucun `baseobj` n\'est donné, vous pouvez fournir les valeurs numériques pour `length`, `width`, et `height` pour créer une structure de bloc.

    -   
        `baseobj`
        
        peut également être n\'importe quel objet solide existant.

Exemple : 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(200, 300)
Structure1 = Arch.makeStructure(Rect, height=2000)
FreeCAD.ActiveDocument.recompute()

Structure2 = Arch.makeStructure(None, length=500, width=1000, height=3000)
Draft.move(Structure2, FreeCAD.Vector(2000, 0, 0))
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Structure/fr
