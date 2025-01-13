# TechDraw General Examples/fr
## Introduction

L\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md) possède de nombreux outils, mais quels sont les éléments nécessaires pour transformer un morceau de papier en un véritable dessin ? Cette page a pour but de donner quelques explications et quelques exemples de ce que TechDraw est déjà capable de faire.



## Dessins

Un dessin consiste en une ou plusieurs vues pour décrire géométriquement une pièce\... Mais vous le savez déjà, n\'est-ce pas ?

Examinons les éléments de base.



### Dessins créés manuellement 



#### La feuille de papier 

Les formats de papier sont normalisés et, pour pouvoir imprimer sans être mis à l\'échelle, le format de notre feuille doit correspondre au format d\'impression souhaité.



#### Les cadres 

Lorsque les dessins étaient réalisés à la main, ils devaient être épinglés ou collés sur une planche à dessin. Des trous de perforation étaient ajoutés au dessin fini pour attacher le dessin plié à un dossier ou à une chemise. Cette zone extérieure est séparée par un cadre rectangulaire. Un autre cadre rectangulaire situé à l\'intérieur du premier définit la zone de dessin. Entre les deux cadres, il y a généralement un ensemble d\'index et de séparateurs qui permettent de localiser certains éléments du dessin.



#### Le cartouche 

Le cartouche contient des informations écrites sur la pièce et le dessin, telles que le numéro de la pièce, le titre, l\'auteur, le propriétaire, etc.



#### La nomenclature 

Les dessins d\'assemblage peuvent éventuellement être accompagnés d\'une nomenclature. La nomenclature peut également être placée sur une feuille de dessin séparée ou sur une feuille de calcul.



#### Changer le journal 

Les modifications apportées à la pièce ou au dessin sont consignées dans un journal sur le dessin ou dans un document séparé et liées au dessin par des index correspondants.



#### Les vues 

Les vues contiennent la description géométrique d\'une pièce dans une certaine direction. La plupart des pièces nécessitent au moins deux vues pour être correctement décrites.



#### Les annotations 

Des textes supplémentaires qui n\'appartiennent pas aux éléments mentionnés ci-dessus.



### Dessins réalisés avec TechDraw 

Techdraw utilise un objet Page comme conteneur pour tous les éléments liés au dessin. Cet objet ne peut pas exister seul, mais doit contenir un modèle. C\'est pourquoi il n\'y a pas de commande Nouvelle page et un nouvel objet page est créé automatiquement chaque fois qu\'un modèle est inséré.



#### Les modèles 

Un objet [Modèle](TechDraw_Templates/fr.md) est un fichier image [SVG](SVG/fr.md) et son code contient toutes les informations nécessaires pour créer une feuille de papier virtuelle avec des cadres et un cartouche correspondants, et éventuellement une nomenclature.

Les images SVG ne sont pas paramétriques. Cela signifie que pour chaque format, un modèle distinct doit être créé, et qu\'un tel ensemble de modèles est nécessaire pour toute variation d\'objets de type cadre ou cartouche. C\'est beaucoup à coder et à gérer, mais d\'un autre côté, les modèles ne peuvent pas être modifiés accidentellement dans FreeCAD.

Il y a plusieurs façons de créer un modèle :

