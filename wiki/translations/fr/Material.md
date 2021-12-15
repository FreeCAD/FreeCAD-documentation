# Material/fr
## Présentation


{{TOCright}}

Cette page vous renseigne sur le système de données des matériaux dans FreeCAD.

## Résumé

Puisqu\'il est difficile, voire impossible, de définir un ensemble fixe ou complet de propriétés de matériaux, nous allons le faire de manière plus ouverte. Chaque objet dans FreeCAD qui doit traiter de matériaux aura une propriété nommée \"Material\". Il s\'agit d\'une liste de clés/valeurs pouvant contenir un nombre infini de propriétés de matériau. Puisqu\'il s\'agit d\'un moyen très ouvert et extensible de traiter ces données, il présente également le risque de désorganisation et de chaos. Par conséquent, cette page définit certaines règles et propriétés de base pour traiter de telles cartes de propriétés de matériaux.

## Règles

Chaque jeu de propriétés a une entrée obligatoire qui est **\"Name\"**. Il s\'agit de la clé principale du matériau. Les autres propriétés du matériau sont facultatives ou peuvent être récupérés à partir d\'un matériau d\'une Base de données (DB).

Les noms des propriétés (key) sont classés par chaînes séparées par des traits de soulignement. La première sous-chaîne est nommée par l\'application ou en standard, ce qui suit peut être utilisé plus tard pour les propriétés de groupe. Les valeurs peuvent également être regroupées par des traits de soulignement, par exemple pour séparer les différentes sortes d\'acier.

Exemples :

-   Name=Steel\_Cast
-   SpecificWeight=7.85 (at 20° in kg/mm3)
-   EN10027\_name = S235JR+AR (steel standard EN 10027-1)
-   FEM\_YoungsModulus = xx (in mm−1·kg·s−2)
-   FEM\_YoungsModulus\_Z
-   FEM\_YoungsModulus\_X

Chaque propriété de description est humainement lisible sur cette page, avec des liens vers des informations complémentaires (par exemple Wikipedia).

Pour chaque propriété une unité doit être définie, l\'unité est basée sur l\'unité interne de FreeCAD mm-kg-s ! Qui permet une traduction et utilisation cohérente.

La clé (Name) et la valeur de la propriété utilisent uniquement des caractères ASCII (7 bits). Les touches sont rédigées selon la casse mais interprétées sans respecter la casse.

Les traits de soulignement permettent un historique et la propriété éditeur/visionneuse permettant leur pliage.

## Outils

Il y a quelques bonnes ressources de matériaux accessibles facilement :

