# Units/fr
Un peu de lecture sur les unités    *

-   [Métrologie](https   *//fr.wikipedia.org/wiki/M%C3%A9trologie)
-   [Système international d\'unités](https   *//fr.wikipedia.org/wiki/Système_international_d'unités)
-   [Système d\'unités impériales](https   *//fr.wikipedia.org/wiki/Syst%C3%A8me_d%27unit%C3%A9s_imp%C3%A9riales)
-   [Unité dérivée du Système international](https   *//fr.wikipedia.org/wiki/Unités_dérivées_du_système_international)
-   [Degré (angle)](https   *//fr.wikipedia.org/wiki/Degré_(angle))
-   [Unités implémentées dans OCC](https   *//github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

## Exemples


```python
# -- some examples of the FreeCAD unit translation system --
# make a shortcut for the examples
pq = FreeCAD.Units.parseQuantity

# 10 meters in internal numbers
pq('10 m')

# doing math
pq('3/8 in')

# combined stuff
pq('100 km/h')

# transfer to other units
pq('100 km/h')/tu('m/s')

# derived units (Ohm)
pq('m^2*kg*s^-3*A^-2')

# or
pq('(m^2*kg)/(A^2*s^3)')

# angles 
pq('2*pi rad') # full circle

# as gon
pq('2*pi rad') / tu('gon')

# more imperial
tu('1ft (3+7/16)in')

# or 
pq('1\' (3+7/16)"') # the ' we have to escape because of python

# trigonometry
pq('sin(pi)')

# Using translated units as parameters, this command will create a 50.8mm x 20mm x 10mm box
b = Part.makeBox(pq('2in'), pq('2m')/100, 10)
```

## Unités supportées 

Une liste complète de toutes les unités prises en charge peut être [trouvée ici](Expressions/fr#Unités.md).

## Objectifs et principes    * propositions d\'extension du système de gestion des unités 

Un système de gestion de la vulgarisation des unités, est en développant. Le concept de **système d\'unités**, est proposé dans les sections suivantes, activé lors d\'une instance en cours d\'exécution de FreeCAD. L\'intérêt pour la définition d\'un tel concept, est de travailler plus facilement avec le plus grand nombre de type d\'unités **physique** que l\'on veut, (même ceux créés par l\'utilisateur), sans augmenter la complexité de la gestion de l\'unité ni pour l\'utilisateur, ni pour les développeurs de FreeCAD.

En bref, un événement de mise à l\'échelle d\'unités, est localisé avec précision, et réalisée génériquement.

Atteindre une telle flexibilité, est particulièrement nécessaire lorsque l\'on commence à traiter les propriétés des matériaux, qui peuvent avoir des unités très différentes, et difficiles à gérer manuellement.

Le raisonnement proposé permet de manipuler les unités telles que décrites dans [Guide for the Use of the International System of Units (SI)](http   *//physics.nist.gov/cuu/pdf/sp811.pdf) et le [The International System of Units (SI)](http   *//physics.nist.gov/Pubs/SP330/sp330.pdf) du NIST.

Dans cette proposition, on rappelle d'abord dans la section [Réflexions](#R.C3.A9flexions.md) quels sont les contextes possibles pour lesquels la gestion des unités est requise.

Dans la section [Organisation](Units/fr#Organisation.md), nous présentons le modèle de données retenu pour la gestion des unités basé sur 3 objets   * *unité*, *base de données d\'unités*, et *système d\'unité*. Enfin, une courte API d\'un 4ème objet appelée *unit manager* est aussi présentée.

## Résultat

Merci pour cette extension, nous visons à faciliter l\'échelle d\'unité qui peut se produire, entre différentes tâches professionnelles. Par exemple, les dessins techniques peuvent être fait dans un système d\'unité standard, tandis que la modélisation par éléments finis, peut être géré dans un système d\'unité plus adapté pour cela.

L\'échange de données, entre ces deux types d\'activités devient plus facile avec cette extension.

## Réflexions

Dans cette section sont mis en évidence les contextes d\'utilisation d\'un tel système de gestion des unités. A partir de ces contextes, nous sommes alors en mesure de définir ses spécifications techniques.

2 contextes, sont essentiellement donnés, à titre d\'exemple.

### Contexte 1    * ouverture de fichiers de données 

Ce cas est probablement le cas le plus fréquent. Vous recevez un fichier contenant par exemple un modèle géométrique, ou décrire un matériau avec beaucoup de propriétés. Le modèle géométrique est exprimé en mètres, ou les propriétés des matériaux selon le système d\'unités international.

Dommage \...

Vous êtes un expert en modélisation par éléments finis, et vous travaillez habituellement avec le millimètre pour la longueur, le mégaPascal pour la contrainte, la tonne pour la masse\...

Dans ce contexte, la gestion des unités est nécessaire pour mettre à l\'échelle les données à partir d\'un système d\'unités initial défini dans le fichier d\'entrée vers un système d\'unités cible défini par l\'utilisateur.

### Contexte 2    * changement entre systèmes d\'unités pendant l\'exécution 

Dans ce cas, vous pouvez être en même temps celui qui réalise le dessin, et celui qui va gérer la modélisation des éléments finis (FE). Comme dans le cas précédent, les systèmes unitaires pour ces 2 tâches, ne sont pas les mêmes, et, vous avez besoin de changer le système d\'unité initial, lors de l\'exécution de celui que vous préférez.

## Organisation

### Logique d\'échelle d\'une unité 

Dans la section [Réflexions](Units/fr#Réflexions.md), deux contextes ont été présentés lors de l\'utilisation de la mise à l\'échelle d\'unités. Certains éléments doivent être souslignés dans ces deux contextes.

#### Cohérence d\'unités tout au long de l\'instance, en cours d\'exécution 

Le système proposé repose sur une hypothèse de base    * l\'utilisateur travaille dans un système d\'unités cohérent. Par exemple, cela signifie que si l\'utilisateur exprime la longueur en millimètres, nécessairement les aires seront exprimées en termes de millimètres carrés, et non de mètres carrés. C\'est **l\'hypothèse 1**.

#### Système d\'unité 

Grâce à l*\'hypothèse 1*, il est possible et pertinent de définir un système d\'unités. Un système d\'unités s\'applique à    *

-   A une instance de FreeCAD en cours d\'exécution dans laquelle vous travaillez
-   Ou il peut également s\'appliquer globalement au contenu d\'un fichier d\'entrée.

Selon le [Guide for the Use of the International System of Units (SI)](http   *//physics.nist.gov/cuu/pdf/sp811.pdf) du NIST, il existe 7 unités physiques de base. Nous avons choisi d\'exprimer un système d\'unités en termes de ces 7 unités de base.

Lorsqu\'il travaille dans une instance de FreeCAD, l\'utilisateur doit donc d\'abord définir le système d\'unités selon lequel il travaille avant de décider de passer à un autre système d\'unités, ou avant d\'importer des données d\'un fichier d\'entrée.

Ce système d\'unités s\'appliquera jusqu\'à ce que l\'utilisateur décide de le changer. S\'il le fait, toutes les données avec des dimensions seront mises à l\'échelle.

En considérant l*\'hypothèse 1*, toutes les données que l\'utilisateur saisira manuellement dans FreeCAD sont supposées être cohérentes avec le système d\'unités choisi.

L\'avantage de travailler avec un *système d\'unités* défini au niveau d\'une instance d\'exécution de FreeCAD, ou au niveau d\'un fichier de données (au lieu des *unités* qui sont définies au niveau des données) est alors que la gestion des unités est considérablement simplifiée.

Voici quelques exemples de systèmes d\'unités.

-   mètre, kilogramme, seconde, ampère, kelvin, mole, candela.
-   millimètre, tonne, milliseconde, ampère, kelvin, mole, candela.
-   millimètre, kilogramme, milliseconde, ampère, kelvin, mole, candela.
-   \...

#### Unités de base et dérivées 

Les unités dérivées sont créées par la combinaison d\'unités de base. Par exemple, une accélération (m/s) combine en même temps la longueur et le temps. Une image intéressante présentant les relations entre les unités de base et les unités dérivées peut être consultée [ici](http   *//physics.nist.gov/cuu/pdf/SIDiagramColorAnnot.pdf) également depuis NIST.

Merci, à la définition d\'une unité centrale, il est possible que l\'utilisateur travaille avec n\'importe quel type d\'unités dérivées, sans la nécessité, que les développeurs de FreeCAD les prévoient à l\'avance.

#### Symboles des unités de base et dérivées 

Selon [Le système international d\'unités (SI)](https   *//physics.nist.gov/cuu/Units/index.html), les symboles pour spécifier une unité sont officiellement approuvés. Deux conséquences peuvent en être mises en évidence.

-   Il n\'est pas facile pour un programme informatique de travailler avec les symboles d\'unités car certains sont des lettres grecques par exemple. Ils peuvent donc être un peu difficiles à traiter par un programme.
-   Alors que certaines unités et leurs symboles sont largement utilisés, ils peuvent ne pas être approuvés officiellement, comme par exemple l\'unité \"tonne\" (voir la page 55 du [Guide d\'utilisation du Système international d\'unités (SI)](https   *//physics.nist.gov/cuu/pdf/sp811.pdf)).

Pour surmonter ces limitations et rester flexible, le système proposé privilégie l\'utilisation de magnitudes unitaires plutôt que de symboles unitaires, qui restent néanmoins disponibles pour une raison d\'ergonomie.

### Modèle de données 

Les trois objets de base, du système de gestion de l\'unité sont présents, à savoir *unité*, *dictionnaire d\'unités* et *système d\'unités*.

#### Unité

En préambule, il est important de souligner qu\'un objet *unité* n\'indique en soi qu\'une **dimension** comme la longueur, la masse, le temps\... Il ne spécifie pas une **magnitude** comme le mètre, le millimètre, le kilomètre\... Cette dernière information est spécifiée par le système d\'unités.

#### Dimension

Chaîne obligatoire indiquant la *dimension* de l\'unité. Les *dimensions* des 7 unités de base sont indiquées ci-dessous (extrait du [Guide d\'utilisation du système international d\'unités (SI)](http   *//physics.nist.gov/cuu/pdf/sp811.pdf)).

-   LONGUEUR
-   MASSE
-   TEMPS
-   COURANT ÉLECTRIQUE
-   TEMPÉRATURE THERMODYNAMIQUE
-   QUANTITÉ DE SUBSTANCE
-   INTENSITÉ LUMINEUSE

L\'attribut *Dimension* permet d\'identifier l\'unité. Deux unités ne peuvent pas partager la même *dimension*.

##### Signature

Tableau d\'entiers obligatoires de taille 7 (nombre d\'unités de base) qui définit ce qu\'est l\'unité. La signature des 7 unités de base sont    *

-   LONGUEUR    * \[1,0,0,0,0,0,0\]
-   MASSE    * \[0,1,0,0,0,0,0,0\].
-   TEMPS    * \[0,0,1,0,0,0,0\]
-   COURANT ÉLECTRIQUE    * \[0,0,0,1,0,0,0\]
-   TEMPÉRATURE THERMODYNAMIQUE    * \[0,0,0,0,0,1,0,0\].
-   QUANTITÉ DE SUBSTANCE    * \[0,0,0,0,0,0,1,0\]
-   INTENSITÉ LUMINEUSE    * \[0,0,0,0,0,0,0,1\]

À partir de ces 7 unités, nous sommes ensuite en mesure d\'exprimer toutes les unités dérivées définies dans le [Guide d\'utilisation du système international d\'unités (SI)](http   *//physics.nist.gov/cuu/pdf/sp811.pdf) et d\'en créer de nouvelles selon les besoins, comme par exemple    *

-   DENSITÉ DE MASSE    * \[-3,1,0,0,0,0,0\]
-   SURFACE    * \[0,2,0,0,0,0,0,0\]

*Signature* est l\'attribut grâce auquel la mise à l\'échelle des unités peut être réalisée de manière générique.

##### Symboles

Tableau de \[real, string\] (signifiant \[*magnitude*, *symbol*\]) qui liste tous les *symbols* connus par FreeCAD. Grâce à ce tableau, l\'API de mise à l\'échelle des unités devient plus ergonomique car les *symboles* et les *magnitudes* associées sont liés.

Ce tableau peut être étendu si nécessaire.

Par exemple, la liste des *symboles* de l\'unité de LONGUEUR, et leurs *magnitudes* correspondantes est la suivante    *

[1e+12,"Tm"],[1e+09,"Gm"],[1e+06,"Mm"],
[1e+03,"km"],[1e+02,"hm"],[1e+01,"dam"],
[1e+00,"m"],[1e-01,"dm"],[1e-02,"cm"],
[1e-03,"mm"],[1e-06,"µm"],[1e-09,"nm"],
[1e-12,"pm"],[1e-15,"fm"]

Les *symboles* standards peuvent être trouvés sur le site de [NIST](http   *//physics.nist.gov/cuu/Units/units.html) pages 23 à 26 et page 32 (*metric ton* ou *tonne*) du [The International System of Units (SI)](http   *//physics.nist.gov/Pubs/SP330/sp330.pdf).

#### Dictionnaire des unités 

Toutes les unités disponibles dans FreeCAD, et les nouvelles unités créées par l\'utilisateur, doivent être stockées dans le *dictionnaire des unités*, qui est un fichier XML (fichier de configuration de FreeCAD), afin d\'être récupérées en cas de besoin, c\'est à dire lors de la mise à l\'échelle des unités.

##### Unités

Tableau d\'unités, contenu dans *unit dictionary* (le dictionnaire d\'unités).

#### Système d\'unité 

Un *système d\'unités* est l\'objet qui permet à l\'utilisateur de définir l\'unité courante *magnitude* de chaque unité de base avec laquelle il travaille. Par exemple, sachant que l\'utilisateur travaille avec le millimètre, la tonne, et la seconde, grâce à l\'utilisation d\'un système d\'unités, FreeCAD peut savoir que l\'énergie est exprimée en termes de milliJoule, la force en termes de Newton, et la contrainte en termes de MegaPascal. Ainsi, un système d\'unités n\'est défini que par un *nom* (par exemple *Système d\'unités standard*) et un *tableau de magnitude* spécifiant pour chacune des 7 unités de base, quelle est sa *magnitude* correspondante.

##### Nom

Chaîne permettant à l\'utilisateur d\'identifier quel est le système d\'unités.

##### Magnitudes

En spécifiant la magnitude des 7 unités de base, on définit un système d\'unités.

Par exemple \[1e-03, 1e+03, 1, 1, 1, 1, 1\], signifiant millimètre, tonne, seconde, ampère, Kelvin, mole, candela.

#### Gestion de l\'API des unités 

Seule, la logique de certaines méthodes est présentée, afin de mettre en évidence certaines caractéristiques. Ces méthodes pourraient appartenir à un objet appelé, *Unit manager* (gestionnaire d\'unités).

##### Vérification du dictionnaire de unités 

###### isValid

Le dictionnaire des unités peut être un fichier XML (fichier de configuration FreeCAD). Il contient une liste d\'unités définies. Un tel dictionnaire est nécessaire pour que le système de gestion des unités proposé fonctionne.

Il doit remplir certaines conditions qui doivent être vérifiées avant d\'activer le système de gestion de l\'unité. Ces conditions sont    *

-   vérifier que toutes les unités de base sont définies
-   vérifier qu\'une \"dimension\" n\'est pas définie deux fois à travers les unités
-   vérifier qu\'un *symbole* n\'est pas défini deux fois dans tous les symboles existants
-   vérifier que les *signatures* de toutes les unités ont toutes la même taille
-   vérifier qu\'un *symbole standard* (pour lequel la *magnitude* est 1) est défini pour toutes les unités

###### isCompatibleWithThisSignature

Un dictionnaire des unités définit un ensemble d\'unités et leurs grandeurs connues. Lors de la gestion d\'une unité, il est pertinent de vérifier que sa signature est compatible avec l\'ensemble des unités enregistrées dans le dictionnaire des unités, afin de pouvoir la traiter. Cette vérification comprend    *

-   vérifier que la longueur de la *signature* en entrée est de la même taille que les *signatures* des unités du dictionnaire des unités.

##### Echelle des unités 

###### scaleUnitFromSymbolToSymbol

Connaissant une valeur, une unité initiale par son symbole, l\'unité cible par son symbole, mettre à l\'échelle la valeur.

###### scaleUnitFromSymbolToUnitSystem

Connaissant une valeur, une unité initiale par son symbole, le système d\'unités cible, mettez la valeur à l\'échelle.

###### scaleUnitFromUnitSystemToSymbol

Connaissant une valeur initiale, d\'un système unitaire, le symbole, de l\'unité cible, donne la valeur de l\'échelle.

#### Les motivations pour une telle gestion    * exemple d\'application 

Supposons que nous allons mettre en place un modèle d\'éléments finis. Pour construire notre modèle, nous avons besoin du maillage, des propriétés des matériaux, et de définir les paramètres numériques. Considérant qu\'il peut y avoir des dizaines de propriétés matérielles à gérer, exprimées avec différentes unités, parfois pas toujours très communes, il est intéressant pour l\'utilisateur de n\'avoir qu\'à spécifier un système d\'unité global, sans se soucier de grand chose.

FreeCAD, ferait alors tout simplement le travail.

Comme les développeurs, et, les utilisateurs de FreeCAD, ne connaissent pas nécessairement toutes les unités, qui peuvent être définies dans les fichiers de propriétés des matériaux, il est intéressant de s\'appuyer sur un système générique.

Supposons que dans un tel fichier, nous avons un bon nombre de propriétés de matériaux exotiques, exprimés avec des unités exotiques, et, que nous voulons travailler dans un système d\'unité spécifique.

Avec le projet d\'extension d\'échelle, il est facile de donner une de ces propriétés, en connaissant leurs signatures de grandeurs, et le système d\'unité ciblée.

Pour chacune des propriétés, la mise à l\'échelle est obtenue en multipliant la valeur de la propriété initiale avec le facteur $\frac{GrandeurInitiale}{GrandeurCible}$.

La *magnitude cible* est alors simplement obtenue par l\'opération $\prod_{bu} targetMagnitude_{bu}^{signature_{bu}}$, *bu* signifiant *unité de base*.

Il devient ainsi très facile de gérer un nombre quelconque de propriétés avec n\'importe quel type d\'unités avec très peu de lignes de Python.

## Voir aussi 

-   La page [Expressions](Expressions/fr#Unit.C3.A9s.md) pour une liste de toutes les unités connues.
-   La documentation de [Quantity](Quantity/fr.md).
-   L\'outil [Std Convertisseur d\'unités](Std_UnitsCalculator/fr.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > Units/fr