1.  Dessinez le avec [Inkscape](https://fr.wikipedia.org/wiki/Inkscape), voir [Comment créer un modèle TechDraw personnalisé](TechDraw_TemplateHowTo/fr.md).
2.  Faites le manuellement, voir [Template explained](Sandbox_TechDraw_TemplateExplained.md).
3.  Utiliser une macro, voir [TechDraw Création de modèles](TechDraw_TemplateGenerator/fr.md) et la [macro TemplateHelper](Macro_TemplateHelper/fr.md).

<img alt="" src=images/TechDraw_ExampleDrawing-01.png  style="width:400px;">



*Résultat du modèle expliqué*

<img alt="" src=images/Macro_TemplateHelper_A3+BOM.png  style="width:400px;">



*Résultat de la macro TemplateHelper, ISO A3 + nomenclature*



#### Le dessin jusqu\'à présent 

Jusqu\'à présent, on peut dire que TechDraw, en relation avec des modèles SVG intégrés, peut fournir une feuille de dessin correcte avec un cadre et un cartouche. Certaines entrées peuvent être modifiées après la création grâce à des textes éditables et certains contenus peuvent être insérés automatiquement si des macros sont impliquées. 

## Les vues 

Les vues contiennent la description géométrique en 2D d\'un objet. Le contenu d\'une vue TechDraw peut être dérivé de la géométrie 3D ou obtenu à partir d\'un autre atelier comme des <img alt="" src=images/TechDraw_ArchView.svg  style="width:16px;"> [vues de Arch](TechDraw_ArchView/fr.md) et des <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [vues de Draft](TechDraw_DraftView/fr.md).

Comme FreeCAD est une application de modélisation 3D, la fonction clé de TechDraw est de dériver des vues 2D à partir d\'une géométrie 3D. Prenons un exemple simple, la pièce du [Tutoriel d\'introduction à PartDesign](Basic_Part_Design_Tutorial/fr.md) qui est également utilisée avec le [TechDraw Tutoriel d\'introduction](Basic_TechDraw_Tutorial/fr.md) :

<img alt="" src=images/Tut17_final_refined.png  style="width:300px;">



*Pièce du tutoriel d'introduction à PartDesign*



### La vue active 

Une <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [vue active](TechDraw_ActiveView/fr.md) est plus ou moins une capture d\'écran de la [vue 3D](3D_View/fr.md) dans son propre type de vue TechDraw.

<img alt="" src=images/TechDraw_ExampleDrawing-02.png  style="width:300px;">



*L'élément affiché dans une vue active avec l'option Pas d'arrière-plan activée*



### La vue 

Une <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [vue](TechDraw_View/fr.md) est l\'objet de vue de base de TechDraw qui permet d\'obtenir des dessins corrects. Contrairement à une vue active, elle n\'est pas limitée aux objets visibles à l\'écran, mais affiche également des objets sélectionnés en dehors de l\'écran. L\'échelle préférée dépend de l\'espace disponible et du niveau de détail à afficher.

<img alt="" src=images/TechDraw_ExampleDrawing-03.png  style="width:300px;">



*L'élément affiché dans une vue arbitraire comme la vue active ci-dessus*



### Le groupe de projection 

Un <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [groupe de projection](TechDraw_ProjectionGroup.md) est un ensemble de vues. Chaque direction de vue est perpendiculaire à sa voisine et toutes dépendent par défaut de la direction de la fenêtre 3D. TechDraw fournit six vues correspondant aux côtés du [cube de navigation](Navigation_Cube/fr.md) et quatre vues isométriques.

<img alt="" src=images/TechDraw_ExampleDrawing-04.png  style="width:300px;">



*L'élément affiché dans un groupe de projection composé de trois vues (en mode projection du premier angle)*



### La vue de la coupe 

TechDraw fournit des outils pour créer une <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [simple vue de la coupe](TechDraw_SectionView/fr.md) ou une <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [vue en coupe complexe](TechDraw_ComplexSection/fr.md). Les deux dépendent d\'une vue de base et d\'outils permettant de définir une ligne de section et de dériver la direction de la vue. Voir [TechDraw Exemples de coupes](TechDraw_Section_Examples/fr.md) pour une vue d\'ensemble.

<img alt="" src=images/TechDraw_ExampleDrawing-05.png  style="width:300px;">



*L'élément de coupe affiché dans une section A-A sur la base de la vue de face*



### Les vues auxiliaires 

Si nous avons besoin d\'une vue d\'un plan incliné pour voir ses vraies longueurs, nous devons définir la direction de la vue dans une vue de base et placer la vue auxiliaire en conséquence, mais TechDraw ne fournit pas encore d\'outil pour les vues auxiliaires.

Bonne nouvelle : il est assez facile de l\'émuler en utilisant l\'outil <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [TechDraw Vue en coupe](TechDraw_SectionView/fr.md) :

1.  Sélectionnez une vue de base.
2.  Créez une <img alt="" src=images/TechDraw_SectionView.svg  style="width:16px;"> [simple vue de coupe](TechDraw_SectionView/fr.md) avec les paramètres par défaut.
3.  Utilisez <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Insérer une cote angulaire](TechDraw_AngleDimension/fr.md) pour mesurer l\'angle du plan.
4.  Modifiez l\'angle de vue de la coupe dans la zone Définir la direction de la vue de son panneau de tâches.
5.  Modifiez les coordonnées de la vue de la coupe dans la zone Emplacement du plan de section de son panneau de tâches. Utilisez des **petits pas** pour déplacer la ligne de la coupe à l\'extérieur de l\'objet ou FreeCAD peut se planter.
6.  Masquez les éléments d\'annotation non désirés tels que la ligne de coupe, les flèches de coupe et le nom de la coupe.
7.  Ajoutez les éléments nécessaires tels que la flèche de vue et le nom de la vue.

