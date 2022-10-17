# Drawing Openbrowser/fr
---
- GuiCommand   */fr   Name   *Drawing Openbrowser   Name/fr   *Vue Web   Workbenches   *[[Drawing Workbench/fr   Dessin]], Complet|MenuLocation   *Mise en plan → Vue Web    Raccourci   *aucun---

## Description

Cette commande vous permet d\'afficher une [Feuille A3 paysage](Drawing_Landscape_A3/fr.md) sélectionnée l\'aide du navigateur Web interne de FreeCAD. Le visionneur de page de dessin de FreeCAD est basée sur [de Qt intégré dans le moteur de rendu SVG](http   *//qt-project.org/doc/qt-5.0/qtsvg/svgrendering.html), qui ne prend en charge qu\'un petit sous-ensemble de la spécification SVG. En conséquence, certaines fonctionnalités de SVG plus avancés, tels que le modèle remplit ou les textes multi-lignes ne sont pas pris en charge par cette visionneuse. Le navigateur web interne FreeCAD , cependant, est construit sur [webkit](http   *//en.wikipedia.org/wiki/WebKit), qui est l\'un des meilleurs moteurs de rendu SVG disponibles, et saura rendre correctement votre page avec toutes ses fonctions.

## Utilisation

1.  Créez un [Feuille A3 paysage](Drawing_Landscape_A3.md)
2.  Ajoutez quelque [Dessin](Drawing_View/fr.md) ou tout autre contenu à votre page
3.  [Rafraichir](Std_Refresh/fr.md) la vue si une vue de dessin n\'a pas été ouverte
4.  Appuyez sur le bouton{{KEY | <img src="images/Drawing_Openbrowser.png" width=16px> [ Vue Web](Drawing_Openbrowser/fr.md)}}

## Limitations

-   Une page ouverte dans le navigateur Web ne réactualise pas automatiquement les modifications. Vous devez utiliser le clique droit → recharger manuellement.


<div class="mw-translate-fuzzy">


{{docnav/fr
|[Masque](Drawing_Clip/fr.md)
|[Vues orthogonales](Drawing_Orthoviews/fr.md)
|[Atelier Mise en plan](Drawing_Workbench/fr.md)
|IconL=Drawing_Clip.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Orthoviews.png
}}


</div>


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing Openbrowser/fr
