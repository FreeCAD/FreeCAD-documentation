 {{Macro/fr
|Name=Macro Wiring And Hoses
|Description=Cette macro crée des câbles et des tubes.
|Author=Piffpoof
}}

**Remarque de [L\'utilisateur: Piffpoof](L'utilisateur:_Piffpoof.md): certains changements entre v 0.14 et v 0.15 ont affecté cette macro qui retardera sa publication**

Ces macros prennent en charge la création et la maintenance des cables et flexibles.

![](images/Macro_Wiring_And_HosesCompletedHouse.jpg )

## Contexte

Dans le cadre de nos autres projets FreeCAD, nous avions besoin d\'un moyen de documenter le câblage et les tuyaux. Cet ensemble de macros a été développé pour répondre à ce besoin. Il y a beaucoup de choses que ce système ne fait pas, mais ce qu\'il fait est de fournir une représentation visuelle du câblage et des tuyaux, soit en tant que système isolé, soit avec le câblage et les tuyaux dans le contexte d\'un modèle FreeCAD. L\'enregistrement de tous les fils et flexibles est conservé dans un fichier au format CSV en dehors de FreeCAD. Le fichier peut donc être chargé dans un tableur ou utilisé par un autre logiciel.

## Description

Dans le cadre d\'un projet de documentation, nous avons découvert que nous devions documenter les fils et les tuyaux. Nous avons essayé différents scénarios tels que la création de lignes ou de cylindres dans le cadre du modèle existant. En raison de problèmes d\'utilisation ou de maintenance, nous avons décidé de conserver les informations dans un format différent et en dehors de FreeCAD. De cette façon, ils pourraient être créés seuls ou créés dans un document existant. Cette décision a permis à l\'utilisateur de travailler avec le câblage et les tuyaux de la manière qui leur convenait. De plus, ils pouvaient travailler avec elle de différentes manières à différents moments selon les besoins.

Au départ, nous ne savions pas comment maintenir une liste de tuyaux et de fils et diverses approches ont été essayées. Le moyen le plus simple semblait être d\'utiliser le format de fichier CSV qui existe depuis longtemps. Il y avait également des routines déjà écrites pour gérer les fichiers CSV à partir de Python. Certains des avantages étaient les suivants:

-   lisible par l\'homme
-   peut être chargé dans n\'importe quelle feuille de calcul
-   peut être maintenu à l\'aide d\'une feuille de calcul ou d\'un simple éditeur de texte
-   une amélioration future possible serait de l\'utiliser avec l\'atelier spreadsheet de FreeCAD

Les décisions suivantes ont été \"comment\" définir de tels câbles. Notre objectif étant principalement la documentation, nous avons choisi d\'exécuter des segments de ligne de point en point. Des problèmes tels que le rayon de virage ne sont pas traités. Le diamètre du câble n\'est pas non plus manipulé. Un tableau des chemins de câbles est conservé dans le fichier CSV, mais des éléments tels que la proximité des câbles (pour les problèmes d\'interférences électriques) et la longueur des câbles ne sont pas pris en charge (bien qu\'il soit possible d\'ajouter une longueur de câble rudimentaire assez facilement).

Cet ensemble de macros est essentiellement une \"démonstration de faisabilité\". Elle démontre quelques idées et leur faisabilité. Notre objectif principal était la documentation et non la gestion physique de l\'usine. Nous avons décidé de maintenir une structure de données de points, qui sont les points par lesquels passent les câbles et les tuyaux. Deuxièmement, nous avons mis en place une structure de données qui définit les câbles et les tuyaux en fonction des points qu\'ils traversent. Un câble ne peut donc être acheminé que là où des points ont été définis pour lui.

Pour les 2 structures de données, nous avons choisi les noms suivants:

-   Nexus - un point par lequel un câble ou un tuyau peut passer (le pluriel est Nexi). Les Nexi ne sont que des points dans 3 espaces, pour faciliter la visualisation, le logiciel place des anneaux toroïdes autour de l\'emplacement, mais uniquement pour une facilité d\'utilisation. Les anneaux toroïdaux peuvent être désactivés ou activés en fonction des préférences de l\'utilisateur
-   Flows (réseaux) - génériquement ce sont des routes composées de Nexi. Un code est associé à chaque type, les codes par défaut étant
    -   W - fils électriques
    -   C - conduits, destinés principalement aux câbles mais peut représenter n\'importe quoi
    -   H - tuyaux pour transporter une variété de liquides
    -   G - conduites de gaz
    -   K - un routage de caméra, c\'est vraiment juste réservé pour une exploration future selon [Tour camera animation](http://forum.freecadweb.org/viewtopic.php?f=24&t=8437)

