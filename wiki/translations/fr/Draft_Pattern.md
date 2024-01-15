# Draft Pattern/fr
## Description

Les objets [Draft](Draft_Workbench/fr.md) ayant une propriété **Make Face** peuvent afficher un motif SVG au lieu d\'une couleur de surface unie.

![](images/DraftPatternSample.png ) 
*Une ellipse et un polygone avec un motif SVG*



## Utilisation

1.  Assurez-vous que les objets sont fermés et planaires, et qu\'ils ne s\'auto-intersectent pas.
2.  Pour fermer une [Draft Polyligne](Draft_Wire/fr.md), une [Draft B-spline](Draft_BSpline/fr.md), une [Draft Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md) ou une [Draft Courbe de Bézier](Draft_BezCurve/fr.md), définissez leur propriété **Closed** à `True`.
3.  Pour fermer un [Draft Cercle](Draft_Circle/fr.md) ou une [Draft Ellipse](Draft_Ellipse/fr.md), attribuez la même valeur aux propriétés **First Angle** et {{PropertyData/fr|Last Angle}}.
4.  Sélectionnez les objets.
5.  Passez à l\'onglet **Visualisation** de l\'[Éditeur de propriétés](Property_editor/fr.md).
6.  La propriété **Display Mode** doit être définie à {{Value|Flat Lines}}.
7.  Sélectionnez un **Pattern**.
8.  Changez éventuellement la **Pattern Size**. Notez qu\'une valeur plus élevée donne un motif plus dense.
9.  Le motif n\'est pas affiché lorsque les objets sont sélectionnés. Désélectionnez-les pour vérifier le résultat.
10. Vous pouvez éventuellement resélectionner les objets pour modifier les propriétés du motif.



## Motifs disponibles 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General_steel.svg\|general_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc



## Remarques

-   Les modèles SVG sont stockés dans des fichiers **.SVG**. Il est possible d\'utiliser vos propres motifs personnalisés. Voir [Préférences](#Pr.C3.A9f.C3.A9rences.md).
-   Les motifs eux-mêmes ne sont pas enregistrés dans le document FreeCAD. Les objets dont le motif **Pattern** ne peut être trouvé sont affichés avec une couleur de surface solide à la place.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour changer **Pattern Size** utilisée pour les nouveaux objets : **Édition → Préférences... → Draft → Paramètres visuels → Taille des motifs SVG**.
-   Pour spécifier un répertoire contenant des motifs SVG supplémentaires : **Édition → Préférences... → Draft → Paramètres visuels → Emplacement des motifs SVG supplémentaires**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern/fr
