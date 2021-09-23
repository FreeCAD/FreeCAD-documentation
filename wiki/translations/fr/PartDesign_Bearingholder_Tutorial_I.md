# PartDesign Bearingholder Tutorial I/fr
{{TutorialInfo
|Topic=Modélisation
|Level=Utilisateur expérimenté
|Author=NormandC
|Time=
|FCVersion= ≥ 0.19.23300
|Files=
}}


**Ce tutoriel a été écrit à l'origine pour une version de développement maintenant obsolète de FreeCAD. Ce tutoriel nécessite une réécriture complète pour s'aligner sur les modifications apportées à PartDesign dans la prochaine version v.17. La réécriture a été lancée dans [NormandC](Sandbox:PartDesign_Bearingholder_Tutorial_I]]. Si vous souhaitez y participer, merci de poster sur la section Wiki du [http://forum.freecadweb.org forum]. - [[Utilisateur: Normandc.md)**

Tutoriel Support de Roulement - Support de roulement terminé

~~Comme l\'indique l\'avertissement en haut de la page , ce **tutoriel ne fonctionnera que si vous compilez une branche spéciale hautement expérimentale du code source FreeCAD** et est un tutoriel d\'introduction à la modélisation avec l\'atelier PartDesign dans FreeCAD **utilisant des plans de référence qui sont une caractéristique qui n\'existe pas encore dans la plupart des versions de FreeCAD**.~~

## L\'objectif en deux mots 

Le but de ce tutoriel est de vous présenter deux flux de travail différents pour créer une pièce moulée avec des ébauches et des congés. Selon les autres programmes de CAO que vous avez utilisés, l\'un ou l\'autre peut vous être familier. Comme exemple de travail, nous allons modéliser un simple support de roulement.

Ceci est la première partie du tutoriel. Elle utilisera ce qu\'on pourrait appeler la méthode «corps unique» , en utilisant la partie (simple) supérieure du support comme un exemple

Évidemment, pour suivre ce tutoriel, vous devez activer l\'Atelier Conception de Pièce.

~~Vous pouvez trouver ma version de la pièce créée dans ce tutoriel [http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4 ici](http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4_ici.md).~~ *Ce fichier n\'est plus disponible, un nouveau fichier sera fourni à une date ultérieure.*

## Les Données de Conception 

Le support doit être en mesure de tenir un Roulement d\'un diamètre de 90mm avec une largeur allant jusqu\'à 33mm (par exemple DIN 630 Type 2308, qui a un diamètre intérieur de 40 mm). Le roulement nécessite une hauteur d\'épaulement d\'au moins 4,5 mm dans le support (et sur l\'arbre). La partie supérieure du support sera boulonné sur l\'autre partie avec deux boulons de 12mm. Pour la tête d\'un tel boulon, il faudra au moins 20 mm de diamètre d\'espace libre. Il devrait y avoir une rainure sur les deux côtés du roulement capables de tenir un arbre standard bague d\'étanchéité DIN 3760: 38x55x7 40x55x7 ou sur un côté, 50x68x8 de l\'autre côté.

Le support sera réalisé dans un moule en sable avec une épaisseur minimale de paroi de 5 mm, un angle de dépouille de 2 degrés, et un rayon de congé minimum de 3mm.

## Mise en place de la géométrie de l\'ossature 

![support de roulement avec les deux plans les plus importants de l\'ossature\|thumb\|right\|text-top\|400px](images/_HolderTop1-2.jpg )

L\'idée de la géométrie de l\'ossature est de capturer les dimensions de base de la conception en une caractéristique unique de référence (par exemple, un plan ou un axe). Lorsque la dimension de conception change, tout ce qui doit être fait est de changer la fonction de squelette. Si le modèle est bien construit, alors toute sa fonction sera de recalculer pour refléter le changement de conception. Cela réduit le risque que, dans un modèle complexe, où les dimensions de conception de base sont utilisées dans de multiples endroits, vous oubliez de changer des éléments quelque part.

L\'alternative à la géométrie de l\'ossature est d\'avoir une table des dimensions de conception de base qui attribuent un nom symbolique à chaque dimension, puis utilisez le nom symbolique là où les dimensions sont nécessaires pour construire le modèle. FreeCAD ne permet pas encore cette approche

![Plans de Base et tous les plans de référence\|thumb\|right\|text-top\|400px](images/HolderTop1-3.jpg )

Dans le cas du support de palier, les deux dimensions de conception les plus importants sont la distance entre les boulons (ce qui limite la taille du roulement qui peut être utilisée) et la hauteur de la tête des boulons. Les dimensions sont choisies \* Distance entre les boulons: rayon de roulement (45) + épaisseur de paroi (5) plus le rayon du trou pour boulon (7) = 57 mm, de sorte que le plan vertical de 57 mm est décalé par rapport au plan YZ. Pour créer ce plan de référence, sélectionnez le plan YZ et ensuite choisir de créer un nouveau plan de référence. Entrez le décalage dans la boîte de dialogue qui se ouvre \* Hauteur de têtes de boulons: Cela a été choisi comme un décalage de 28mm du plan XZ

Pour plus de commodité, deux autres plans de référence peuvent être créés pour refléter la quantité de matériau qui doit être coupée des côtés du support déroulement. Ils sont décalés de +22 et -22 depuis le plan XY.

Il est conseillé de donner des noms clairs à la géométrie du de l\'ossature. La plupart du temps, vous voudrez désactiver la visibilité des plans de référence, car ils encombrent l\'écran, et si les plans ont des noms explicites vous pouvez simplement choisir leur nom au lieu de les choisir depuis l\'écran.

## Le solide géométrique 

![ thumb \| 400px \| right \| text-top \| Croquis du première protusion](images/_HolderTop1-4.jpg ) Maintenant il est temps de commencer à créer une géométrie réelle. L\'esquisse pour la première protusion est affichée sur la droite. Elle est placée sur le plan XY. Il y a juste trois dimensions: le rayon intérieur (de 22,5 mm), l\'allocation d\'usinage (3mm) à la base comme un décalage au pla-XZ et la distance entre le plan de référence représentant l\'axe du boulon (7mm). Cela signifie que si vous vous déplacez plus tard, le plan de référence, la protusion ajustera automatiquement son rayon extérieur. N\'oubliez pas qu\'avant de pouvoir utiliser le plan de référence pour le dimensionnement, vous devez introduire la géométrie externe au sketcher

Vous vous demandez probablement pourquoi il y a ce petit segment de droite au bas de chaque arc. Ce segment indique qu\'il y aura un angle de deux degrés sur les arcs. Cela pourrait ressembler à beaucoup de travail pour un très petit avantage, mais de nombreux programmes de CAO (et peut-être un jour FreeCAD) disposent d\'outils qui mettent en évidence un modèle solide en différentes couleurs immédiatement et vous présentent toutes les faces où l\'angle de dépouille n\'est pas correct. Vous ne voulez pas que cela arrive à votre modèle, en particulier après la mise en place d\'un grand nombre de congés!
Lorsque vous avez fait le croquis (qui est un peu difficile à cause des deux degrés des lignes tangentielles), ajuster la protusion symétriquement au plan d\'esquisse d\'une longueur de 62mm: 34mm pour le palier, 2x 9mm pour les bagues d\'étanchéité, 2x 5mm pour l\'épaisseur de paroi.
![ thumb \| 400px \| right \| text-top \| Croquis de la coupe sur le coté de la Protusion](images/_HolderTop1-5.jpg ) Ensuite, nous voulons retrancher certains matériaux où sont les bagues d\'étanchéité, parce que leur diamètre extérieur est beaucoup moins que le roulement . La meilleure façon de créer les croquis est de sélectionner l\'esquisse de la protusion et puis choisissez \"sélection Dupliquer\" dans le menu d\'édition. Vous pouvez ensuite redéfinir le croquis sur le côté de la protusion, et le modifier comme indiqué dans l\'image.

Les deux seules dimensions importantes dans l\'esquisse sont 3 mm de surépaisseur d\'usinage au fond, et un diamètre intérieur de 78mm : 68mm pour le diamètre extérieur de l\'épaisseur de paroi + 2x5mm de bague d\'étanchéité. Puisque la bague d\'étanchéité de l\'autre côté aura un diamètre de 55mm, la découpe peut être de 65mm ici.

Après avoir créé l\'esquisse, creusez jusqu\'au plan de référence marquant le coté du roulement plus l\'épaisseur de paroi 5 mm . Si jamais vous voulez modifier le support pour qu\'il soit capable de porter des roulements plus larges, tout ce que vous avez à faire est de changer la dimension de ces plans de référence, et la profondeur de découpe devra suivre.
<img alt=" text-top\|Croquis de découpe à l\'intérieur de la protusion" src=images/_HolderTop1-6.jpg  style="width:400px;"> Pour réduire la quantité d\'usinage nécessaire, nous voulons aussi découper certains matériaux à l\'intérieur du support . Encore une fois, la duplication de l\'esquisse de la première Protusion est pratique. Elle n\'a même pas besoin d\'être reconfigurée. Encore une fois, les seules dimensions importantes sont la surépaisseur d\'usinage (3mm) et les diamètres extérieurs: 84mm pour le l\'emplacement du roulement (90mm - 2x allocation d\'usinage), 49mm pour le petit anneau d\'étanchéité (55mm - 2x 3mm) et 62mm pour la bague d\'étanchéité plus grande.

Après avoir créé les esquisses, les creuser: Symétriquement 28mm pour la découpe du roulement (34mm - 2x surépaisseur d\'usinage ) et 23mm sur un coté pour les découpes des bagues d\'étanchéité: 34mm / 2 pour la moitié de la largeur du roulement + 9mm pour la bagues d\'étanchéité - surépaisseur d\'usinage de 3mm.
[thumb\|400px\|right \| text-top\|Géométrie principale du haut du support](Image:_HolderTop1-7.jpg.md) La pièce doit maintenant ressembler à l\'image sur la droite. Notez comment les différentes découpes se combinent pour créer une épaisseur de paroi presque uniforme, ce qui rendra la coulée plus facile et moins susceptibles d\'avoir des pores.
<img alt=" text-top\|Croquis avec l\'emplacement des boulons" src=images/_HolderTop1-8.jpg  style="width:400px;"> Maintenant tout ce qui reste a faire est de créer de la matière pour le passage des boulons. Vous pourriez être tenté d\'esquisser ceci comme un cercle puis le protuser, mais cela vous dirigera vers des problèmes lorsque vous essaierez de le mettre plus tard sur le projet (je suppose que c\'est une faiblesse d\'OpenCascade). Donc, pour éviter les problèmes, il est préférable de créer une esquisse de l\'angle projeté inclus, puis la tourner de 360 degrés.

Là encore, les plans de l\'ossature deviennent utile. Vous aurez besoin du plan de l\'axe du boulon et du plan de la tête du boulon comme géométrie externe. Ensuite, créez une ligne droite pour l\'axe de rotation et assurez-vous qu\'il est contraint à l\'axe du boulon du plan de référence. Le basculer pour devenir une géométrie de construction. Puis, esquisser le reste du contour. Les dimensions importantes sont la surépaisseur d\'usinage en haut et en bas et le rayon de 12 mm : 7 mm pour le rayon du trou + épaisseur de paroi de 5 mm.
<img alt="géométrie finie de la partie supérieure du support (sans projet et congés)" src=images/_HolderTop1-9.jpg  style="width:400px;"> Créer une fonction de révolution de l\'esquisse, puis la symétriser sur le plan YZ . C\'est toute la géométrie solide nous devons modéliser. Le reste est brouillon et congés.

## Application de dépouille sur les faces latérales 

[thumb\|400px\|right\|text-top \| Le plan neutre pour la création de dépouille](Image:_HolderTop1-10.jpg.md) L\'étape suivante consiste à appliquer des dépouilles sur toutes les faces . Il est important de bien choisir l\'emplacement du plan neutre, c\'est le plan autour duquel on tourne. Si nous choisissons comme plan neutre, le bas du support, alors nous aurons un problème avec l\'épaisseur de paroi dans la partie supérieure du support. Par conséquent, nous créons un plan de référence avec un décalage de 40 mm par rapport au plan XZ comme un compromis entre le haut de la porte devant mince et le bas de devenant large .
<img alt=" ext-top\|Application de dépouille sur les faces latérales du support" src=images/_HolderTop1-11.jpg  style="width:400px;"> Pour mettre une dépouille sur une face , sélectionner cette face et créer la caractéristique de la dépouille . Vous pouvez ensuite sélectionner plusieurs faces et appliquer la dépouille dessus . Si vous avez une grande pièce, il est conseillé de dépouiller une seule face à la fois. Cela signifie que si vous modifiez la géométrie et qu\'une dépouille échoue, seul cette caractéristique va échouer, alors que si vous mettez sur tous les faces une fonction de dépouille, alors l\'ensemble des fonction ensemble pourrait échouer à cause d\'une faute d\'une face. Pour une petite pièce comme le support de roulement, c\'est suffisant de créer deux fonctions de dépouille : Une pour les quatre faces extérieures, et une pour les faces internes.

La boîte de dialogue va vous forcer à choisir un plan neutre avant de remplir. Vous pouvez laisser la direction d\'étirement vide, dans ce cas, il sera perpendiculaire au plan neutre. Ne oubliez pas de régler l\'angle de dépouille à 2 degrés.

## Congés sur le support 

![ thumb \| 400px \| right \| text-top \|Congés où seront les boulons](images/_HolderTop1-13.jpg ) Nous pouvons maintenant arrondir la pièce. La photo montre le premier jeu de congés. Commencez par les petits congés circulaires et leurs donner un rayon 4mm. Même si 3 mm suffiraient selon les spécifications de la pièce, un rayon de 4 mm signifie qu\'après l\'usinage du congé 1 mm est laissé, réduisant l\'arête vive produite par l\'usinage. Les grands congés ont un rayon de 6mm pour aider à répandre la force des boulons sur le reste de la pièce. Ce serait bien de faire ce rayon encore plus grand, mais malheureusement OpenCascade ne peut pas gérer encore les congés qui se chevauchent .

Comme avec les dépouilles, dans un cadre complexe, vous devez arrondir un seul bord à la fois pour éviter les échecs inutiles si la géométrie de base change.
![ thumb \| 400px \| right \| text-top \| Congé à l\'extérieur du support](images/_HolderTop1-12.jpg ) Le reste des congés ont tout simplement un rayon de 3 mm. En regardant l\'image sur la droite, les deux congés mis en évidence pourraient effectivement être des congés avec un rayon de 5 mm pour atteindre une épaisseur de paroi plus uniforme pour la coulée. Après usinage, l\'épaisseur de paroi minimale de 5 mm serait toujours maintenue. Mais encore une fois le fait que OpenCascade ne peut pas gérer le chevauchement des congés nous empêche de le faire pour les deux congés intérieurs mis en évidence.
<img alt="Congé à l\'intérieur du support - bord problématique" src=images/_HolderTop1-14.jpg  style="width:400px;"> Faire des congés l\'intérieur de la pièce nous présente une difficulté qui ne peut être résolue avec les outils actuels dans l\'atelier PartDesign. Le bord du congé ne peut pas du tout être mis en évidence , encore une fois parce que les congés se chevaucheraient. Cela pourrait être contourné par la création d\'une courbe à la place d\'un congé, sauf que les courbes ne sont pas encore mises en œuvre dans PartDesign. Pour le moment, nous sommes forcés de quitter le bord comme il est.
<img alt="La pièce en congé (sauf pour le bord impossible)" src=images/_HolderTop1-15.jpg  style="width:400px;"> L\'image de droite montre la pièce finie dans l\'état où elle sera avant l\'usinage (à l\'exception de l\'un des bords où il est impossible de créer un congé). Vous remarquerez qu\'un bord qui tourne autour de toute la pièce a été laissé sans congé dans ce but. Il s\'agit du bord où la partie inférieure et la partie supérieure du moule se rencontrent. Ici, pas de congé possible (et aucun n\' est requis de toute façon).

## Usinage

<img alt="Usinage haut et bas du support" src=images/_HolderTop1-16.jpg  style="width:400px;"> <img alt="Usinage intérieur du support de Roulement" src=images/_HolderTop1-17.jpg  style="width:400px;"> maintenant, nous pouvons couper le matériel qui sera usiné à partir de la pièce brute en fonte. C\'est très facile avec la géométrie du squelette défini. L\'idée est de créer toutes les caractéristiques d\'usinage (Cavités et rainures) en utilisant uniquement donnée caractéristiques. Cela signifie qu\'ils vont être totalement indépendant de la géométrie solide du support de roulement, ce qui nous donne quelques grands avantages: \* Peu importe comment vous modifiez la géométrie solide, les caractéristiques pour l\'usinage ne pourront pas échouer. \* Vous pouvez créer la géométrie d\'usinage avant de finaliser le solide, ce qui vous donne une rétroaction visuelle utile. \* Si vous déplacez les plans squelettes de repère, alors la géométrie du solide et l\'usinage s\'adapteront automatiquement en même temps . \* Si vous faites une erreur dans votre géométrie solide, l\'usinage sera toujours dans la position correcte, et très probablement l\'erreur deviendra flagrante (par exemple, une épaisseur de paroi de 2 mm au lieu 5mm). Alors que si vous faites référence à l\'usinage de la géométrie solide, il va s\'adapter à l\'erreur dans le solide et, par exemple maintenir l\'épaisseur de paroi de 5 mm, juste au mauvais endroit où se trouve le solide.

Avant de commencer la géométrie d\'usinage, j\'aime placer un point de référence dans l\'arbre et le nommer comme \"Usinage\_démarrera\_ici\". C\'est utile si vous souhaitez basculer entre l\'état brut et l\'état usiné de la pièce parce que vous pouvez voir en un coup d\'œil où déplacer le point d\'insertion pour obtenir l\'état brut.

Pour usiner la partie inférieure du support, il suffit de tracer un grand rectangle dans le plan XZ et le creuser. Pour le haut, esquisser un cercle sur le plan de référence définissant l\'emplacement de la tête de vis, puis symétriser la cavité sur le plan YZ. De la même manière, créer une cavité pour le trou où passe le boulon et le symétriser. Pour usiner l\'intérieur du support, créer une esquisse sur le plan YZ et le rainurer.
![ thumb \| 400px \| right \| text-top \| Pièce finie](images/_HolderTop1-1.jpg ) Une fois que vous avez réaliser l\'usinage, vous pouvez avoir un bon effet visuel en colorant toutes les surfaces usinées de sorte que vous pouvez voir d\'un coup d\'œil les parties qui sont brut de fonderie et celles qui sont usinées après la coulée.

## Notes Finales 

Nous avons modélisé le haut du support de roulement avec les dimensions qu\'il aura après la coulée. Pour créer le moule, vous devez appliquer un retrait à votre pièce parce que après la coulée, lorsque le métal chaud se refroidit, il va diminuer de quelques pour cent (selon le matériau). Habituellement, il est préférable de laisser l\'application de retrait à la fonderie faisant la pièce parce qu\'ils ont les connaissances particulières requises. Ils devraient également vous dire si votre pièce comporte des zones problématiques, par exemple parois très épaisse rejoignant brusquement des sections très minces sans transition correcte entre elles.

## Partie Deux 

[Tutoriel de Conception Support de Roulement II](PartDesign_Bearingholder_Tutorial_II/fr.md)



[Category:Tutorials](Category:Tutorials.md)

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Bearingholder Tutorial I/fr