Nexi et Flows ont tous deux des noms attribués par l\'utilisateur, de plus Nexi a des ID attribués en interne pour faciliter la gestion. Les points ou emplacements dans Nexi à 3 espaces n\'ont pas de couleurs mais les Flows peuvent avoir l\'une des 48 couleurs définies. L\'accent mis sur les couleurs revient au but recherché, celui de la documentation.

Le workflow général est

-   définir et positionner Nexi
-   définir Flow(s) en terme de Nexi
-   à des fins de maintenance, modifiez Nexi et Flows visuellement à l\'aide de l\'interface graphique FreeCAD ou à l\'aide d\'une approche tabulaire et des définitions CSV

Le fichier de données contenant à la fois des définitions Nexi et Flow est basé sur du texte. Il peut être utilisé dans n\'importe quel éditeur de texte ou par tout autre programme souhaitant accéder aux données.

### Modes de navigation {#modes_de_navigation}

Comme une grande partie du travail avec ces macros dépend de la manipulation de l\'affichage du modèle pour placer et vérifier le placement du point dans 3 espaces, il est essentiel d\'être à l\'aise avec les modes de navigation de FreeCAD qui sont documentés sur la page [Navigation par la souris](Mouse_navigation/fr.md). Il est essentiel de pouvoir faire pivoter le modèle dans la 3-D puis d\'effectuer des opérations sur un modèle stationnaire.

## Installation

