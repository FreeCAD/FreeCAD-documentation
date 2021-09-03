---
- GuiCommand:/fr
   Name:Curves SketchOnSurface
   Name/fr:Curves Esquisse sur une surface
   MenuLocation:Surfaces → Sketch on Surface
   Workbenches:[Curves](Curves_Workbench/fr.md)
---

## Description

Cet outil mappe une esquisse sur une face comme une étiquette sur une bouteille. L\'esquisse doit être réellement attachée à une face (voir Sketch.Support). Le mode `Map` de l\'esquisse n\'a aucun effet sur le résultat.

<img alt="" src=images/Curves_SketchOnSurface_demo.png  style="width:600" height="400px;"> *Ci-dessus: affiche l'objet `Sketch_on_surface* appliqué à la face du cylindre (gauche) et à l'esquisse source en mode édition (droite)`

## Utilisation

1.  Passer à l\'atelier <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench/fr.md) (à installer à partir du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) si ce n\'est pas déjà fait)
2.  Il existe 2 méthodes pour utiliser l\'outil Esquisse sur une surface:

    Vous avez déjà une esquisse que vous souhaitez mapper sur une surface :

    1.  Fixez l\'esquisse sur la face cible.
    2.  Modifiez l\'esquisse et ajoutez un rectangle de construction (bleu) autour des géométries.
        -   Ce rectangle sera les limites paramétriques de la face.
    3.  Quittez le mode d\'édition.
    4.  Sélectionnez l\'esquisse et activez Esquisse sur une surface soit:
        1.  En appuyant sur le bouton <img alt="" src=images/Curves_SketchOnSurface.svg  style="width:24px;">
        2.  Utilisation de l\'entrée **Surfaces → Sketch on Surface** dans le menu Curves

    Vous n\'avez pas encore de croquis à cartographier:

    1.  Sélectionnez la face cible dans la [vue 3D](3D_view/fr.md)
    2.  Activez Esquisse sur une surface soit :
        1.  En appuyant sur le bouton <img alt="" src=images/Curves_SketchOnSurface.svg  style="width:24px;">
        2.  Utilisation de l\'entrée **Surfaces → Sketch on Surface** dans le menu Curves

        :   Un objet \"Sketch on surface\" apparaît dans la [Vue Combinée](Combo_view/fr.md).
        :   Cliquez sur cet objet pour faire apparaître \"Mapped sketch\" dessous.
        :   Cliquez sur la barre d\'espace pour activer \"Mapped sketch\". Avec un double clic sur \"Mapped sketch\", un cadre bleu apparaît. Les dimensions données du cadre bleu correspondent à la surface de l\'objet sur lequel vous souhaitez mapper votre esquisse. L\'esquisse sera placée perpendiculairement à la surface à couvrir.
        :   Dessinez un objet SketchOnSurface sur cette esquisse, dans le cadre bleu, comme une esquisse habituelle et contraignez-la à 100% (recommandé).
        :   Fermez l\'esquisse - important.
        :   Un objet SketchOnSurface sera créé sur cette esquisse sur la surface de votre objet.
    3.  Modifiez l\'esquisse et ajoutez des géométries à l\'intérieur des limites de construction bleues.

## Options

-   Fill Extrusion : lorsque la valeur Thickness n\'est pas nulle, cela générera des faces lissées (les faces bleues dans la capture d\'écran ci-dessus).
-   Fill Faces : cela remplira toutes les figures géométriques fermées en faces (les faces rouges dans la capture d\'écran ci-dessus).
-   Offset : cela enfoncera les formes mappées ci-dessus dans la face cible. Ne mettez pas un offset plus grand que l\'épaisseur, cela fera disparaitre la face à l\'intérieur.
-   Thickness : si elle n\'est pas nulle, cela donnera de l\'épaisseur aux surfaces crées ci-dessus.

## Propriétés

## Limitations

Les lignes de construction bleues de l\'esquisse font partie de l\'esquisse même si elles ne sont pas visibles lorsque l\'esquisse est fermée et même si les lignes bleues dépassent le cadre de construction bleu. L\'esquisse complète sera automatiquement mise à l\'échelle de sorte qu\'elle ne soit pas plus grande que la zone à couvrir.

## Script





{{Curves Tools navi

}} 
