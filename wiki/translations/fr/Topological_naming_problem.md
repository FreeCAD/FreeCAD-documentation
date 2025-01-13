# Topological naming problem/fr
## Introduction




Le **problème de dénomination topologique** dans FreeCAD fait référence au conséquences d'une forme qui change de nom interne après une opération de modélisation (protusion, coupe, union, chanfrein, congé, etc.). Cela a pour conséquence la casse ou le calcul incorrect d\'autres caractéristiques paramétriques dépendantes de cette forme. Ce problème concerne tous les objets dans FreeCAD, mais est particulièrement important lors de la création de solides avec l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md) et lors de la cotation de ces solides avec l\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md).

-   Dans <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md), si une entité est prise en charge sur une face (ou une arête ou un sommet), elle peut se rompre si le solide sous-jacent change de taille ou d\'orientation, car la face d\'origine (ou l\'arête ou le sommet) peut être renommé de manière interne.
-   Dans <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/fr.md), si une dimension mesure la longueur d\'un bord projeté, elle risque de se briser si le modèle 3D est modifié, car les sommets peuvent être renommés, modifiant ainsi le bord mesuré.

Le problème de la dénomination topologique est un problème complexe en modélisation CAO qui découle de la façon dont les routines internes FreeCAD traitent les mises à jour des formes géométriques créées avec le [noyau OCCT](OpenCASCADE/fr.md). Ce problème n\'est pas propre à FreeCAD. Il est généralement présent dans les logiciels de CAO, mais la plupart des autres logiciels de CAO disposent d\'une heuristique permettant de réduire l\'impact du problème sur les utilisateurs.

Depuis FreeCAD 0.19, des efforts de développement sont en cours pour améliorer la gestion des formes en ajoutant des techniques heuristiques qui réduisent l\'impact de ces problèmes. L\'[algorithme de nommage](#Algorithme_de_nommage_topologique.md) est conçu pour réduire l\'effort manuel, parfois en corrigeant automatiquement les problèmes, d\'autres fois en présentant une solution probable, et sinon en montrant au moins clairement ce qui a causé le problème. La première version stable de FreeCAD à utiliser ce nouvel algorithme de nommage est la version 1.0. Au fil du temps, cet algorithme sera appliqué à d\'autres parties de FreeCAD, et d\'autres réparations automatiques et assistées seront ajoutées dans les versions ultérieures.

Le problème de dénomination topologique affecte et trouble le plus souvent les nouveaux utilisateurs de FreeCAD. Dans PartDesign, il est conseillé à l\'utilisateur de suivre les meilleures pratiques décrites dans la page [Édition de fonctions](feature_editing/fr.md). L\'utilisation d\'objets de référence pris en charge, tels que les [plans](PartDesign_Plane/fr.md) et les [systèmes de coordonnées locaux](PartDesign_CoordinateSystem/fr.md), est fortement recommandée pour produire des modèles qui ne sont pas facilement sujets à de telles erreurs topologiques. Dans TechDraw, il est conseillé à l\'utilisateur d\'ajouter des cotes uniquement lorsque le modèle 3D est terminé et ne sera plus modifié.



## Exemple

1\. Dans l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md), créez un [PartDesign Corps](PartDesign_Body/fr.md) <img alt="" src=images/PartDesign_Body.svg  style="width:24px;">, puis utilisez <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md) et sélectionnez le plan XY pour dessiner l\'esquisse de base. Effectuez ensuite une <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) pour créer un premier solide.

<img alt="" src=images/FreeCAD_topological_problem_01_solid.png  style="width:" height="400px;">

2\. Sélectionnez la face supérieure du solide précédent et utilisez <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md) pour dessiner une autre esquisse. Effectuez ensuite une deuxième protrusion.

+++
| <img alt="" src=images/FreeCAD_topological_problem_02_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_03_solid_2.png  style="width:" height="400px;"> |
+++

3\. Sélectionnez la face supérieure de l\'extrusion précédente et créez à nouveau une esquisse et une protrusion.

