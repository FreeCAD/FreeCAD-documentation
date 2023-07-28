# TechDraw Section Examples/fr
{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md) a fait un grand pas en avant en ce qui concerne la génération de **vues de coupe**. Pour ne pas surcharger les pages de référence, l\'objet de cette page est de donner des exemples et de fournir des noms appropriés pour les tâches effectuées.

Je fais de mon mieux pour trouver les termes corrects, mais comme je ne suis pas de langue maternelle anglaise, c\'est à vous de corriger mes erreurs si vous en trouvez.



## Coupes

Les coupes sont utilisées pour regarder à l\'intérieur d\'un objet afin de montrer des détails qui sont autrement invisibles ou difficiles à reconnaître. Le dessin comporte généralement des vues montrant l\'objet dans au moins deux directions. Si une coupe est fournie, sa position et son orientation sont indiquées par une ligne de coupe dans l\'une des vues.

Dans FreeCAD, il n\'est pas possible de dessiner directement une ligne de coupe, FreeCAD s\'appuie plutôt sur les entrées du [panneau de tâches](Task_panel.md) (voir [TechDraw Coupe simple](TechDraw_SectionView/fr#Utilisation.md) et [TechDraw Coupe complexe](TechDraw_ComplexSection/fr#Utilisation.md)).



## Exemple d\'objet 

Cet objet n\'a aucune utilité si ce n\'est de décrire les différentes représentations des coupes.

<img alt="" src=images/TechDraw_ExampleSection-01.png  style="width:400px;"> 
*3 vues et une image 3D de l'objet*



## Les coupes simples 

L\'outil <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [TechDraw Vue en coupe](TechDraw_SectionView/fr.md) crée une coupe simple qui utilise un seul plan pour couper un objet.

L\'outil nécessite une vue de base (propriété **Base View**) pour positionner le plan de coupe. L\'axe vertical du plan de coupe est toujours la normale de la vue de base et l\'axe horizontal du plan de coupe est parallèle à la ligne de coupe. En général, la vue de section est orientée avec son axe horizontal également parallèle à la ligne de coupe. L\'angle entre la ligne de coupe et l\'axe horizontal de la vue de base est contrôlé par des widgets dans la zone **Définir la direction de la vue** du panneau des tâches de l\'outil :

<img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width:200px;">

La boîte combinée **Direction de la vue selon un angle** permet de définir un angle arbitraire. Les quatre boutons peuvent être utilisés des angles prédéfinis :

<img alt="" src=images/Section-up.svg  style="width:32px;"> 90° (haut), <img alt="" src=images/Section-down.svg  style="width:32px;"> 270° (bas), <img alt="" src=images/Section-left.svg  style="width:32px;"> 180° (gauche), <img alt="" src=images/Section-right.svg  style="width:32px;"> 0° (droit)



### Coupe horizontale 

Coupe A-A (coupe vers le haut)

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-03.png  style="width:200px;"> 
*Vue de base + <img src="images/Section-up.svg" width=24px> → Vue de base et coupe A-A dans sa position par défaut*

<img alt="" src=images/TechDraw_ExampleSection-04.png  style="width:200px;"> 
*Vue de base et coupe A-A dans sa position correcte*

Coupe B-B (coupe vers le bas)

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-05.png  style="width:200px;"> 
*Vue de base + <img src="images/Section-down.svg" width=24px> → Vue de base et coupe B-B dans sa position par défaut*

<img alt="" src=images/TechDraw_ExampleSection-06.png  style="width:200px;"> 
*Vue de base et coupe B-B dans sa position correcte*



### Coupe verticale 

Coupe C-C (coupe à gauche)

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-07.png  style="width:200px;"> 
*Vue de base + <img src="images/Section-left.svg" width=24px> → Vue de base et coupe C-C dans sa position par défaut*

<img alt="" src=images/TechDraw_ExampleSection-08.png  style="width:300px;"> 
*Vue de base et coupe C-C dans sa position correcte*

