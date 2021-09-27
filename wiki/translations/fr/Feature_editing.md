# Feature editing/fr
{{TOCright}}

## Introduction

Cette page explique la manière dont <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [l\'atelier PartDesign](PartDesign_Workbench/fr.md) doit être utilisé à partir de FreeCAD 0.17.

Alors que <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> _ utilise des **[fonctions](PartDesign_Feature/fr.md)**. Une [fonction](https://en.wikipedia.org/wiki/Feature_recognition) est une opération qui modifie la forme d\'un modèle.

## Méthodologie d\'édition de fonctions 

La première fonction est communément appelée la **fonction de base**. Au fur et à mesure que de nouvelles fonctions sont ajoutées au modèle, chaque fonction prends la forme de la fonction précédente et ajoute ou enlève de la matière, créant des dépendances directes d\'une fonction à la suivante. Cette méthodologie imite un procédé de fabrication typique : un bloc est coupé sur un côté, puis sur un autre côté, des trous sont percés, puis des congés appliqués, etc.

Toutes les fonctions sont listées de façon séquentielle dans l\'arborescence Modèle et peuvent être modifiées à tout moment, avec la dernière fonction représentant la pièce finale.

Les fonctions peuvent être classées selon différentes catégories :

-   **Basée sur un profil** : ces fonctions partent d\'un profil pour définir la forme de la matière à ajouter ou enlever. Le profil consistera en une esquisse, une face plane de la géométrie existante (un profil sera extrait de ses arêtes), une forme liée ou un objet Draft qui aura préalablement été inclus dans le corps actif.

-   **Additive** : ajoute de la matière au modèle existant. Les fonctions additives ont des icônes de couleur jaune.

-   **Soustractive** : enlève de la matière du modèle existant. Les fonctions soustractives ont des icônes de couleurs rouge et bleu.

-   **Basée sur des primitives** : basée sur des primitives géométriques (cube, cylindre, cône, tore\...). Elles peuvent être additives ou soustractives.

-   **Fonctions de transformation** : elles appliquent une transformation à des fonctions existantes (symétrie, répétition linéaire ou circulaire, transformation multiple).

-   **Habillage** : ces fonctions appliquent un traitement à des arêtes ou des faces, tels que des arrondis/congés, chanfreins ou dépouilles.

-   **De procédure** : peut être dit de fonctions qui ne sont pas basées sur des profils, comme les fonctions de transformation et d\'habillage.

## Corps

Travailler sous l\'atelier PartDesign requière d\'abord de créer un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[PartDesign Corps](PartDesign_Body/fr.md)**. Le Corps PartDesign est un conteneur qui groupe une séquence de fonctions formant un solide unique.

![](images/PartDesign_Body_tree.png )

**Qu\'est-ce qu\'un solide unique contigu ?** Il s\'agit d\'un objet comme une pièce coulée ou usinée à partir d\'un bloc de métal. Si l\'objet contient des clous, des vis, de la colle ou de la soudure, ce n\'est pas un solide unique contigu. Par exemple, une chaise en bois sera faite de plusieurs corps, avec un corps pour chacune de ses composantes (pieds, lattes, siège, etc.).

Un document FreeCAD peut contenir plusieurs corps ; ils peuvent aussi être combinés pour former un solide unique.

Un seul corps peut être actif dans un document. Le corps actif recevra les fonctions nouvellement créées. Un corps peut être activé ou désactivé par un double-clic sur son étiquette dans l\'arborescence Modèle. Le corps actif est surligné en bleu pâle. À partir de la version 0.18, la couleur de surlignage peut être définie dans les préférences d\'Affichage, sous l\'onglet Couleurs, Conteneur actif.

Lorsqu\'un modèle nécessite plusieurs corps, comme la chaise de l\'exemple précédent, <img alt="" src=images/Std_Part.svg  style="width:24px;"> [le Part Conteneur](Std_Part/fr.md) d\'usage général peut être utilisé pour les grouper et les déplacer comme un tout.

### Gestion de la visibilité du corps 

Un corps expose à l\'extérieur par défaut la fonction la plus récente. Cette fonction est définie par défaut comme la fonction résultante. On peut utiliser l\'analogie de *la pointe de l\'iceberg* : seule la fonction résultante est visible hors de l\'eau, le reste de l\'iceberg (les autres fonctions) sont cachées. Lorsqu\'une nouvelle fonction est ajoutée au corps, la fonction précédente est automatiquement masquée, et la nouvelle fonction devient la fonction résultante.

Il ne peut y avoir qu\'une seule [fonction visible](Std_ToggleVisibility/fr.md) à la fois. Il est possible de basculer la visibilité de toute fonction dans le corps, en la sélectionnant dans l\'arborescence Modèle et en appuyant sur la **barre espace**, ce qui a l\'effet de remonter dans l\'historique du corps.

### Origine du corps 

Le corps possède une Origine qui comprend des plans de référence (XY, XZ, YZ) et des axes (X, Y, Z) qui peuvent être utilisés par des esquisses et des fonctions. Les esquisses peuvent être attachées à des plans de l\'Origine, et il n\'est plus nécessaire de les appliquer sur des faces planes pour que les fonctions basées sur celles-ci ajoutent ou enlèvent de la matière du modèle.

### Déplacer et réordonner des objets 

Il est possible de redéfinir temporairement la fonction résultante sur une fonction au milieu de l\'arborescence du Corps pour insérer de nouveaux objets (fonctions, esquisses ou géométrie de référence). Il est également possible de réordonner les objets sous un Corps, ou les déplacer dans un autre Corps. Sélectionnez l\'objet et faites un clic droit pour faire apparaître le menu contextuel qui propose les deux options. L\'opération pourrait échouer si l\'objet a des dépendances au Corps source, comme être attaché à une face. Pour déplacer une esquisse vers un autre Corps, celle-ci ne devrait pas contenir de liens à des géométries externes.

### Différence avec d\'autres systèmes CAO 

Une différence fondamentale entre FreeCAD et d\'autres programmes, tels que Catia, est que FreeCAD ne vous permet pas d\'avoir plusieurs solides déconnectés dans le même <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[PartDesign Corps](PartDesign_Body/fr.md)**. C\'est-à-dire qu\'une nouvelle fonctionnalité doit toujours être construite sur la précédente. Autrement dit, la nouvelle fonctionnalité devrait \"toucher\" à la précédente, de sorte que les deux soient fusionnées et deviennent un seul solide. Vous ne pouvez pas avoir de solides \"flottants\".

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width:550px;">


*Différence entre Catia et FreeCAD. A gauche: Catia permet aux corps d'être déconnectés des caractéristiques précédentes du corps. Dans FreeCAD, cela provoque une erreur. A droite: la nouvelle fonctionnalité doit toujours être en contact ou intersecter la précédente de sorte qu'elle soit fusionnée avec elle et devienne un corps unique.*

## Géométries de référence 

Les géométries de référence consistent en des plans personnalisés, des droites, des points ou des formes liées de l\'extérieur du corps. Elles peuvent être créées afin de servir de référence à des esquisses et des fonctions. Il y a une multitude de possibilités d\'ancrage aux géométries de référence.

Dans d\'autres systèmes de CAO, vous pouvez définir un plan de référence décalé par rapport au corps précédent et créer un solide déconnecté. Donc, placer beaucoup de plans de référence et y construire des objets est acceptable et ne causera pas d\'erreur. En règle générale, vous ajustez éventuellement les plans à leurs positions finales, de sorte que les objets individuels soient fusionnés.

Dans FreeCAD, comme mentionné dans la section précédente, les solides déconnectés ne sont **PAS** autorisés, donc une esquisse sur un plan de référence qui créerait un solide non contigu échouera.

Dans FreeCAD, les plans de référence ont du sens si vous placez des esquisses (et une protrusion, des cavités, etc.) dans des orientations non standard, c\'est-à-dire dans des plans décalés ou pivotés autour des trois axes principaux. Étant donné que les esquisses peuvent également être placées dans des orientations non standard de la même manière que les plans de référence, il n\'est souvent pas nécessaire d\'utiliser des plans de référence.

Les plans de référence ont également un sens s\'il y aura plus d\'une esquisse dans la même orientation non standard. Dans ce cas, un plan de référence peut être utilisé et l\'orientation ne doit être ajustée que pour le plan de référence afin d\'ajuster toutes les esquisses associées et les fonctions créées à partir des esquisses.

Les esquisses et les plans de référence doivent être attachés aux plans de base. Le référencement de la géométrie générée (géométrie qui est le résultat d\'une opération de création d\'entité, par exemple une protrusion ou une poche) doit être évité car les faces et les arêtes sont renommées et renumérotées et les références ne font plus référence à la même chose. Ceci est appelé instabilité topologique et est dû à la façon dont FreeCAD utilise certaines bibliothèques géométriques externes. Espérons que cela sera amélioré à l\'avenir. (Voir les conseils pour créer des modèles stables ci-dessous).

Même s\'ils ne sont pas utilisés pour supporter des esquisses, les objets de référence sont toujours utiles en tant qu\'indicateurs visuels pour attirer l\'attention sur des caractéristiques ou des distances importantes dans le processus de modélisation. (Cependant, le simple fait d\'ajouter une géométrie à une esquisse fournit également un retour visuel similaire.)

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width:550px;">


*Différence entre Catia et FreeCAD. A gauche: Catia permet aux corps d'être déconnectés des caractéristiques précédentes du corps. Dans FreeCAD, cela provoque une erreur. A droite : la nouvelle fonctionnalité doit toujours être en contact ou intersecter la précédente, de sorte qu'elle soit fusionnée avec elle et devienne un corps unique. Dans cet exemple, le nouveau solide est basé sur un plan de référence qui tourne autour de l'axe des ordonnées.*

## Référencement croisé 

Il est possible de référencer des éléments d\'un corps à un autre à travers les géométries de référence. Par exemple, la forme liée permet de copier des faces d\'un corps comme référence dans un autre corps. Cela devrait permettre de construire facilement une boîte avec un couvercle adapté dans deux corps différents. FreeCAD vous aide à éviter de vous relier accidentellement à d\'autres corps en demandant une confirmation de votre intention.

## Ancrage

L\'ancrage d\'objets n\'est pas un outil spécifique à PartDesign, mais plutôt un outil de l\'atelier Part introduit dans la version 0.17 et qui se trouve dans le menu Pièce. Il est fortement utilisé dans l\'atelier PartDesign pour ancrer des esquisses et des géométries de référence à des plans et axes standards du Corps. Des moyens très complets de création de points de référence, de droites et de plans sont disponibles. Les paramètres de décalage d\'ancrage rendent cet outil très polyvalent.

Consulter la page [Part Ancrage](Part_EditAttachment/fr.md) pour plus d\'informations et [Tutoriel La base pour l\'ancrage](Basic_Attachment_Tutorial/fr.md).

## Conseils pour la création de modèles robustes 

Le principe de conception paramétrique sous-tend que quand les valeurs de certains paramètres sont changées, les étapes subséquentes seront automatiquement mises à jour selon ces nouvelles valeurs. Toutefois, quand des changements importants sont apportés, le modèle peut casser en raison du problème de [problème de nommage topologique](topological_naming_problem.md) qui est toujours non résolu dans FreeCAD. Les brisures peuvent être minimisées en suivant les principes de conception suivants :

-   Évitez de joindre des esquisses et des objets de référence à la géométrie générée du modèle. (La géométrie générée est toute face ou arête créée à la suite d\'un tampon, d\'une poche, etc.)
-   Placez vos esquisses sur des plans de coordonnées standard ou sur des plans de référence personnalisés attachés à des plans standard.
    -   Les esquisses attachées à des plans/axes de coordonnées de base ou à des plans de référence attachés à des plans/axes de coordonnées ne seront pas rattachées de manière inattendue à une référence différente.
-   Lors de la création de la géométrie de référence, ne l\'attachez pas à la géométrie générée
    -   Attachez-le à des plans/axes standard et / ou des esquisses ou des objets de référence qui utilisent des décalages d\'ancrage aux plans/axes standard.
    -   Une esquisse principale doit être aussi simple que possible, contenant des éléments géométriques de base de votre modèle.
    -   Les éléments de l\'esquisse principale peuvent être référencés lors de la modélisation d\'entités ultérieures.
    -   Une esquisse principale peut être la première esquisse dans le corps ou complètement à l\'extérieur du corps
    -   Une esquisse principale peut être référencée en tant que géométrie externe ou via un ShapeBinder.
-   Ne créez pas de ShapeBinders à partir de la géométrie générée.
-   Gardez à l\'esprit que les ShapeBinders peuvent être un problème lorsque la géométrie est supprimée de l\'esquisse sur laquelle elle est basée.
-   Si vous devez inévitablement référencer une fonction intermédiaire, par ex. le résultat d\'une opération d\'épaisseur.
    -   Utilisez la première référence possible dans la liste des entités suivantes où l\'élément géométrique référencé apparaît.
    -   Si vous prenez une fonctionnalité initiale comme référence, toutes les modifications apportées aux étapes intermédiaires ne casseront pas votre modèle.
    -   Essayez de référencer une esquisse ou une géométrie d\'esquisse plutôt qu\'une géométrie générée.
-   Utilisez des *finitions*, comme des filets et des chanfreins, aussi tard que possible dans l\'arbre des fonctionnalités
-   Notez que l\'utilisation de feuilles de calcul, de données dynamiques, d\'esquisses principales etc\... produisent généralement des modèles plus paramétriques et permettent d\'éviter le problème de dénomination topologique.

## Travail sur la construction du corps 

Il existe plusieurs méthodes de travail possibles avec l\'[atelier PartDesign](PartDesign_Workbench/fr.md). Ce qui doit toujours être retenu est que toutes les fonctionnalités créées dans un [PartDesign Corps](PartDesign_Body/fr.md) seront fusionnées pour obtenir l\'objet final.

### Différentes esquisses 

Les esquisses doivent être prises en charge par un plan. Ce plan peut être l\'un des plans principaux (XY, XZ ou YZ) définis par l\'origine du corps. Une esquisse est soit extrudée en un solide positif (additif), avec un outil tel que <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> _. Le premier ajoute du volume à la forme finale du corps, tandis que le dernier déduit le volume de la forme finale. Vous pouvez créer un nombre illimité d\'esquisses et de solides partiels. la forme finale (pointe) résulte de la fusion de ces opérations. Naturellement, le corps ne peut se composer que d'opérations soustractives, car la forme finale doit être un solide avec un volume positif non nul.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width:600px;">

### Fonctions séquentielles 

Les esquisses peuvent être supportées par les faces des opérations solides précédentes. Cela peut être nécessaire si vous avez besoin d\'accéder à une face disponible uniquement après la création d\'une certaine fonctionnalité. Cependant, ce flux de travail n\'est pas recommandé car, si la fonctionnalité d\'origine est modifiée, les fonctionnalités suivantes de la séquence pourraient être endommagées. C\'est un [Problème de dénomination topologique](Topological_naming_problem/fr.md).

<img alt="" src=images/PartDesign_workflow_2.svg  style="width:600px;">

### Utilisation des plans de travail comme supports 

Les plans de référence sont utiles pour soutenir les esquisses. Ces plans auxiliaires doivent être attachés aux plans de base du corps.

\'\'Remarque: dans de nombreux cas, une esquisse attachée à un plan de base avec des décalages d\'attache peut remplir la même fonction. Les références sont particulièrement utiles lorsque plusieurs esquisses ou autres constructions utiliseront la référence. Cela signifie que toutes les modifications apportées à la référence s\'appliqueront aux esquisses attachées, etc. L\'ajout d\'une seule esquisse à une référence, plutôt que d\'utiliser des décalages d\'ancrage dans les propriétés de l\'esquisse, est une étape supplémentaire et est essentiellement redondante. \'\'

Comme pour les esquisses, il est possible d\'attacher des plans de référence à la géométrie générée (arêtes, faces de solides précédemment créés), \'\'\'\'\'mais ce n\'est pas recommandé \'\'\'\'\'car cela peut causer le problème de dénomination topologique.

De plus, une <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [PartDesign Forme liée](PartDesign_ShapeBinder/fr.md) peut être utilisée pour importer une géométrie externe dans le corps pour servir de référence; alors des esquisses peuvent être attachées à ce corps auxiliaire, en utilisant ou non des plans de référence.

*Encore une fois, le ShapeBinder (Forme liée) doit être basé sur des esquisses du corps précédent, et non sur une géométrie générée.*

L\'utilisation d\'objets de référence est souvent le meilleur moyen de produire des modèles stables, lorsqu\'ils sont utilisés avec des plans de base et des décalages d\'ancrage, bien que cela nécessite un peu plus de travail de la part de l\'utilisateur. Pour plus d\'informations sur les pièces jointes de base, voir: [Tutoriel La base de l\'ancrage](Basic_Attachment_Tutorial/fr.md) *Remarque: bien que ce tutoriel parle d\'esquisses, l\'ancrage aux références se fait de la même manière.*

## Tutoriels

La page des [tutoriels](Tutorials/fr.md) fournit des exemples d\'utilisation de la méthode d\'[édition des fonctionnalités](feature_editing/fr.md) de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">.

-   [Créer une pièce simple avec PartDesign](Creating_a_simple_part_with_PartDesign/fr.md)
-   [Tutoriel d\'introduction à l\'atelier PartDesign](Basic_Part_Design_Tutorial/fr.md)
-   [Tutoriel La base de l\'ancrage](Basic_Attachment_Tutorial/fr.md)

## En relation 

-   [Géométrie Solide Constructive](Constructive_solid_geometry/fr.md)

<img alt="" src=images/PartDesign_workflow_3.svg  style="width:600px;">


{{PartDesign Tools navi

}} 

_

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Feature editing/fr
