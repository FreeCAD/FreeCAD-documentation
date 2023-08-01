# Package Metadata/fr
## Introduction

A partir de la version 0.20 de FreeCAD, les extensions externes (ateliers, macros, et kits de préférences) peuvent être distribuées avec un fichier de métadonnées décrivant le contenu du package. Si le fichier \"package.xml\" est présent, il est lu par FreeCAD et son contenu est utilisé dans diverses parties de l\'interface utilisateur. Il est pour l\'instant facultatif pour les ateliers et les macros, et obligatoire pour les kits de préférences. Cette page documente le format de ce fichier de métadonnées. Le format (et le contenu de cette page Wiki) est basé sur [REP 149](https://ros.org/reps/rep-0149.html).



## Format général du fichier 

Ce document décrit actuellement la version 1 du format de fichier.

Le fichier de métadonnées doit être un document XML 1.0 valide et bien formé. Il doit s\'appeler \"package.xml\", et doit exister dans le répertoire de base de la branche principale du logiciel (comme spécifié par le [fichier .gitmodules des extensions de FreeCAD](https://github.com/FreeCAD/FreeCAD-addons/blob/master/.gitmodules)) dans son dépôt git. Seul le fichier package.xml de la branche principale est pris en compte par le gestionnaire des extensions. Toutes les balises XML comprises sont en minuscules, mais les balises non reconnues ne sont **pas** une erreur. La plupart des balises sont facultatives, et certaines ne s\'appliquent qu\'à certains types de contenu de paquet (par exemple, seuls les ateliers fournissent actuellement un élément \"classname\"). Les éléments inutiles ou non reconnus sont ignorés.

