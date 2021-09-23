# Units/fr
Un peu de lecture sur les unités :

-   [Métrologie](https://fr.wikipedia.org/wiki/M%C3%A9trologie)
-   [Système international d\'unités](https://fr.wikipedia.org/wiki/Système_international_d'unités)
-   [Système d\'unités impériales](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27unit%C3%A9s_imp%C3%A9riales)
-   [Unité dérivée du Système international](https://fr.wikipedia.org/wiki/Unités_dérivées_du_système_international)
-   [Degré (angle)](https://fr.wikipedia.org/wiki/Degré_(angle))
-   [Unités implémentées dans OCC](https://github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

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

## Objectifs et principes : propositions d\'extension du système de gestion des unités 

Un système de gestion de la vulgarisation des unités, est en développant. Le concept de **système d\'unités**, est proposé dans les sections suivantes, activé lors d\'une instance en cours d\'exécution de FreeCAD. L\'intérêt pour la définition d\'un tel concept, est de travailler plus facilement avec le plus grand nombre de type d\'unités **physique** que l\'on veut, (même ceux créés par l\'utilisateur), sans augmenter la complexité de la gestion de l\'unité ni pour l\'utilisateur, ni pour les développeurs de FreeCAD.

En bref, un événement de mise à l\'échelle d\'unités, est localisé avec précision, et réalisée génériquement.

Atteindre une telle flexibilité, est particulièrement nécessaire lorsque l\'on commence à traiter les propriétés des matériaux, qui peuvent avoir des unités très différentes, et difficiles à gérer manuellement.

Le raisonnement proposé, permet la manutention des unités telles que décrites dans le [\"Guide for the Use of the International System of Units (SI)\"](http://physics.nist.gov/cuu/pdf/sp811.pdf) et [\"The International System of Units (SI)\"](http://physics.nist.gov/Pubs/SP330/sp330.pdf), tous les deux du [NIST](http://www.nist.gov/index.html).

Dans cette proposition, on rappelle d'abord dans la section [ Réflexion](Units/fr#Réflexion.md) quels sont les contextes possibles pour lesquels la gestion des unités est requise.

Dans la section [ Organisation](Units/fr#Organisation.md), nous présentons le modèle de données retenu pour la gestion des unités basé sur 3 objets: l**\'unité**, une **base de données d\'unités**, et le **système d\'unité**.
Enfin, une courte API d\'un 4ème objet appelée l**\'unit manager** est aussi présentée.

## Résultat

Merci pour cette extension, nous visons à faciliter l\'échelle d\'unité qui peut se produire, entre différentes tâches professionnelles. Par exemple, les dessins techniques peuvent être fait dans un système d\'unité standard, tandis que la modélisation par éléments finis, peut être géré dans un système d\'unité plus adapté pour cela.

L\'échange de données, entre ces deux types d\'activités devient plus facile avec cette extension.

## Réflexion

Dans cette section, sont présents les contextes d\'utilisation d\'un tel système de gestion d\'unité. A partir de ces contextes, nous sommes alors en mesure de définir ses spécifications techniques.

2 contextes, sont essentiellement donnés, à titre d\'exemple.

### Contexte 1 : ouverture de fichiers de données 

Ce cas est probablement le cas le plus fréquent. Vous recevez un fichier contenant par exemple un modèle géométrique, ou décrire un matériau avec beaucoup de propriétés. Le modèle géométrique est exprimé en mètres, ou les propriétés des matériaux selon le système d\'unités international.

Dommage \...

Vous êtes un expert en [FE modélisation](http://fr.wikipedia.org/wiki/Méthode_des_éléments_finis), et vous travaillerez généralement avec, des **millimètres** pour la longueur, **MegaPascal** pour la pression, **tonne** pour la masse \...

Dans ce contexte, la gestion de l\'unité est nécessaire à l\'échelle des données, à partir d\'un système unitaire initialement défini dans le fichier d\'entrée, dans le système défini par l\'utilisateur de l\'unité cible.

### Contexte 2 : changement entre systèmes d\'unités pendant l\'exécution 

Dans ce cas, vous pouvez être en même temps celui qui réalise le dessin, et celui qui va gérer la modélisation des éléments finis (FE). Comme dans le cas précédent, les systèmes unitaires pour ces 2 tâches, ne sont pas les mêmes, et, vous avez besoin de changer le système d\'unité initial, lors de l\'exécution de celui que vous préférez.

## Organisation

### Logique d\'échelle d\'une unité 

Dans la section [Réflexion](Units/fr#Réflexion.md), deux contextes ont été présentés lors de l\'utilisation de la mise à l\'échelle d\'unités. Certains éléments doivent être souslignés dans ces deux contextes.

#### Cohérence d\'unités tout au long de l\'instance, en cours d\'exécution 

Le système proposé, est basé sur une hypothèse : l\'utilisateur, travaille dans un système d\'unité cohérent. Par exemple, cela signifie que si l\'utilisateur exprime la longueur en millimètres, nécessairement la surface sera exprimée en millimètres carrés, et non en mètres carrés. Il s\'agit d\'une **hypothèse**.

#### Système d\'unité 

En raison d**\'une hypothèse** , il est pertinent de définir un système d\'unités. Un système d\'unité s\'applique à :

-   une instance FreeCAD en cours d\'exécution, et, dans laquelle vous travaillez.
-   ou bien, peut également s\'appliquer globalement au contenu d\'un fichier ouvert.

Selon Guide [\"Guide for the Use of the International System of Units (SI)\"](http://physics.nist.gov/cuu/pdf/sp811.pdf) du [NIST](http://www.nist.gov/index.html), il y a 7 unités physiques de base. Nous avons choisi d\'exprimer un système d\'unités en fonction de ces 7 unités de base.

Lorsque vous travaillez au sein d\'une instance **FreeCAD**, l\'utilisateur doit d\'abord définir le système d\'unités selon laquelle il/elle travaille, avant qu\'il/elle décide de passer à un autre système d\'unité, ou avant d\'importer des données à partir d\'un fichier.

Ce système s\'appliquera, jusqu\'à ce que l\'utilisateur décide de changer l\'unité. S\'il/elle le fait, toutes les données de **Grandeur** seront réduites.

En considérant cette **seule hypothèse**, toutes les données que l\'utilisateur va entrer manuellement dans FreeCAD, sont supposées être cohérentes avec le système d\'unité choisi.

C\'est l\'avantage, de travailler avec un **système d\'unités**, défini au niveau de l\'instance en cours d\'exécution de FreeCAD, ou, au niveau du fichier de données, (au lieu de l\'unité définie au niveau des données) c\'est alors, que la gestion de l\'unité est considérablement simplifiée.

Voici quelques exemples de systèmes d\'unités.

-   mètre, kilogramme, seconde, ampère, kelvin, mole, candela.
-   millimètre, tonne, milliseconde, ampère, kelvin, mole, candela.
-   millimètre, kilogramme, milliseconde, ampère, kelvin, mole, candela.
-   \...

#### Unités de base et dérivées 

les unités dérivées sont créées par la combinaison d\'unités de base. Par exemple, d\'une **accélération (m/s)**, combine à la fois la **longueur**, et, le **temps**. Une image intéressante présentant les relations entre les unités de base, et, les unités dérivées, peut être vu [ici](http://physics.nist.gov/cuu/pdf/SIDiagramColorAnnot.pdf), aussi de [NIST](http://www.nist.gov/index.html).

Merci, à la définition d\'une unité centrale, il est possible que l\'utilisateur travaille avec n\'importe quel type d\'unités dérivées, sans la nécessité, que les développeurs de FreeCAD les prévoient à l\'avance.

#### Symboles des unités de base dérivées 

Selon [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf), les symboles pour préciser les unités, sont officiellement approuvées. Deux conséquences peuvent être misent en évidence à partir de cela.

-   il n\'est pas facile pour un programme informatique de travailler avec les symboles d\'unités, parce que certains symboles, sont des [lettres grecques](http://fr.wikipedia.org/wiki/Alphabet_grec). Par conséquent, le traitement par un programme peut être difficile.
-   alors que certaines unités, et, leurs symboles peuvent être largement utilisés, ils peuvent, ne pas être approuvés officiellement, comme par exemple l\'unité, la **tonne** (voir p32 [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf)).

Pour surmonter ces limites, et, garder une bonne flexibilité, le système proposé favorise l\'utilisation des **grandeurs d\'unités** au lieu des **symboles d\'unité**, qui restent néanmoins disponibles pour une raison d\'ergonomie.

### Modèle de données 

Les trois objets de base, du système de gestion de l\'unité sont présents, à savoir **l\'unité**, le **dictionnaire d\'unités** et le **système d\'unités**.

#### Unité

Comme avant-propos, il est important de souligner, que l\'objet unité en lui-même indique, une **grandeur** comme la longueur, la masse, le temps \... Il n\'en précise pas l\'ampleur, comme le mètre, millimètre, kilomètre \... Cette dernière information est spécifiée par le système d\'unité.

##### Grandeur

Obligatoirement, une chaîne, indique la **Grandeur** de l\'unité. La **Grandeur** des 7 unités de base sont indiquées ci-dessous (à partir de [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf)).

      **Grandeur**
  --- ---------------------------
  1   LENGTH
  2   MASS
  3   TIME
  4   ELECTRIC CURRENT
  5   THERMODYNAMIC TEMPERATURE
  6   AMOUNT OF SUBSTANCE
  7   LUMINOUS INTENSITY

L\'attribut de **Grandeur** permet d\'identifier l\'unité. Deux unités ne peuvent pas partager la même **Grandeur**.

##### Signature

La signature, est dans tableau d\'INTEGER (entiers) de 7 cases, la signature doit obligatoirement avoir une taille de 7 (chiffres), la position du chiffre dans le tableau définit l\'unité.

La signature des 7 unités de base sont les suivantes:

      **Grandeur**
  --- ---------------------------
  1   LENGTH
  2   MASS
  3   TIME
  4   ELECTRIC CURRENT
  5   THERMODYNAMIC TEMPERATURE
  6   AMOUNT OF SUBSTANCE
  7   LUMINOUS INTENSITY

À partir de ces 7 unités, nous sommes en mesure d\'exprimer toutes les unités dérivées, définies dans [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf), et, au besoin, d\'en créer de nouvelles, comme par exemple :

      **Grandeur**
  --- --------------
  1   MASS DENSITY
  2   AREA

La **signature**, est l\'attribut de mise à l\'échelle, qui peut être réalisée pour l\'unité, d\'une manière générique.

##### Symboles

Un tableau de **\[real, string\]** (sens **\[grandeur** (magnitude), **symbol\]**) qui répertorie tous les symboles connus par FreeCAD. Merci pour ce tableau, de cette manière, l\'API de mise à l\'échelle d\'une unité devient plus ergonomique, car les symboles et grandeurs connexes sont liées.

Ce tableau peut être étendu si nécessaire.

Par exemple, la liste des **symboles** de l\'unité de longueur, et ses associés de **grandeurs** (magnitudes) est :

 [1e+12,"Tm"],[1e+09,"Gm"],[1e+06,"Mm"],
[1e+03,"km"],[1e+02,"hm"],[1e+01,"dam"],
[1e+00,"m"],[1e-01,"dm"],[1e-02,"cm"],
[1e-03,"mm"],[1e-06,"µm"],[1e-09,"nm"],
[1e-12,"pm"],[1e-15,"fm"]

Les **symboles** standards peuvent être trouvés sur le site de [NIST](http://physics.nist.gov/cuu/Units/units.html) pages 23 à 26 et page 32 (**metric ton** ou **tonne** ) du [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf).

#### Base de données d\'unités 

Toutes les unités disponibles dans FreeCAD, et les nouvelles créés par l\'utilisateur, doivent être stockées dans **unit dictionary** , qui est un fichier [.XML](http://fr.wikipedia.org/wiki/Extensible_Markup_Language) (fichier de configuration FreeCAD), de façon à être récupéré en cas de besoin, soit lors de la réalisation d\'échelle unité.

##### Unités

Tableau d\'unités, contenu dans **unit dictionary** (le dictionnaire d\'unités).

#### Unit system 

Un **système d\'unité** est l\'objet qui permet à l\'utilisateur de définir l\'unité actuelle (grandeur), de chacune des unités de base avec lesquelles il/elle travaille. Par exemple, sachant que l\'utilisateur travaille en **millimétres**, **tonnes**, et **secondes**, à l\'utilisation d\'un système d\'unités, FreeCAD peut savoir que l\'énergie est exprimée en termes de **millijoule**, la force en termes de **Newton**, et la pression en **mégapascal**. Ainsi, un système d\'unité est uniquement défini par un **nom** (par exemple **Standard unit system**), et une **table de grandeurs**, en spécifiant pour chacune des 7 unités de base son correspondant **grandeur**.

##### Nom

Chaîne permettant à l\'utilisateur d\'identifier quel est le système d\'unités.

##### Grandeur (Magnitude) 

En spécifiant la Grandeur de chacune des 7 unités de base, le système d\'unités est définie.

Par exemple **\[1e-03, 1e +03, 1, 1, 1, 1, 1\]**, ce qui signifie, millimètre, tonne, seconde, ampère, kelvin, mole, candela.

#### Gestion de l\'API des unités 

Seule, la logique de certaines méthodes est présentée, afin de mettre en évidence certaines caractéristiques. Ces méthodes pourraient appartenir à un objet appelé, **Unit manager** (gestionnaire d\'Unités).

##### Vérification du dictionnaire de unités 

###### isValid

Le dictionnaire des unité peut être un fichier [.XML](http://fr.wikipedia.org/wiki/Extensible_Markup_Language) (fichier de configuration de FreeCAD). Il contient une liste d\'unités définies. Un tel dictionnaire, est nécessaire pour le système de gestion des unités proposées pour travailler.

Il faut remplir certaines conditions qui doivent être vérifiées avant d\'activer le système de gestion d\'unités.

Ces conditions sont les suivantes :

-   vérifier que toutes les unités de base sont définies.
-   vérifier que la grandeur n\'est pas définie deux fois dans les unités.
-   vérifier que le symbole n\'est pas défini deux fois dans tous les symboles existants.
-   vérifier que les signatures de toutes les unités ont toutes la même taille.
-   vérifier qu\'un symbole standard (avec la **grandeur** fixée sur 1) est défini pour l\'ensemble des unités

###### isCompatibleWithThisSignature

Un dictionnaire d\'unités, définit un ensemble d\'unités, et, leurs grandeurs connues. Lors de la gestion d\'une unité, il est important de vérifier, que sa signature est compatible avec l\'ensemble des unités enregistrées dans le dictionnaire des unités, pour pouvoir les traiter.

Ce contrôle comprend :

-   Vérifiez que la longueur de la **signature**, est de la même taille que la **signature** de l\'unité dans le dictionnaire.

##### Echelle des unités 

###### scaleUnitFromSymbolToSymbol

Connaissant la valeur initiale d\'une unité par son symbole, le symbole, de l\'unité cible, donne la valeur de l\'échelle.

###### scaleUnitFromSymbolToUnitSystem

Connaissant la valeur initiale d\'une unité par son symbole, le système d\'unité cible, donne la valeur de l\'échelle.

###### scaleUnitFromUnitSystemToSymbol

Connaissant une valeur initiale, d\'un système unitaire, le symbole, de l\'unité cible, donne la valeur de l\'échelle.

#### Les motivations pour une telle gestion : exemple d\'application 

Supposons, que nous allons mettre en place un modèle d\'éléments finis. Pour construire notre modèle, nous avons besoin de mailles (mesh), de propriétés de matériaux, et de définir les paramètres numériques. Considérant qu\'il peut y avoir des dizaines de propriétés de matériaux à gérer, exprimées avec des unités différentes, parfois pas toujours très communes, il est intéressant pour l\'utilisateur de n\'avoir à spécifier, qu\'un système global d\'unité, sans trop de soucis.

FreeCAD, ferait alors tout simplement le travail.

Comme les développeurs, et, les utilisateurs de FreeCAD, ne connaissent pas nécessairement toutes les unités, qui peuvent être définies dans les fichiers de propriétés des matériaux, il est intéressant de s\'appuyer sur un système générique.

Supposons que dans un tel fichier, nous avons un bon nombre de propriétés de matériaux exotiques, exprimés avec des unités exotiques, et, que nous voulons travailler dans un système d\'unité spécifique.

Avec le projet d\'extension d\'échelle, il est facile de donner une de ces propriétés, en connaissant leurs signatures de grandeurs, et le système d\'unité ciblée.

Pour chacune des propriétés, la mise à l\'échelle est obtenue en multipliant la valeur de la propriété initiale avec le facteur $\frac{GrandeurInitiale}{GrandeurCible}$.

La **GrandeurCible** est alors simplement obtenue, avec l\'opération $\prod_{bu} targetMagnitude_{bu}^{signature_{bu}}$, ou **bu** est l**\'unité de base** permanente.

Il devient ainsi très facile, de gérer un grand nombre de propriétés avec n\'importe quels types d\'unités, et, avec très peu de code **Python**.

## Voir aussi 

-   La page [Expressions](Expressions/fr#Unit.C3.A9s.md) pour une liste de toutes les unités connues.
-   La documentation de [Quantity](Quantity/fr.md).
-   L\'outil [Std Convertisseur d\'unités](Std_UnitsCalculator/fr.md).


{{Powerdocnavi

}}

---
[documentation index](../README.md) > Units/fr
