---
- GuiCommand:/fr
   Name:Arch Panel
   Name/fr:Arch Panneau
   MenuLocation:Arch → Pannels tools → Panneau
   Workbenches:[Arch](Arch_Module/fr.md)
   Shortcut:**P** **A**
   Version:0.15
   SeeAlso:[Arch Découpe de panneaux](Arch_Panel_Cut/fr.md), [Arch Panneau feuille](Arch_Panel_Sheet/fr.md)
---


</div>

## Description

Cet outil vous permet de créer toutes sortes d\'éléments semblables à des panneaux, généralement pour des constructions de panneaux comme le projet [WikiHouse](http://www.wikihouse.cc/) , mais aussi pour toutes sortes d\'objets qui sont basés sur un profil plat.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*L\'image ci-dessus montre une série d\'objets panneau, tout simplement fabriqués à partir de contours 2D importés à partir d\'un fichier DXF. Ils peuvent alors être entraînés en rotation et assemblés pour créer des structures.*

Depuis la version {{VersionPlus/fr|0.17}}, Arch Panneau peut également être utilisé pour créer des profils ondulées ou trapézoïdaux:

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">

## Utilisation

1.  Sélectionnez une forme 2D (objet draft, face ou esquisse)
2.  Cliquez sur le bouton **<img src="images/Arch_Panel.svg" width=16px>[Panneau](Arch_Panel/fr.md)
**, appuyez les touche **P** puis **A**
3.  Ajustez les propriétés souhaitées

### Limitations

-   Il n\'existe actuellement pas de système automatique pour produire des feuilles de coupe 2D à partir d\'objets du panneau, mais cette fonction est dans les plans et sera ajouté à l\'avenir.

## Options

-   L\'outil Pannels partage les propriétés et comportements communs de tous les composants [Arch Composants](Arch_Component/fr.md)
-   L\'épaisseur d\'un panneau peut être réglée après la création
-   Appuyez sur le bouton **Echap** ou **Annuler** pour abandonner la commande actuelle.
-   Un double-clic sur le panneau de l\'arborescence après sa création vous permet d\'entrer en mode d\'édition et d\'avoir l\'accès et de modifier ses additions et soustractions
-   Il est possible de faire automatiquement des groupes composés de plus d\'une feuille d\'un matériau, en augmentant sa propriété Feuilles.
-   Les panneaux peuvent utiliser la fonction <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [Arch Matériaux multiples](Arch_MultiMaterial/fr.md). Lors de l\'utilisation d\'un multi-matériau, le panneau deviendra multi-couche, en utilisant les épaisseurs spécifiées par les multi-matériaux. Toute couche avec une épaisseur de zéro aura son épaisseur définie automatiquement par l\'espace restant défini par la valeur d\'épaisseur du panneau, après avoir soustrait les autres couches.

## Propriétés

-    {{PropertyData/fr|Length}}: La longueur du panneau

-    {{PropertyData/fr|Width}}: La largeur du panneau

-    {{PropertyData/fr|Thickness}}: L\'épaisseur du panneau

-    {{PropertyData/fr|Area}}: La surface du panneau

-    {{PropertyData/fr|Sheets}}: Le nombre de feuilles de matériaux qui constituent le panneau

-    {{PropertyData/fr|Wave Length}}: La longueur de l\'ondulé du panneau

-    {{PropertyData/fr|Wave Height}}: La hauteur de l\'ondulé du panneau

-    {{PropertyData/fr|Wave Type}}: Le type d\'ondulation du panneau, courbe, trapézoïdal ou pointu

-    {{PropertyData/fr|Wave Direction}}: l\'orientation de l\'ondulé

-    {{PropertyData/fr|Bottom Wave}}: Si l\'ondulation du fond du panneau est plate ou non

## Script


**Voir aussi:**

[API](Arch_API/fr.md) and [Débuter avec les scripts](FreeCAD_Scripting_Basics.md).

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

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial/fr.md)


<div class="mw-translate-fuzzy">





</div>


 
