---
- TutorialInfo:   Topic:Ancrage
   Level: Débutant et intermédiaire
   Author:Bance
   Time:1 heure
   FCVersion: V0.17 ou au delà
   Files:[https://github.com/BanceFC/Examples/blob/master/AttachmentTutorial.FCStd Basic Attachment Tutorial.FCStd]
---

# Basic Attachment Tutorial/fr





![centre\|Le modèle terminé](images/Attachment_Model.png )

Ce tutoriel devrait servir d\'introduction à [Part Ancrage](Part_EditAttachment/fr.md). Il n\'est pas exhaustif mais nous espérons qu\'il aidera les utilisateurs à se familiariser avec.

Ancrage est un utilitaire pour attacher un objet à un autre. Cela lie les propriétés de placement des deux objets, l\'objet ancré suivra alors l\'original (si son placement est modifié.) L\'accent est mis sur l\'atelier Part Design et l\'ancrage d\'esquisses à d\'autres esquisses. Il s\'agit d\'une méthode recommandée pour créer des modèles [*stables*](Feature_editing/fr#Conseils_pour_la_cr.C3.A9ation_de_mod.C3.A8les_robustes.md). Écrit pour la V0.19, mais devrait être valide pour toute version V0.17 et ultérieure. Cependant, les choses peuvent différer dans certains détails. Le modèle original a été conçu par Md. Aminul Islam et téléchargé à partir d\'ici : <https://grabcad.com/library/50-cad-exercise-drawing-1>



## Prérequis

Avant de démarrer ce tutoriel l\'utilisateur doit :

1.  Utiliser la version 0.17 ou supérieure.
2.  Être à l\'aise pour naviguer dans la [Vue 3D](3D_view/fr.md).
3.  Être capable de créer et de contraindre une [esquisse](Sketcher_Workbench/fr.md).
4.  Avoir une connaissance de base de l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Atelier PartDesign](PartDesign_Workbench/fr.md).
5.  Avoir une connaissance de base des [Expressions](Expressions/fr.md).



## Objectifs

Le but de ce tutoriel est de montrer comment un modèle peut être construit en positionnant des esquisses par rapport à d\'autres géométries à l\'aide de certains des différents modes d\'ancrage disponibles.

Bien qu\'il soit possible d\'utiliser la géométrie solide (sommets, arêtes et faces) pour la géométrie de référence, dans l\'intérêt de ce qui est considéré comme une bonne pratique, ce tutoriel s\'abstiendra de le faire. Voir [Édition de fonctions](Feature_editing/fr.md) pour plus d\'explications.



## Préliminaires

Avant de commencer, examinons comment nous devrions procéder pour construire ce modèle.

Quel que soit l\'angle sous lequel nous le regardons, nous voyons un carré ou un rectangle avec un coin coupé.

![centre\|La vue TechDraw](images/AttachmentTD.png )

Il existe cependant un axe évident à partir duquel toutes les caractéristiques sont communes.

Il est parfaitement possible de créer une géométrie de données ici et d\'y attacher toutes les esquisses. Dans certains modèles, ce serait un choix judicieux, pour les besoins de ce tutoriel, nous nous limiterons Std Plans et aux esquisses.

Nous pourrions faire une esquisse sur n\'importe lequel des grands plans. Nous pourrions inclure un coin coupé dans notre esquisse de base, mais laissons cela et incluons une esquisse et une poche supplémentaire, à des fins d\'apprentissage.