-   [Units calculator](http://www.dimensionengine.com/) pour obtenir des informations sur les matériaux dans l\'unité nécessaire à FreeCAD.
-   [<http://www.matweb.com/>](http://www.matweb.com/) [gratuit](http://matweb.com/reference/terms.aspx) base de données gratuite avec des milliers de caractéristiques de matériaux.

## Base de données de matériaux 

Étant donné que la norme ci-dessus est appliquée, il serait stupide de stocker toutes les propriétés au niveau des objets. Fondamentalement, nous pouvons construire une Base de données de matériaux avec le nom comme clé principale. Donc si vous n\'avez pas de besoins spéciaux pour votre matériau, vous avez juste a définir par exemple Name=Steel et FreeCAD récupérera toutes les propriétés dans cette Base de données. Chaque propriété supplémentaire que vous définirez dans le plan se substituera à celui de la Base de données.

À l\'avenir, nous pourrons héberger cette base de données quelque part sur le Web et créer une base de données de matériaux OpenSource générale.

Pour le moment, je pense à une compilation d\'un mini-jeu de données avec un ensemble de matériaux \"de base\" et leurs propriétés de base, et une version complète basée sur SQLite.

## Material.py

Étant donné que les manipulations des propriétés des matériaux sont un travail fastidieux, nous devrions mettre en place un module principal en Python appelé {{FileName|Material.py}}. Ce sera l\'endroit pour mettre en œuvre toutes sortes de méthodes d\'assistance pour choisir un matériau adapté.

-   Calcul de masse par Volume et densité
-   Traduction en différents systèmes d\'unités
-   Calculs nécessaires dans l\'application spéciale (par ex. FEM)
-   et toutes choses que nous ne connaissons pas encore

Le module doit être implémenté et peut être exécuté dans FreeCAD ou rester seul en ligne de commande par le module Python (charte-matériau-propriété).

## Le format de fichier de carte des matériaux FreeCAD 

Travailler avec des matériaux signifie souvent importer / exporter des définitions de matériaux. Par conséquent, un format de fichier est nécessaire. Étant donné que nous n\'avons que la forme clé / valeur, nous pouvons utiliser un format de fichier simple et facile à lire et à analyser. C\'est pourquoi le format [ini-file](http://en.wikipedia.org/wiki/INI_file) est choisi. Is est standardisé et a déjà un analyseur disponible. Par exemple, le [module d\'analyseur de configuration en python](http://docs.python.org/2/library/configparser.html).

Chaque définition de matière réside dans un fichier avec extension {{FileName|.FCMat}}. Certains de ces fichiers font partie du source de FreeCAD et sont compilés dans le fichier binaire. Il s\'agit de sauver des dépenses dans la distribution et l\'accès. Mais les fichiers peuvent aussi être placés et répartis à différents endroits pour accepter les autres définitions de matériaux non standards.

### Exemples fichier .FCMat 


```python
 ; last modified 1 April 2001 by John Doe
 
 Name=Steel_Cast
 Father=Steel
 Source=Some material book everyone knows (or not) ;Some comment
  
 [EN10027]
 ; steel standard EN 10027-1
 Name=S235JR+AR      
 
 [Graphic]
 EmissiveColor = 255,255,255
```

## Propriétés du matériau 

Voici maintenant la description des propriétés du matériau convenues. N\'hésitez pas à ajouter un paragraphe pour les propriétés de matériaux de votre champ d\'application.

### Généralités

  Nom de la propriété   Description                                                                                                                                                                                                                           Unité/Type de donnée
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------
  Name                  Nom unique de la propriété, suivant les règles décrites ci-dessus                                                                                                                                                                     ASCII string 7-bit
  Father                Nom du groupe de matériaux à qui ce matériau appartient. Si ce matériau est défini il hérite de toutes les propriétés Father (Parent). Ce qui signifie que s\'il n\'est pas défini les propriétés Father (Parent) seront utilisées.   ASCII string 7-bit
  Description           Un espace réservé pour une plus longue description du matériau                                                                                                                                                                        ASCII string 7-bit
  SpecificWeight        Le poids spécifique (également connu sous le nom du poids unitaire) est le poids (plus exactement la masse) par unité de volume d\'un matériau. Voir: [Specific\_weight](http://en.wikipedia.org/wiki/Specific_weight)                kg/mm$^3$
  Vendor                Spécifie la marque ou le fournisseur du matériau                                                                                                                                                                                      ASCII string 7-bit
  ProductURL            Une URL où trouver plus d\'informations sur le matériau                                                                                                                                                                               ASCII string 7-bit
  SpecificPrice         Le prix unitaire de ce matériau. Les unités peuvent beaucoup varier (USD/m$^3$, EUR/pièce, etc\...)                                                                                                                                   ASCII string 7-bit

  : Propriétés générales des matériaux

**ToDos (à faire):** ajouter certaines propriétés avec un système de commandes de matériaux (métal, alliage, minéral, bois\...)

### Mécanique

  Nom de la propriété                        Description                                                                                                                                                                                                                                                                                                                                                                         Unité/Type de donnée
  ------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------
  Young\'s Modulus                           Module de Young, également connu sous le nom de Module de traction ou module d\'élasticité, est une mesure de raideur d\'un matériau élastique et est une quantité utilisée pour caractériser les matériaux. Voir: [1](http://fr.wikipedia.org/wiki/Module_de_Young)                                                                                                                kg\*mm\^-1\*s\^-2 (MPa)
  Poisson\'s Ratio                           La contraction latérale des matériaux sous tension en une fraction de leur allongement. Voir: [Poisson\'s Ratio](https://en.wikipedia.org/wiki/Poisson%27s_ratio)                                                                                                                                                                                                                   Adimensionnelle (-)
  Rendement                                  La contrainte à laquelle un matériau ductile (comme l\'acier) commence à développer une déformation plastique (irréversible). Voir: [Yield Strength](https://en.wikipedia.org/wiki/Yield_(engineering))                                                                                                                                                                             N\'\*mm\^-2 (MPa)
  Résistance à la traction ultime (UTS)      L\'effort auquel la matière se rompt. Pour les matériaux ductiles, peut être dû à une déformation plastique importante (voir la section Rendement). Pour un matériau fragile, la résistance à la rupture et la résistance à la traction ultime coïncidente. Voir: [UTS](https://en.wikipedia.org/wiki/Ultimate_tensile_strength)                                                    N\'\*mm\^-2 (MPa)
  Points de rendement                        Utilisé dans un objet matériau non linéaire FEM pour décrire une courbe contrainte-déformation uniaxiale ductile d\'un matériau. Les valeurs sont entrées en tant que tuples (limite d\'élasticité, déformation plastique), où la première combinaison est (Rendement, 0) et la dernière (UTS, Fracture Strain) Voir: [YieldPoints](https://en.wikipedia.org/wiki/Work_hardening)   (N\'\*mm\^-2 (MPa), adimensionnelle (-)
  Résistance à la compression axiale (FCK)   La résistance à la compression du béton, définie comme la résistance d\'un cube de 150 mm testé après 28 jours. Voir [FCK](http://eurocodes.jrc.ec.europa.eu/doc/WS2008/EN1992_1_Walraven.pdf)                                                                                                                                                                                      N\'\*mm\^-2 (MPa)
  Angle de friction (PHI)                    The angle of internal friction of a granular material like sand or concrete, as used in the Mohr-Coulomb yield criterion. See [PHI](https://en.wikipedia.org/wiki/Mohr%E2%80%93Coulomb_theory)                                                                                                                                                                                      degrees (-)
  Dureté                                     Des\...                                                                                                                                                                                                                                                                                                                                                                             
  EN-10027-1                                 En cas de matériau en acier le [grade](http://en.wikipedia.org/wiki/Steel_grades) est défini dans [European standard](http://en.wikipedia.org/wiki/European_Committee_for_Standardization) No. 10027-1.                                                                                                                                                                             string ASCII 7-bit

  : Propriétés des matériaux utilisés en génie mécanique

**ToDos (à faire):** ajouter encore des propriétés requises pour la conception mécanique.

### Graphique

Cette section définit les propriétés du matériau qui sont liées à l\'apparence visuelle du matériau. Le

  Nom de la propriété   Description                                                                                                                 Unité/Type de donnée
  --------------------- --------------------------------------------------------------------------------------------------------------------------- ----------------------------------
  AmbientColor          Couleur d\'ambiance dans le modèle de couleur Coin3D                                                                        float,float,float range: 0.0-1.0
  DiffuseColor          Diffusion de Couleur dans le modèle de couleur Coin3D                                                                       float,float,float range: 0.0-1.0
  SpecularColor         Couleur spéculaire dans le modèle de couleur Coin3D                                                                         float,float,float range: 0.0-1.0
  EmissiveColor         Couleur émissive dans la palette de couleurs Coin3D                                                                         float,float,float range: 0.0-1.0
  SectionColor          Couleur affichée lorsque le matériau est coupé dans le modèle de couleur Coin3D                                             float,float,float range: 0.0-1.0
  Shininess             Couleur d\'ambiance dans le modèle de couleur Coin3D                                                                        float range: 0.0-1.0
  Transparency          Transparence de Couleur dans le modèle de couleur Coin3D                                                                    float range: 0.0-1.0
  VertxShader           Programme de nuancier vertex au sens de [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)                        Multi line string ASCII 7-bit
  FragmentShader        Programme de shader (ombre) de fragment, tel que défini dans [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)   Multi line string ASCII 7-bit

  : visual appearance

### Thermique

  Nom de la propriété           Description                                                                                                                                                                   Unité/Donnée-Type
  ----------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------
  Conductivité Thermique        La [Conductivité Thermique (R ou coefficient lambda)](http://en.wikipedia.org/wiki/Thermal_conductivity) qui indique la capacité de transférer de la chaleur d\'un matériau   W/m²K
  ThermalExpansionCoefficient                                                                                                                                                                                 
  SpecificHeat                                                                                                                                                                                                

  : Propriétés Thermiques

### Architecture et BIM 

  Nom de la propriété   Description                                                                                                                                                                                                                                                                                                                                Unité/Type de donnée
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------
  StandardCodeXXXX      Où XXXX est le nom de la norme (extrait de [dépôt des normes BlenderBIM](https://github.com/Moult/IfcClassification/tree/master/ifc)), par exemple, StandardCodeUniclass2. La valeur est le code spécifique de ce matériau dans la norme donnée. Cette propriété peut apparaître plusieurs fois, chacune avec un code standard différent   Chaîne ASCII 7-bit
  StandardCode          Le code spécifique de ce matériau dans le format standard ci-dessus                                                                                                                                                                                                                                                                        Chaîne ASCII 7-bit
  FireStandard          La norme de résistance au feu utilisée dans le matériau                                                                                                                                                                                                                                                                                    Chaîne ASCII 7-bit
  FireClass             La [classe de résistance au feu](http://en.wikipedia.org/wiki/Fire-resistance_rating) du matériau selon la norme ci-dessus                                                                                                                                                                                                                 Chaîne ASCII 7-bit
  SoundTransmission     Le coefficient de transmission sonore de ce matériau                                                                                                                                                                                                                                                                                       W/m$^2$K
  Finish                Le type de finition/couche de surface de ce matériau                                                                                                                                                                                                                                                                                       Chaîne ASCII 7-bit
  Color                 La spécification de couleur de ce matériau. Ce n\'est pas nécessairement la couleur à afficher dans la fenêtre mais peut être par exemple le nom de couleur spécifié dans le catalogue d\'un fournisseur                                                                                                                                   Chaîne ASCII 7-bit
  UnitsArea             Le nombre d\'unités de ce matériau nécessaires pour remplir une certaine zone. Par exemple, dans le cas d\'une brique, 45 briques/m²                                                                                                                                                                                                       Unités/m$^2$

  : Propriétés des matériaux utilisés dans la conception architecturale

## A faire 

-   ajouter durabilité et propriétés LEED

 {{FEM Tools navi}} 

_ _ _ _ _

---
[documentation index](../README.md) > [Developer](Category_Developer.md) > Material/fr