Coupe D-D (coupe à droite)

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-09.png  style="width:200px;"> 
*Vue de base + <img src="images/Section-right.svg" width=24px> → Vue de base et coupe D-D dans sa position par défaut*

<img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:300px;"> 
*Vue de base et coupe D-D dans sa position correcte*



### Coupe arbitraire 

Coupe E-E (coupe selon un angle arbitraire)

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-11.png  style="width:200px;"> 
*Vue de base + "Direction de la vue selon un angle" réglée à {{Value|30°* → Vue de base et coupe E-E dans sa position par défaut}}

<img alt="" src=images/TechDraw_ExampleSection-12.png  style="width:300px;"> 
*Vue de base et coupe E-E dans sa position correcte*

Par défaut, le plan de coupe passe par le centre de gravité de l\'objet. Pour obtenir une coupe décalée, nous devons modifier les valeurs dans la zone **Emplacement du plan de coupe**.

<img alt="" src=images/TechDraw_ExampleSection-16.png  style="width:300px;">

<img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:300px;"> 
*Ici, la ligne de coupe a été déplacée de 22 mm dans la direction X et de 14 mm dans la direction Y (sans qu'il soit prouvé que la ligne passe par les centres des trous). La valeur Z générée automatiquement n'a aucune influence dans ce cas.*



### Vue secondaire 

FreeCAD n\'a pas d\'outil pour dériver des vues secondaires à partir d\'une vue de base, mais <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [TechDraw Vue de coupe](TechDraw_SectionView/fr.md) peut s\'en charger :

En utilisant la coupe E-E ci-dessus et en changeant les valeurs mentionnées en X = {{Value|40 mm}} et Y = {{Value|-23 mm}}, la coupe ne coupe plus l\'objet et devient une vue secondaire. Remarque : soyez prudent lorsque vous changez les valeurs, de grandes variations peuvent faire planter FreeCAD !

<img alt="" src=images/TechDraw_ExampleSection-12.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-18.png  style="width:300px;"> 
*Coupe E-E comme dans l'exemple ci-dessus + ligne/plan de coupe déplacé(e) → Vue E*

L\'étiquette a été modifiée. La ligne de coupe et une flèche doivent être masquées dans les étapes suivantes car une seule flèche suffit pour définir correctement une vue secondaire.



### Remarques

-   Versions utilisées :
    -   Les exemples ont été créés en utilisant la version de développment 0.21 - 31155 avec le premier angle et l\'ISO sélectionnés.
    -   C-C, D-D, et E-E : les positions par défaut ont été mises à jour pour afficher le placement par défaut actuel (version de développment 0.21 - 31709) (mise à jour 2023-02-03).
-   A cette occasion, je me suis rendu compte que les lignes centrales horizontales et verticales sont orientées en fonction de la page mais pas de la vue et ne peuvent donc pas être utilisées pour aligner la vue de la base et de la coupe, comme je m\'y attendrais.
-   L\'application d\'un décalage à une ligne de coupe/un plan est un peu compliquée car elle ne peut être déplacée que le long d\'axes globaux et non en fonction des axes de vue (locaux).



## Les coupes simples dans la pratique 



### Coupe unique 

Si le dessin ne comporte qu\'une seule coupe et qu\'il est évident que l\'objet est coupé le long d\'une ligne centrale, la ligne de coupe, y compris les flèches, et le titre de la vue peuvent être omis.

<img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:300px;"> <img alt="" src=images/TechDraw_ExampleSection-14.png  style="width:300px;"> 
*Les deux dessins sont conformes aux normes*



### Coupe intérieure 

Une vue de coupe peut être intégrée à la vue de base. Dans ce cas, il n\'est pas nécessaire de prévoir des flèches et un titre.

<img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:200px;">



## Les coupes complexes 

L\'outil <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:24px;"> [TechDraw Coupe complexe](TechDraw_ComplexSection/fr.md) crée une coupe complexe, telle qu\'une coupe alignée ou une coupe décalée, qui utilise plus d\'un plan pour couper un objet.

L\'outil nécessite une vue de base (propriété **Base View**) pour placer plusieurs plans de coupe reliés afin de couper l\'objet, ceux-ci étant définis par une polyligne 3D. (Cet outil peut également traiter les courbes, mais les coupes courbes sont plutôt inhabituelles).

Les axes verticaux des plans de coupe sont toujours parallèles à la normale de la vue de base. Leurs axes horizontaux sont dérivés des segments connexes de la polyligne 3D. L\'orientation de la vue de coupe dépend de l\'un des segments de la polyligne 3D et est influencée par les widgets de la zone **Définir la direction de la vue** du panneau des tâches de l\'outil :

<img alt="" src=images/TechDraw_ComplexSection_Taskview1.png  style="width:" height="250px;"> <img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width:" height="250px;">

Cet outil propose 3 options dans la boîte combinée **Stratégie de projection** pour traiter les segments de la ligne de coupe :

-    {{Value|Décalage}}: seuls les segments perpendiculaires à la direction de la vue sont affichés (par défaut).

-    {{Value|Aligné}}: tous les segments sont affichés dans leur longueur réelle.

-    {{Value|NonParallèle}}: tous les segments sont projetés dans la même direction. En fonction de l\'angle entre un segment et la direction de la vue, la projection peut être plus courte que la zone de coupe. Les segments parallèles à la direction de la vue sont projetés sur une seule ligne.



### Coupe décalée 

Une coupe décalée commence par une vue de base plus une polyligne 3D, une <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [esquisse](PartDesign_NewSketch/fr.md) dans ce cas.

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-19.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-20.png  style="width:200px;"> 
*Vue de base + esquisse + "Stratégie de projection" définie à {{Value|Décalage* + "Direction de la vue selon un angle" définie à {{Value|30°}} → Vue de base et coupe G-G dans sa position par défaut}}

L\'angle de direction de la vue doit être réglé sur une valeur correspondante afin d\'éviter des résultats inattendus.

<img alt="" src=images/TechDraw_ExampleSection-21.png  style="width:300px;"> 
*Vue de base et coupe G-G dans sa position correcte*



### Coupe alignée 

Une coupe alignée commence également par une vue de base et une polyligne 3D.

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-22.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-23.png  style="width:200px;"> 
*Vue de base + esquisse + "Stratégie de projection" définie à {{Value|Aligné* + <img src="images/Section-right.svg" width=24px> (ou "Direction de la vue selon un angle" définie à {{Value|0°}}) → Vue de base et coupe H-H dans sa position par défaut}}

L\'angle de direction de la vue peut être défini avec <img alt="" src=images/Section-right.svg  style="width:24px;"> et <img alt="" src=images/Section-left.svg  style="width:24px;"> pour une orientation approximative. L\'angle doit être deviné et fixé à la meilleure valeur possible, faute de quoi le résultat peut être surprenant.

<img alt="" src=images/TechDraw_ExampleSection-24.png  style="width:300px;"> 
*Vue de base et coupe H-H si "Direction de la vue selon un angle" est réglée à {{Value|30°* (parallèle au segment inférieur de la ligne de coupe). La coupe a été déplacée vers sa bonne position}}

Si l\'angle de la direction de la vue est mal réglé, le résultat peut ressembler à ceci :

<img alt="" src=images/TechDraw_ExampleSection-25.png  style="width:200px;"> 
*Les flèches situées de part et d'autre de la ligne de coupe donnent lieu à une projection étrange, "Direction de la vue selon un angle" est réglé à {{Value|90°*}}



### Vue secondaire 

L\'outil <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:24px;"> [TechDraw Vue en coupe complexe](TechDraw_ComplexSection/fr.md) peut, comme l\'outil <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [TechDraw Vue en coupe](TechDraw_SectionView/fr.md), créer des vues secondaires à partir de vues de base :

Une vue secondaire commence par une vue de base et une seule ligne 3D placée à l\'extérieur de l\'objet.

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-26.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-27.png  style="width:300px;"> 
*Vue de base + ligne 3D → Vue I*

La valeur **Direction de la vue selon un angle** doit être extraite manuellement de la ligne 3D. L\'étiquette a été modifiée. La ligne de coupe et une flèche doivent être masquées dans les étapes suivantes car une seule flèche suffit pour définir correctement une vue secondaire.



### Coupe non parallèle 

Une coupe non parallèle est un mélange de coupes alignées et de coupes décalées.

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-30.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-31.png  style="width:250px;"> 
*Vue de base + esquisse → Vue de base et coupe K-K tournée de -85° et déplacée*

La direction de la flèche aurait dû être horizontale mais l\'outil ne fonctionnait pas lorsque la valeur de **Direction de la vue selon un angle** était définie à {{Value|0°}}. L\'esquisse a donc été tournée de 5° et l\'angle a également été défini sur {{Value|5°}}.



### Comparaison de Non parallèle versus Décalage et Aligné 

<img alt="" src=images/TechDraw_ExampleSection-32.png  style="width:400px;"> 
*Vue de base et coupe K-K en 3 versions : "Décalage" : hachures bleues, "Non parallèle" : hachures noires, "Aligné" : hachures rouges*

Pour une raison inconnue, si la valeur de **Direction de la vue selon un angle** de la coupe alignée est exactement réglée à {{Value|5°}}, le résultat est erroné. Ce n\'est qu\'après avoir modifié la coupe et accepté la valeur étrange de {{Value|5.14°}} à laquelle l\'angle est fixé que le résultat correct s\'affiche.

<img alt="" src=images/TechDraw_ExampleSection-33.png  style="width:400px;"> 
*Même chose que ci-dessus avec "Direction de la vue selon un angle" exactement réglé à {{Value|5°* : la direction de la vue du deuxième segment en partant du haut est inversée (l'arbre est visible)}}



### Coupes complexes avec une ligne 

La longueur (largeur) d\'une coupe complexe dépend de la longueur de la ligne de coupe 3D utilisée, mais les résultats diffèrent d\'une coupe décalée à une coupe non parallèle :

<img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:400px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:400px;"> 
*Deux coupes basées sur la même ligne de coupe 3D.<br>
À gauche : la coupe décalée présente le segment entre les flèches comme une coupe tandis que le reste de l'objet reste non coupé.<br>
À droite : la coupe non parallèle ne montre que la coupe entre les flèches et omet le reste de l'objet.*



## Les coupes complexes dans la pratique 



### Demi coupe 

Une vue montrant un objet symétrique coupé d\'un côté d\'une ligne centrale et non coupé de l\'autre. La profondeur est généralement définie par une autre ligne centrale.

<img alt="" src=images/TechDraw_ExampleSection-28.png  style="width:200px;"> <img alt="" src=images/TechDraw_ExampleSection-29.png  style="width:200px;"> <img alt="" src=images/TechDraw_ExampleSection-36.png  style="width:170px;"> 
*A gauche et au centre : vue décalée de la coupe avec et sans flèches de ligne de coupe et titre, les deux étant conformes aux normes.<br>
A droite : vue décalée de la coupe basée sur une ligne de coupe alternative, voir la coupe M-M ci-dessus.*



### Remarques 

-   Versions utilisées :
    -   Les exemples ont été créés en utilisant la version de développment 0.21 - 31155 avec le premier angle et l\'ISO sélectionnés.
    -   Version de développment 0.21 - 31340 pour M-M.
-   La direction de la vue (l\'orientation des flèches) doit être déterminée manuellement.
-   Toutes les coupes complexes doivent être tournées manuellement.
-   Une valeur de **Direction de la vue selon un angle** de {{Value|0°}} ne fonctionne pas pour les coupes décalées. (180°, aussi ?)
-   La **Direction de la vue selon un angle** sera réinitialisée à une valeur étrange chaque fois qu\'une vue de coupe est activée pour modification.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Section Examples/fr