<img alt="" src=images/FreeCAD_topological_problem_04_solid_3.png  style="width:" height="400px;">

4\. Double-cliquez à présent sur la seconde esquisse et modifiez la de manière à ce que sa longueur soit dans la direction X ; cela recréera la deuxième protrusion. Les troisième esquisse et protrusion resteront au même endroit.

+++
| <img alt="" src=images/FreeCAD_topological_problem_05_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_06_solid_2.png  style="width:" height="400px;"> |
+++

<img alt="" src=images/FreeCAD_topological_problem_07_solid_3.png  style="width:" height="400px;">

5\. Double-cliquez à nouveau sur la seconde esquisse et ajustez ses points de sorte qu\'une partie de celle-ci se situe en dehors des limites définies par la première protrusion. En faisant cela, la deuxième protrusion se recalculera correctement, cependant en regardant la [vue arborescente](tree_view/fr.md) une erreur sera indiquée dans la troisième protrusion.

+++
| <img alt="" src=images/FreeCAD_topological_problem_08_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_09_solid_2.png  style="width:" height="400px;"> |
+++

![](images/FreeCAD_topological_problem_12_broken_tree.png )

6\. En rendant visible les troisièmes esquisse et protrusion, il est clair que le calcul du nouveau solide ne s\'est pas déroulé correctement. La troisième esquisse, au lieu d\'être appuyée par la face supérieure de la deuxième protrusion, apparaît dans un endroit étrange, avec sa normale orientée vers la direction X. Cela entraîne une protrusion non valide, car cette protrusion serait déconnectée du reste du <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md), ce qui n\'est pas autorisé.

Le problème semble être que lorsque la deuxième esquisse a été modifiée, la face supérieure du deuxième bloc a été renommée de `Face13` à `Face14`. La troisième esquisse est attachée à `Face13` comme elle l'était à l'origine, mais comme cette face est maintenant latérale et non plus au dessus, l'esquisse suit son orientation et est maintenant mal positionnée.

+++
| <img alt="" src=images/FreeCAD_topological_problem_10_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_11_solid_2_faces.png  style="width:" height="400px;"> |
+++

7\. Pour résoudre le problème, la troisième esquisse doit à nouveau être tracée sur la face supérieure. Sélectionnez l\'esquisse, cliquez sur les points de suspension (trois points) en regard de la {{PropertyData/fr|Map Mode}}, puis choisissez à nouveau la face supérieure du second bloc. Ensuite, l\'esquisse se déplace vers le haut du solide existant et le troisième bloc est généré sans problème.

![](images/FreeCAD_topological_problem_13_remap_sketch_2.png )

+++
| <img alt="" src=images/FreeCAD_topological_problem_14_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_15_solid_3.png  style="width:" height="400px;"> |
+++

Le retraçage d\'une esquisse de cette manière peut être effectué chaque fois qu\'il y a une erreur de nom topologique. Toutefois, cette opération peut s\'avérer fastidieuse si le modèle est compliqué et que de nombreuses esquisses de ce type doivent être ajustées.

## Solution

![](images/FreeCAD_topological_problem_16_dependency_graph.png )

Le [graphe des dépendances](Std_DependencyGraph/fr.md) est un outil utile pour observer les relations entre les différents corps du document. L\'utilisation du flux de travail de modélisation d\'origine révèle la relation directe qui existe entre les esquisses et les protusions. Comme une chaîne, il est facile de voir que cette dépendance directe sera sujette à des problèmes de dénomination topologique si l\'un des liens de la séquence change.

Comme expliqué sur la page d\'[édition de fonctions](Feature_editing/fr.md), une solution à ce problème consiste à prendre en charge les esquisses non pas sur les faces, mais sur les plans principaux de l\'origine du [PartDesign Corps](PartDesign_Body/fr.md) ou sur les plans de référence attachés à ces plans principaux. L\'utilisation de plans de référence pour prendre en charge une seule esquisse, comme décrit ci-dessous, n\'est en fait pas nécessaire car l\'esquisse elle-même peut être directement attachée à un plan principal et dispose des mêmes options de décalage qu\'un plan de référence. Toutefois, l\'utilisation de plans de référence peut s\'avérer utile pour le positionnement de plusieurs esquisses.

