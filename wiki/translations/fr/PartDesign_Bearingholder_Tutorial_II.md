# PartDesign Bearingholder Tutorial II/fr




{{TutorialInfo
|Topic=Modélisation
|Level=Utilisateur expérimenté
|Author=NormandC
|Time=
|FCVersion= ≥ 0.19.23300
|Files=
}}


**Ce tutoriel a été écrit à l'origine pour une version de développement maintenant obsolète de FreeCAD. Depuis avril 2016, ces fonctionnalités ont été intégrées à la version 0.17 de pré-développement disponible [https://github.com/FreeCAD/FreeCAD/releases/tag/0.17_pre ici].
<br />
Veuillez noter que cette version de FreeCAD en est encore à ses débuts. De plus, ce tutoriel peut nécessiter une mise à jour. Si vous souhaitez participer à sa révision et à sa mise à jour, publiez-le dans la section Wiki du [http://forum.freecadweb.org forum].**

![ Tutoriel Support de Roulement - support de roulement terminé(en haut) \| thumb \| right \| 400px](images/_HolderTop2-19.jpg )

~~Comme l\'indique l\'avertissement en haut de la page , ce **tutoriel ne fonctionnera que si vous compilez une branche spéciale hautement expérimentale du code source FreeCAD** et est un tutoriel d\'introduction à la modélisation avec l\'atelier PartDesign dans FreeCAD **utilisant des plans de référence qui sont une caractéristique qui n\'existe pas encore dans la plupart des versions de FreeCAD**.~~

## L\'objectif en deux mots 

Le but de ce tutoriel est de vous présenter deux flux de travail différents pour créer une pièce moulée avec des ébauches et des congés. Selon les autres programmes de CAO que vous avez utilisés, l\'un ou l\'autre peut vous être familier. Comme exemple de travail, nous allons modéliser un simple support de roulement.

C\'est la deuxième partie du tutoriel. Il utilisera ce qu\'on pourrait appeler le flux de travail \'de corps multiples », en utilisant la (simple) partie supérieure du support comme exemple.

Évidemment, pour suivre ce tutoriel, vous devez activer l\'Atelier Conception de Pièce.

~~Vous pouvez trouver ma version de la pièce créée dans ce tutoriel [http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4 ici](http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4_ici.md)~~ *Le fichier n\'est plus disponible, un nouveau fichier sera fourni à certains date ultérieure*.

## 

Les Données de Conception == ==

Le support doit être en mesure de tenir un Roulement d\'un diamètre de 90mm avec une largeur allant jusqu\'à 33mm (par exemple DIN 630 Type 2308, qui a un diamètre intérieur de 40 mm). Le palier nécessite une hauteur d\'épaulement d\'au moins 4,5 mm dans le support (et sur l\'arbre). La partie supérieure du support sera boulonné sur le fond avec deux boulons de 12mm. Pour la tête d\'un tel boulon, il faudra au moins 20 mm de diamètre d\'espace libre. Il devrait y avoir une rainure sur les deux côtés du roulement capables de tenir un arbre standard bague d\'étanchéité DIN 3760: 38x55x7 40x55x7 ou sur un côté, 50x68x8 de l\'autre côté.

Le support sera réalisé dans un moule en sable avec une épaisseur minimale de paroi de 5 mm, un angle de dépouille de 2 degrés, et un rayon de congé minimum de 3mm.

## Configuration de la géométrie de l\'ossature 

![ Croquis de la géométrie du squelette \| thumb \| right \| 400px](images/_HolderTop2-2.png ) Créer une nouvelle pièce dans l\'atelier de Conception de Pièce. Renommez le Corps qui est créé par défaut pour l\'Ossature. Cet organe est probablement déjà activé, vous pouvez voir par la couleur de fond bleu dans l\'arborescence. Créer une nouvelle esquisse sur le plan YZ contenant le contour de l\'arbre, du roulements et bagues d\'étanchéité. Après avoir terminé l\'esquisse, faites une fonction de révolution de celle-ci. Cette fonction squelette sera ensuite utilisé pour référencer la géométrie réelle à celle-ci. Cela signifie que si vous souhaitez modifier les dimensions, tout ce que vous devez faire est d\'ajuster les dimensions de la fonction squelette et le reste de la pièce se mettra à jour en conséquence. ![ La géométrie de l\'ossature \| thumb \| right \| 400px](images/_HolderTop2-2-1.jpg )

## Le corps principal 

![ Esquisse de la première Protusion \| thumb \| right \| 400px](images/_HolderTop2-3.jpg ) Créer un nouveau corps et le rendre actif. L\'esquisse pour la première protusion est affichée sur la droite. Elle est placée sur un plan de référence avec un décalage de 5 mm (épaisseur de paroi) de la face de l\'ossature marquant le côté de l\'une des bagues d\'étanchéité du proulement. Parce que toutes les dimensions importantes sont prises à partir du squelette, il y a seulement trois dimensions: La surépaisseur d\'usinage (3mm) à la base comme un décalage du plan XY, l\'épaisseur de paroi de 5 mm de diamètre extérieur du squelette, et les deux angle de dépouille. Pour créer la dimension 5mm, vous devez d\'abord sélectionner le cercle extérieur (rayon 45mm) de la géométrie de l\'ossature comme la géométrie externe dans l\'esquisse, puis mettez une ligne de construction contrainte tangentiellement à ce cercle et avec un angle de deux degrés.

Vous vous demandez probablement pourquoi il y a ce petit segment de droite au bas de chaque arc. Ce segment indique qu\'il y aura un angle de deux degrés sur les arcs. Cela pourrait ressembler à beaucoup de travail pour un très petit avantage, mais de nombreux programmes de CAO (et peut-être un jour FreeCAD) disposent d\'outils qui mettent en évidence un modèle solide en différentes couleurs immédiatement et vous présentent toutes les faces où l\'angle de dépouille n\'est pas correct. Vous ne voulez pas que cela arrive à votre modèle, en particulier après la mise en place d\'un grand nombre de congés!
![ La première Protusion \| thumb \| right \| 400px](images/_HolderTop2-4.jpg ) Quand vous avez fait le croquis (qui est un peu difficile à cause des deux degrés des lignes tangentielles), créer une Protusion de celui-ci s\'étendant jusqu\'à l\'autre côté de la géométrie de l\'ossature, à nouveau avec un décalage de 5 mm à la face latérale. Vous n\'avez pas besoin de créer un plan de référence cette fois, le mode \"jusqu\'à la face \" du dialogue de Protusion propose d\'entrée un décalage.
![ Esquisse pour Pad coupé-out \| thumb \| right \| 400px](images/_HolderTop2-5.jpg ) Ensuite, nous allons réduire la matière sur les deux extrémités de la Protusion car il est toujours idéal pour les pièces en fonte d\'avoir une épaisseur de paroi aussi uniforme que possible. Créez une esquisse sur chacune des faces d\'extrémité de la Protusion et dimensionner à 5 mm le décalage du cercle représentant la bague d\'étanchéité du roulement (rayon de 27,5 mm d\'un côté et 34mm sur l\'autre). Pour le segment de la ligne de fond de l\'esquisse , créer une autre géométrie externe de Protusion et la contraindre. Ainsi l\'esquisse n\'a qu\'une seule dimension, l\'épaisseur de paroi de 5 mm (les dimensions de 150mm et 75mm ne sont pas importants tant qu\'ils sont assez grands pour s\' assurer que tout est coupé).
![ La Protusion avec des découpes pour obtenir une épaisseur de paroi uniforme \| thumb \| right \| 400px](images/_HolderTop2-6.jpg ) Utilisez le croquis que vous avez créé pour faire une Cavité et l\'étendre jusqu\'à la face de la géométrie du squelette qui représente le palier, moins 5 mm pour compenser l\'épaisseur de paroi. Pour la deuxième cavité, vous pouvez utiliser l\'option «Dupliquer objet sélectionné\" dans le menu PartDesign pour reproduire le croquis que vous avez déjà fait (choisissez de ne pas reproduire les objets dépendants si la question apparaît). Ensuite, sélectionnez la face sur laquelle vous souhaitez déplacer cette esquisse , et de dire à FreeCAD de dessiner l\'esquisse sur cette face (c\'est un élément du menu PartDesign). Après la création de la deuxième Cavité, vous pouvez regarder le résultat du fond pour vérifier que vous avez une épaisseur de paroi uniforme de 5 mm sur le contour de la géométrie du squelette.
![ Plan neutre pour appliquer le projet \| thumb \| right \| 400px](images/_HolderTop2-7.jpg ) Maintenant, il est temps de créer le projet et les congés. Le projet nécessite un plan neutre, ce qui signifie que la géométrie qui est coupée par ce plan restera à sa place, tandis que le reste de la face est incliné de l\'angle de dépouille. L\'utilisation du fond de la Protusion à cette fin n\'est pas une bonne idée, parce que l\'épaisseur de la paroi dans la partie supérieure du support deviendrait inférieure à 5 mm. Donc nous créons un plan de référence décalé environ 35mm de XY à cet effet. Activez le squelette et créer le plan, parce que nous en aurons besoin pour appliquer le projet à d\'autres organes, aussi.
![ Première corps avec le projet et les flancs de raccordement \| thumb \| right \| 400px](images/_HolderTop2-8.jpg ) L\'image de droite montre le premier corps fini avec le projet et les congés appliqués. On notera que les bords (concaves) extérieurs ont un rayon de de raccordement plus large de 5 mm, de nouveau avec le but de créer une épaisseur de paroi plus uniforme (plus de 5 mm n\'est pas possible, car alors, après usinage de l\'intérieur du support l\'épaisseur de paroi deviendrait inférieure à 5 mm).

## Ajouter des organes pour les boulons 

![ Le croquis pour le corps des boulons \| thumb \| right \| 400px](images/_HolderTop2-13.jpg ) Les boulons ont besoin de deux corps cylindriques des deux côtés du corps principal. Il est préférable d\'inclure l\'angle de dépouille de 2 degrés dans l\'esquisse. J\'ai essayé de tourner un cylindre et d\'appliquer plus tard un projet, mais des choses étranges se sont passées après la symétrie et je ne pouvais pas mettre les congés sur elle parce que la surface a été déformée en quelque sorte.

Le dessin est dimensionné pour que l\'axe de rotation soit à distance de 12mm du diamètre externe de l\'ossature du corps, 7 mm pour le rayon du trou, plus de 5 mm pour l\'épaisseur de paroi. Pour le plaisir d\'avoir une partie entièrement paramétrique, c\'est une bonne idée d\'ajouter un plan au squelette environ 25 mm au-dessus du plan XY pour marquer le sommet des cylindres. Comme ce sera usinée, l\'esquisse est dimensionné 3mm au-dessus.

![ Le corps des boulons \| thumb \| right \| 400px](images/_HolderTop2-14.jpg ) Créez une révolution de l\'esquisse et appliquer un congé de 4mm vers le haut. Cela signifie que, après usinage et enlèvement de 3mm, un léger rayon restera qui permet d\'éviter une arête vive où quelqu\'un pourrait se couper la main pour serrer la vis.
![ Le corps principal avec les deux organes pour les boulons \| thumb \| right \| 400px](images/_HolderTop2-16.jpg ) Créer une fonction booléenne pour fusionner le corps principal et le corps du boulon. Puis créer un nouvel organe pour l\'autre côté. Dupliquer le croquis de la révolution, le déplacer à cet organe et créez le deuxième corps pour les boulons (Symétriser un corps n\'est pas encore pris en charge si vous avez besoin de refaire la plus grande partie). Puis fusionner ce deuxième corps dans le corps principal . Enfin, appliquez un grand congé sur le bord créé par l\'opération de fusion booléenne. Le plus grand que je pouvais obtenir était 4mm.

## Vider le corps principal 

![ La première Protusion du corps découpe l\'intérieur du corps principal \| thumb \| right \| 300px](images/_HolderTop2-9.jpg ) Nous allons maintenant travailler à l\'intérieur du support et évider pour faire place aux roulements et bagues d\'étanchéité. En faisant cela bien sûr, nous devons garder à l\'esprit la surépaisseur de 3mm. Puisque ce tutoriel enseigne la méthode multi-corps, nous allons créer la géométrie à l\'intérieur comme un corps séparé, puis le couper sur le corps principal par une opération booléenne.

Créer un nouveau corps et le rendre actif. Premièrement, nous avons besoin d\'un plan de référence de 3 mm de décalage intérieur de la face du squelette qui montre le côté du roulement. Puis, dupliquer l\'esquisse de la première Protusion du corps principal. Il sera ajouté au corps principal, donc faites un clic droit dessus et choisissez le pour le déplacer vers le corps nouvellement créé (cette option n\' est disponible que dans le menu contextuel si l\' atelier PartDesign est actif). Dessiner le croquis sur le plan de référence (si l\'esquisse s\'inverse après le dessin, déplacer le plan de référence de l\'autre côté du palier, à côté de l\'endroit où l\'esquisse dupliqué est située). Maintenant, modifier l\'esquisse de sorte que le diamètre est de 3 mm inférieur au diamètre externe de la géométrie de l\'ossature qui représente le palier. Tout ce que vous devez faire est de retirer lpaliera dimension 5mm, faites glisser l\'esquisse à l\'intérieur du cercle de référence, et créez une nouvelle dimension de 3 mm.

![ Le corps de découpe à l\'intérieur du corps du squelette \| thumb \| right \| 400px](images/_HolderTop2-10.jpg ) Ensuite, nous voulons deux autres protusions pour creuser l\'emplacement des bagues d\'étanchéité. Dupliquer le croquis de la première plage de l\'Organe de découpe et de dessiner au plan XZ. Modifier l\'esquisse et remplacer la référence externe avec le diamètre extérieur de la bague d\'étanchéité du roulement. Extruder cette esquisse avec un décalage de 3 mm du côté de la bague d\'étanchéité. Répétez l\'ensemble du processus pour la bague d\'étanchéité de l\'autre côté.

Après cela, nous voulons créer deux autres Protusions comme les deux derniers pour donner à l\'arbre un dégagement (par exemple 3 mm) à l\'intérieur du support.
![ Le corps de découpe complet (congés minimum impossibles) \| thumb \| right \| 400px](images/_HolderTop2-11.jpg ) Maintenant tout ce qui reste est d\'appliquer le projet sur les faces latérales planes, en utilisant le même plan neutre que pour le corps principal, et le congé. Appliquer un congé général de 3mm à tous les bords. Vous remarquerez qu\'il y a plusieurs bords qui ne peuvent pas avoir de congé\... c\'est un défaut du noyau géométrique sous-jacent qui utilise FreeCAD.
![ La pièce brute complète du support (sans usinage) \| thumb \| right \| 400px](images/_HolderTop2-15.jpg ) Nous sommes prêts à creuser le corps principal. Sélectionnez-le et choisissez de créer une nouvelle opération booléenne. Ajouter le corps de découpe à la liste de la fenêtre et régler l\'opération pour \"Couper\". Mettre un congé de 3 mm sur les deux bords résultant de l\'opération de découpe (encore certains bords restent qui sont \"non congéable»). Le résultat devrait ressembler à l\'image sur la droite.

La pièce brute est maintenant terminée. C\'est ce à quoi le support va ressembler avant l\'usinage. A noter que puisque le moule aura une moitié supérieure et inférieure, le bord entre les deux n\'a pas de congé. Aussi, si vous donnez ce modèle à une fonderie assurez-vous de souligner qu\'il a les dimensions après la coulée. La fonderie devra ensuite appliquer un certain pourcentage de retrait au modèle (faire le modèle numérique utilisé pour fabriquer le moule plus grand de sorte que lorsque le métal se refroidit et se contracte après la coulée, il aura la bonne taille).

## Usinage

![ Esquisse pour percer le trou pour les boulons \| thumb \| right \| 400px](images/_HolderTop2-17.jpg ) Pour enlever la matièrie pour l\'usinage de l\'intérieur du support, nous pouvons utiliser le Squelette du corps . Si vous ne voulez pas parce qu\'alors le squelette se cache quelque part au fond de l\'arborescence, vous pouvez également dupliquer l\'esquisse de la fonction de révolution du squelette et recréer la révolution dans un autre corps. Ce ne est pas complètement paramétrique, cependant, parce que l\'esquisse dupliquée est indépendante de l\'original, ainsi vous aurez à travailler sur les deux si vous changez une dimension. Les entités dupliquées dépendantes pourront être prises en charge dans l\'avenir.

Pour le reste de l\'usinage, créer un nouveau corps. Le fond du support sera usinée par une Protusion esquissée sur le plan XY s\' étendant vers le bas. Ensuite, esquisser une révolution pour faire un trou pour les boulons. Vous aurez besoin d\'esquisser sur le plan XZ et tourner de sorte que vous pouvez choisir le diamètre extérieur du squelette du Corps comme une référence externe. La partie supérieure de l\'esquisse servira à usiner un endroit plat pour la tête du boulon. Elle est dimensionnée pour laisser une épaisseur de paroi d\'au moins 5 mm dans le support. Si cela ne donne pas suffisamment d\'espace pour la tête de boulon, vous pouvez déplacer le plan de référence vers le haut. Bien sûr, vous pourriez mettre cette logique dans le squelette, qui est laissé comme exercice pour le lecteur!
![ L\'usinage du corps \| thumb \| right \| 400px](images/_HolderTop2-18.jpg ) Vous pouvez symétriser la révolution sur l\'axe YZ. L\'image de droite montre l\'«usinage» du corps. Bien sûr, la plupart des dimensions des Protusions et révolutions ne sont pas importantes aussi longtemps qu\' il ya beaucoup de chevauchement.
![ Le support fini avec l\'usinage \| thumb \| right \| 400px](images/_HolderTop2-19.jpg ) Enfin, créer une opération booléenne pour couper le Corps de usiné par le Corps principal. Si vous voulez un bel effet visuel, vous pouvez colorer les surfaces usinées différemment du reste de la pièce. C\'est aussi une rétroaction optique utile, vous indiquant si vous avez oublié d\'usiner quelque part.

## Partie Une 

[ Tutoriel de Conception Support de Roulement I](PartDesign_Bearingholder_Tutorial_I/fr.md)



[Category:Tutorials](Category:Tutorials.md)
