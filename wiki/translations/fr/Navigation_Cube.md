# Navigation Cube/fr
{{TOCright}}

Le contrôle du **cube de navigation** est une aide graphique de l\'interface utilisateur permettant de réorienter la vue 3D. Par défaut, il est visible et réside dans le coin supérieur droit de l'affichage 3D. Si vous regardez la vue 3D standard, cela ressemble à ce qui suit :

![](images/FreeCAD-v0-18-NavCube_Axonometric.png )

Le cube de navigation est composé de plusieurs parties:

-   Flèches directionnelles
-   Cube de navigation principal
-   Menu mini-cube

Si vous placez le pointeur de la souris sur une entité du cube de navigation, elle devient bleu clair. En cliquant, vous réorienterez la vue 3D comme il est indiqué par la fonction. Dans l\'exemple ci-dessous, la vue 3D a été pivotée par un [mouvement à la souris](Mouse_Model/fr.md) vers une orientation \"non standard\". Le pointeur se trouve sur un coin (indiqué par la couleur bleue); En cliquant, vous réorienterez la vue 3D sur une vue axonométrique standard avec ce coin en face de vous.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

## Flèches directionnelles. 

Six flèches directionnelles: quatre pointes de flèche triangulaires, une en haut, une en bas, une à gauche et une à droite; et deux flèches courbées, une de chaque côté de la flèche du haut.

En cliquant sur les flèches triangulaires, la vue 3D pivote de 45 degrés autour d\'une ligne perpendiculaire à la direction de la flèche. En cliquant sur les flèches incurvées, la vue 3D pivote autour d\'une ligne pointant vers vous.

## Cube de navigation principal 

Le cube de navigation principal (\"cube de navigation\" dans le reste de cette section) suit l\'orientation de l\'objet dans la partie principale de la vue 3D. Toute opération qui réoriente la vue 3D principale réorientera également le cube de navigation.

Le cube de navigation est essentiellement une vue 3D d\'un cube avec ses trois principaux types de composants (facettes, arêtes et angles) améliorés de sorte qu\'ils puissent être facilement cliqués avec le pointeur. En cliquant sur un composant particulier, la vue 3D sera centrée et orientée vers vous. Le cube de navigation est un peu \"écrasé\", comme si la caractéristique la plus éloignée de vous était plus grande que celle qui se trouvait directement en face de vous. Cela permet de voir les éléments adjacents à celui qui vous fait face et par conséquent de les sélectionner. Par exemple, dans une vue \"normale\" d\'un cube normal, lorsqu\'une face vous fait face, vous pouvez également voir les quatre bords et les quatre coins de cette facette. Dans le cube de navigation \"écrasé\", vous pouvez également voir des entités représentant chacune des facettes adjacentes, les quatre arêtes reliant les coins de la face face à vous avec la face opposée et les angles de la face opposée. Cela vous permet de sélectionner n\'importe quelle vue standard possible, à l\'exception de la facette opposée et de ses bords (21 vues possibles sur 26):

-   La facette qui vous fait face (ne fait rien car c\'est la vue en cours)
-   Les quatre arêtes de la facette courante
-   Les quatre coins du facette actuel
-   Les quatre facettes adjacentes
-   Les quatre arêtes menant à la facette opposée
-   Les quatre coins de la facette opposée

Pas possible:

-   La facette opposée
-   Les bords de la facette opposée

Remarque: Au moment de la rédaction de cet article (v 0.18), le cube de navigation pose quelques problèmes. toutes les fonctionnalités ne sont pas actuellement sélectionnables. En particulier, les arêtes ne peuvent pas être sélectionnées, ni les quatre coins de la face immédiatement en regard.

### Sélection d\'une facette 

En cliquant sur une facette, vous orienterez la vue 3D avec cete facette particulier qui vous fait face. Comme indiqué ci-dessus, d\'autres points de sélection sont disponibles dans la vue de face. Il y a quatre \"barres\" minces sur chacun des bords extérieurs, représentant les quatre facettes adjacentes; en cliquant dessus, vous sélectionnez la vue correspondant à la facette adjacente. Quatre angles arrondis peuvent être utilisés pour définir la vue axonométrique correspondante. Il existe également un ensemble intérieur d\'arêtes et de coins, actuellement non fonctionnels.

### Sélection du bord 

Malheureusement, la sélection des bords est actuellement interrompue. Tenter de sélectionner une arête sélectionnera le visage qui se trouve derrière celle-ci. En cliquant sur un bord, vous devez le centrer pour qu\'il soit face à vous.

### Sélection du coin 

En cliquant sur l\'un des coins, vous obtiendrez une vue axonométrique vue de ce coin. Comme indiqué ci-dessus, actuellement, lorsqu\'un visage est directement face à vous, les coins de ce visage ne peuvent pas être sélectionnés.

## Menu du mini-cube 

Dans le coin inférieur droit du cube de navigation se trouve un petit cube. En cliquant sur ce cube, vous obtiendrez un menu que vous pourrez utiliser pour changer le type de vue (Orthographique, Perspective, Isométrique). et de faire un \"Zoom to Fit\".

## Déplacement de l'affichage du cube de navigation 

Vous pouvez déplacer l\'ensemble de la structure de contrôle du cube de navigation vers un autre endroit de l\'affichage 3D en appuyant sur la souris n\'importe où dans le cube de navigation principal et en la faisant glisser. La structure ne commencera à se déplacer que lorsque le pointeur de la souris aura dépassé le bord du cube de navigation principal.

## Configuration

Le cube de navigation est configurable, notamment en ajustant sa taille : **Edition → Préférences... → Affichage → Navigation → Cube de navigation** {{Version/fr|0.19}}.

Pour une configuration plus avancée, consultez l\'[atelier externe](External_workbenches/fr.md) [Cube Menu](Interface_Customization/fr#Menu_Cube.md).







_

---
[documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/fr
