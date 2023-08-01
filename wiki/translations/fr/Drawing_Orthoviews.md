---
- GuiCommand:
   Name:Drawing Orthoviews
   Name/fr:Drawing Vues orthogonales
   Workbenches:[Drawing](Drawing_Workbench/fr.md)
   MenuLocation:Drawing → Insérer des vues orthogonales
   Shortcut:
   SeeAlso:[Drawing A3 Paysage](Drawing_Landscape_A3/fr.md)
---

# Drawing Orthoviews/fr

L\'outil Orthoviews insère un ensemble de projections orthographiques de l\'objet sélectionné dans la feuille de dessin active. Notez qu\'il ne crée pas un seul objet de vue sur la page. Au lieu de cela, une projection orthographique séparée sera créée pour chacune des vues sélectionnées dans les options.

L\'outil Orthoviews crée toutes les projections orthographiques à l\'emplacement approprié pour la vue principale donnée.

## Utilisation

1.  Sélectionnez une fonctionnalité dans l\'arborescence du modèle.
2.  S\'il y a plus d\'une page, sélectionnez la page souhaitée plusieurs fois (tout en maintenant la fonction sélectionnée).
3.  Appuyez sur le bouton **<img src="images/Drawing_Orthoviews.png" width=16px> [Inserérer une projection orthogonale...](Drawing_Orthoviews.md)**.
4.  Définissez les options de création de vue souhaitées. Voir [Options](#Options/fr.md).
5.  Cliquez sur OK pour créer les vues de la fonction sélectionnée sur la page sélectionnée.

## Options

Selon les sélections effectuées, certaines options peuvent ne pas être disponibles.

![](images/Drawing_Orthoviews_Options.png )

-   **Projection**: choisissez si vous voulez une projection avec un troisième angle (par défaut) ou un premier angle.
-   **View from**: choisissez l\'axe qui fera face à la feuille de dessin en direction de l\'utilisateur.
-   **Axis aligned right**: choisissez l\'axe qui pointe vers la droite sur la feuille de dessin. L\'axe restant sera vertical sur la page.
-   **Secondary views**: choisissez les vues que vous souhaitez créer. La vue principale se situe au centre des cases à cocher et est orientée par les options {{Variable|View from}} et {{Variable|Axis aligned right}}. Des vues secondaires seront créées pour chaque case cochée.

### Généralités

-   **Auto scale / position**: si cette case est cochée, l\'échelle de vue, l\'emplacement et l\'espacement seront choisis de manière à utiliser au mieux l\'espace disponible sur la page. Si cette case n\'est pas cochée, l\'utilisateur spécifie l\'échelle, l\'emplacement et l\'espacement.
-   **Scale**: L\'échelle de la vue, exprimée en tant que dénominateur d\'une fraction d\'échelle. Ainsi {{SystemInput|2|}} créera un ensemble de vues à l\'échelle 1:2.
-   **Top left x / y**: emplacement du jeu de vues en haut à gauche de la page. L\'augmentation de la valeur x (première colonne) déplace les vues vers la droite. L\'augmentation de la valeur y (deuxième colonne) déplace les vues vers le bas de la page.
-   **Spacing dx / dy**: les espacements x (première colonne) et y (deuxième colonne) entre les vues adjacentes. Les espacements sont l\'espacement du système de coordonnées de la pièce; dans la plupart des cas, il y aura moins d\'espace vide entre les vues que la valeur d\'espacement (car les vues ont des dimensions x et y).
-   **Show hidden lines**: si cette option est sélectionnée, les lignes cachées seront visibles dans les vues créées.
-   **Show smooth lines**: si cette option est sélectionnée, affiche les lignes où la courbure est discontinue (par exemple, lorsqu\'un congé est relié à une partie plate).

## Propriétés

Il n\'y a pas de propriétés pour cette commande. La commande crée des propriétés pour chacune des vues individuelles.

## Script

Orthoviews n\'est pas appelé dans les scripts. Les vues individuelles créées par la commande Drawing Orthoviews peuvent être créées dans des scripts.

## Limitations

A ajouter.

## Tutoriels

-   [Tutoriel de Dessin](Drawing_tutorial/fr.md) introduction à la création de plans avec l\'atelier de dessin.
-   [Manuel : Génération de dessins 2D](Manual:Generating_2D_drawings/fr.md) avec l\'atelier Drawing et l\'extension Cotation du dessin.





{{Drawing Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing Orthoviews/fr
