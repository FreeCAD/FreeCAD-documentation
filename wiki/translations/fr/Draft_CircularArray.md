---
- GuiCommand:/fr
   Name:Draft PolarArray
   Name/fr:Draft Réseau circulaire
   MenuLocation:Modification → Array tools → Circular array
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Draft Réseau orthogonal](Draft_OrthoArray.md), [Draft Réseau polaire](Draft_PolarArray/fr.md), [Draft Chemin pour série de copies](Draft_PathArray/fr.md), [Draft Réseau lié selon une courbe](Draft_PathLinkArray/fr.md), [Draft Réseau de points](Draft_PointArray/fr.md), [Draft Réseau lié selon des points](Draft_PointLinkArray/fr.md)
---

# Draft CircularArray/fr

## Description

La commande <img alt="" src=images/Draft_CircularArray.svg  style="width:24px;"> **Draft Réseau circulaire** crée un réseau à partir d\'un objet sélectionné en plaçant des copies le long de circonférences concentriques. La commande peut éventuellement créer un réseau [Link](App_Link/fr.md), plus efficace qu\'un réseau normal.

Cette commande peut être utilisée sur des objets 2D créés avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi sur de nombreux objets 3D tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md), l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ou l\'[atelier Arch](Arch_Workbench/fr.md).

<img alt="" src=images/Draft_CircularArray_example.png  style="width:400px;"> 
*Un réseau circulaire Draft*

## Utilisation

Voir aussi : [Draft Accrochage](Draft_Snap/fr.md).

1.  Optionnellement, sélectionnez un objet.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_CircularArray.svg" width=16px> [Circular Array](Draft_CircularArray/fr.md)**.
    -   Sélectionnez l\'option **Modification → Array tools → <img src="images/Draft_CircularArray.svg" width=16px> Circular array** dans le menu.
3.  Le panneau de tâches **Réseau circulaire** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez en un.
5.  Saisissez les paramètres requis dans le panneau des tâches.
6.  Pour terminer la commande, effectuez l\'une des opérations suivantes :
    -   Choisissez un point dans la [Vue 3D](3D_view/fr.md) pour le **Centre de rotation**.
    -   Appuyez sur **Entrée**.
    -   Appuyez sur le bouton **OK**.

## Options

-   Entrez la **Distance radiale** pour spécifier la distance entre les couches circulaires et entre le centre et la première couche circulaire.
-   Entrez la **Distance tangentielle** pour spécifier la distance entre les éléments d\'une même couche circulaire. Elle doit être supérieure à zéro.
-   Entrez le **Nombre de couches circulaires**. L\'élément au centre compte pour une couche. Doit être au moins {{Value|2}}. Le maximum pouvant être saisi dans le panneau de tâches est {{Value|99}}, mais des valeurs plus élevées sont possibles en modifiant la propriété {{PropertyData/fr|Number Circles}} du tableau.
-   Saisissez la valeur **Symétrie**. Ce nombre détermine la façon dont les éléments sont répartis. Une valeur de {{Value|3}}, par exemple, donne un motif comportant trois secteurs égaux de 120°. Des valeurs plus élevées pour la **Symétrie** et la **Distance tangentielle** permettent d\'obtenir moins d\'éléments, voire aucun, sur les couches internes.
-   Choisissez un point dans la [Vue 3D](3D_view/fr.md), notez que cela terminera également la commande ou rentrez des coordonnées pour le **Centre de rotation**. L\'axe de rotation du réseau passera par ce point. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur le bouton **Réinitialiser le point** pour réinitialiser le **Centre de rotation** à l\'origine.
-   Si la case **Union** est cochée, les éléments qui se chevauchent dans le réseau seront fusionnés. Cela ne fonctionne pas pour les réseaux de liens.
-   Si la case **Réseau de liens** est cochée, un réseau de liens est créé au lieu d\'un réseau normal. Un réseau de liens est plus performant car ses éléments sont des objets [App Link](App_Link/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour abandonner la commande.

## Remarques

-   L\'axe de rotation par défaut du tableau est l\'axe Z positif. Il peut être modifié en éditant sa propriété {{PropertyData/fr|Axis}}.
-   Un Draft Réseau circulaire peut être transformé en un [Draft Réseau orthogonal](Draft_OrthoArray/fr.md) ou un [Draft Réseau polaire](Draft_PolarArray/fr.md) en modifiant sa propriété {{PropertyData/fr|Array Type}}.
-   Un réseau de liens ne peut pas être transformé en un réseau normal ou vice versa. Le type de réseau doit être décidé au moment de la création.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées et des distances : **Edition → Préférences... → Général → Unités → Systèmes d'unités → Nombre de décimales**.

## Propriétés

Voir [Draft Réseau orthogonal](Draft_OrthoArray/fr#Propri.C3.A9t.C3.A9s.md).

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer un réseau circulaire, utilisez la méthode `make_array` ({{Version/fr|0.19}}) de l\'atelier Draft. Cette méthode remplace la méthode dépréciée `makeArray`. La méthode `make_array` peut créer des [Draft Réseaux orthogonaux](Draft_OrthoArray/fr.md), [Draft Réseaux polaires](Draft_PolarArray/fr.md) et Draft Réseaux circulaires. Pour chaque type de réseau, une ou plusieurs enveloppes sont disponibles.

La méthode principale :


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

L\'enveloppe pour les réseaux circulaires est :


```python
array = make_circular_array(base_object,
                            r_distance=100, tan_distance=50,
                            number=3, symmetry=1,
                            axis=App.Vector(0, 0, 1), center=App.Vector(0, 0, 0),
                            use_link=True)
```

-    `base_object`est l\'objet à mettre en réseau. Il peut également s\'agir d\'un `Label` (chaîne de caractères) d\'un objet du document en cours.

-    `r_distance`et `tan_distance` sont les distances radiale et tangentielle entre les éléments.

-    `number`est le nombre de couches circulaires dans le motif, l\'objet original comptant comme la première couche.

-    `symmetry`est un nombre entier utilisé dans certains calculs qui affectent la façon dont les éléments sont répartis sur les circonférences. Les valeurs habituelles vont de 1 à 6. Les valeurs plus élevées ne sont pas recommandées et font disparaître les éléments des couches intérieures.

-    `axis`et `center` sont des vecteurs qui décrivent la direction de l\'axe de rotation et un point par lequel cet axe passe.

-   Si `use_link` est `True`, les éléments créés sont des [App Links](App_Link/fr.md) au lieu de copies ordinaires.

-    `array`est retourné avec l\'objet réseau créé.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)

array = Draft.make_circular_array(tri, 1800, 1200, 4, 1)
doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CircularArray/fr