<img alt="" src=images/TechDraw_ExampleDrawing-06.png  style="width:300px;">



*Une vue de la coupe par défaut basée sur la vue de gauche affichant l'angle de la ligne de la coupe*

<img alt="" src=images/TechDraw_ExampleDrawing-07.png  style="width:300px;">



*Vue de la coupe avec l'angle de la ligne de section fixé à {{value|218,93°* (38,93° plus 180° pour inverser la direction)}}

<img alt="" src=images/TechDraw_ExampleDrawing-08.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-09.png  style="width:300px;">



*Vue la coupe avec ligne la coupe déplacée → Vue auxiliaire terminée*



### La vue détaillée 

Une <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [vue détaillée](TechDraw_DetailView/fr.md) est une copie d\'une zone d\'une vue de base, généralement pour agrandir la géométrie à peine visible.

<img alt="" src=images/TechDraw_ExampleDrawing-10.png  style="width:300px;">



*Détail Y (vue) basé sur la coupe A-A*

#### Imperfections

-   Les vues détaillées conformes à la norme ISO n\'ont pas de cadre/bordure (la partie supérieure du cercle qui les entoure). Note de l\'éditeur : qu\'entend-on par là ? Les cadres ne sont pas imprimés\...
-   La ligne de rupture qui coupe le détail du reste doit être une fine ligne à main levée ou l\'équivalent en CAO, une fine ligne en zigzag. FreeCAD/TechDraw ne fournissent pas (encore) de lignes à main levée ou en zigzag.
-   Les zones hachurées dans la vue de base doivent également être hachurées dans la vue de détail.



### La vue de Arch 

Une <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [vue de Arch](TechDraw_ArchView/fr.md) affiche une vue d\'un <img alt="" src=images/Arch_SectionPlane.svg  style="width:16px;"> [Arch Plan de coupe](Arch_SectionPlane/fr.md). Son contenu est rendu par l\'<img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [atelier BIM](Workbench_BIM/fr.md).



### La vue de Draft 

Une <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [vue de Draft](TechDraw_DraftView/fr.md) affiche une vue d\'un objet ou d\'un groupe d\'objets sélectionnés basés sur [Part](Part_Workbench/fr.md). Elle est destinée aux objets 2D. Son contenu est rendu par l\'<img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [atelier Draft](Draft_Workbench/fr.md).

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:300px;">



*Certains éléments de Draft dans la vue 3D → Les mêmes éléments affichés dans une vue Draft sur un dessin*



### La vue de Spreadsheet 

Une <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [vue de Spreadsheet](TechDraw_SpreadsheetView/fr.md) affiche une vue d\'une feuille de l\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md).

<img alt="" src=images/TechDraw_Spreadsheetview.png  style="width:300px;">



*Élément de feuille de calcul affiché dans une vue de Spreadsheet*



### Les vues jusqu\'à présent 

TechDraw a besoin de quelques ajouts tels que des lignes de rupture, un outil de visualisation auxiliaire approprié et une amélioration de l\'outil de visualisation détaillée. Mais même dans cet état, nous pouvons décrire nos objets visuellement assez bien :

<img alt="" src=images/TechDraw_ExampleDrawing-11.png  style="width:300px;">



*Voici à quoi pourrait ressembler un dessin avec un ensemble de vues de l'objet de l'exemple*


{{Top}}



## Coter