1\. Sélectionnez l\'origine du [PartDesign Corps](PartDesign_Body/fr.md) et assurez-vous qu\'il est visible. Sélectionnez ensuite le plan XY et cliquez sur [PartDesign Plan de référence](PartDesign_Plane/fr.md). Dans la fenêtre de dialogue Décalage, attribuez-lui un décalage dans la direction Z afin que le plan de référence soit coplanaire avec la face supérieure du premier bloc.

2\. Répétez l\'opération en ajoutant cette fois un décalage plus important afin que le deuxième plan de référence soit coplanaire avec la face supérieure du second bloc.




+++
| <img alt="" src=images/FreeCAD_topological_problem_17_datum_plane_1.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_18_datum_plane_2.png  style="width:" height="400px;"> |
+++

3\. Sélectionnez la seconde esquisse, cliquez sur les points de suspension en regard de la propriété {{PropertyData/fr|Map Mode}}, puis sélectionnez le premier plan de référence. Le plan de référence est déjà décalé par rapport au plan XY du corps, de sorte qu\'aucun autre décalage Z n\'est requis pour l\'esquisse.

4\. Répétez le processus avec la troisième esquisse et sélectionnez le deuxième plan de référence comme support. Là encore, aucun décalage Z supplémentaire n\'est nécessaire.

5\. Le graphe de dépendance montre maintenant que les esquisses et les blocs sont pris en charge par les plans de référence. Ce modèle est plus stable car chaque esquisse peut être modifiée essentiellement indépendamment les uns des autres.

![](images/FreeCAD_topological_problem_19_dependency_graph_datum_planes.png )

6\. Double-cliquez sur la deuxième esquisse et modifiez la forme. Le deuxième bloc doit être mis à jour immédiatement sans causer de problèmes topologiques au troisième dessin et au troisième bloc.

<img alt="" src=images/FreeCAD_topological_problem_20_independent_solid_2.png  style="width:" height="400px;">

7\. En fait, chaque esquisse peut être modifiée sans interférer avec chacun des autres blocs. Tant que les blocs ont une longueur d\'extrusion suffisante pour qu\'ils se touchent et forment un solide contigu, le corps entier sera valide.

<img alt="" src=images/FreeCAD_topological_problem_21_independent_solids_all.png  style="width:" height="400px;">



## Compromis

Ajouter des objets de référence demande plus de travail à l\'utilisateur, mais produit finalement des modèles plus stables et moins sujets au problème de dénomination topologique.

Naturellement, des objets de référence peuvent être créés avant que des esquisses ne soient dessinées et que des blocs ne soient produits. Cela peut être utile pour visualiser la forme approximative et les dimensions du corps final.

Les plans de référence peuvent également être basés sur d'autres plans de référence. Cela crée une chaîne de dépendances pouvant également entraîner des problèmes topologiques ; Cependant, comme les plans de données sont des objets très simples, le risque d'avoir ces problèmes est moindre que si la face d'un objet solide servait de support.

Les objets de référence, [points](PartDesign_Point/fr.md), [lignes](PartDesign_Line/fr.md), [plans](PartDesign_Plane/fr.md), et [systèmes de coordonnées](PartDesign_CoordinateSystem/fr.md) peuvent également être utiles en tant que géométrie de référence, c'est-à-dire en tant qu'aide visuelle pour montrer les caractéristiques importantes du modèle, même si aucune esquisse n'y est directement attachée.



## Algorithme de nommage topologique 

L\'algorithme de nommage topologique de Realthunder, décrit dans le fil de discussion [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278), qui a été choisi pour réduire l\'impact de ce problème, a été largement décrit comme « réglant le problème du nommage topologique ». Cela a involontairement induit de nombreux utilisateurs en erreur en leur faisant croire qu\'il ne serait plus utile d\'utiliser des techniques telles que les référentiels, le placement explicite d\'esquisses et la [modification de fonctions](Feature_editing/fr#Conseils_pour_la_création_de_modèles_robustes.md) pour rendre les modèles plus stables. L\'algorithme n\'a pas pour but de résoudre tous les problèmes liés à l\'ambiguïté des noms topologiques. Il a plutôt trois objectifs.

