# Draft Pattern/fr






{{TOCright}}

## Description

Les objets [Draft](Draft_Workbench/fr.md) ayant une propriété {{PropertyData/fr|Make Face}} peuvent afficher un motif hachuré au lieu d\'une couleur de surface unie.

![](images/DraftPatternSample.png ) *Une ellipse et un polygone avec un motif hachuré*

## Utilisation

1.  Assurez-vous que les objets sont fermés et planaires, et qu\'ils ne s\'auto-intersectent pas.
2.  Pour fermer une [Draft Polyligne](Draft_Wire/fr.md), une [Draft B-spline](Draft_BSpline/fr.md), une [Draft Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md) ou une [Draft Courbe de Bézier](Draft_BezCurve/fr.md), définissez leur propriété {{PropertyData/fr|Closed}} à `True`.
3.  Pour fermer un [Draft Cercle](Draft_Circle/fr.md) ou une [Draft Ellipse](Draft_Ellipse/fr.md), attribuez la même valeur aux propriétés {{PropertyData/fr|First Angle}} et {{PropertyData/fr|Last Angle}}.
4.  Sélectionnez les objets.
5.  Passez à l\'onglet **Visualisation** de l\'[Éditeur de propriétés](Property_editor/fr.md).
6.  La propriété {{PropertyView/fr|Display Mode}} doit être définie à {{Value|Flat Lines}}.
7.  Sélectionnez un {{PropertyView/fr|Pattern}}.
8.  Changez éventuellement la {{PropertyView/fr|Pattern Size}}. Notez qu\'une valeur plus élevée donne un motif plus dense.
9.  Le motif hachuré n\'est pas affiché lorsque les objets sont sélectionnés. Désélectionnez-les pour vérifier le résultat.
10. Vous pouvez éventuellement resélectionner les objets pour modifier les propriétés du motif.

## Motifs disponibles 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brique01 Image:Concrete.svg\|béton Image:Cross.svg\|croix Image:Cuprous.svg\|cuivre Image:Diagonal1.svg\|diagonale1 Image:Diagonal2.svg\|diagonale2 Image:Earth.svg\|terre Image:General\_steel.svg\|general\_steel Image:Glass.svg\|verre Image:Hbone.svg\|hbone Image:Line.svg\|ligne Image:Plastic.svg\|plastique Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solide Image:Square.svg\|carré Image:Steel.svg\|acier Image:Titanium.svg\|titane Image:Wood.svg\|bois Image:Woodgrain.svg\|grain de bois Image:Zinc.svg\|zinc

## Remarques

-   Les modèles de hachures sont stockés dans des fichiers {{FileName|.SVG}}. Il est possible d\'utiliser vos propres motifs personnalisés. Voir [Préférences](#Pr.C3.A9f.C3.A9rences.md).
-   Les motifs eux-mêmes ne sont pas enregistrés dans le document FreeCAD. Les objets dont le motif {{PropertyView/fr|Pattern}} ne peut être trouvé sont affichés avec une couleur de surface solide à la place.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour spécifier un répertoire avec des motifs de hachures supplémentaires : **Edition → Préférences... → Draft → Paramètres visuels → Autre emplacement des motifs de hachures SVG**. Sélectionnez un fichier dans le répertoire, puis supprimez le nom du fichier dans la zone de saisie des préférences, ne laissant que le chemin d\'accès. Après avoir modifié cette préférence, vous devez redémarrer FreeCAD.
-   La fenêtre **Edition → Préférences... → Draft → Paramètres visuels → Résolution des motifs de hachures** préférence n\'est pas utilisée.
-   Pour modifier la taille du motif {{PropertyView/fr|Pattern Size}} utilisée pour les nouveaux objets : **Edition → Préférences... → Draft → Paramètres visuels → Taille par défaut du motif des hachures**.





 