Maintenant que notre article est décrit géométriquement, des cotes seront ajoutées pour mieux définir la forme et des tolérances pour définir l\'écart autorisé. TechDraw propose plusieurs outils pour appliquer des cotes à la représentation 2D de notre objet :

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Cote de longueur](TechDraw_LengthDimension/fr.md)
-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Cote horizontale](TechDraw_HorizontalDimension/fr.md)
-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Cote verticale](TechDraw_VerticalDimension/fr.md)
-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:16px;"> [Cote de rayon](TechDraw_RadiusDimension/fr.md)
-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> [Cote de diamètre](TechDraw_DiameterDimension/fr.md)
-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Cote angulaire](TechDraw_AngleDimension/fr.md)
-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [Cote angulaire par 3 points](TechDraw_3PtAngleDimension/fr.md)

Elles ont en commun de mesurer la forme projetée de l\'élément. Si vous avez appris le dessin à la main, vous savez comment utiliser les vues auxiliaires pour placer l\'élément dans une position où les longueurs projetées sont égales aux longueurs réelles. Pour une visualisation différente de cette vieille méthode, les cotes peuvent être liées à la géométrie 3D à l\'aide de <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:16px;"> [TechDraw Réparation des cotes](TechDraw_DimensionRepair/fr.md) pour afficher les \"vraies dimensions\".

Deux autres outils mesurent la longueur totale horizontalement ou verticalement respectivement :

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:16px;"> [Cote étendue horizontale](TechDraw_HorizontalExtentDimension/fr.md)
-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:16px;"> [Cote étendue verticale](TechDraw_VerticalExtentDimension/fr.md)

Ils ne peuvent pas (encore) être liés à la géométrie 3D.

Voir [Fenêtre de dialogue Cote](TechDraw_LengthDimension/fr#Fenêtre_de_dialogue_Cote.md) (et la section suivante sur les propriétés) pour tous les paramètres qui ne sont pas mentionnés dans cet aperçu.



### Les cotes simples 

Le texte de la cote dépend principalement de ces propriétés :

-    **Format Spec**
    

-    **Format Spec Over Tolerance**
    

-    **Format Spec Under Tolerance**
    

:   Par défaut, leurs valeurs sont {{Value|%.2f}}

Pour \"tricher\", nous pouvons utiliser ces deux propriétés :

-    **Arbitrary**
    

:   

    :   Définie à `False` pour utiliser le contenu de **Format Spec** pour formater la valeur de la cote réelle.
    :   Défini à `True` pour utiliser le contenu de **Format Spec** pour afficher du texte à la place de la valeur de la cote.

-    **Arbitrary Tolerances**: comme **Arbitrary**, mais pour la tolérance.

Si nous n\'avons besoin que de la valeur de la cote, il n\'y a rien d\'autre à faire que de changer le nombre de décimales si nécessaire.

:   Par exemple : {{Value|%.2f}} → {{Value|%.3f}} pour afficher 3 décimales, ou {{Value|%.2f}} → {{Value|%.0f}} pour afficher des nombres entiers.



#### Cote de longueur 

Il existe trois outils pour ajouter des cotes de longueur : <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Cote de longueur](TechDraw_LengthDimension/fr.md), <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Cote horizontale](TechDraw_HorizontalDimension/fr.md) et <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Cote verticale](TechDraw_VerticalDimension/fr.md).

<img alt="" src=images/TechDraw_ExampleDrawing-17.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-18.png  style="width:300px;">



*À gauche : deux vues d'un objet avec des cotes de longueur appliquées → À droite : la même vue de face tournée de 20°*

Cela montre qu\'il est important de faire pivoter une vue de face dans la boîte de dialogue Groupe de projection, sinon les vues connectées ne suivront pas. D\'autre part, cela nous limiterait à des rotations de 90°.

Si une cote doit être parallèle à un bord, il faut une autre ligne sélectionnable perpendiculaire au bord et l\'outil <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Cote de longueur](TechDraw_LengthDimension/fr.md), qui peut trouver la distance la plus courte (= perpendiculaire) entre un point et une ligne. Une arête ne sera pas automatiquement prolongée par une ligne imaginaire et nous devons donc créer une ligne auxiliaire (cosmétique) manuellement. (Un point cosmétique pourrait également être utilisé, mais cela demande encore plus de travail).