Tout chemin de fichier spécifié dans package.xml doit utiliser la barre oblique (\"/\") comme séparateur de répertoire : sur les systèmes qui attendent un séparateur différent pendant l\'exécution (par exemple Windows), FreeCAD convertira automatiquement vers le séparateur correct.



## Éléments de contenu 

### 

Le seul élément de haut niveau autorisé est , et le fichier ne peut contenir qu\'un seul élément . Immédiatement subordonnés à celui-ci se trouvent plusieurs éléments obligatoires ou facultatifs, définis ici. Aucune autre balise n\'est autorisée directement sous l\'élément .

    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">

La balise  est la balise unique de premier niveau dans un fichier package.xml. Toutes les autres balises sont imbriquées sous elle.



#### Attributs

-   format=\"NUMERO\" : Spécifier le format package.xml utilisé. Pour cette interface, vous devez spécifier format=\"1\".
-   xmlns=\"NAMESPACE\" : Spécifie l\'espace de noms XML pour ce paquet, et doit être inclus exactement comme indiqué ci-dessus, comme un lien vers <https://wiki.freecad.org/Package_Metadata>.



#### Balises enfant requises 

L\'élément  de niveau supérieur doit contenir au moins les balises suivantes :

-   [](#.3Cname.3E.md)
-   [](#.3Cversion.3E.md)
-   [](#.3Cdate.3E.md)
-   [](#.3Cdescription.3E.md)
-   [](#.3Cmaintainer.3E.md) (plusieurs, mais au moins un)
-   [](#.3Clicense.3E.md) (plusieurs, mais au moins un)
-   [](#.3Cicon.3E.md) (plusieurs, mais au moins un)
-   [](#.3Ccontent.3E.md) (élément conteneur pour les éléments de contenu du paquet)



#### Balises enfant facultatives 

-   [](#.3Curl.3E.md) (plusieurs)
-   [](#.3Cauthor.3E.md) (plusieurs)
-   [](#.3Cdepend.3E.md) (plusieurs)
-   [](#.3Cconflict.3E.md) (plusieurs)
-   [](#.3Creplace.3E.md) (plusieurs)
-   [](#.3Ctag.3E.md) (plusieurs)
-   [](#.3Cfreecadmin.3E.md)
-   [](#.3Cfreecadmax.3E.md)
-   [](#.3Cpythonmin.3E.md)

###  

OBLIGATOIRE

Le nom de ce paquet. Ne doit contenir que des caractères valides pour les noms de fichiers (les caractères non autorisés sont /\\?%\*:\|\"\<\> ).

###  

OBLIGATOIRE

Un numéro de version qui suit soit la [norme de versionnement sémantique 2.0](https://semver.org) (par exemple 1.0.2-beta), soit le [style CalVer](https://calver.org/) (par exemple 2021.12.08). Notez que vous ne pouvez pas inclure les deux types, et que le passage d\'un type à l\'autre n\'est pas pris en charge. En interne, le code n\'a aucune notion du type choisi, lors de la comparaison des versions, il effectue une simple comparaison numérique entre chaque composant numérique successif, quel que soit le type. Notez que ce champ ne peut pas être laissé vide, un numéro de version doit être attribué. Lorsque le gestionnaire d\'addons détecte une augmentation du numéro de version, il affiche l\'information \"mise à jour disponible\" aux utilisateurs.

###  

OBLIGATOIRE

La date de la version en cours, au format AAAA-MM-JJ ou AAAA.MM.JJ.

###  

OBLIGATOIRE

Une description textuelle concise (plusieurs phrases maximum) de ce paquet. Aucun balisage n\'est pris en charge.

###  

AU MOINS UN OBLIGATOIRE (plusieurs autorisés)

Le nom de la personne qui maintient le paquet. Tous les paquets nécessitent un mainteneur. Pour les paquets orphelins, voir ci-dessous.



#### Attributs 

-   email=\"name@domain.tld\" (obligatoire) : Adresse électronique du responsable.

Un paquet orphelin est un paquet qui n\'a pas de mainteneur attitré. Les paquets orphelins doivent utiliser les informations suivantes sur le mainteneur :

    <maintainer email="no-one@freecad.org">No current maintainer</maintainer>

###  

AU MOINS UN OBLIGATOIRE (plusieurs autorisés)

Identifiant court SPDX de la (des) licence(s) pour ce paquet, par exemple BSD-2-Clause, GPL-3, LGPL-2.1. Afin de faciliter la lecture par les machines, n\'incluez que l\'identifiant court SPDX de la licence (voir [le site SPDX](https://spdx.org/licenses/)). Pour les licences multiples, plusieurs balises distinctes doivent être utilisées. Un paquet aura plusieurs licences si les différents fichiers sources ont des licences différentes. Chaque licence présente dans les fichiers source doit avoir une balise  correspondante. Pour tout texte explicatif sur les mises en garde concernant les licences, veuillez utiliser la balise .

Les licences les plus utilisées :

-    `"Apache-2.0"`
    

-    `"BSD-2-Clause"`
    

-    `"BSD-3-Clause"`
    

-    `"BSL-1.0"`
    

-    `"GPL-2.0-or-later"`
    

-    `"GPL-3.0-or-later"`
    

-    `"LGPL-2.1-or-later"`
    

-    `"LGPL-3.0-or-later"`
    

-    `"MIT"`
    

-    `"MPL-1.1"`
    

-    `"CC0-1.0"`(Déclaration du domaine public)



#### Attributs 

-    `file<nowiki>=</nowiki>"FILE"`(facultatif) : un chemin relatif au fichier `package.xml` contenant le texte complet de la licence. De nombreuses licences exigent l\'inclusion du texte de la licence lors de la redistribution du logiciel. Par exemple, la licence Apache, version 2.0, stipule au paragraphe 4.1 : \"Vous devez remettre à tout autre destinataire de l\'œuvre ou des œuvres dérivées une copie de la présente licence\".

###  

OBLIGATOIRE

La balise  décrit le contenu réel du paquet. Elle n\'a pas d\'attributs, et contient un nombre quelconque d\'enfants. Ces enfants peuvent avoir des noms de balises arbitraires, dont seuls certains peuvent être reconnus par FreeCAD. FreeCAD supporte actuellement les éléments \"workbench\", \"macro\", et \"preferencepack\". Chaque enfant est ensuite défini récursivement par cette norme, contenant n\'importe quel ou tous les éléments autorisés pour le noeud racine . Par exemple :

    <content>
      <preferencepack>
        <name>Unicorn Sparkles Theme</name>
        <version>1.0.0</version>
        <url type="readme">https://github.com/chennes/FreeCAD-themes/blob/main/Unicorn%20Sparkles%20Theme/Readme.md</url>
        <icon>sparkles.svg</icon>
      </preferencepack>
    </content>

L\'existence d\'éléments  implique un ensemble de sous-dossiers, un pour chaque élément de contenu, nommé exactement comme le nom donné à l\'élément. Ainsi, pour l\'exemple ci-dessus, la structure des dossiers du paquet est la suivante :

    Package Directory/
      package.xml
      Unicorn Sparkles Theme/
        Unicorn Sparkles Theme.cfg
        sparkles.svg
        (the theme's other files)

Outre les autres éléments de , les éléments de contenu peuvent éventuellement fournir des informations dans les balises ,  et  (techniquement, celles-ci peuvent également être fournies à la balise racine , mais elles y sont généralement inutilisées).

**Note de rétrocompatibilité** : pour éviter de devoir restructurer les paquets antérieurs à cette norme de métadonnées, la balise facultative [](#.3Csubdirectory.3E.md) est autorisée à spécifier \"./\" comme sous-répertoire pour un élément de contenu, auquel cas aucun sous-répertoire n\'est nécessaire. Cela correspond au système pré-standard où un seul poste de travail était situé au sommet de la structure des répertoires.

####  

OBLIGATOIRE pour les ateliers

Le chemin d\'accès à un fichier d\'icône. S\'il s\'agit d\'une icône pour le paquet de premier niveau, ce chemin est relatif au fichier package.xml lui-même. Si l\'icône est un élément d\'un élément , le chemin est relatif au dossier du contenu. Le gestionnaire d\'addons affichera l\'icône de niveau supérieur comme l\'icône du paquetage global. Si aucune icône de niveau supérieur n\'est présente, la première icône de banc de travail spécifiée sera utilisée comme icône du paquet.

####  

Optionnel.

Normalement, un élément de contenu est supposé se trouver dans un sous-répertoire portant le même nom que l\'élément. Dans certains cas, cependant, il est utile de spécifier explicitement le sous-répertoire. Par exemple, de nombreuses macros peuvent se trouver dans un seul sous-répertoire, mais chacune a sa propre entrée dans le fichier package.xml. Cela fournit également un support de rétrocompatibilité pour les paquets antérieurs à la spécification du format de fichier package.xml, et qui ne suivent pas la structure de sous-répertoire attendue. Souvent, dans ces cas, un \"./\" est utilisé pour indiquer que l\'élément n\'est pas situé dans un sous-répertoire du tout.

####  

OBLIGATOIRE pour les ateliers

Pour les ateliers, le nom de la classe d\'entrée principale en Python. C\'est la classe que FreeCAD essaiera de charger au démarrage pour localiser l\'icône de l\'atelier, qui doit être définie comme une variable membre de la classe. Par exemple, si votre atelier définit la classe suivante (généralement dans InitGui.py) :


```python
class MyNewWB:
    Icon = "resources/icon.svg"
```

alors le fichier package.xml attend :

    <classname>MyNewWB</classname>

####  

Optionnel.

Fournis pour la convivialité d\'autres outils, un certain nombre d\'autres fichiers peuvent être répertoriés ici. Leur utilisation dépend du type de contenu. Dans un élément de contenu macro, chaque entrée de fichier est une macro unique et sera liée au répertoire d\'installation des macros de l\'utilisateur par le [Gestionnaire des extensions](Std_AddonMgr/fr.md).

###  

Plusieurs autorisés : le \"dépôt\" est obligatoire et le type \"readme\" est fortement recommandé.

Un URL (Uniform Resource Locator) pour le site web du paquet, le système de suivi des bogues, le dépôt des sources, le lien de téléchargement du zip, le fichier readme ou la documentation (comme spécifié par l\'attribut \"type\", voir ci-dessous).

Lorsque vous spécifiez le type \"readme\", un lien direct vers une version restituée du fichier README doit être fourni. Par exemple, sur GitHub, il s\'agit d\'un lien de type \"blob\" tel que \"<https://github.com/FreeCAD/FreeCAD-addons/blob/master/README.md>\", ou sur une instance GitLab, \"<https://gitlab.com/opensimproject/cfdof/-/blob/master/README.md>\" (notez le format d\'URL légèrement différent entre les deux).

C\'est une bonne idée d\'inclure des balises  pointant les utilisateurs vers les ressources en ligne de votre paquet. Il s\'agit généralement d\'une page wiki de wiki.freecad.org où les utilisateurs peuvent trouver et mettre à jour des informations sur le paquet, par exemple. Le gestionnaire d\'addons répertorie ces URL et fournit des liens cliquables vers celles-ci dans la description du paquet.



#### Attributs 

-   type=\"TYPE\" (obligatoire) : Le type doit être l\'un des identifiants suivants : \"website\", \"bugtracker\", \"repository\", \"readme\", \"documentation\" ou \"discussion\".
-   branch=\"BRANCH\" (obligatoire pour type=\"repository\") : Le nom de la branche à extraire pour obtenir ce paquet. Il s\'agit généralement du nom de votre branche de développement principale. Peut également spécifier tout autre type de référence git, par exemple une balise ou un commit spécifique.

###  

Multiple autorisé

Le nom d\'une personne qui est un auteur du paquet, comme reconnaissance de son travail et pour les questions.



#### Attributs 

-   email=\"name@domain.tld\" (facultatif) : Adresse électronique de l\'auteur.

###  

Multiple autorisé

Déclare une dépendance sur une autre extension de FreeCAD ou un atelier interne, ou un module en Python. La dépendance nommée est d\'abord vérifiée par rapport à la liste des extensions connues (par exemple ceux disponibles soit dans le dépôt git officiel des extensions de FreeCAD, soit dans un dépôt personnalisé spécifié par l\'utilisateur). La vérification porte sur le nom canonique de l\'extension. Si un fichier package.xml est présent pour cette extension, le nom est l\'élément  de ce package. Une correspondance exacte est requise. Si aucune correspondance n\'est trouvée, le nom est comparé à la liste des ateliers internes connus (installés et désinstallés). Enfin, si la dépendance nommée n\'a pas été localisée lors des deux étapes précédentes, elle est supposée être une dépendance du module en Python. Notez que toutes les fonctionnalités liées aux dépendances ne sont pas encore complètement implémentées.



#### Attributs 

Toutes les dépendances et relations peuvent restreindre leur applicabilité à des versions particulières. Un attribut peut être utilisé pour chaque opérateur de comparaison. Deux de ces attributs peuvent être utilisés ensemble pour décrire une gamme de versions.

-   version_lt=\"VERSION\" (facultatif) : la dépendance au paquet est limitée aux versions inférieures au numéro de version indiqué.
-   version_lte=\"VERSION\" (facultatif) : la dépendance au paquet est limitée aux versions inférieures ou égales au numéro de version indiqué.
-   version_eq=\"VERSION\" (facultatif) : la dépendance au paquet est restreinte à une version égale au numéro de version indiqué.
-   version_gte=\"VERSION\" (facultatif) : la dépendance au paquet est limitée aux versions supérieures ou égales au numéro de version indiqué.
-   version_gt=\"VERSION\" (facultatif) : la dépendance au paquet est limitée aux versions supérieures au numéro de version indiqué.
-   condition=\"CONDITION_EXPRESSION\" : chaque dépendance peut être conditionnée par une expression de condition. Si l\'expression de condition vaut \"true\", la dépendance est utilisée et considérée comme si elle n\'avait pas d\'attribut de condition. Si l\'expression conditionnelle vaut \"false\", la dépendance est ignorée et considérée comme si elle n\'existait pas. L\'expression doit être une expression FreeCAD valide (i.e. syntaxe en Python), et peut faire référence aux variables \"\$BuildVersionMajor\", \"\$BuildVersionMinor\", et \"\$BuildRevision\" représentant la version de FreeCAD en cours d\'exécution.
-   optional=\"true\|false\" : si \"optional\" est \"true\", la dépendance est traitée comme facultative lorsque l\'extension est installée à l\'aide du gestionnaire des extensions. En général, cela signifie qu\'un échec de l\'installation de la dépendance n\'empêche pas l\'installation de l\'extension, et l\'utilisateur peut être invité à dire s\'il veut l\'installer. Les versions de FreeCAD antérieures à 0.21 ne reconnaissent pas cet attribut et l\'ignorent.
-   type=\"automatic\|addon\|internal\|python\" : facultatif, la valeur par défaut est \"automatic\". Indique à quoi se réfère cette déclaration de dépendance. \"addon\" est pour les extensions externes, \"internal\" est pour les ateliers internes (par exemple \"arch\", \"sketcher\", etc.), et \"python\" indique une dépendance du paquetage Python. Les versions de FreeCAD antérieures à 0.21 n\'utilisent pas cet attribut, et \"automatic\" est toujours supposé.

###  

Multiple autorisé

Déclare un nom de paquet avec lequel ce paquet est en conflit. Ce paquet et le paquet en conflit ne doivent pas être installés en même temps.



#### Attributs 

Voir .

###  

Multiple autorisé

Déclare un nom de paquet que ce paquet est destiné à remplacer.



#### Attributs 

Voir .

###  

Une simple balise texte utilisée pour la catégorisation lors de l\'utilisation d\'un gestionnaire de paquets. Plusieurs éléments  peuvent être spécifiés.

###  

La version minimale de FreeCAD requise pour utiliser ce paquetage/élément, sous la forme d\'une chaîne sémantique version 2.0 au format MAJOR.MINOR.BUILD

###  

La version maximale de FreeCAD requise pour utiliser le paquetage/élément, sous la forme d\'une chaîne sémantique de la version 2.0 au format MAJOR.MINOR.BUILD.

###  

(Nouveau dans FreeCAD 0.21, ignoré par les versions précédentes). La version minimale requise de Python pour utiliser le package/élément, sous la forme d\'une chaîne sémantique version 2.0 au format MAJOR.MINOR. Le gestionnaire des extensions ne permettra pas l\'installation d\'une extension sur un système utilisant une version de Python antérieure à celle-ci. Seules les versions Python 3.x sont prises en charge. Bien que vous puissiez spécifier une version à trois composants, seul le numéro mineur est pris en compte lors de la vérification de la compatibilité.

## Validation

Pour valider votre fichier package.xml, vous pouvez activer le \"mode développeur\" dans le gestionnaire d\'addons : créez une variable booléenne appelée \"developerMode\" dans le groupe de paramètres \"Addons\" et définissez-la sur True : **Outils → Editer les paramètres... → BaseApp → Préférences → Addons → developerMode**. Lorsque le gestionnaire d\'addons a fini de lire la base de données des addons, il examine tous les fichiers package.xml disponibles à la recherche d\'erreurs.



## Guide rapide 

Pour un guide rapide sur la façon de créer un fichier package.xml de base et d\'ajouter un atelier au [Gestionnaire des extensions](Std_AddonMgr/fr.md) voir : [Ajouter un atelier au gestionnaire des extensions](Add_Workbench_to_Addon_Manager/fr.md).



## Exemples

Notez que les commentaires (le texte entre `&lt;&#33;--` et `--&gt;`) sont ignorés par l\'analyseur XML et ne sont pas une partie obligatoire du format de fichier. Ils sont fournis ici à titre d\'information et peuvent être omis du package.xml final si vous le souhaitez.

Un paquet simple réservé à l\'atelier (par exemple, pour ajouter un fichier de métadonnées à un paquet antérieur à ce format de métadonnées) :

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
      <name>Legacy Workbench</name> 
      <description>Text that the Addon Manager shows for the Addon. Any length, but remember that Addon Manager's compact view only shows the first sentence or so.</description>
      <version>1.0.1</version> 
      <date>2022-01-07</date> 
      <maintainer email="your_address@null.com">Your Name</maintainer>
      <license file="LICENSE">LGPL-2.1-or-later</license> 
      <url type="repository" branch="main">https://github.com/chennes/FreeCAD-Package</url> 
      <url type="readme">https://github.com/chennes/FreeCAD-Package/blob/main/README.md</url> 
      <icon>Resources/icons/PackageIcon.svg</icon> 

      <content>
        <workbench>
          <classname>MyLegacyWorkbench</classname> 
          <subdirectory>./</subdirectory>
        </workbench>
      </content>

    </package>

Un paquet complexe, à plusieurs composantes :

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
      <name>Example Package Format</name>
      <description>An example of the package.xml file format</description>
      <version>2022.01</version>
      <date>2022-01-07</date>
      <maintainer email="no-one@freecad.org">No Maintainer</maintainer>
      <license file="LICENSE">GPL-3.0-or-later</license>
      <url type="repository" branch="main">https://github.com/chennes/FreeCAD-Package</url>
      <icon>PackageIcon.svg</icon>

      <content>
        <preferencepack>
          <name>FreeCAD Classic Colors</name>
          <description>FreeCAD default colors for core app and included Mods.</description>
          <version>1.0.0</version>
          <tag>color</tag>
          <tag>stylesheet</tag>
        </preferencepack>
        <workbench>
          <name>Metadata Creation Workbench</name>
          <description>A set of tools to assist in creation of package.xml metadata files</description>
          <classname>MetadataCreationWorkbench</classname>
          <subdirectory>MCW</subdirectory>
          <icon>Resources/mcw.svg</icon>
          <tag>developers</tag>
          <version>0.9.0-alpha</version>
        </workbench>
        <macro>
          <name>Problem Solver 9000</name>
          <description>Deletes all emails in your inbox</description>
          <subdirectory>./</subdirectory>
          <file>PS9000.FCMacro</file>
        </macro>
      </content>

    </package>

Un paquet avec des dépendances :

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
      <name>Example with Dependencies</name>
      <description>An example of the package.xml file format</description>
      <version>1.0.1-beta3</version>
      <date>2022-01-07</date>
      <maintainer email="no-one@freecad.org">No Maintainer</maintainer>
      <license file="LICENSE">GPL-3.0-or-later</license>
      <url type="repository" branch="main">https://github.com/chennes/FreeCAD-Package</url>
      <icon>PackageIcon.svg</icon>

      <content>
        <workbench>
          <name>Metadata Creation Workbench</name>
          <description>A set of tools to assist in creation of package.xml metadata files</description>
          <classname>MetadataCreationWorkbench</classname>
          <subdirectory>MCW</subdirectory>
          <icon>Resources/mcw.svg</icon>
          <tag>developers</tag>

          <depend>FEM</depend>
          <depend version_gte="0.3.0">Curves workbench</depend>
          <depend version_gte="3.3" version_lt="4">Steel column</depend>

          
          <depend optional="true" type="python">markdown</depend>
          <depend type="addon">TabBar</depend>

          
          <replace>Metadata Creation Workbench Beta</replace>

          
          <conflict condition="$BuildRevision==24267">Do not use with build 24267</conflict> 

          
          <depend>matplotlib</depend>
          <depend>some_other_package</depend> 
        </workbench>
      </content>

    </package>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Package Metadata/fr
