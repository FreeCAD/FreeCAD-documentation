---
 GuiCommand:
   Name: Arch Panel
   Name/fr: Arch Panneau
   MenuLocation: 3D/BIM , Panneau<br>Utilitaires , Outils pour les  panneaux , Panneau
   Workbenches: BIM_Workbench/fr
   Shortcut: **P** **A**
   Version: 0.15
   SeeAlso: Arch_Panel_Cut/fr, Arch_Panel_Sheet/fr
---

# Arch Panel/fr

## Description

L\'outil **Arch Panneau** vous permet de créer toutes sortes d\'éléments semblables à des panneaux, généralement pour des constructions de panneaux comme le projet [WikiHouse](https://www.wikihouse.cc/), mais aussi pour toutes sortes d\'objets qui sont basés sur un profil plat.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*L\'image ci-dessus montre une série d\'objets panneaux, simplement réalisés à partir de contours 2D importés d\'un fichier DXF. Ils peuvent ensuite être pivotés et assemblés pour créer des structures.*

Depuis la version {{VersionPlus/fr|0.17}}, Arch Panneau peut également être utilisé pour créer des profils ondulées ou trapézoïdaux :

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">



## Utilisation

1.  Sélectionnez une forme 2D (objet Draft, face ou esquisse).
2.  Cliquez sur le bouton **<img src="images/Arch_Panel.svg" width=16px> [Panneau](Arch_Panel/fr.md)**, appuyez les touche **P** puis **A**.
3.  Ajustez les propriétés souhaitées.

### Limitations

-   Il n\'existe actuellement aucun système automatique permettant de produire des feuilles de découpe en 2D à partir de panneaux, mais cette fonctionnalité est prévue et sera ajoutée à l\'avenir.

## Options

-   L\'outil Panneau partage les propriétés et comportements communs de tous les [Arch Composants](Arch_Component/fr.md).
-   L\'épaisseur d\'un panneau peut être réglée après la création.
-   Appuyez sur le bouton **Échap** ou **Annuler** pour abandonner la commande en cours.
-   Un double-clic sur le panneau dans la vue en arborescence après sa création permet d\'entrer en mode édition et d\'accéder et de modifier ses ajouts et soustractions.
-   Il est possible de créer automatiquement des panneaux composés de plus d\'une feuille d\'un matériau, en augmentant sa propriété Sheets.
-   Les panneaux peuvent faire appel à <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [Arch Multi-matériaux](Arch_MultiMaterial/fr.md). Lorsqu\'on utilise un multi-matériaux, le panneau devient multi-couche, en utilisant les épaisseurs spécifiées du multi-matériaux. Toute couche dont l\'épaisseur est égale à zéro verra son épaisseur définie automatiquement par l\'espace restant défini par la valeur Thickness du panneau, après soustraction des autres couches.



## Propriétés

-    **Length**: longueur du panneau

-    **Width**: largeur du panneau

-    **Thickness**: épaisseur du panneau

-    **Area**: surface du panneau (automatique)

-    **Sheets**: nombre de feuilles de matériau dont est composé le panneau.

-    **Wave Length**: longueur de l\'ondulation pour les panneaux ondulés.

-    **Wave Height**: hauteur de l\'ondulation pour les panneaux ondulés.

-    **Wave Type**: type de l\'ondulation pour les panneaux ondulés, courbe, trapézoïdale ou en pointe.

-    **Wave Direction**: orientation des ondulations pour les panneaux ondulés.

-    **Bottom Wave**: si l\'ondulation du fond du panneau est plate ou non.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Panneau peut-être utilisé dans une [macro](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Crée un objet `Panel` à partir du `baseobj` donné qui est un profil fermé et de l\'extrusion donnée `thickness`.
    -   Si aucun `baseobj` n\'est indiqué, vous pouvez fournir les valeurs numériques pour `length`, `width` et `thickness` pour créer un bloc panneau.
-   Si un `placement` est donné, il est utilisé.

Exemple :


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```



## Tutoriels

-   [Tutoriel de portage Wikihouse](Wikihouse_porting_tutorial/fr.md)



---
⏵ [documentation index](../README.md) > Arch Panel/fr
