---
- GuiCommand   */fr
   Name   *Curves SketchOnSurface
   Name/fr   *Curves Esquisse sur une surface
   MenuLocation   *Surfaces → Sketch on Surface
   Workbenches   *[Curves](Curves_Workbench/fr.md)
---

# Curves SketchOnSurface/fr

## Description

Cet outil applique une esquisse sur une face comme une étiquette sur une bouteille. L\'esquisse doit être réellement attachée à une face (voir Sketch.Support). Le mode `Map` de l\'esquisse n\'a aucun effet sur le résultat.

<img alt="" src=images/Curves_SketchOnSurface_demo.png  style="width   *600" height="400px;"> 
*Ci-dessus   * affiche l'objet `Sketch_On_Surface* appliqué à la face du cylindre (gauche) et à l'esquisse source en mode édition (droite)`

## Utilisation

1.  Passez à l\'atelier <img alt="" src=images/Curves_workbench_icon.svg  style="width   *24px;"> [Curves](Curves_Workbench/fr.md) (l\'installation de <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) est nécessaire, si elle n\'est pas déjà installée)
2.  Il existe 2 méthodes pour utiliser l\'outil SketchOnSurface    *
3.  ; Vous avez déjà une esquisse que vous voulez appliquer sur une face    *
    1.  Attachez l\'esquisse à la face cible.
    2.  Editez l\'esquisse et ajoutez un rectangle de construction (bleu) autour des géométries. Ce rectangle sera les limites paramétriques de la face.
    3.  Quittez le mode d\'édition.
    4.  Sélectionnez l\'esquisse.
    5.  Activez SketchOnSurface soit    *
        -   En appuyant sur le bouton <img alt="" src=images/Curves_SketchOnSurface.svg  style="width   *24px;">.
        -   En utilisant l\'entrée **Surfaces → Sketch on Surface** dans le menu Curves.

        1.  Vous n\'avez pas encore d\'esquisse à plaquer    *
    6.  Sélectionnez la face cible dans la [vue 3D](3D_view/fr.md).
        1.  Activez SketchOnSurface soit par    *

        -   En appuyant sur le bouton <img alt="" src=images/Curves_SketchOnSurface.svg  style="width   *24px;">.
        -   En utilisant l\'entrée **Surfaces → Sketch on Surface** dans le menu Curves.
    7.  Un objet Sketch\_On\_Surface apparaît dans la [Vue en arborescence](Tree_view/fr.md).
    8.  Développez cet objet pour faire apparaître l\'esquisse Mapped\_Sketch ci-dessous.
    9.  Modifiez l\'esquisse et ajoutez des géométries à l\'intérieur des limites de construction bleues.
    10. Un objet SketchOnSurface sera créé sur la surface de votre objet à partir de cette esquisse.

## Options

-   Fill Extrusion    * lorsque la valeur Thickness n\'est pas nulle, cela générera des faces lissées (les faces bleues dans la capture d\'écran ci-dessus).
-   Fill Faces    * cela remplira toutes les figures géométriques fermées en faces (les faces rouges dans la capture d\'écran ci-dessus).
-   Offset    * cela enfoncera les formes appliquées ci-dessus dans la face cible. Ne mettez pas un décalage plus grand que l\'épaisseur, cela ferait disparaître la face à l\'intérieur.
-   Thickness    * si elle n\'est pas nulle, cela donnera de l\'épaisseur aux surfaces crées ci-dessus.

## Remarques

On suppose que toute la géométrie de l\'esquisse est incluse dans le cadre de construction bleu. Cela inclut toute autre géométrie de construction, ainsi que la géométrie interne visible des courbes complexes (Bézier, Ellipse). Si ce n\'est pas le cas, la boîte de délimitation de l\'esquisse sera plus grande que le cadre de construction et le mappage final sera réduit en conséquence. Si nécessaire, [cachez la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md) qui n\'est pas entièrement à l\'intérieur du cadre de construction.

## Propriétés

## Script





{{Curves Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves SketchOnSurface/fr
