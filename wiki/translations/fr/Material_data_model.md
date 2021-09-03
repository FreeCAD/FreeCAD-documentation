


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

## Buts et principes {#buts_et_principes}

En stockant les propriétés des matériaux dans une structure de données unifiées, l\'un vise à faciliter la récupération des données, qui peuvent être réalisées dans des contextes différents :

-   lors de la construction d\'un modèle d\'éléments finis.
-   lors du rendu d\'un modèle 3D.
-   pour être en mesure de suivre l\'évolution de la matière d\'un **composant** créé dans FreeCAD, pour [PDM](http://en.wikipedia.org/wiki/Product_Data_Management) applications.
-   [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling) application (architecture et construction industrielle).

Pour gérer les propriétés des matériaux, il est proposé de créer un modèle de données spécifique, qui sera instancié, si un nouveau matériau est créé dans FreeCAD.

Il sera possible de créer un matériau soit en définissant ses propriétés à la main, à travers un plan de travail (workbench), ou en lisant les propriétés des matériaux à partir d\'un fichier. Les formats de ces fichiers doivent être défini (certains existent déjà, comme, [MatML](http://www.matml.org/), [STEP](http://fr.wikipedia.org/wiki/Standard_pour_l'échange_de_données_de_produit), [AP235](http://www.steptools.com/support/stdev_docs/express/ap235/index.html) et IGR45 \...).

En outre, il sera possible d\'enregistrer les propriétés des matériaux, dans une collection de fichiers, dans un format qui doit aussi être choisi. La collection de fichiers peut être stockée dans un répertoire commun, et, constituera la base de données de matériaux de FreeCAD.

Grâce à ce modèle de données, le matériel peut être défini dans FreeCAD sans la nécessité de définir un **composant**.

Un nouveau pointeur sera créé dans un **composant** modèle de données, pour créer un lien, vers le matériau qui a été défini par le modèle de données matérielles.

## Résultats

Grâce à ce modèle de données de matériau, il est proposé d\'offrir un outil, pour gérer facilement les données matérielles dans FreeCAD.

## Réflexions

## Organisation

Différents types de données, doivent être gérées pour décrire un matériau. Un modèle de données matérielles est proposé ci-dessous. Quelques exemples de données, qui peuvent être stockées au sein de cette structure, sont aussi bien données.

### Modèle de données Matérielles {#modèle_de_données_matérielles}

En plus des classiques \"chaînes\" d\'attributs telles que le nom, et, une famille, 3 différents types d\'informations spécifiques, doivent être gérées, pour décrire un matériau dans FreeCAD.

-   **propriétés** : structure générique pour stocker des données, décrivant les propriétés mécaniques du matériau.
-   **Composition chimique** : composition chimique de la matière.
-   **apparence** : informations décrivant comment le matériau sera représenté dans FreeCAD (couleur, brillance \...)

Tous ces types d\'informations, ne doivent pas nécessairement être définis pour le matériel existant. Enfin, voici la liste des attributs retenus pour décrire un matériau dans FreeCAD.

#### Nom

Une chaîne de caractères, indiquant le nom de la matière. C\'est sa désignation.

#### Famille

Une chaîne de caractères, indiquant la famille de la matière, comme par exemple :

-   métal
-   plastique
-   \...

En plus, il est proposé de créer une carte entre les familles, (par exemple stockés dans un fichier XML), afin d\'être en mesure de parcourir la base de données de matériaux dans FreeCAD.

Une telle carte pourrait par exemple, contenir un arbre, présentant les relations entre les familles, comme :

-   métal -\> acier - acier \> plat au carbone -\> pointe en acier à haute résistance.
-   métal -\> aluminium -\> aluminium coulé.

#### Fabricant

Une chaîne de caractères, indiquant le fabricant de la matière.

#### URL

Une adresse, indiquant la page Web présentant le matériel.

#### Propriétés

##### Description

Le modèle de données du matériel comprend une collection de propriétés. La taille d\'une telle collection n\'est pas fixe, et, peut être étendue avec de nouvelles propriétés définies par l\'utilisateur.

Une propriété contient les attributs suivants :

-   **name** : chaîne de caractères.
-   **symbol** : Chaîne de caractères, écrite en symbole mathématiques (au format Latex ?).
-   **type** : \"scalaire\" ou \"tableau\".
-   **value** : scalaire (si c\'est un scalaire).
-   **values** : array (s\'il s\'agit d\'un tableau).
-   **parameterNames** : tableau de chaîne de caractères (pour la propriété de type \"array\").
-   **parameterValues** : tableau de scalaires (pour la propriété de type \"array\").
-   **unit** et **unitMagnitude** (objet spécifique décrit dans Unités ) (à noter : les exemples incluent unitMagnitude, alors que je ne suis pas complètement sûr que ce devrait être défini au niveau de la propriété Le système d\'unités peuvent être définies au niveau matériel).
-   **direction** : un vecteur indiquant la direction, dans laquelle doit être comprise la valeur de la propriété. Le vecteur est lui-même un objet FreeCAD, exprimé dans le système de coordonnées global, ou dans un mode défini par le système de coordonnées.
-   **notes** : chaîne qui peut être utilisé pour décrire un peu plus la propriété, comme, quel est son sens, comment at-elle été mesurée \... Il peut aussi aider à comprendre le nom de la propriété.

Les propriétés des matériaux, seront identifiées, grâce à leurs noms, afin de les traiter, c\'est à dire, par exemple, écrire la limite d\'élasticité dans un modèle d\'éléments finis, afin de faciliter sa création, au sein des données de FreeCAD, dans une liste normalisée des noms de propriétés, ainsi que leurs unités standard, sera proposé à l\'utilisateur. Néanmoins, l\'utilisateur est libre de créer de nouvelles propriétés, avec de nouveaux noms, de nouvelles unités, et ainsi de suite \...

Ci-dessous, une proposition de bibliothèque standard de propriétés. N\'hésitez pas à en ajouter de nouvelles \...


<?xml version="1.0" encoding="UTF-8"?>



  
        
     








Notes: \"Le coefficient de Lankford moyen est représentatif de l\'anisotropie d\'une tôle mince.\" \"Le coefficient de durcissement est représentatif de la capacité de durcissement d\'un métal. Il apparaît dans la formule de Hollomon qui permet de relier la déformation plastique cumulée à la contrainte.\"

##### Exemple 1 : Coût par tonne {#exemple_1_coût_par_tonne}

Ci-dessous, un premier exemple est donné, pour montrer, comment un **coût par tonne**, de biens peut être stocké.

-   **name** : coût par tonne
-   **symbol** : non applicable
-   **type** : scalaire
-   **value** : 500
-   **values** : non applicable (mais, pourrait être : les valeurs de coût différents, par exemple, pour différents pays)
-   **parameterNames** : non applicable (mais, pourrait être : les valeurs de coût différents, par exemple, pour différents pays)
-   **parameterValues** : non applicable (mais, pourrait être : les valeurs de coût différents, par exemple, pour différents pays)
-   **parameterUnits** : non applicable
-   **unit & unitMagnitude** : \[\[ 0, -3, 0, 0, 0, 0, 0\], 1\]
    -   meaning m\^(-3) (plus de détails sur les unités et système d\'unités sur la page [unités](Units/fr.md))
-   **direction** : non applicable

##### Exemple 2 : Limite d\'élasticité {#exemple_2_limite_délasticité}

Ci-dessous, un second exemple est donné, pour montrer, comment la propriété de la limite d\'élasticitéé peut être stockée.

-   **name** : rendement d\'élasticité
-   **symbol** : YS
-   **type** : scalaire
-   **value** : 450
-   **values** : non applicable
-   **parameterNames** : non applicable
-   **parameterValues** : non applicable
-   **parameterUnits** : non applicable
-   **unit & unitMagnitude** : \[\[ -1, 1, -2, 0, 0, 0, 0\], 1\]
    -   **meaning Pa** (plus de détails sur les unités et système d\'unités sur la page [unités](Units/fr.md))
-   **direction** : \[ 1, 0, 0\] dans le système de coordonnées global
    -   données d\'une tôle d\'acier, ce qui signifie que la **limite d\'élasticité** donnée, est exprimée dans une direction **x**, qui peut être par exemple, la direction du laminage

##### Exemple 3 : écrouissage {#exemple_3_écrouissage}

Un troisième exemple est donné ci-dessous, pour montrer comment la propriété d\'écrouissage peut être stockée. Il s\'agit d\'un exemple plus complexe, car l\'écrouissage est représenté par une série de courbes. Les courbes représentent l\'évolution de la contrainte à l\'égard de la déformation plastique. 3 courbes ont été obtenues à des vitesses de déformation différentes. Toutes les courbes ont été obtenues à température ambiante.

-   **name** : écrouissage
-   **symbol** : non applicable
-   **type** : scalaire
-   **value** : non applicable
-   **values** : \[\... \[0, 100, 150, 200\], \[0, 120, 180, 210\], \[0, 140, 190, 220\]\]
-   **ParameterNames** : \[Déformation plastique, vitesse de déformation, température\]
-   **ParameterValues** :
    -   Le premier des trois tableaux représente l\'évolutions de déformation plastique
    -   La 2ème série de trois tableaux représente les évolutions du taux de déformation. Une seule valeur est indiquée dans chacun des tableaux, ce qui signifie que la vitesse de déformation ne change pas pour chaque évolution des contraintes correspondantes.
    -   Cette fois une seule valeur est écrite dans un seul tableau, ce qui signifie que la température ne change pas pour un tableau donné de contrainte, et ceci s\'applique à tous les tableaux de contrainte.

:   **\[\[\[0. , 0,4, 0,8, 1\], \[0, 0,4, 0,8, 1\], \[0, 0,4, 0,8, 1\]\]**,





:   **\[\[0.\] , \[100\] , \[1000.\] \]**,





:   **\[\[18.\] \],\]**

-   **parameterUnits** et **parameterUnitMagnitudes** : **\[\[\[0, 0, 0, 0, 0, 0, 0\], 1\], \[\[0, 0, -1, 0, 0, 0, 0\], 1\], \[\[0, 0, 0, 0, 1, 0, 0\], 1\]\]**
    -   ne signifie pas, **s\^(-1)** et **K** (plus de détails sur l\'unité et les spécifications du système unitaires sur la page **[Unités](Units/fr.md)**)
-   **unit** et **unitMagnitude** : **\[\[-1, 1, -2, 0, 0, 0, 0\], 1\]**
    -   sens Pa (plus de détails sur l\'unité et les spécifications du système unitaires sur la page **[Unités](Units/fr.md)**)

**direction** : non applicable

#### Composition chimique {#composition_chimique}

\[à documenter\]

#### Apparence

\[à documenter\]

#### Notes

Une chaîne où l\'utilisateur peut ajouter ses propres commentaires sur le matériel.

### Application des données de modèle de matériel : quelques exemples {#application_des_données_de_modèle_de_matériel_quelques_exemples}

##### Exemple 1 : briques de maçonnerie {#exemple_1_briques_de_maçonnerie}

###### Nom {#nom_1}

Briques de maçonnerie.

###### Famille {#famille_1}

? chaîne de caractères ?

###### Properties

-   **Weight** : 1kg/m³
-   **Cost per cubic meter** : 1€/m³
-   **Number of bricks por base unit** : ?float?
-   **Volume of mortar por base unit** : ?float?
-   **Mortar type** : ?string?
-   **Brick type** : ?string?
-   **Fire resistance class** : ?string?
-   **Thermal conductivity** : 1 W/mK

###### Vendeur

? chaîne de caractères ?

###### URL {#url_1}

? Une adresse Web ?

###### Notes {#notes_1}

Remarques sur la maintenance, précautions spéciale à prendre, etc ..

Code CSI/[MasterFormat](http://en.wikipedia.org/wiki/MasterFormat) (comme il existe plusieurs systèmes utilisés dans l\'industrie, qui donnent des documents spécialements codés, je propose d\'en prendre note, car il ne me semble pas pertinent, de créer des propriétés spécifiques, que nous ne sommes pas en mesure, de bien nommer).

## Actions suivantes {#actions_suivantes}

-   Définir un ensemble de noms pour les propriétés classiques, que nous pouvons définir dans une bibliothèque (fichier de configuration FreeCAD). Ces propriétés peuvent notamment être réutilisées dans d\'autres contextes, tels que le module [FEM](FEM_project/fr.md).

-   Remplir la section **composition chimique**.
-   Remplissez la section **Apparence**.
-   Définir un ensemble de composants chimiques par défaut.
-   Examen par d\'autres personnes.
-   Implémenter un modèle de données en C++ et la capacité de lecture/écriture dans un fichier ([ISO 10303-45](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=45306) travers [SCL](http://fr.wikipedia.org/wiki/Texte_structuré)?).
-   Implémenter les bibliothèques au format [XML](http://fr.wikipedia.org/wiki/Extensible_Markup_Language) pour stocker les propriétés par défaut, avec leurs unités, qui peuvent être utilisées par l\'utilisateur.
-   Implémenter l\'interface graphique Python pour gérer ces données.



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
