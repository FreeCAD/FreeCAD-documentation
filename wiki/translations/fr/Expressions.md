# Expressions/fr
{{TOCright}}

## Vue d\'ensemble 

Il est possible de définir des propriétés à l\'aide d\'expressions mathématiques. Dans l\'interface graphique, les zones de sélection numérique ou les champs de saisie liés aux propriétés contiennent une icône bleue <img alt="" src=images/Sketcher_Expressions.png  style="width:24px;">. Cliquez sur l\'icône ou tapez le signe égal **&#61;** pour ouvrir l\'éditeur d\'expression pour cette propriété particulière.

Une expression FreeCAD est une expression mathématique qui suit la notation pour les opérateurs mathématiques standard et fonctionne comme décrit ci-dessous. En outre, l\'expression peut faire référence à d\'autres propriétés et également utiliser des conditions. Une unité facultative peut être attachée aux nombres d\'une expression.

Les nombres peuvent utiliser une virgule `,` ou un point décimal `.` séparer les chiffres entiers des décimales. Lorsque le marqueur décimal est utilisé, il doit obligatoirement être suivi d\'au moins un chiffre. Ainsi, les expressions `1.+2.` et `1,+2,` ne sont pas valides, mais `1.0 + 2.0` et `1,0 + 2,0` sont valables.

Les opérateurs et fonctions reconnaissent les unités de mesure et nécessitent des combinaisons valides si elles sont fournies. Par exemple, `2mm + 4mm` est une expression valide, tandis que `2mm + 4` ne l\'est pas (la raison est qu\'une expression comme `1in + 4` sera très probablement interprété comme `1in + 4in` par le dessinateur mais comme toutes les unités en interne sont converties au système international SI, et le système est totalement incapable de deviner de quelle unité il s\'agit). Ces [unités](#Unités.md) sont actuellement reconnues.