-   La ligne noire (ligne point à point) <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Cote de longueur](TechDraw_LengthDimension/fr.md) dépend d\'une ligne cosmétique qui ne tourne pas avec la vue. (Un point cosmétique ne serait pas utile non plus).
-   La <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Cote horizontale](TechDraw_HorizontalDimension/fr.md) et <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Cote verticale](TechDraw_VerticalDimension/fr.md) (rouge et verte) suivent l\'orientation de la page et changent leurs cotes en conséquence.
-   La bleue est une ligne point à point <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Cote de longueur](TechDraw_LengthDimension/fr.md) mais tourne avec la vue car il n\'y a pas de géométrie cosmétique impliquée.



#### Cote angulaire 

TechDraw propose deux outils pour ajouter des cotes angulaires : <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Cote angulaire](TechDraw_AngleDimension/fr.md) et <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [Cote angulaire par 3 points](TechDraw_3PtAngleDimension/fr.md).

<img alt="" src=images/TechDraw_ExampleDrawing-19.png  style="width:300px;">



*Deux façons d'ajouter une cote d'angle*

-   En bleu : une <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [cote angulaire](TechDraw_AngleDimension/fr.md) entre deux arêtes.
-   En rouge : une <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [cote angulaire par 3 points](TechDraw_3PtAngleDimension/fr.md) utilisant les deux extrémités et le point central d\'un arc.



#### Cote de chanfrein 