Le code pour le câblage et les flexibles est dans plusieurs macros et une bibliothèque. L\'installation consiste donc à copier le code dans le répertoire Macro approprié et à appeler l\'utilitaire de génération à partir du menu Macro, de la console Python ou d\'un bouton de barre d\'outils (la méthode préférée).
-   voir [Comment installer les macros](How_to_install_macros/fr.md) pour plus d\'informations sur l\'installation de ce code de macro
-   voir [Personnaliser les barres d\'outils](Customize_Toolbars/fr.md) pour plus d\'informations sur l\'installation en tant que bouton sur une barre d\'outils

## Utilisation

Il existe en réalité deux approches différentes pour travailler avec ces macros: le nexi et les flows peuvent être définis seuls à l\'aide de leurs coordonnées 3-D ou bien, un document FreeCAD existant peut être utilisé et le nexi et les flows peuvent être définis dans le contexte de ce document. Il ne s\'agit pas d\'une décision «l\'un ou l\'autre», mais plutôt les deux approches peuvent être utilisées lorsqu\'elles sont les plus appropriées. Comme les définitions du nexi et des flows sont conservées dans un fichier au format CSV qui est stocké en dehors de FreeCAD, la présence ou l\'absence d\'un document FreeCAD n\'affecte pas le travail avec le nexi et le flow, cela facilite la tâche en fournissant un contexte visuel. Pour cette description de l\'utilisation, l\'exemple utilisera un document FreeCAD précédemment chargé comme contexte car il est plus facile de placer le

L\'utilisation de ces macros se décompose vraiment en 3 sections:

-   définir les nexi
-   définir les flows
-   éditez le fichier au format CSV pour modifier ou ajouter nexi et flows

Il existe d\'autres façons d\'effectuer certaines des tâches décrites ci-dessous et les préférences personnelles peuvent décider. Cet exemple appliquera le câblage électrique et la plomberie d\'eau froide à une maison. Notre maison vide ressemble à ceci

![](images/Macro_Wiring_And_HosesEmptyHouse.jpg )

et attend l\'installation d\'eau froide et d\'électricité. Pour des raisons d\'explication, tous les éléments électriques sont en jaune et l\'eau en bleu (à l\'exception des 2 lavabos).

### Définir les Nexi {#définir_les_nexi}

La première étape consiste à créer des points dans l\'espace 3-D (appelés «nexus» ou «nexi» au pluriel). Ces points seront utilisés dans l\'étape suivante pour définir un réseau ou Flow. Nous créons ces points en cliquant sur (c\'est-à-dire en sélectionnant ) une surface et en donnant ensuite un nom au nexi. Cette description consiste à définir le nexi pour le débit d\'eau.

1.  cliquez sur 
2.  la boîte de dialogue suivante apparaîtra:

 (Capture d\'écran que vous souhaitez charger) Cela vous demande si vous souhaitez ouvrir et charger un document FreeCAD contenant le modèle auquel vous souhaitez ajouter nexi et les flows. Il n\'est pas nécessaire d\'en charger un mais pour cet exemple nous chargerons notre maison vide

1.  sélectionnez une surface en cliquant dessus, elle sera mise en surbrillance dans la fenêtre Arborescence et aura une couleur indiquant sa sélection à l\'écran.
2.  cliquez sur 
3.  la boîte de dialogue suivante apparaîtra demandant un nom pour le nouveau nexi:



1.  le nexi va maintenant être défini. Il sera positionné dans un espace 3-D afin qu\'il soit sur la ligne du visage sélectionné au spectateur, positionné juste à côté du visage afin qu\'il ne soit pas à l\'intérieur de l\'objet. Bien que le lien ne soit peut-être pas dans la position parfaite, laissez-le pour le moment car il sera modifié ultérieurement. Un tore (c\'est-à-dire un anneau) sera affiché, il est centré sur le point du nexus. Cet anneau est purement un outil de visualisation afin que l\'emplacement du point puisse être identifié. Les anneaux de visualisation peuvent être activés/désactivés à tout moment.
2.  définir plus de nexi de la même manière en donnant à chacun un nom significatif
3.  cliquez sur 
4.  la boîte de dialogue suivante apparaîtra:



1.  répondez Yes pour enregistrer votre nouveau nexi

Remarque: à tout moment vous pouvez fusionner un projet existant afin d\'avoir un contexte visuel

### Définir le Flow {#définir_le_flow}

Une fois que les nexi ont été définis, ils peuvent être utilisés pour définir un Flow (réseau). Notre maison ressemble maintenant à ceci:

\<image d\'une maison avec nexi mais pas de flows\>

les Nexis sont définis pour le débit d\'eau mais pas les Flows encore.

1.  cliquez sur l\'

la boîte de dialogue suivante apparaît:



Cela vous demande si vous sélectionnez le nexi dans l\'ordre dans lequel vous souhaitez qu\'il crée votre réseau.

1.  sélectionner le type de débit: fils, conduits, tuyaux, conduites de gaz
2.  en utilisant la deuxième popup, sélectionnez les nexi dans l\'ordre que vous voulez



1.  fournir un nom pour le réseau
2.  sélectionnez une couleur pour le réseau
3.  cliquez sur OK ou sur Annuler. Si vous faites une erreur en sélectionnant le nexi (que ce soit une commande ou en incluant un mauvais nexi), cliquez sur Annuler et redémarrez cette étape.

\<image d\'une maison avec un réseau d\'eau\>\>

![](images/Macro_Wiring_And_HosesFlowsOnly.jpg )

### Modification de Nexi et des Flows {#modification_de_nexi_et_des_flows}

Il existe 3 façons différentes de modifier nexi. Comme les réseaux sont définis en termes de nexi, la modification de nexi affectera tout flux qui les inclut. Pour les attributs de flux descriptifs comme la couleur et le nom, il existe un moyen d\'effectuer des modifications.

Jusqu\'à présent, dans cet exemple, nous avons généré le tableau suivant:







## Interface utilisateur {#interface_utilisateur}

L\'interface utilisateur est une combinaison d\'écrans personnalisés et de parties standard de l\'interface graphique FreeCAD.

\<snapshot 1 defining Nexi\>

\<snapshot 2 defining flow\>

\<snapshot 3 editing CSV file\>

\<snapshot 4 editing Position\>

## Options

À l\'heure actuelle, il n\'y a pas vraiment d\'options pour le câblage et les tuyaux.

## Exemples de fichiers {#exemples_de_fichiers}

bla bla bla

## Remarques

blah blah blah

## Problèmes connus {#problèmes_connus}

bla bla bla

## Possibilités futures {#possibilités_futures}

bla bla bla

## Glossaire

blah blah blah

## Liens

blah blah blah

## Script

blah blah blah