Vous pouvez utiliser des [constantes prédéfinies](#Constantes_prises_en_charge.md) et des [fonctions](#Fonctions_support.C3.A9es.md).

### Arguments de la fonction 

Lorsqu\'une fonction prend plusieurs arguments, ceux-ci peuvent être séparés par un point-virgule suivie par un espace `, `. Dans ce derniers cas, la virgule est convertie en point-virgule après la saisie. Quand on utilise un point-virgule, il n\'est pas nécessaire de finir la ligne par un espace.

Les arguments peuvent inclure des références à des cellules dans une feuille de calcul. Une référence de cellule se compose de la lettre en majuscule de la ligne de la cellule suivie de son numéro de colonne, par exemple `A1`. Une cellule peut également être référencée en utilisant l\'alias de la cellule, par exemple `Spreadsheet.MyPartWidth`.

### Référencement d\'objets 

Vous pouvez faire référence à un objet par sa {{PropertyData/fr|Name}} ou sa {{PropertyData/fr|Label}}. Dans le cas d\'une {{PropertyData/fr|Label}}, vous devez l\'entourer de double symboles `<<` et `>>`, comme ceci `<<Label>>`.

Vous pouvez référencer n\'importe quelle propriété numérique d\'un objet. Par exemple, pour référencer la hauteur d\'un cylindre, vous pouvez utiliser `Cylinder.Height` ou `<<Long_name_of_cylinder>>. Hauteur`.

Pour référencer des objets de liste, utilisez `<<object_label>>.list[list_index]` ou `object_name.list [index_liste]`. Si vous souhaitez par exemple référencer une contrainte dans une esquisse, utilisez `<<MySketch>>.Constraints[16]`. Si vous êtes dans la même esquisse, vous pouvez omettre son nom et utiliser simplement `Constraints[16]`.
**Remarque :** L\'index commence par 0, la contrainte 17 a donc l\'index 16.

Pour plus d\'informations sur le référencement des objets, voir [Référence aux données CAO](#R.C3.A9f.C3.A9rence_aux_donn.C3.A9es_CAO.md).

## Constantes prises en charge 

Les constantes suivantes sont supportées:

  Constante   Description
  ----------- -------------------------------------------------------------
  **e**       [nombre d\'Euler](https://fr.wikipedia.org/wiki/E_(nombre))
  **pi**      [Pi](https://fr.wikipedia.org/wiki/Pi)

## Opérateurs pris en charge 

Les opérations suivantes sont supportées:

  Opération   Description
  ----------- -------------------------------------------------------------------
  **+**       [Addition](https://fr.wikipedia.org/wiki/Addition)
  **-**       [Soustraction](https://fr.wikipedia.org/wiki/Soustraction)
  **\***      [Multiplication](https://fr.wikipedia.org/wiki/Multiplication)
  **/**       Point flottant [Division](https://fr.wikipedia.org/wiki/Division)
  **%**       [Reste](https://fr.wikipedia.org/wiki/Reste)
  **\^**      [Exponentiation](https://fr.wikipedia.org/wiki/Exponentiation)

## Fonctions supportées 

### Fonctions mathématiques générales 

Les fonctions mathématiques suivantes sont disponibles.

Les [fonctions trigonométriques](https://fr.wikipedia.org/wiki/Fonction_trigonom%C3%A9trique) utilisent le degré comme unité par défaut. Pour la mesure en radian, ajoutez première valeur dans une expression. Par exemple `cos(45)` est identique à `cos(pi rad / 4)`. Les expressions en `deg` ou `°`, comme `360deg - atan2(3; 4)` ou `360&deg; - atan2(3; 4)`. Si une expression est sans unités et doit être convertie en degrés ou radians pour la compatibilité, multipliez par `1&nbsp;deg`, `1&nbsp;°` ou `1&nbsp;rad` selon le cas, par ex. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`.
Ces fonctions trigonométriques sont supportées :

  Fonction      Description                                                                    Plage des valeurs
  ------------- ------------------------------------------------------------------------------ ------------------------------------
  acos(x)       [Arc cosinus](https://fr.wikipedia.org/wiki/Arc_cosinus)                       -1 \<= x \<= 1
  asin(x)       [Arc sinus](https://fr.wikipedia.org/wiki/Arc_sinus)                           -1 \<= x \<= 1
  atan(x)       [Arc tangente](https://fr.wikipedia.org/wiki/Arc_tangente)                     tout
  atan2(x, y)   [atan2](https://fr.wikipedia.org/wiki/Atan2) de *x/y*                          tout sauf y = 0
  cos(x)        [Cosinus](https://fr.wikipedia.org/wiki/Cosinus)                               tout
  cosh(x)       [Cosinus hyperbolique](https://fr.wikipedia.org/wiki/Cosinus_hyperbolique)     tout
  sin(x)        [Sinus](https://fr.wikipedia.org/wiki/Sinus_(math%C3%A9matiques))              tout
  sinh(x)       [Sinus hyperbolique](https://fr.wikipedia.org/wiki/Sinus_hyperbolique)         tout
  tan(x)        [Tangente](https://fr.wikipedia.org/wiki/Tangente_(trigonom%C3%A9trie))        tout sauf x = n·90 avec n = entier
  tanh(x)       [Tangente hyperbolique](https://fr.wikipedia.org/wiki/Tangente_hyperbolique)   tout

Ces fonctions d'exponentiation et de logarithmisation sont prises en charge:

  Fonction    Description                                                                      Plage des valeurs
  ----------- -------------------------------------------------------------------------------- -------------------
  exp(x)      [Fonction exponentielle](https://fr.wikipedia.org/wiki/Fonction_exponentielle)   tout
  log(x)      [Logarithme népérien](https://fr.wikipedia.org/wiki/Logarithme_naturel)          x \> 0
  log10(x)    [Logarithme décimal](https://fr.wikipedia.org/wiki/Logarithme_d%C3%A9cimal)      x \> 0
  pow(x, y)   [Les puissances](https://fr.wikipedia.org/wiki/Exposant_(math%C3%A9matiques))    tout
  sqrt(x)     [Racine carrée](https://fr.wikipedia.org/wiki/Racine_carr%C3%A9e)                x \>= 0

Ces fonctions d\'arrondi, de troncature et de reste sont supportées:

  Fonction    Description                                                                                                                                                                                 Plage des valeurs
  ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------
  abs(x)      [Valeur absolue](https://fr.wikipedia.org/wiki/Valeur_absolue)                                                                                                                              tout
  ceil(x)     [Partie entière par excès](https://fr.wikipedia.org/wiki/Partie_enti%C3%A8re_et_partie_fractionnaire#Fonction_partie_enti%C3%A8re), la plus petite valeur entière supérieure ou égale à x   tout
  floor(x)    [Partie entière](https://fr.wikipedia.org/wiki/Partie_enti%C3%A8re_et_partie_fractionnaire#Fonction_partie_enti%C3%A8re), la plus grande valeur entière inférieure ou égale à x             tout
  mod(x, y)   [Reste](https://fr.wikipedia.org/wiki/Reste) après la division de *x* par *y*                                                                                                               tout sauf y = 0
  round(x)    [Arrondi](https://fr.wikipedia.org/wiki/Arrondi_(math%C3%A9matiques)) au nombre entier le plus proche                                                                                       tout
  trunc(x)    [Troncature](https://fr.wikipedia.org/wiki/Troncature) au nombre entier le plus proche en direction de zéro                                                                                 tout

### Statistiques et fonctions d\'agrégation 

[Les fonctions d\'agrégation](https://fr.wikipedia.org/wiki/Fonction_d%27agr%C3%A9gation) prennent un ou plusieurs arguments.
Les arguments individuels pour agréger les fonctions peuvent être constitués de plages de cellules. Une plage de cellules est exprimée sous la forme de deux références de cellule séparées par deux points {{Incode|:}}, par exemple {{Incode|average(B1:B8)}} ou {{Incode|sum(A1:A4; B1:B4)}}. Les références de cellule peuvent également utiliser des alias de cellule, par exemple {{Incode|average(StartTemp:EndTemp)}} {{Version/fr|0.19}}.

Les fonctions cumulatives supportées sont

  Fonction                 Description                                                                                                                                      Plage des valeurs
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------ -------------------
  average(a; b; c; \...)   Valeur [Moyenne](https://fr.wikipedia.org/wiki/Moyenne_arithm%C3%A9tique) des arguments; identique à sum(a; b; c; \...) / count(a; b; c; \...)   tout
  count(a; b; c; \...)     [Comptage](https://fr.wikipedia.org/wiki/D%C3%A9nombrement) des arguments; généralement utilisé pour les plages de cellules                      tout
  max(a; b; c; \...)       Valeur [Maximum](https://fr.wikipedia.org/wiki/Extremum) des arguments                                                                           tout
  min(a; b; c; \...)       Valeur [Minimum](https://fr.wikipedia.org/wiki/Extremum) des arguments                                                                           tout
  stddev(a; b; c; \...)    [Écart type](https://fr.wikipedia.org/wiki/%C3%89cart_type) des valeurs des arguments                                                            tout
  sum(a; b; c; \...)       [Somme](https://fr.wikipedia.org/wiki/Somme_(arithm%C3%A9tique)) des valeurs des arguments; généralement utilisé pour les plages de cellules     tout

### Manipulation de chaînes de caractères 

#### Identification de la chaîne caractères 

Les chaînes de caractères sont identifiées dans les expressions en les entourant de doubles chevrons ouvrants/fermants (comme les étiquettes).

Dans l\'exemple suivant, \"TEXT\" est reconnu comme une chaîne de caractères : `<<TEXT>>`.

#### Concaténation de chaînes de caractères 

Les chaînes de caractères peuvent être concaténées à l\'aide du signe \'+\'.

L\'exemple suivant `<<MY>> + <<TEXT>>` sera concaténé en \"MYTEXT\".

#### Formatage des chaînes de caractères 

Le formatage des chaînes de caractères est pris en charge en utilisant le (vieux) style % de Python.

Tous les spécificateurs % tels que définis dans la [documentation Python](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Par exemple, supposons que vous ayez un cube par défaut de 10mm de côté nommé \'Box\' \--nomination par défaut de FreeCAD\--, l\'expression suivante `<<Cube length : %s>> % Box.Length` se développera en \"Cube length : 10.0 mm\"

Une limitation est qu\'un seul spécificateur % est autorisé dans une chaîne, vous devez donc utiliser la concaténation de chaînes si plusieurs sont nécessaires. Dans la même situation que ci-dessus, l\'expression `<<Cube length is %s>> % Box.Length + << and width is %s>> % Box.Width` se développera en \"Cube length is 10.0 mm and width is 10.0 mm\".

Un exemple de fichier FreeCAD utilisant le formatage des chaînes de caractères est disponible [dans le forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657).

## Expressions conditionnelles 

Les expressions conditionnelles sont de la forme `condition ? resultTrue : resultFalse`. (*condition ? résultat si VRAI : résultat si FAUX*). La condition est définie comme une expression dont le résultat est `0` (faux) ou différent de zéro (vrai). Remarquez que le fait de mettre l\'expression conditionnelle entre parenthèses est actuellement considéré comme une erreur. {{VersionMinus/fr|0.19}}

Les [opérateurs relationnels](https://en.wikipedia.org/wiki/Relational_operator#Standard_relational_operators) suivants sont définis:

  Unité     Description
  --------- ----------------------------
  **==**    égal à
  **!=**    différent de
  **\>**    strictement plus grand que
  **\<**    strictement plus petit que
  **\>=**   plus grand ou égal à
  **\<=**   plus petit ou égal à

## Unités

Les unités peuvent être directement utilisées dans des expressions. L\'analyseur les connecte à la valeur précédente. Donc `2mm` ou `2 mm` sont valides tandis que `mm` est invalide car il n\'y a pas de valeur.

Toutes les valeurs doivent avoir une unité. Par conséquent, vous devez généralement utiliser une unité pour les valeurs dans les feuilles de calcul.
Dans certains cas, cela fonctionne même sans unité, par exemple si vous avez dans la cellule B1 du calculateur, juste le nombre `1.5` et qu\'il se reporte à la hauteur du pavé. Cela ne fonctionne que parce que la hauteur du pad prédéfinit l\'unité `mm` utilisée si aucune unité n\'est donnée. Il échouera néanmoins si vous utilisez pour la hauteur du pad, par exemple `Sketch1.Constraints.Width - Spreadsheet.B1` car `Sketch1.Constraints.Width` a une unité et `Spreadsheet.B1` n\'en a pas.

Les unités avec des exposants peuvent être directement entrées. Donc, par exemple `mm^3` sera reconnu comme mm³ et `m^3` sera reconnu comme m³.

Si vous avez une variable dont le nom est celui d\'une unité, vous devez mettre la variable entre `<< >>` pour éviter qu\'elle ne soit reconnue comme une unité. Par exemple, si vous avez la dimension `Sketch.Constraints.A`, elle serait reconnue comme l\'unité Ampère. Par conséquent, vous devez l\'écrire dans l\'expression sous la forme `Sketch.Constraints.<<A>>`.

Les unités suivantes sont reconnues par l'analyseur d'expression:

Une quantité de matière:

  Unité   Description
  ------- --------------------------------------------------------------
  mmol    Milli[mole](https://fr.wikipedia.org/wiki/Mole_(unit%C3%A9))
  mol     [Mole](https://fr.wikipedia.org/wiki/Mole_(unit%C3%A9))

Angle:

  Unité   Description
  ------- ------------------------------------------------------------------------------------------------------------
  °       [Degré](https://fr.wikipedia.org/wiki/Degree_(angle)); alternative à l\'unité *deg*
  deg     [Degré](https://fr.wikipedia.org/wiki/Degree_(angle)); alternative à l\'unité *°*
  rad     [Radian](https://fr.wikipedia.org/wiki/Radian)
  gon     [Gradian](https://fr.wikipedia.org/wiki/Gon_(unit))
  S       [Seconde d\'arc](https://fr.wikipedia.org/wiki/Sous-unit%C3%A9s_du_degr%C3%A9)
  ″       [Seconde d\'arc](https://fr.wikipedia.org/wiki/Sous-unit%C3%A9s_du_degr%C3%A9); alternative à l\'unité *S*
  M       [Minute d\'arc](https://fr.wikipedia.org/wiki/Sous-unit%C3%A9s_du_degr%C3%A9)
  ′       [Minute d\'arc](https://fr.wikipedia.org/wiki/Sous-unit%C3%A9s_du_degr%C3%A9); à l\'unité *M*

Courant:

  Unité   Description
  ------- ----------------------------------------------------------
  mA      Milli[Ampère](https://fr.wikipedia.org/wiki/Amp%C3%A8re)
  A       [Ampère](https://fr.wikipedia.org/wiki/Amp%C3%A8re)
  kA      Kilo[Ampère](https://fr.wikipedia.org/wiki/Amp%C3%A8re)
  MA      Méga[Ampère](https://fr.wikipedia.org/wiki/Amp%C3%A8re)

Capacité électrique:

  Unité   Description
  ------- -------------------------------------------------------------------------------------------------------------------
  pF      Pico[farad](https://fr.wikipedia.org/wiki/Farad), {{Version/fr|0.19}}
  nF      Nano[farad](https://fr.wikipedia.org/wiki/Farad), {{Version/fr|0.19}}
  uF      Micro[farad](https://fr.wikipedia.org/wiki/Farad); alternative à l\'unité *µF*, {{Version/fr|0.19}}
  µF      Micro[farad](https://fr.wikipedia.org/wiki/Farad); alternative à l\'unité *uF*, {{Version/fr|0.19}}
  mF      Milli[farad](https://fr.wikipedia.org/wiki/Farad), {{Version/fr|0.19}}
  F       [Farad](https://fr.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg, {{Version/fr|0.19}}

Conductance électrique:

  Unité   Description
  ------- ------------------------------------------------------------------------------------------------------------------------------------
  uS      Micro[siemens](https://fr.wikipedia.org/wiki/Siemens_(unit%C3%A9)); alternative à l\'unité *µS*, {{Version/fr|0.19}}
  µS      Micro[siemens](https://fr.wikipedia.org/wiki/Siemens_(unit%C3%A9)); alternative à l\'unité *uS*, {{Version/fr|0.19}}
  mS      Milli[siemens](https://fr.wikipedia.org/wiki/Siemens_(unit%C3%A9)), {{Version/fr|0.19}}
  S       [Siemens](https://fr.wikipedia.org/wiki/Siemens_(unit%C3%A9)); 1 S = 1 s\^3·A\^2/kg/m\^2, {{Version/fr|0.19}}
  kS      Kilo[siemens](https://fr.wikipedia.org/wiki/Siemens_(unit%C3%A9)), {{Version/fr|0.20}}
  MS      Mega[siemens](https://fr.wikipedia.org/wiki/Siemens_(unit%C3%A9)), {{Version/fr|0.20}}

Inductance électrique:

  Unité   Description
  ------- --------------------------------------------------------------------------------------------------------------------------------
  nH      Nano[henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)), {{Version/fr|0.19}}
  uH      Micro[henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)); alternative à l\'unité *µH*, {{Version/fr|0.19}}
  µH      Micro[henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)); alternative à l\'unité *uH*, {{Version/fr|0.19}}
  mH      Milli[henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)), {{Version/fr|0.19}}
  H       [Henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)); 1 H = 1 kg·m\^2/s\^2/A\^2, {{Version/fr|0.19}}

Résistance électrique:

  Unité   Description
  ------- -----------------------------------------------------------------------------------------------------------------------
  Ohm     [Ohm](https://fr.wikipedia.org/wiki/Ohm_(unit%C3%A9)); 1 Ohm = 1 kg·m\^2/s\^3/A\^2, {{Version/fr|0.19}}
  kOhm    Kilo[ohm](https://fr.wikipedia.org/wiki/Ohm_(unit%C3%A9)), {{Version/fr|0.19}}
  MOhm    Mega[ohm](https://fr.wikipedia.org/wiki/Ohm_(unit%C3%A9)), {{Version/fr|0.19}}

Charge électrique:

  Unité   Description
  ------- --------------------------------------------------------------------------------------------------
  C       [Coulomb](https://fr.wikipedia.org/wiki/Coulomb); 1 C = 1 A·s, {{Version/fr|0.19}}

Différence de potentiel électrique:

  Unité   Description
  ------- -------------------------------------------------
  mV      Milli[volt](https://fr.wikipedia.org/wiki/Volt)
  V       [Volt](https://fr.wikipedia.org/wiki/Volt)
  kV      Kilo[volt](https://fr.wikipedia.org/wiki/Volt)

Energie / Travail:

  Unité   Description
  ------- --------------------------------------------------------------------------------------------------------------------------------
  mJ      Milli[joule](https://fr.wikipedia.org/wiki/Joule)
  J       [Joule](https://fr.wikipedia.org/wiki/Joule)
  kJ      Kilo[joule](https://fr.wikipedia.org/wiki/Joule), {{Version/fr|0.19}}
  eV      [Electronvolt](https://fr.wikipedia.org/wiki/%C3%89lectronvolt) ; 1 ev = 1.602176634e-19 J, {{Version/fr|0.19}}
  keV     Kilo[electronvolt](https://fr.wikipedia.org/wiki/%C3%89lectronvolt), <small>(v0.19)</small> 
  MeV     Mega[electronvolt](https://fr.wikipedia.org/wiki/%C3%89lectronvolt), <small>(v0.19)</small> 
  kWh     [Kilowatt heure](https://fr.wikipedia.org/wiki/Kilowatt-heure) ; 1 kWh = 3.6e6 J, {{Version/fr|0.19}}
  Ws      [Watt second](https://fr.wikipedia.org/wiki/Joule#Dans_la_vie_courante#Conversion) ; alternative à l\'unité *Joule*
  VAs     [Volt ampère seconde](https://fr.wikipedia.org/wiki/Joule) ; alternative à l\'unité *Joule*, {{Version/fr|0.19}}
  CV      [Coulomb·volt](https://en.wikipedia.org/wiki/Joule) ; alternative à l\'unité *Joule*, {{Version/fr|0.19}}

Force:

  Unité   Description
  ------- ------------------------------------------------------------------
  mN      [milliNewton](https://fr.wikipedia.org/wiki/Newton_(unit%C3%A9))
  N       [Newton](https://fr.wikipedia.org/wiki/Newton_(unit%C3%A9))
  kN      [kiloNewton](https://fr.wikipedia.org/wiki/Newton_(unit%C3%A9))
  MN      [mégaNewton](https://fr.wikipedia.org/wiki/Newton_(unit%C3%A9))
  lbf     [Livre-force](https://fr.wikipedia.org/wiki/Livre-force)

Longueur:

  Unité   Description
  ------- ---------------------------------------------------------------------------------------------------------
  nm      [nanomètre](https://fr.wikipedia.org/wiki/M%C3%A8tre)
  mu      [micromètre](https://fr.wikipedia.org/wiki/M%C3%A8tre); alternative à l\'unité *µm*
  µm      [micromètre](https://fr.wikipedia.org/wiki/M%C3%A8tre); alternative à l\'unité *um*
  mm      [millimètre](https://fr.wikipedia.org/wiki/M%C3%A8tre)
  cm      [centimètre](https://fr.wikipedia.org/wiki/M%C3%A8tre)
  m       [mètre](https://fr.wikipedia.org/wiki/M%C3%A8tre)
  dm      [décimètre](https://fr.wikipedia.org/wiki/M%C3%A8tre)
  km      [kilomètre](https://fr.wikipedia.org/wiki/M%C3%A8tre)
  mil     [millième de pouce](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternative à l\'unité *thou*
  thou    [millième de pouce](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternative à l\'unité *mil*
  in      [pouce](https://fr.wikipedia.org/wiki/Pouce_(unit%C3%A9))
  ft      [pied](https://fr.wikipedia.org/wiki/Pied_(unit%C3%A9)); alternative à l\'unité \'
  \'      [pied](https://fr.wikipedia.org/wiki/Pied_(unit%C3%A9)); alternative à l\'unité *ft*
  yd      [yard ou verge](https://fr.wikipedia.org/wiki/Verge_(unit%C3%A9))
  mi      [mille](https://fr.wikipedia.org/wiki/Mille_(unit%C3%A9))

Intensité lumineuse :

  Unit\"   Description
  -------- --------------------------------------------------
  cd       [Candela](https://fr.wikipedia.org/wiki/Candela)

Intensité du champ magnétique:

  Unité   Description
  ------- ---------------------------------------------------------------------------------------------------------------------------
  Oe      [Oersted](https://fr.wikipedia.org/wiki/%C5%92rsted_(unit%C3%A9)); 1 Oe = 79.57747 A/m, {{Version/fr|0.19}}

Flux d\'induction magnétique

  Unité   Description
  ------- ------------------------------------------------------------------------------------------------------------------------
  Wb      [Weber](https://fr.wikipedia.org/wiki/Weber_(unit%C3%A9)); 1 Wb = 1 kg\*m\^2/s\^2/A, {{Version/fr|0.19}}

Densité de flux magnétique :

  Unité   Description
  ------- -------------------------------------------------------------------------------------------------------
  G       [Gauss](https://en.wikipedia.org/wiki/Gauss_(unit)); 1 G = 1 e-4 T, <small>(v0.19)</small> \|-

Poids:

  Unité   Description
  ------- --------------------------------------------------------------------------------------------------
  ug      [microgramme](https://fr.wikipedia.org/wiki/Gramme); alternative à l\'unité *µg*
  µg      [microgramme](https://fr.wikipedia.org/wiki/Gramme); alternative à l\'unité *ug*
  mg      [milligramme](https://fr.wikipedia.org/wiki/Gramme)
  g       [gramme](https://fr.wikipedia.org/wiki/Gramme)
  kg      [kilogramme](https://fr.wikipedia.org/wiki/Gramme)
  t       [Tonne](https://fr.wikipedia.org/wiki/Tonne)
  oz      [Once](https://fr.wikipedia.org/wiki/Once_(unit%C3%A9))
  lb      [livre](https://fr.wikipedia.org/wiki/Livre_(unit%C3%A9_de_masse)); alternative à l\'unité *lbm*
  lbm     [Pound](https://fr.wikipedia.org/wiki/Livre_(unit%C3%A9_de_masse)); alternative à l\'unité *lb*
  st      [Stone](https://fr.wikipedia.org/wiki/Stone_(unit%C3%A9))
  cwt     [Hundredweight](https://en.wikipedia.org/wiki/Hundredweight)

Puissance:

  Unité   Description
  ------- -----------------------------------------------------------------------------------
  W       [Watt](https://fr.wikipedia.org/wiki/Watt)
  kW      Kilo[watt](https://fr.wikipedia.org/wiki/Watt), {{Version/fr|0.19}}
  VA      [Voltampère](https://fr.wikipedia.org/wiki/Voltamp%C3%A8re)

Pression:

  Unité   Description
  ------- --------------------------------------------------------------------------------------------------------------------------------------
  Pa      [pascal](https://fr.wikipedia.org/wiki/Pascal_(unit%C3%A9))
  kPa     Kilo[pascal](https://fr.wikipedia.org/wiki/Pascal_(unit%C3%A9))
  MPa     Méga[pascal](https://fr.wikipedia.org/wiki/Pascal_(unit%C3%A9))
  GPa     Giga[pascal](https://fr.wikipedia.org/wiki/Pascal_(unit%C3%A9))
  mbar    Milli[Bar](https://fr.wikipedia.org/wiki/Bar_(unit%C3%A9)), {{Version/fr|0.19}}
  bar     [Bar](https://fr.wikipedia.org/wiki/Bar_(unit%C3%A9)), {{Version/fr|0.19}}
  uTorr   Micro[torr](https://fr.wikipedia.org/wiki/Torr); alternative à l\'unité *µTorr*
  µTorr   Micro[torr](https://fr.wikipedia.org/wiki/Torr); alternative à l\'unité *uTorr*
  mTorr   Milli[torr](https://fr.wikipedia.org/wiki/Torr)
  Torr    [Torr](https://fr.wikipedia.org/wiki/Torr); 1 Torr = 133.32 Pa
  psi     [Livre-force par pouce carré](https://fr.wikipedia.org/wiki/Livre-force_par_pouce_carr%C3%A9); 1 psi = 6.895 kPa
  ksi     Kilo[livre-force par pouce carré](https://fr.wikipedia.org/wiki/Livre-force_par_pouce_carr%C3%A9)
  Mpsi    Mega[livre-force par pouce carré](https://fr.wikipedia.org/wiki/Livre-force_par_pouce_carr%C3%A9), {{Version/fr|0.19}}

Température:

  Unité   Description
  ------- ----------------------------------------------------------------------------------
  uK      [microkelvin](https://fr.wikipedia.org/wiki/Kelvin); alternative à l\'unité *µK*
  µK      [microkelvin](https://fr.wikipedia.org/wiki/Kelvin); alternative à l\'unité *uK*
  mK      [millikelvin](https://fr.wikipedia.org/wiki/Kelvin)
  K       [Kelvin](https://fr.wikipedia.org/wiki/Kelvin)

Inductance électrique:

  Unité   Description
  ------- --------------------------------------------------------------------------------------------------------------------------------
  nH      Nano[henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)), {{Version/fr|0.19}}
  uH      Micro[henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)); alternative à l\'unité *µH*, {{Version/fr|0.19}}
  µH      Micro[henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)); alternative à l\'unité *uH*, {{Version/fr|0.19}}
  mH      Milli[henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)), {{Version/fr|0.19}}
  H       [Henry](https://fr.wikipedia.org/wiki/Henry_(unit%C3%A9)); 1 H = 1 kg·m\^2/s\^2/A\^2, {{Version/fr|0.19}}

Volume:

  Unité   Description
  ------- -------------------------------------------------------------------------------------------------
  ml      Milli[Litre](https://fr.wikipedia.org/wiki/Litre), {{Version/fr|0.19}}
  l       [Litre](https://fr.wikipedia.org/wiki/Litre)
  cft     [Pied](https://fr.wikipedia.org/wiki/Pied_(unit%C3%A9)) cube, {{Version/fr|0.19}}

Unités impériales spéciales:

  Unité   Description
  ------- -----------------------------------------------------------------------------------------------------
  mph     [Mille par heure](https://fr.wikipedia.org/wiki/Mille_par_heure), {{Version/fr|0.19}}
  sqft    [Pied carré](https://fr.wikipedia.org/wiki/Pied_carr%C3%A9), {{Version/fr|0.19}}

Les unités couramment utilisées suivantes ne sont pas encore prises en charge:

  Unité   Description                                                                                                                                 Alternative
  ------- ------------------------------------------------------------------------------------------------------------------------------------------- --------------------------
  °C      [Celsius](https://en.wikipedia.org/wiki/Celsius)                                                                                            \[°C\] + 273.15 K
  °F      [Fahrenheit](https://en.wikipedia.org/wiki/Fahrenheit);                                                                                     (\[°F\] + 459.67) × ​5/9
  u       [Unité de masse atomique unifiée](https://fr.wikipedia.org/wiki/Unit%C3%A9_de_masse_atomique_unifi%C3%A9e); alternative à l\'unité \"Da\"   1.66053906660e-27 kg
  Da      [Dalton](https://fr.wikipedia.org/wiki/Unit%C3%A9_de_masse_atomique_unifi%C3%A9e); alternative à l\'unité \"u\"                             1.66053906660e-27 kg
  sr      [Steradian](https://fr.wikipedia.org/wiki/Steradian)                                                                                        Pas directement
  lm      [Lumen](https://fr.wikipedia.org/wiki/Lumen_(unit%C3%A9))                                                                                   Pas directement
  lx      [Lux](https://fr.wikipedia.org/wiki/Lux_(unit%C3%A9))                                                                                       Pas directement
  px      [Pixel](https://fr.wikipedia.org/wiki/Pixel)                                                                                                Pas directement

## Caractères et noms non valides 

La fonction expression est très puissante mais pour atteindre cette puissance, elle présente certaines limitations concernant certains caractères. Pour surmonter cela, FreeCAD propose d\'utiliser des étiquettes et de les référencer à la place des noms d\'objets. Dans les étiquettes, vous pouvez utiliser presque tous les caractères spéciaux.

Dans les cas où vous ne pouvez pas utiliser une étiquette, telle que le nom des contraintes d\'une esquisse, vous devez savoir quels caractères ne sont pas autorisés.

### Étiquettes

Pour les [étiquettes](Object_name/fr#Label_.28Etiquette.29.md), il n\'y a pas de caractères non valides, cependant certains caractères doivent être évités:

+----------------------------------------------------------+------------------------------------------------------------------------+
| Caractères                                               | Description                                                            |
+==========================================================+========================================================================+
|                                           | Doivent être évités en ajoutant `\` devant eux. |
| `'`                                             |                                                                        |
|                                                       |                                                                        |
| , `\`, `"` |                                                                        |
+----------------------------------------------------------+------------------------------------------------------------------------+

Par exemple, l\'étiquette `Sketch\002` doit être référencée comme `<<Sketch\\002>>`.

### Noms

Les [Noms](Object_name/fr#Name_.28Nom.29.md) d\'objets tels que des dimensions, des croquis, etc\... peuvent ne pas avoir les caractères ou les séquences de caractères répertoriés ci-dessous, auquel cas le nom n\'est pas valide:

  Caractères / Séquences de caractères                                                                                                             Description
  ------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**                     Caractères qui sont des opérateurs mathématiques ou qui font partie de constructions mathématiques
  **A**, **kA**, **mA**, **MA**, **C**, **G**, **F**, **uF**, **µF**, **J**, **K**, \'\'\' \' \'\'\', \'\'\' ft \'\'\', **°** et bien d\'autres!   Caractères et séquences de caractères qui sont des [unités](Expressions/fr#Unit.C3.A9s.md)
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, and many more!                            Caractères utilisés comme espace réservé ou pour déclencher des opérations spéciales
  **pi**, **e**                                                                                                                                    Constantes mathématiques
  **´**, **\**, \'\'\' \' \'\'\', **\"**                                                                                                          Caractères utilisés pour les accents
  espace                                                                                                                                           Un espace définit la fin d\'un nom et ne peut donc pas être utilisé

Par exemple, le nom suivant est valide: `<<Sketch>>.Constraints.T2üßµ@`, alors que ces noms sont non valables: `<<Sketch>>.Constraints.test\result_2` (\\r signifie \"retour chariot\") ou `<<Sketch>>.Constraints.mol` (mol est une unité).

**Remarque:** puisque des noms plus courts (surtout s\'ils n\'ont qu\'un ou deux caractères) peuvent facilement entraîner des noms invalides, envisagez d\'utiliser des noms plus longs et/ou d\'établir une convention de dénomination appropriée.

### Cell aliases 

For [spreadsheet cell aliases](Spreadsheet_SetAlias.md) only alphanumeric characters and underscores (`A` to `Z`, `a` to `z`, `0` to `9` and `_`) are allowed.

## Référence aux données CAO 

Il est possible d\'utiliser les données du modèle lui-même dans une expression. Pour référencer une propriété, utilisez `object.property`. Si la propriété est un composé de champs, les champs individuels sont accessibles en tant que `object.property.field`.

Le tableau suivant montre quelques exemples :

+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Données CAO                                              | Appel dans l\'expression              | Résultat                                                                                                                                                                                                  |
+==========================================================+=======================================+===========================================================================================================================================================================================================+
| Longueur paramétrique d\'un Cube de l\'atelier Part      |                        | Longueur en mm                                                                                                                                                                                            |
|                                                          | `Cube.Length`                |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume du Cube                                           |                        | Volume en mm³ sans unité                                                                                                                                                                                  |
|                                                          | `Cube.Shape.Volume`          |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type de la forme Cube                                    |                        | Chaîne de caractère : Solid                                                                                                                                                                               |
|                                                          | `Cube.Shape.ShapeType`       |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Label du Cube                                            |                        | Chaîne de caractère : Label                                                                                                                                                                               |
|                                                          | `Cube.Label`                 |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Coordonnée x du centre de gravité du Cube                |                        | coordonnée x en mm sans unité                                                                                                                                                                             |
|                                                          | `Cube.Shape.CenterOfMass.x`  |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Valeur d\'une contrainte dans une esquisse               |                        | Valeur numérique de la contrainte nommée `Width` dans l\'esquisse, si l\'expression est utilisée dans l\'esquisse elle-même.                                                       |
|                                                          | `Constraints.Width`          |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Valeur d\'une contrainte provenant d\'une autre esquisse |                        | Valeur numérique de la contrainte nommée `Width` dans l\'esquisse, si l\'expression est utilisée en dehors de l\'esquisse.                                                         |
|                                                          | `MySketch.Constraints.Width` |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Valeur d\'un alias de feuille de calcul                  |                        | Valeur de l\'alias nommé `Depth` dans la feuille de calcul `Spreadsheet`                                                                                    |
|                                                          | `Spreadsheet.Depth`          |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Valeur d\'une propriété locale                           |                        | Valeur de la propriété {{PropertyData/fr|Length}}, par exemple dans un objet Pad, on pourrait l\'utiliser pour calculer {{PropertyData/fr|Length2}}, si celle-ci est utilisé. |
|                                                          | `Length`                     |                                                                                                                                                                                                           |
|                                                          |                                    |                                                                                                                                                                                                           |
+----------------------------------------------------------+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Variables globales 

Pour le moment il n\'y a pas de notion de variables globales dans FreeCAD. Mais des variables arbitraires peuvent être définies comme des cellules dans une feuille de calcul en utilisant [l\'atelier Spreadsheet](Spreadsheet_Workbench/fr.md), auquelles on aura donné un nom en utilisant l\'alias de la propriété pour la cellule utilisée (clic-droit dans la cellule). Ainsi, elles peuvent être accessibles à partir de toute expression comme toute autre propriété de l\'objet.

## Liaison entre documents 

Il est possible (avec limitations) de définir une propriété d\'un objet dans votre document actuel (fichier \".FCstd\") en utilisant une expression pour référencer une propriété d\'un objet contenu dans un autre document (fichier \".FCstd\"). Par exemple, une cellule dans une feuille de calcul ou la {{PropertyData/fr|Length}} d\'un cube de pièce, etc. dans un document peut être définie par une expression faisant référence à la valeur de placement X ou à une autre propriété d\'un objet contenu dans un autre document.

Note importante : Imaginez que vous utilisiez le nom d\'un document pour le référencer depuis d\'autres documents. Lorsque vous sauverez ce document pour la première fois, vous allez certainement lui choisir un nom différent de \"Unnamed1\" (ou sa version traduite), et là, quand vous allez le ré-ouvrir, les liens seront perdus. Il est donc recommandé de créer en premier le document \"maître\", puis d\'y créer immédiatement la feuille de calcul, de sauver le document maître avec un nom had-hoc et de le fermer. Après l\'avoir ouvert à nouveau, son nom sera fixé en interne dans FreeCAD. Ensuite vous pourrez toujours faire des modification mais il ne faudra pas le renommer.

Une fois que le document maître avec la feuille de calcul est créé et enregistré (nommé), vous pouvez créer des documents dépendants en toute sécurité. Par exemple, si vous nommez le document maître `master`, la feuille de calcul `modelConstants` et attribuez à une cellule un nom d\'alias `Length`, vous pouvez ensuite accéder à la valeur comme suit:


`master#modelConstants.Length`

**Remarque:** le document maître doit être chargé pour que les valeurs de ce dernier soient disponibles pour le document dépendant.

Malheureusement, le vérificateur intégré suppose parfois qu'aucun nom valide étendu n'existe. Continuez à taper quand même. Lorsque vous avez terminé la référence complète, le bouton **OK** devient actif.

Bien sûr, vous pouvez charger les documents correspondants à tout moment pour y faire les modifications que vous voudrez.

## Problèmes connus / tâches restantes 

-   Le graphe de dépendance est basé sur la relation entre les objets et le document, et non sur les propriétés. Cela signifie que vous ne pouvez pas renseigner et interroger le même objet, par exemple dans une feuille de calcul, même si il n\'y a pas de dépendance cyclique si l\'on considère seulement les propriétés, vous ne pouvez pas avoir d\'objet dont les dimensions proviennent de la feuille de calcul et calculer son volume dans la même feuille de calcul. Pour contourner le problème, utilisez plusieurs feuilles de calcul, l\'un pour contrôler votre modèle et l\'autre pour faire des rapports.
-   L\'analyseur syntaxique d\'expressions ne gère pas bien les parenthèses et n\'est pas capable d\'analyser correctement certaines expressions. Par exemple : `<nowiki>=</nowiki> (A1 > A2) ? 1 : 0` donne une erreur, alors que `<nowiki>=</nowiki> A1 > A2 ? 1 : 0` est accepté. L\'expression `<nowiki>=</nowiki> 5 + ((A1>A2) ? 1 : 0)` va contrarier l\'analyseur syntaxique dans tous les cas.
-   Comme indiqué ci-dessus, malheureusement, le vérificateur intégré prétend parfois qu\'un nom valide n\'existe pas. Continuez à taper quand même. Une fois la référence complète terminée, le bouton **OK** devient actif.
-   FreeCAD ne dispose pas encore d\'un gestionnaire d\'expressions intégré où toutes les expressions d\'un document sont listées et peuvent être créées, supprimées, interrogées etc\... Un addon est disponible : [fcxref expression manager](https://github.com/gbroques/fcxref).
-   les bogues et tickets ouverts pour les expressions sont référencés sur le [Bugtracker de Freecad, catégorie Expressions](https://freecadweb.org/tracker/set_project.php?project_id=4;20)


{{Powerdocnavi

}} 

_

---
[documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/fr