Une cote de chanfrein peut être appliquée en tant que [cote de longueur](#Cote_de_longueur.md) avec une propriété **Format Spec** modifiée manuellement ou en utilisant <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:16px;"> [Cote horizontale et d\'angle de chanfrein](TechDraw_ExtensionCreateHorizChamferDimension/fr.md) et <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:16px;">. [Cote verticale et d\'angle de chanfrein](TechDraw_ExtensionCreateVertChamferDimension/fr.md) pour créer une cote de longueur et d\'angle pour un chanfrein.

<img alt="" src=images/TechDraw_ExampleDrawing-14.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-15.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-16.png  style="width:300px;">



*À gauche : cotes du chanfrein appliquées à un objet dont les côtés sont horizontaux et verticaux<br>Au centre : la même vue tournée de 10°<br>À droite : l'objet est incliné de 10°, vue à 0°*

Les outils de chanfrein fonctionnent bien pour les objets dont les côtés sont horizontaux et verticaux, à condition qu\'ils soient parallèles aux axes de la vue = aux axes X et Y de la page, mais de nombreuses pièces ne nous feront pas la faveur d\'être parfaitement alignées.

Les valeurs d\'angle ne sont pas paramétriques ! Elles ne changent pas si la vue est inclinée. La dernière page indique les bons angles mais des cotes positionnées de la sorte sont inutiles.

Pour aligner la cote du chanfrein le long d\'une arête, nous avons besoin d\'un point auxiliaire (cosmétique) où les arêtes non chanfreinées se rejoignent. Nous devons utiliser <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Cote de longueur](TechDraw_LengthDimension/fr.md) sauf que le point cosmétique ne suivra pas les arêtes si la vue est inclinée. (voir aussi [Cote de longueur](#Cote_de_longueur.md)).



#### Cote de rayon 

Une <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [cote de rayon](TechDraw_RadiusDimension/fr.md) ajoute une cote de rayon à un cercle ou un arc de cercle, ni plus ni moins.

<img alt="" src=images/TechDraw_ExampleDrawing-20.png  style="width:300px;">



*Deux façons d'ajouter une cote de rayon, la rouge avec la pointe de flèche inversée*

Pour modifier la direction de la flèche, il suffit de définir la propriété **Flip Arrowheads** à {{true}}.



#### Cote de diamètre 

Les cotes de diamètre peuvent être ajoutées en tant que <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> [Cote de diamètre](TechDraw_DiameterDimension/fr.md) ou l\'une des cotes de longueur <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Cote de longueur](TechDraw_LengthDimension/fr.md), <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Cote horizontale](TechDraw_HorizontalDimension/fr.md) et <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Cote verticale](TechDraw_VerticalDimension/fr.md). (Ou en relation avec une ligne directrice pointant vers le centre d\'un cercle ou une ligne centrale - non affichée).

<img alt="" src=images/TechDraw_ExampleDrawing-12.png  style="width:300px;">



*Plusieurs façons de placer une cote de diamètre (Ignorez la ligne centrale manquante)*

-   En bleu : une <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> cote de longueur dans la vue latérale du trou doit être précédée d\'un \"⌀\" pour la distinguer d\'un trou rectangulaire.

:   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:16px;"> [Insérer un préfixe \"⌀\"](TechDraw_ExtensionInsertDiameter/fr.md) est un moyen facile de le faire, mais la propriété **Format Spec** peut également être modifiée manuellement.

-   En vert : une simple <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> cote de longueur.

:   Elle nécessite une géométrie auxiliaire (points cosmétiques) car elle ne peut pas être appliquée directement aux cercles.

-   En rouge : une <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> cote de diamètre. Si vous regardez le long de l\'axe du trou et que vous pouvez voir la forme circulaire du trou, le \"⌀\" peut être omis. Pour le supprimer, modifiez manuellement la propriété **Format Spec**.



#### Cote de filetage 

Les cotes de filetage peuvent être appliquées tout comme les cotes de diamètre, mais elles nécessitent une géométrie auxiliaire créée au préalable : <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:16px;"> [Corps de taraudage](TechDraw_ExtensionThreadHoleSide/fr.md), <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:16px;"> [Taraudage](TechDraw_ExtensionThreadHoleBottom/fr.md), <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:16px;"> [Corps de filetage](TechDraw_ExtensionThreadBoltSide/fr.md) ou <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:16px;"> [Filetage](TechDraw_ExtensionThreadBoltBottom/fr.md).

<img alt="" src=images/TechDraw_ExampleDrawing-13.png  style="width:350px;">



*Un filetage à tête fraisée avec plusieurs façons de placer une cote de filetage (et un diamètre de tête fraisée)*

Toutes les cotes des filetages sont appliquées aux lignes ou cercles auxiliaires (cosmétiques) (en relation avec les points cosmétiques) et toutes les propriétés **Format Spec** doivent être modifiées manuellement par le préfixe \"M\" pour les filetages métriques.



### Tolérances

Les tolérances indiquent de combien une cote mesurée peut s\'écarter de la valeur de la cote sur le dessin. Pour ajouter une tolérance à la valeur de la cote, il suffit de donner à la propriété **Over Tolerance** une valeur autre que {{Value|0}}, ce qui donne une tolérance symétrique telle que {{Value|±0,5}}.

Pour une tolérance asymétrique, définissez la propriété **Equal Tolerance** à {{false}} et spécifiez également une valeur inférieure pour la propriété **Under Tolerance**.

Les valeurs peuvent être définies dans la [fenêtre de dialogue Cote](TechDraw_LengthDimension/fr#Fenêtre_de_dialogue_Cote.md) ou directement dans l\'[éditeur de propriétés](Property_editor/fr.md).



#### Tolérance de trou/d\'arbre 

Les tolérances d\'ajustement peuvent être ajoutées en ajoutant des classes de tolérance à une cote. Une classe de tolérance se compose d\'un spécificateur de champ de tolérance (lettre, majuscule pour les trous, minuscule pour les arbres) et d\'un spécificateur de degré de tolérance (nombre) :

1.  Définissez la propriété **Arbitrary Tolerances** à {{true}} et spécifier les deux classes de tolérance dans les propriétés **Over Tolerance** et **Under Tolerance**.
2.  Utilisez l\'outil <img alt="" src=images/TechDraw_HoleShaftFit.svg  style="width:16px;"> [TechDraw Tolérance de trou/d\'arbre](TechDraw_HoleShaftFit/fr.md). Ceci ne suffixe qu\'une seule classe de tolérance mais ajoute les valeurs correspondantes aux propriétés **Over Tolerance** et **Under Tolerance**.
3.  Pour une tolérance unique, il suffit d\'ajouter la classe de tolérance au spécificateur de format dans la propriété **Format Spec**.



#### Tolérance de filetage 

Les tolérances d\'ajustement du filetage peuvent être suffixées comme décrit ci-dessus pour les tolérances d\'ajustement de trou/d\'arbre, à l\'exception de la méthode 2. Les classes de tolérance de filetage affichent le spécificateur de l\'échelon de tolérance (nombre) devant le spécificateur du champ de tolérance (lettre, majuscule pour les filetages intérieurs, minuscule pour les filetages extérieurs).



### Cotes de contrôle 

Les cotes de contrôle (cotes de test) ne sont pas encore implémentées.

:   (Peut-être déjà obsolète. Voir [\...test dimension was withdrawn\...](https://forum.freecad.org/viewtopic.php?p=691914#p691914) sur le forum)

Pour simuler une cote de contrôle, nous définissons la propriété **Format Spec** à \" \" (un espace - pas de caractère du tout et nous n\'aurions pas de poignée pour saisir la ligne de cote afin de la déplacer) et définissons ensuite la propriété **Arbitrary** à `True`. Il en résulte une cote sans valeur. La valeur peut alors être remplacée par une infobulle sans ligne de reférence. Cela ne fonctionne qu\'avec les cotes horizontales, car il n\'est pas possible de faire pivoter les infobulles.

<img alt="" src=images/TechDraw_ExampleDrawing-21.png  style="width:300px;">



*L'exemple d'un élément avec une cote de contrôle. Dans ce cas, 100 % des éléments de production doivent être vérifiés pour s'assurer qu'ils se situent dans la tolérance*

.



### Dimensionnement géométrique et tolérance 

Le système de [Dimensionnement géométrique et tolérance](TechDraw_Geometric_dimensioning_and_tolerancing/fr.md) (GD&T (en)) vise à décrire les formes avec plus de précision que ne le permettent les seules cotes tolérées. Elle s\'appuie sur des référentiels, des cotes théoriquement exactes et des indicateurs de tolérance.



#### Référentiels

Les référentiels sont des surfaces, des plans, des lignes et des points virtuels utilisés comme références pour décrire des caractéristiques géométriques avec des cotes et des indicateurs de tolérance théoriquement exacts. Elles peuvent être utilisées pour construire un système de coordonnées virtuelles théoriquement exactes.



#### Fonction de référence 

Une fonction de référence est une fonction géométrique d\'un objet correspondant à une certaine référence. Les symboles d\'éléments de référence sont ajoutés à l\'aide d\'annotations d\'<img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [infobulles](TechDraw_Balloon/fr.md).

<img alt="" src=images/TechDraw_ExampleDrawing-22.png  style="width:350px;">



*Exemple d'élément avec des fonctions de référence. Les deux vues affichent exactement les mêmes fonctions de référence*

La propriété **Kink Length** doit être réglée à {{Value|0}} pour les lignes verticales. {{VersionMinus/fr|0.21}}, une partie de la ligne apparaît dans le cadre.

<img alt="" src=images/TechDraw_ExampleDrawing-27.png  style="width:200px;">



*Désormais, la ligne de repère commence sur le cadre, ce qui est parfait pour les lignes horizontales, mais il est désormais impossible de dessiner correctement les lignes de repère verticales*

.



#### Cible de référence 

Les cibles de référence sont des points ou des zones relativement petites qui indiquent d\'où faire dériver une référence. L\'utilisation la plus courante consiste à créer un système de coordonnées virtuelles théoriquement exactes à partir d\'un ensemble de six cibles de référence.

<img alt="" src=images/TechDraw_ExampleDrawing-23.png  style="width:300px;">



*Ce type de cible de référence n'est pas encore mis en œuvre*

Il n\'y a pas de solution connue pour le moment.

:   Les symboles de points spéciaux pour indiquer le point de référence de la cible de référence ne sont pas encore inclus dans les options des lignes de repère.
:   Les cercles doivent être dérivés de la géométrie 3D et sont difficiles à gérer dans les groupes de projection.



#### Cotes théoriquement exactes 

Les cotes théoriquement exactes sont ajoutées de la même manière que de [simples cotes](#Les_cotes_simples.md). La case à cocher Théoriquement exact fait la différence : elle met la propriété **Theoretically Exact ** à {{true}}, ajoute un cadre rectangulaire à la valeur de la cote et désactive les tolérances et tous les paramètres de tolérance.



#### Indicateur de tolérance 

Un indicateur de tolérance, également appelé \"cadre de contrôle des caractéristiques\", est un cadre contenant des informations sur les tolérances :

-   quelle caractéristique géométrique est tolérée
-   la forme et la taille du champ de la tolérance
-   les référentiels à utiliser
-   quelques symboles supplémentaires pour décrire les caractéristiques avec encore plus de précision.

<img alt="" src=images/TechDraw_ExampleDrawing-24.png  style="width:300px;">



*Cotes théoriquement exactes (en rouge) et indicateurs de tolérance par rapport à l'élément de référence A (en bleu)*

Les indicateurs de tolérance sont comme des symboles d\'éléments de référence ajoutés à l\'aide des <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [infobulles](TechDraw_Balloon/fr.md) mais en utilisant l\'option {{value|Rectangle}}. Utilisez <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width:16px;"> [Personnaliser l\'infobulle](TechDraw_ExtensionCustomizeFormat/fr.md) pour insérer des caractères spéciaux.

Dans la plupart des cas, les indicateurs de tolérance sont alignés sur une ligne de cote, ce qui est impossible dans TechDraw, sauf pour les cotes horizontales car, comme nous l\'avons déjà mentionné, les annotations des infobulles ne peuvent pas pivotées. {{Top}}

## Annotations



### Lignes de repère 

Une <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:16px;"> [ligne de repère](TechDraw_LeaderLine/fr.md) pointe vers un sommet, une arête ou une face où des informations rattachées sont valides.

:   Les outils qui fournissent des informations et s\'attachent à une ligne de repère présélectionnée sont l\'<img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:16px;"> [Annotation texte enrichi](TechDraw_RichTextAnnotation/fr.md) et la <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:16px;"> [Soudure](TechDraw_WeldSymbol/fr.md).



### Infobulles

Une <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [infobulle](TechDraw_Balloon/fr.md) est une combinaison d\'une ligne de repère et d\'un texte court. Elle nécessite une vue présélectionnée, ou un élément appartenant à une vue, sinon la commande renverra un message d\'erreur. La ligne de repère commence tout le temps horizontalement et pointe vers l\'élément sélectionné après une courte distance définie dans la propriété **Kink Length**. Sa valeur peut également être fixée à {{Value|0}}.



### Texte

Techdraw fournit deux outils pour ajouter du texte à un dessin :

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:16px;"> [Annotation](TechDraw_Annotation/fr.md) ajoute un bloc de texte en tant qu\'annotation à une page. Les annotations utilisent les mêmes paramètres par défaut que les cotes, certains paramètres peuvent être modifiés et ils peuvent être édités et tournés mais ils ne peuvent pas être rattachés.
-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:16px;"> [Annotation texte enrichi](TechDraw_RichTextAnnotation/fr.md) ajoute un bloc de texte enrichi comme annotation à une page, une ligne de référence ou une vue. Les annotations rattachées à une ligne de référence ou à une vue se déplacent de manière synchrone avec la vue ou la ligne de repère lorsque leur position change.



### Symboles de soudure 

L\'outil <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:16px;"> [Soudure](TechDraw_WeldSymbol/fr.md) s\'attache à une ligne de référence présélectionnée et ajoute des informations sur la manière de créer une certaine soudure entre deux objets afin d\'éviter de modéliser les faces de soudure sur les pièces brutes. Le texte de la fourche détermine le processus de soudage ou de brasage à utiliser pour la soudure.

:   Il semble que les symboles de soudure nécessitent une ligne de repère intégrée pour obtenir un symbole de fourche correspondant à la taille du texte, sinon les symboles sur la ligne de repère doivent être redimensionnables.

<img alt="" src=images/TechDraw_ExampleDrawing-26.png  style="width:300px;">



*Symbole de soudure pour un soudure en V circulaire, 111 signifiant soudage manuel à l'arc - Ne me frappez pas si j'ai cité l'internet de façon erronée*



### Symboles d\'état de surface 

<img alt="" src=images/TechDraw_SurfaceFinishSymbols.svg  style="width:16px;"> [Symbole de finition de surface](TechDraw_SurfaceFinishSymbols/fr.md) ajoute un symbole de finition de surface à la page, ce qui signifie que ces symboles ne se déplacent pas avec la géométrie référencée.

<img alt="" src=images/TechDraw_ExampleDrawing-25.png  style="width:300px;">



*Symbole d'état de surface par rapport à une dimension*

Ces symboles ne peuvent pas être personnalisés en ce qui concerne la largeur de ligne et le type de police pour correspondre aux dimensions et ils peuvent difficilement être modifiés après leur création. {{Top}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw General Examples/fr
