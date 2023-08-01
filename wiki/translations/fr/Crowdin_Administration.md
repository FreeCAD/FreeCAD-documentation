# Crowdin Administration/fr
{{TOCright}}

## Rôles

-   Traducteur
    -   Possibilité de proposer et de voter sur les traductions dans une langue.
    -   Demander plus de contexte; demander de la clarté; signaler des erreurs dans la chaîne de caractères à traduire; contester une entrée de traduction en cours, etc.

-   Relecteur
    -   Gère les traductions que les traducteurs suggèrent et/ou votent. Le relecteur accepte/rejette alors la traduction.
    -   Une étape supplémentaire est nécessaire pour donner également l\'approbation finale de la chaîne de traduction. Parce que \'approuver\' une traduction nécessite de la relire et de la cocher, cela fournit une vérifiction \'Assurance qualité\'. Une fois qu\'une traduction est approuvée, elle marquera la chaîne en vert et ajoutera plus de progrès à la barre d\'état verte de la langue en cours de traduction. La barre de progression verte peut indiquer la \'\'qualité\' de la langue traduite. Cela permet également une flexibilité supplémentaire aux développeurs pour fusionner les traductions qui ont seulement été approuvées.
    -   Répondez aux questions des traducteurs dans l\'interface Crowdin. Par exemple, si plus de contexte est nécessaire; ou il y a une erreur dans la chaîne à traduire, ou une traduction qui a été acceptée ou approuvée est contestée etc \...
    -   Signalez aux développeurs tout problème pertinent nécessitant des modifications du code source, etc.

## Filtrer les chaînes de caractères 

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width:500px;">

Le filtrage des chaînes est une fonctionnalité utile pour les relecteurs et les gestionnaires. Il donne à la personne la possibilité de trier efficacement de nombreuses chaînes de traduction pour ne montrer, par exemple, que les chaînes marquées comme \"manquant d\'informations plus contextuelles\" ou \"chaîne source incorrecte\". Ce service fourni par les traducteurs pour FreeCAD fournit une couche supplémentaire de tests d\'assurance qualité. De nombreuses fautes de frappe, problèmes de grammaire et même des bogues peuvent être exposés via la vérification des chaînes de traduction. Et donc les utilisateurs marquent ces chaînes problématiques pour que nous puissions y répondre et éventuellement les résoudre.

## Raccourcis clavier 

<img alt="" src=images/Crowdin_keyboard_shortcuts.png  style="width:300px;">

L\'utilisation de raccourcis clavier est une astuce majeure pour gagner du temps et gagner en efficacité. Cela vaut la peine d\'apprendre si vous êtes traducteur, relecteur ou gestionnaire. Il est possible de voir la liste des raccourcis clavier en appuyant sur l'icône du clavier dans la partie supérieure droite de l'interface utilisateur Crowdin.

**Remarque importante:** Veillez à ne pas introduire d\'erreurs dans les chaînes de traduction générées par des pressions de touches non fiables qui étaient censées être un raccourci clavier.

**Raccourcis fréquemment utilisés:**

-   Copier la traduction source : **Alt**+**C**
-   Enregistrer la traduction : **Ctrl**+**Entrée**
-   Approuver la traduction : **Alt**+**L** (utile pour les correcteurs)

## Correction des problèmes de traduction 

Si vous remarquez une chaîne dans l\'interface utilisateur de FreeCAD qui n\'est pas traduite, faites ce qui suit :

1.  Si vous n\'êtes pas sûr de l\'atelier auquel la chaîne appartient, localisez-la d\'abord dans le code source de FreeCAD. Sous Linux vous pouvez utiliser {{Incode|grep -r "English text" *}}.
2.  Par exemple, si la chaîne est {{Incode|"Solver Calculix Standard"}} vous trouverez ce fichier : **src/Mod/Fem/femcommands/commands.py**, et vous saurez que la chaîne appartient à l\'atelier FEM.
3.  Recherchez maintenant cette chaîne sur Crowdin. Si votre langue est le français, visitez <https://crowdin.com/project/freecad/fr>, allez dans l\'atelier FEM, et vérifiez si elle est là et traduite.
4.  Il y a deux possibilités :
    1.  La chaîne de caractères n\'est pas sur Crowdin parce qu\'elle n\'a pas été récupérée par le script qui rassemble les chaînes de caractères du code source de FreeCAD et les empaquette dans des fichiers **.ts**. Il peut y avoir deux raisons à cela :
        -   La chaîne de caractères n\'est pas correctement traitée par le code {{Incode|translate()}} (ou le code {{Incode|QT_TRANSLATE_NOOP()}} pour les cas particuliers comme les noms de commandes), cela signifie qu\'il y a un problème qui doit être résolu dans le code source.
        -   Tout semble normal, mais le script de collecte a un problème avec cette chaîne spécifique, ce qui peut arriver car il a de nombreux bugs.

        1.  La chaîne est sur Crowdin. Il y a plusieurs possibilités alors :

        -   Il se peut que les dernières chaînes de Crowdin n\'aient pas encore été fusionnées. Vous pouvez vérifier si c\'est le cas en recherchant la chaîne (voir ci-dessus), et vérifier si elle apparaît dans les fichiers **.ts** traduits. Dans notre exemple, {{Incode|"Solver Calculix Standard"}} se trouverait alors dans **src/Mod/Fem/Gui/Resources/translations/Fem_fr.ts**. Cela indique que la chaîne de caractères traduite se trouve dans les sources de FreeCAD et que tout devrait bien se passer dans la prochaine version.
        -   Si la chaîne est toujours manquante dans la prochaine version, le problème est plus complexe et nous devrons faire un peu de débogage :
            1.  Vérifier dans le fichier source si la chaîne originale est traitée par {{Incode|translate()}} ou {{Incode|QT_TRANSLATE_NOOP()}}.
            2.  Vérifier que le contexte correspond à ce qui est sur Crowdin.
            3.  Dans le cas de {{Incode|QT_TRANSLATE_NOOP()}}, il y a plusieurs cas particuliers. Pour les commandes, le contexte doit être le nom exact de la commande, le même que celui utilisé dans {{Incode|FreeCADGui.runCommand()}}. Pour les propriétés, il doit être {{Incode|"App::Property"}}. Pour les noms des menus et des barres d\'outils, il doit être {{Incode|"Workbench"}}.

## Liens

-   [Localisation](Localisation/fr.md)
-   [Scripts pour Crowdin](Crowdin_Scripts/fr.md)
-   [Processus de mise à jour](Release_process.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Administration](Category_Administration.md) > Crowdin Administration/fr
