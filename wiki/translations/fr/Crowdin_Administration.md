# Crowdin Administration/fr



## Rôles

-   Traducteur
    -   Possibilité de proposer et de voter sur les traductions dans une langue.
    -   Demander plus de contexte; demander de la clarté; signaler des erreurs dans la chaîne de caractères à traduire; contester une entrée de traduction en cours, etc.

-   Relecteur
    -   Gère les traductions que les traducteurs suggèrent et/ou votent. Le relecteur accepte/rejette alors la traduction.
    -   Une étape supplémentaire est nécessaire pour donner également l\'approbation finale de la chaîne de traduction. Parce que \'approuver\' une traduction nécessite de la relire et de la cocher, cela fournit une vérifiction \'Assurance qualité\'. Une fois qu\'une traduction est approuvée, elle marquera la chaîne en vert et ajoutera plus de progrès à la barre d\'état verte de la langue en cours de traduction. La barre de progression verte peut indiquer la \'\'qualité\' de la langue traduite. Cela permet également une flexibilité supplémentaire aux développeurs pour fusionner les traductions qui ont seulement été approuvées.
    -   Répondez aux questions des traducteurs dans l\'interface Crowdin. Par exemple, si plus de contexte est nécessaire; ou il y a une erreur dans la chaîne à traduire, ou une traduction qui a été acceptée ou approuvée est contestée etc \...
    -   Signalez aux développeurs tout problème pertinent nécessitant des modifications du code source, etc.

### Filtering Strings 

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width:300px;"> Le filtrage des chaînes est une fonctionnalité utile pour les relecteurs et les gestionnaires. Il donne à la personne la possibilité de trier efficacement de nombreuses chaînes de traduction pour ne montrer, par exemple, que les chaînes marquées comme \"manquant d\'informations plus contextuelles\" ou \"chaîne source incorrecte\". Ce service fourni par les traducteurs pour FreeCAD fournit une couche supplémentaire de tests d\'assurance qualité. De nombreuses fautes de frappe, problèmes de grammaire et même des bogues peuvent être exposés via la vérification des chaînes de traduction. Et donc les utilisateurs marquent ces chaînes problématiques pour que nous puissions y répondre et éventuellement les résoudre.

------------------------------------------------------------------------

### Raccourcis clavier 

![](images/Crowdin_keyboard_shortcuts.png ) L\'utilisation de raccourcis clavier est une astuce majeure pour gagner du temps et gagner en efficacité. Cela vaut la peine d\'apprendre si vous êtes traducteur, relecteur ou gestionnaire. Il est possible de voir la liste des raccourcis clavier en appuyant sur l'icône du clavier dans la partie supérieure droite de l'interface utilisateur Crowdin.

**Remarque importante:** Veillez à ne pas introduire d\'erreurs dans les chaînes de traduction générées par des pressions de touches non fiables qui étaient censées être un raccourci clavier.

#### Raccourcis fréquemment utilisés 

-   Copier la traduction source: **Alt**+**C**
-   Enregistrer la traduction: **Ctrl**+**Enter**
-   Approuver la traduction: **Alt**+**L** (pertinent pour les relecteurs)

### Pages pertinentes 

-   [Localisation](Localisation/fr.md)
-   [Crowdin Scripts](Crowdin_Scripts/fr.md)
-   [Processus de mise à jour](Release_process/fr.md)




[Category:Administration](Category:Administration.md)