![centre\|L\'axe commun](images/CommonAxis.png )



## Ancrage

Nous commencerons par un bloc et nous enlèverons l\'excédent à l\'aide d\'une cavité.

Basculez vers l\'atelier Part Design, ouvrez un nouveau document, créez un corps et une nouvelle esquisse sur le plan XY.

Là, vous venez de faire un ***ancrage***. Lorsque vous sélectionnez le plan sur lequel réaliser l\'esquisse, c\'est en fait ce qui est fait, le dialogue de sélection du plan n\'est qu\'une version simplifiée du dialogue d\'ancrage, où tous les décalages sont fixés à zéro.

Dessinez un rectangle, centrez-le sur l\'origine, contraignez-le avec une longueur (horizontale) de 70 mm et nommez-le \"length\", contraignez-le encore avec une largeur (verticale) de 40 mm et nommez-le \"width\".

Sélectionner l\'esquisse, presser le bouton **F2** et le renommer \"BaseSketch\"

![centre\|L\'esquisse de base](images/Sketch1.png )

[En haut](#top.md)



### Décalage de l\'ancrage 

Si nous laissons l\'esquisse où elle est, l\'exemple serait trop facile, alors changeons la position de l\'esquisse en modifiant le décalage de son ancrage.

Dans la vue combinée (onglet Données), regardez dans la section Attachment du volet des propriétés, ici nous pouvons voir que BaseSketch a un support de XY_Plane et est attaché avec le mode Flat Face. Regardez plus bas et trouvez Attachment Offset (décalage d\'ancrage) et développez-le, en cliquant sur le signe plus à côté.

Faire de même pour le sous-titre Position. Modifier le décalage X à 80 mm et le décalage Y à 90 mm.

![centre\|Décalage d\'ancrage](images/comboview.png )

Le décalage d\'ancrage est généralement utilisé en conjonction avec des expressions pour offrir une position paramétrique parallèle au plan, par exemple pour positionner une esquisse sur la face supérieure d\'un bloc, en utilisant une expression (Pad.Length) pour le décalage axe Z.

L\'esquisse peut maintenant être extrudée <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;">, supposons que la hauteur de l\'extrusion doit être la même que la largeur de l\'esquisse. Dans la boîte de dialogue **Pad parameters**, sélectionnez la case **Length**, appuyez sur **<nowiki>=</nowiki>** ou sélectionnez l\'icône de fonction <img alt="" src=images/Bound-expression.svg  style="width:24px;"> et tapez \"**Sketch.Constraints.width**\", cette expression devrait donné \"40 mm\", puis cocher **Symmetric to plane** et appuyez sur la touche **OK**.

![centre\|La protrusion de base](images/BasePad2.png )

Faisons l\'esquisse suivante, ce n\'est pas vraiment important celle que nous choisissons, mais le plus facile est le triangle isocèle 20x20 qui empiète sur la longueur du bloc.

Faites une nouvelle esquisse, choisissez le plan que vous voulez (nous allons de toute façon changer son ancrage).

Dessinez le triangle, rendez les deux côtés égaux et contraignez sa longueur de la même manière que vous l\'avez fait pour la longueur du pavé, mais cette fois, faites la formule \"**Sketch.Constraints.width/2**\".

Il devrait rester deux degrés de liberté, à savoir la position par rapport à l\'origine. Fixez l\'un des coins à l\'origine de sorte que l\'esquisse ressemble à ceci:

![centre\|Le premier triangle](images/IsoscelesSketch.png )

[En haut](#top.md)



### Changer l\'ancrage 

Fermez l\'esquisse. Renommez l\'esquisse en l\'appelant \'IsoscelesSketch\'. L\'origine de l\'esquisse est le point qui sera attaché dans le futur. Il est donc important de choisir comment l\'esquisse est contrainte à l\'origine. L\'origine peut être considérée comme un crochet qui s\'ancre à la référence. Nous pouvons ajuster la position de l\'esquisse à l\'aide de décalages, mais il est préférable de faire un choix judicieux dès le départ.

Nous allons maintenant changer le mode d\'ancrage de l\'esquisse dans notre modèle.

Sélectionnez la protrusion et rendez-la invisible, et rendez BaseSketch visible. Nous devons voir BaseSketch et nous voulons masquer la protrusion afin d\'éviter de faire des sélections incorrectes.

La vue 3D devrait ressembler à quelque chose comme ceci :

![centre\|Deux esquisses](images/TwoSketches.png )

j\'ai choisi XY comme plan de construction du triangle isocèle mais un autre plan peut être choisi.

Nous devons maintenant sélectionner IsoscelesSketch et accéder au volet des propriétés dans la vue Combo. Cliquez dans la case de valeur à côté de la propriété Map Mode, un bouton apparaît avec une ellipse **...**.

![centre\|Sélection du mode Map](images/MapModeSelect.png )

Cliquez dessus et un volet de tâches s\'ouvrira avec la boîte de dialogue Attachment.

![centre\|Boîte de dialogue Attachment](images/AttachmentDialogue.png )

Maintenant on voit l\'ancrage où l\'esquisse a été créée (dans la boîte de dialogue sélection du plan).

Le bouton **Référence 1** est en mode sélection, donc dans la vue 3D, sélectionnez l\'un des côtés longs de l\'esquisse de base.

L\'IsoscelesSketch s\'attachera à la ligne que vous avez sélectionnée, et la fenêtre du mode d\'attachement changera pour refléter les modes disponibles. Si le triangle pointe dans le mauvais sens, vous pouvez le corriger en cochant la case \"Inverser les côtés\" au bas de la boîte de dialogue (ou plus tard, après avoir fermé la boîte de dialogue, vous pouvez le modifier dans l\'onglet de données des propriétés en réglant \"Map Reversed\" à \"True\").

![centre\|Normale à l\'arête isocèle](images/NormalToEdgeIsosceles.png )

![centre\|Normale à l\'arrête Attachment](images/NormalToEdgeAttachment.png )

Vous pouvez voir que l\'IsocelesSketch a été attaché à la ligne sélectionnée au point que nous avons contraint à l\'origine plus tôt.

Cette notion de l\'origine étant le point d\'ancrage est importante, elle rend les modes d\'attache très flexibles et peut être un outil puissant dans votre modélisation.

Il peut être utilisé avec l\'ajout de décalages pour positionner avec précision les esquisses sans dépendre de la géométrie générée et de tous les problèmes pouvant découler de leur utilisation.

FreeCAD essaie de prédire le mode d\'ancrage pour vous et filtre les modes disponibles pour la sélection donnée.

Dans ce cas, les options sont \"Désactivées\", [**Normal à une arête**](Part_EditAttachment/fr#Normal_.C3.A0_une_ar.C3.AAte.md) et [Inertie 2-3](Part_EditAttachment/fr#Inertie_2-3.md). Normal à une arête est en gras et est considéré comme la sélection préférée.

La zone de notification en haut de la boîte de dialogue affiche un message en vert indiquant le mode utilisé.

Les options grisées indiquent que d\'autres sélections sont nécessaires pour les activer.

À ce stade, vous pouvez faire une autre sélection et voir la différence entre les modes. N\'oubliez pas de revenir en mode \"**Normal To Edge**\" avant de poursuivre le tutoriel.

L\'IsocelesSketch est maintenant correctement positionné, confirmez et quittez le dialogue.

Vous pouvez maintenant [découper](PartDesign_Pocket/fr.md) l\'esquisse.

![centre\|Découpe](images/Pocket.png )

[En haut](#top.md)



### Un pas plus loin 

Créez l\'esquisse suivante, les dimensions doivent être des expressions (\"**Sketch.Constraints.width**\",\"**Sketch.Constraints.width/2**\") et elle doit être contrainte à l\'origine au sommet adjacent à l\'hypoténuse et son côté le plus court. (Dans l\'esquisse vide, si vous connaissez la **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Copie carbone](Sketcher_CarbonCopy/fr.md)**, vous pouvez l\'utiliser pour faire une copie de l\'esquisse \'IsoscelesSketch\' et modifiez ses paramètres en conséquence.)

Renommer l\'esquisse RightAngleTriangleSketch.

![centre\|RightAngleTriangleSketch](images/FinalSketch.png )

Encore une fois, nous devons masquer le solide, dans ce cas Pocket, et nous assurer que les deux esquisses sont visibles pour la sélection (laissez isocelesSketch invisible, cela ne fera que gêner!).

Sélectionner RightAngleTriangleSketch et ouvrer la boite de dialogue de l\'ancrage.

Sélectionnez l\'un des côtés courts des rectangles comme première référence.

![centre\|RightAngleTriangleSketch mode Normal To Edge](images/RATNormalToEdge.png )

La vue 3D doit être similaire à l\'image ci-dessus. Peu importe à quelle extrémité de la ligne le triangle est attaché (cela dépend de la façon dont le rectangle a été dessiné !)

Si vous avez choisi la mauvaise ligne, changez-la maintenant. Si le triangle pointe dans le mauvais sens, vous pouvez le corriger en cochant la case \"Retourner les côtés\" au bas de la boîte de dialogue (ou plus tard après avoir fermé la boîte de dialogue, il peut être modifié dans l\'onglet des données des propriétés en définissant \"Map Reversed\" à \"True\").

Le RightAngleTriangleSketch est maintenant dans une position qui nous donnera la bonne géométrie après une opération de pocket, mais nous pouvons être un peu inventifs ici et positionner l\'esquisse de manière à ce qu\'il nous soit plus facile d\'attacher plus tard la géométrie. Nous allons déplacer notre esquisse au milieu de la ligne afin qu\'elle nous fournisse un sommet en haut du [chanfrein](Glossary/fr#C.md) d\'angle.

Dans la boîte de dialogue d\'attachement, nous allons changer le mode d\'ancrage de [**Normal à une arête**](Part_EditAttachment/fr#Normal_.C3.A0_une_ar.C3.AAte.md) à [Inertie 2-3](Part_EditAttachment/fr#Inertie_2-3.md). Cela changera la position au centre de la ligne, cela dépasse le cadre de ce tutoriel pour décrire tous les modes d\'ancrage, leurs descriptions peuvent être trouvées à la page <img alt="" src=images/Part_Attachment.svg  style="width:24px;"> [Part Ancrage](Part_EditAttachment/fr.md). Il est clair qu\'inertia 2-3 utilise le centre de masse et fait l\'affaire ici.

![centre\|Boîte de dialogue Attachment en mode Inertia 2-3](images/ADInertia.png )

![centre\|RightAngleTriangleSketch mode Inertia 2-3](images/3DInertia.png )

Le RightAngleTriangleSketch est maintenant correctement positionné, confirmez et quittez le dialogue.

Vous pouvez maintenant effectuer une opération de poche sur l\'esquisse. Cette fois, utilisez Mirroir par rapport au plan.

![centre\|2ème poche](images/2ndPocket.png )

[En haut](#top.md)



### Manipulation de l\'ancrage 

En général il vaut mieux positionner nos esquisses simplement avec des modes d\'ancrage. Mais il n\'est pas toujours possible de positionner les esquisses exactement là où nous en avons besoin sans modifier le mode d\'ancrage d\'une manière ou d\'une autre.

FreeCAD fournit un certain nombre de moyens de le faire.

1.  [Attachment Offset](Part_Part2DObject/fr#Property_Attachment_Offset.md) permet le positionnement par rapport aux coordonnées locales du point d\'ancrage. (où l\'origine de l\'esquisse positionnée est attachée).
2.  [Map Path](Part_Part2DObject/fr#Property_Map_Path.md) (Propriété dans l\'onglet Données avec l\'option Afficher tout activée) : permet le positionnement le long d\'une arête sélectionnée.
3.  [Flip Sides/Map Reversed](Part_Part2DObject/fr#Property_Map_Reversed.md). Miroir effectif de l\'esquisse.

Pour notre esquisse finale, nous l\'attacherons arbitrairement et corrigerons sa position à l\'aide des modificateurs répertoriés ci-dessus.

Créez l\'esquisse finale, les dimensions doivent être des expressions (\"**Sketch.Constraints.width\'\'\", \"**Sketch.Constraints.width/2\'\'\'\") et elle doit être contrainte à l\'origine au sommet adjacent à l\'hypoténuse et à son côté le plus court.

Renommer le sketch FinalSketch.

![centre\|FinalSketch](images/RightAngleTriangle.png )

Notez que FinalSketch a été contrainte à l\'origine différemment. Sinon, nous aurions pu utiliser **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Copie carbone](Sketcher_CarbonCopy/fr.md)** mais l\'esquisse ne contient que trois lignes et cinq contraintes.

Une fois encore, nous devons masquer le solide, dans ce cas Pocket001, et nous assurer que les deux esquisses sont visibles pour la sélection (BaseSketch et FinalSketch).

Sélectionnez FinalSketch et ouvrez la boîte de dialogue d\'ancrage, sélectionnez l\'un des côtés courts des rectangles comme première référence.

![centre\|FinalSketchAttachment](images/NormalToEdgeFinal.png )

La vue 3D doit être similaire à l\'image ci-dessus. Peu importe à quelle extrémité de la ligne le triangle est attaché (cela dépend de la façon dont le rectangle a été dessiné !)

Maintenant, nous devons l\'inverser, le translater de 90° et le décaler vers le coin.

Au bas de la boîte de dialogue d\'ancrage se trouve une case à cocher intitulée \"Flip Sides\", cochez cette case.

Le FinalSketch se réfléchit lui-même.

Nous allons maintenant translater de 90°. À partir de l\'illustration FinalSketch ci-dessus, nous pouvons voir que l\'axe de révolution devrait être l\'axe X. Dans le Wiki, cela s\'appelle [\"Roulis\"](Tasks_Placement/fr#Roll.md). N\'oubliez pas que ceci est relatif au système de coordonnées local. Entrez 90° dans la case \"around X-axis\" de la section décalage de la boîte de dialogue d\'ancrage.

![centre\|FinalSketch retourné et pivoté](images/FSFlipRot.png )

![centre\|Boîte de dialogue d\'ancrage de FinalSketch](images/FSFlipRotAD.png )

Nous pourrions utiliser le décalage de la direction Z - qui correspond maintenant à la direction Y opposée dans le système de coordonnées global - pour déplacer FinalSketch vers le coin, mais je voudrais démontrer une autre fonctionnalité.

Alors validons et fermons le dialogue pour l\'instant.

[En haut](#top.md)



### Paramètre Map Path 

Sélectionnez FinalSketch et regardez dans la vue combinée, le volet des propriétés dans la section attachment, juste en dessous de la propriété Map Mode se trouve le paramètre Map Path.

![centre\|Panneau des propriétés de FinalSketch](images/FinalSketchProperties.png )

Le paramètre par défaut est 0.0 si nous le changeons en 1, l\'esquisse sera mappée à l\'autre extrémité de la ligne et 0.5 nous donne la moitié du chemin. Entrez 0.5 dans la colonne de valeur.

La combinaison de \'Normal To Edge\' et le paramètre Map Path est très utile pour positionner les esquisses pour les lissages ou les balayages.

![centre\|Position de FinalSketch](images/FinalSketchPosition.png )

Vous pouvez maintenant effectuer une opération de poche sur l\'esquisse. N\'oubliez pas d\'utiliser Mirroir par rapport au plan.

![centre\|3ème poche](images/3rdPocket.png )

[En haut](#top.md)



### Un mode de sélection différent 

Jusqu\'à présent, nous avons vu comment positionner des esquisses avec des modes d\'attachement et des décalages, mais nous aurions pu utiliser des plans standard car le positionnement relatif était assez simple.

Maintenant, nous sommes confrontés à un problème plus difficile, comment pouvons-nous couper ce morceau qui reste ?

![centre\|Résidus de coupe](images/3rdPocketMarked.png )

Nous pouvons voir qu\'il y a un plan qui passe par les coins du triangle rouge, ce serait simple si nous pouvions simplement le découper là.

Eh bien parce que nous avons fait attention à la façon dont nous avons positionné nos esquisses plus tôt, nous le pouvons!

Tout d\'abord, rendez le solide invisible, en fait, rendez tout invisible sauf RightAngleTriangleSketch et FinalSketch.

Sélectionnez maintenant les trois points qui forment le plan, N\'oubliez pas de maintenir la touche **Ctrl** (CMD sur un Mac) pendant la sélection.

![centre\|Sélection](images/TwoTriangles.png )

Lorsque vous appuyez sur **<img src="images/PartDesign_Plane.svg" width=16px> [Créer un plan de référence](PartDesign_Plane/fr.md)**, le dialogue d\'ancrage s\'ouvrira montrant les trois points que vous avez sélectionnés comme références 1-3 et un mode \'Plane By 3 Points\'.

![centre\|Boîte de dialogue Attachment](images/DPAttachDia.png )

Confirmez et fermez la boîte de dialogue. Nous pouvons maintenant utiliser le plan de référence pour créer une esquisse, mais il n\'est pas nécessaire d\'utiliser le plan directement pour effectuer le pocket du matériau en excès. Assurez-vous que le plan de référence est sélectionné et cliquez sur pocket, dans le dialogue de pocket sélectionnez \"A travers tout\" et \"inversé\". Fermez le dialogue et nous avons tous terminé.

![centre\|L\'objet fini](images/FinishedArticle.png )

[En haut](#top.md)



### Ancrage temporaire à un plan généré 

Parfois, il est difficile de déterminer comment aligner l\'esquisse ou le plan de référence sur la face générée sans réellement s\'y attacher, ce qui, comme indiqué ci-dessus, peut être problématique. Une solution consiste à attacher à la géométrie générée, puis à modifier l\'ancrage à l\'un des plans de coordonnées. FreeCAD conservera intactes la position et l\'orientation existantes mais la référencera désormais à des plans stables, évitant ainsi les problèmes de renommage topologique. Cependant, le coût de cette opération est que le lien paramétrique avec la géométrie générée est perdu. Si le modèle sous-jacent est modifié, tout ne s\'effondrera pas comme cela arrive souvent lors de l\'ancrage à la géométrie générée mais l\'ancrage ne suivra pas les changements et devra être ajusté en répétant l\'astuce d\'ancrage temporaire.

La méthode précédente est plus robuste mais plus abstraite et complexe à réaliser. L\'astuce de l\'ancrage temporaire est rapide et facile à mettre en œuvre, plus robuste que l\'ancrage à la géométrie générée, mais perd un certain degré de liaison dans le processus de modélisation paramétrique.

## Conclusion

Part Ancrage ne garantit pas un modèle robuste. La clé est d\'éviter d\'ancrer ou de placer des esquisses sur la géométrie générée comme les faces ou les bords des protrusions et des poches.

Il existe de nombreux modes d\'ancrage disponibles pour les utilisateurs, seules les bases sont couvertes ici.

Une chose importante à retenir de ce tutoriel, c\'est l\'importance de l\'origine qui est le \"crochet\". Rappelez-vous également que l\'orientation se fait dans le système de coordonnées locales.

Happy Attaching!

[En haut](#top.md)


{{PartDesign_Tools_navi

}} {{Sketcher_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Basic Attachment Tutorial/fr
