---
 GuiCommand:
   Name: Draft Scale
   Name/fr: Draft Échelle
   MenuLocation: Draft/BIM : Modification , Mettre à l'échelle
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   Shortcut: **S** **C**
   SeeAlso: Draft_SubelementHighlight/fr, Draft_Clone/fr
---

# Draft Scale/fr

## Description

La commande <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> **Draft Échelle** met à l\'échelle ou copie les objets sélectionnés autour d\'un point de base. En mode sous-élément, la commande met à l\'échelle les points et les arêtes sélectionnés de [Draft Lignes](Draft_Line/fr.md) et [Draft Polylignes](Draft_Wire/fr.md).

Cette commande peut être utilisée sur des objets 2D créés avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi sur de nombreux objets 3D tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md), l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ou l\'[atelier BIM](BIM_Workbench/fr.md).

<img alt="" src=images/Draft_Scale_example.png  style="width:400px;"> 
*Mise à l'échelle d'un objet autour d'un point de base*

## Usage

Voir aussi : [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Vous pouvez sélectionner un ou plusieurs objets, ou un ou plusieurs sous-éléments de [Draft Lignes](Draft_Line/fr.md) ou [Draft Polylignes](Draft_Wire/fr.md).
2.  Il existe plusieurs manières de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Scale.svg" width=16px> [Draft Mettre à l'échelle](Draft_Scale/fr.md)**.
    -   [Draft](Draft_Workbench/fr.md) : sélectionnez l\'option **Modification → <img src="images/Draft_Scale.svg" width=16px> Mettre à l'échelle** du menu.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Modification → <img src="images/Draft_Scale.svg" width=16px> Mettre à l'échelle** du menu.
    -   Utilisez le raccourci clavier : **S** puis **C**.
3.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet dans la [vue 3D](3D_view/fr.md).
4.  Le panneau des tâches **Échelle** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
5.  Si des sous-éléments ont été sélectionnés : cochez la case **Modifier les sous-éléments** pour activer le mode sous-élément.
6.  Choisissez le point de base dans la [vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrer un point**.
7.  Entrez les facteurs d\'échelle X, Y et Z.
8.  Appuyez sur **Entrée** ou sur le bouton **OK** pour terminer la commande.

## Options



### Premier panneau des tâches 

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement les coordonnées du point de base, saisissez les composantes X, Y et Z et appuyez sur **Entrée** après chacune. Ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrer un point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **G** ou cochez la case **Global** pour basculer en mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées de [Draft Plan de travail](Draft_SelectPlane/fr.md).
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur le bouton **Fermer** pour annuler la commande.



### Deuxième panneau de tâches 

-   Entrez les facteurs X, Y et Z pour définir l\'échelle. Les valeurs doivent être supérieures à zéro.
-   Cochez la case **Mise à l'échelle uniforme** pour verrouiller les facteurs X, Y et Z sur la même valeur.
-   Si la case **Orientation du plan de travail** est cochée, les facteurs d\'échelle sont relatifs au système de coordonnées de [Draft Plan de travail](Draft_SelectPlane/fr.md), sinon ils sont relatifs au système de coordonnées global.
-   Si la case **Copier** est cochée, une copie à l\'échelle de l\'objet d\'origine est créée. Cela ne fonctionne que pour les objets Draft qui ont une propriété **Points**, tels que [Draft Polylignes](Draft_Wire/fr.md).
-   Si la case **Modifier les sous-éléments** est cochée, la commande utilisera les sous-éléments sélectionnés au lieu de l\'ensemble des objets. Les sous-éléments doivent appartenir à [Draft Lignes](Draft_Line/fr.md) ou [Draft Polylignes](Draft_Wire/fr.md).
-   Si la case **Créer un clone** est cochée, les [Draft Clones](Draft_Clone/fr.md) des objets originaux sont créés. Cela fonctionne pour tous les types d\'objets. Pour les objets qui ne sont pas des objets Draft ou pour les objets Draft qui n\'ont pas de propriété **Points**, cette option **doit** être sélectionnée.
-   Appuyez sur le bouton **Sélectionnez à partir de/vers les points** et sélectionnez deux points supplémentaires dans la [vue 3D](3D_view/fr.md) pour calculer les facteurs d\'échelle. Cela cochera automatiquement la case **Mise à l'échelle uniforme**. Les facteurs d\'échelle X, Y et Z seront donc égaux et seront réglés sur la distance entre le point de base et le point \"à partir de\" divisé par la distance entre le point de base et le point \"vers\".
-   Appuyez sur **Échap** ou sur le bouton **Annuler** pour annuler la commande.



## Remarques

-   La commande peut également mettre à l\'échelle des [plans d\'image](Image_CreateImagePlane/fr.md) mais pas en mode clone.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour resélectionner les objets de base après avoir copié des objets : **Édition → Préférences... → Draft → Général → Sélectionner les objets de base après la copie**.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour mettre à l\'échelle des objets, utilisez la méthode `scale` du module Draft.


```python
scaled_list = scale(objectslist, scale=Vector(1,1,1), center=Vector(0,0,0), copy=False)
```

-    `objectslist`contient les objets à mettre à l\'échelle. Il s\'agit soit d\'un objet unique, soit d\'une liste d\'objets.

-    `scale`est le vecteur qui spécifie les facteurs d\'échelle X, Y et Z.

-    `center`est le point central de l\'opération de mise à l\'échelle.

-   Si `copy` est `True`, des copies sont créées au lieu de mettre à l\'échelle les objets originaux.

-    `scaled_list`est retourné avec les objets originaux mis à l\'échelle, ou avec les nouvelles copies. Il s\'agit soit d\'un objet unique, soit d\'une liste d\'objets, en fonction de `objectslist`.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pts = [App.Vector(0, 0, 0), App.Vector(500, 500, 0), App.Vector(600, 0, 0)]
wire1 = Draft.make_wire(pts, closed=True)
doc.recompute()

scale1 = App.Vector(2.3, 0.75, 0)
wire2 = Draft.scale(wire1, scale1, copy=True)
doc.recompute()

scale2 = App.Vector(-2, -1.5, 0)
wires = Draft.scale([wire1, wire2], scale2, copy=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Scale/fr
