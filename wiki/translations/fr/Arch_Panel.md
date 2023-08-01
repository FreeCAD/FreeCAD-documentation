---
- GuiCommand:
   Name:Arch Panel
   Name/fr:Arch Panneau
   MenuLocation:Arch → Outils pour les  panneaux → Panneau
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**P** **A**
   Version:0.15
   SeeAlso:[Arch Découpe de panneau](Arch_Panel_Cut/fr.md), [Arch Feuille de panneaux](Arch_Panel_Sheet/fr.md)
---

# Arch Panel/fr

## Description

Cet outil vous permet de créer toutes sortes d\'éléments semblables à des panneaux, généralement pour des constructions de panneaux comme le projet [WikiHouse](http://www.wikihouse.cc/), mais aussi pour toutes sortes d\'objets qui sont basés sur un profil plat.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*L\'image ci-dessus montre une série d\'objets panneaux, simplement réalisés à partir de contours 2D importés d\'un fichier DXF. Ils peuvent ensuite être tournés et assemblés pour créer des structures.*

Depuis la version {{VersionPlus/fr|0.17}}, Arch Panneau peut également être utilisé pour créer des profils ondulées ou trapézoïdaux:

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">



## Utilisation

1.  Sélectionnez une forme 2D (objet Draft, face ou esquisse)
2.  Cliquez sur le bouton **<img src="images/Arch_Panel.svg" width=16px> [Panneau](Arch_Panel/fr.md)
**, appuyez les touche **P** puis **A**
3.  Ajustez les propriétés souhaitées

### Limitations

-   Il n\'existe actuellement aucun système automatique permettant de produire des feuilles de découpe en 2D à partir de panneaux, mais cette fonctionnalité est prévue et sera ajoutée à l\'avenir.

## Options

-   L\'outil Panneaux partage les propriétés et comportements communs de tous les composants [Arch Composants](Arch_Component/fr.md)
-   L\'épaisseur d\'un panneau peut être réglée après la création
-   Appuyez sur le bouton **Echap** ou **Annuler** pour abandonner la commande en cours.
-   Un double-clic sur le panneau dans la vue enarborescence après sa création permet d\'entrer en mode édition et d\'accéder et de modifier ses ajouts et soustractions.
-   Il est possible de créer automatiquement des panneaux composés de plus d\'une feuille d\'un matériau, en augmentant sa propriété Sheets.
-   Les panneaux peuvent faire appel à <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [Arch Matériaux multiples](Arch_MultiMaterial/fr.md). Lorsqu\'on utilise un multi-matériau, le panneau devient multi-couche, en utilisant les épaisseurs spécifiées par le multi-matériau. Toute couche dont l\'épaisseur est égale à zéro verra son épaisseur définie automatiquement par l\'espace restant défini par la valeur Thickness du panneau, après soustraction des autres couches.



## Propriétés

-    **Length**: La longueur du panneau

-    **Width**: La largeur du panneau

-    **Thickness**: L\'épaisseur du panneau

-    **Area**: La surface du panneau (automatique)

-    **Sheets**: Le nombre de feuilles de matériau dont est composé le panneau.

-    **Wave Length**: La longueur de l\'ondulation pour les panneaux ondulés.

-    **Wave Height**: La hauteur de l\'ondulation pour les panneaux ondulés.

-    **Wave Type**: Le type de l\'ondulation pour les panneaux ondulés, courbe, trapézoïdale ou en pointe.

-    **Wave Direction**: L\'orientation des ondulations pour les panneaux ondulés.

-    **Bottom Wave**: Si l\'ondulation du fond du panneau est plate ou non.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Panneau peut-être utilisé dans une [macro](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Crée un objet `Panel` à partir du `baseobj` donné qui est un profil fermé et de l\'extrusion donnée `thickness`.
    -   Si aucun `baseobj` n\'est indiqué, vous pouvez fournir les valeurs numériques pour `length`, `width` et `thickness` pour créer un bloc panneau.
-   Si un `placement` est donné, il est utilisé.

Exemple: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```



## Tutoriels

-   [Tutoriel de portage Wikihouse](Wikihouse_porting_tutorial/fr.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel/fr