1.  L\'objectif premier et le plus important est, dans la mesure du possible, d\'« identifier » les références cassées par des changements topologiques et d\'afficher une erreur à l\'utilisateur. Au lieu d\'avoir à parcourir une série d\'opérations pour trouver la première opération qui diverge de l\'intention de conception, l\'opération qui change les noms sera normalement signalée par une erreur, ce qui rendra beaucoup plus facile la correction manuelle des problèmes de modèle introduits par des changements d\'opérations ou de paramètres.
2.  Parfois, FreeCAD sera capable d\'identifier une correction **probable** pour une référence cassée, de sorte que lorsque l\'utilisateur répare manuellement la référence brisée signalée, un candidat lui sera présenté pour qu\'il l\'accepte ou la modifie. Un exemple courant est celui des opérations d\'habillage telles que les congés et les chanfreins, pour lesquelles l\'utilisateur peut être amené à éditer l\'opération et à accepter la sélection d\'éléments de remplacement proposée ou à la modifier pour la corriger.
3.  Dans certains cas, FreeCAD sera capable de résoudre **automatiquement** la référence cassée, parce que suffisamment d\'informations sur la référence sont stockées pour avoir une grande confiance dans le fait que le remplacement est correct. Par exemple, lorsque l\'on dessine directement sur une face, l\'algorithme répare souvent (mais pas toujours) correctement la référence à la face lorsque la géométrie sous-jacente est modifiée de manière paramétrique. (Lorsque l\'on modifie la structure, par exemple en ajoutant ou en supprimant des opérations au milieu d\'un corps de conception de pièce, ce type de réparation automatique est moins probable). Cependant, FreeCAD ne le fera qu\'avec une grande confiance dans l\'exactitude de la réparation, parce qu\'une réparation automatique incorrecte peut réintroduire le problème d\'avoir à chercher où un problème a été introduit afin de réparer un modèle après une modification. *D\'abord, ne pas nuire*.

Dans FreeCAD 1.0, l\'implémentation de cet algorithme dans la version officielle de FreeCAD a atteint la parité avec le fork « Linkstage 3 » de Realthunder, où il a développé l\'algorithme à l\'origine, au moment où le travail d\'intégration a commencé. Il y a de nouvelles fonctionnalités de FreeCAD qui pourraient utiliser l\'algorithme mais ne le font pas encore, et il y aura toujours d\'autres opportunités d\'ajouter des corrections candidates et des réparations automatiques. Le travail initial a fourni un « cadre » à utiliser pour ces améliorations supplémentaires au fil du temps, à la fois dans le noyau de FreeCAD et dans les modules complémentaires.



## Liens

-   [PartDesign Congé - Nom topologique](PartDesign_Fillet/fr#D.C3.A9nomination_topologique.md)
-   [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278) : une solution possible par realthunder.
-   [Topological Naming Project](Topological_Naming_Project.md) : idée pour résoudre le problème, par ickby.
-   [Script pour création topologique](Topological_data_scripting/fr.md)
-   [Édition de fonctions](Feature_editing/fr.md) : contient des conseils complémentaires sur les techniques de modélisation stables.
-   [Clarification et extension de la documentation sur le « problème de dénomination topologique »](https://forum.freecad.org/viewtopic.php?p=770360) : clarification des attentes concernant l\'algorithme de dénomination topologique de Realthunder sélectionné pour FreeCAD 1.0.



## Vidéos

-   [Why do my FreeCAD models break? - \"Topological Naming Problem\"](https://youtu.be/6p2vqEEmWq4): Une explication vidéo des problèmes sous-jacents du [Problème de dénomination topologique](Topological_naming_problem/fr.md)


 {{TechDraw Tools navi}} {{PartDesign Tools navi}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [TechDraw](Category_TechDraw.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Topological naming problem/fr
