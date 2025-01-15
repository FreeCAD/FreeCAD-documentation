# Localisation/fr
## Présentation

La **localisation** est en général le processus qui consiste à doter un logiciel d\'une interface utilisateur multilingue. Dans FreeCAD, vous pouvez définir la langue par le menu **Édition → Préférences → Général → Onglet Général → Langue**. FreeCAD utilise [Qt](https://fr.wikipedia.org/wiki/Qt) pour activer la prise en charge de plusieurs langues. Sur les systèmes Unix/Linux, FreeCAD utilise les paramètres régionaux actuels de votre système par défaut.



## Aider à la traduction de FreeCAD 

Une des choses importantes que les utilisateurs peuvent apporter à FreeCAD (s'ils ne possèdent pas de compétences en programmation, par exemple) est d'aider à traduire ses différents aspects (code source, wiki, site web, documentation, etc.) dans une autre langue. Voici les moyens de le faire.



## Traduire le code source de FreeCAD 

FreeCAD utilise un système de traduction en ligne tiers collaboratif appelé [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

Il s\'agit d\'un logiciel propriétaire mais gratuit pour les projets [FOSS](https://fr.wikipedia.org/wiki/Free/Libre_Open_Source_Software). Vous trouverez ci-dessous des instructions sur son utilisation :

-   Aller à la page du [projet de traduction de FreeCAD sur Crowdin](http://crowdin.net/project/freecad)
-   Se connecter en créant un nouveau profil, ou en utilisant un compte tiers, comme votre adresse (GitHub, GitLab, GMail etc\...)
-   Cliquer sur la langue à traduire
-   Commencer la traduction en cliquant sur ​​le bouton **Translate** à côté d\'un des fichiers. Par exemple, **FreeCAD.ts** contient les chaînes de texte pour l\'interface principale de FreeCAD.
-   Il est possible de voter pour les traductions existantes ou de créer une nouvelle traduction.

{{Message|Si vous prenez une part active dans la traduction de FreeCAD, et que vous voulez être informé avant le lancement de la prochaine version, afin d'avoir le temps de revoir votre traduction, inscrivez vous à une des équipes de traduction de FreeCAD sur Crowdin.}}


**Remarque :**

les détails sur l\'utilisation de Crowdin peuvent être trouvés sur la page [Administration de Crowdin](Crowdin_Administration/fr.md).



## Traduction des ateliers externes 

Visitez [Traduction d\'un atelier externe](Translating_an_external_workbench/fr.md).



## Préférences de FreeCAD pour les traducteurs 

A partir de FreeCAD 0.20, les variables suivantes peuvent être ajoutées manuellement à la section BaseApp/Préférences/Général du fichier user.cfg pour aider au développement de nouvelles traductions :

**AdditionalLanguageDomainEntries** - pour ajouter des langues entièrement nouvelles à FreeCAD qui ne sont pas encore prises en charge par le code source, vous pouvez utiliser cette préférence d\'utilisateur pour ajouter à la liste des langues disponibles. Le format des langues est \"Nom de la langue\"=\"code\", par exemple :

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - ajoute un répertoire supplémentaire pour que FreeCAD recherche les fichiers \*.qm. Cet emplacement aura la priorité sur \$userAppDataDir/translations et \$resourceDir/translations. Par exemple :

    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>



## Traduire le wiki FreeCAD 

Ce wiki héberge un contenu volumineux, dont l\'essentiel sert à produire le manuel. Vous pouvez naviguer dans la documentation à partir de la [page principale](Main_Page/fr.md) ou consulter la [table des matières](Online_Help_Toc/fr.md) du guide de l\'utilisateur.

Pour pouvoir traduire le wiki, vous devez bien sûr [obtenir les droits d\'édition au wiki](Frequently_asked_questions/fr#Comment_puis-je_obtenir_les_droits_pour_modifier_le_wiki_.3F.md).

Il est recommandé d\'avoir des connaissances de base du formatage de style wiki et des directives générales du wiki FreeCAD, car vous devrez ajuster le code de balisage lors des traductions. Vous trouverez cette information sur la page [Les pages Wiki](WikiPages/fr.md).



### Extension de traduction Mediawiki 

Après le départ du wiki de SourceForge, [Yorik](User_Yorik.md) a installé un [plugin de traduction MediaWiki](http://www.mediawiki.org/wiki/Help:Extension:Translate/fr) qui facilite les traductions de pages. Les avantages de l\'extension de traduction sont que le titre de la page peut maintenant être traduit, qu\'il garde une trace des traductions, qu\'il informe si la page d\'origine a été mise à jour et qu\'il maintient la synchronisation des traductions avec la page anglaise d\'origine.

L\'outil est documenté dans [MediaWiki Traduire](http://www.mediawiki.org/wiki/Help:Extension:Translate/fr) et fait parti de l\'[MediaWiki offre groupée d\'extension linguistique](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

Pour commencer rapidement la préparation d\'une page pour la traduction et activer le plugin, veuillez lire l\'[Exemple de traduction de page](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr). Une paire de balises doit entourer la page entière pour activer le système de traduction :

    &lt;translate&gt; ... &lt;/translate&gt;

La page doit également être marquée pour la traduction.

Pour voir un exemple de comment l\'outil de traduction fonctionne, vous pouvez visiter la [page principale](Main_Page/fr.md). Vous verrez qu\'une barre de menu de langues est automatiquement générée en haut de page. Cliquez par exemple sur le lien *français* et vous serez redirigé sur [Main_Page/fr](Main_Page/fr.md). Juste sous le titre, vous pourrez lire  (XX étant le pourcentage de traduction réalisé). Cliquez sur le lien \"Traduire\" pour lancer l\'utilitaire de traduction pour mettre à jour, corriger ou revoir une traduction existante.

Si vous vous rendez sur la [page principale](Main_Page/fr.md), vous remarquerez que vous ne pouvez plus modifier la page directement en cliquant sur les balises \[Edit\], et que le lien supérieur \"Modifier\" a été remplacé par le lien \"Traduire\" qui ouvre l\'utilitaire de traduction.

Lors de l\'ajout de nouveau contenu, la page anglaise devrait être créée en premier, puis traduite dans une autre langue. Si vous désirez changer ou ajouter du contenu dans une page, la modification doit en premier se faire dans la page anglaise.

Si vous ne savez pas comment procéder, n\'hésitez pas à demander de l\'aide dans le sous-forum [Development → Wiki](https://forum.freecadweb.org/viewforum.php?f=21) ou dans le [sous-forum français](https://forum.freecadweb.org/viewforum.php?f=12).



### Remarques importantes 

Chaque utilisateur du wiki disposant des autorisations \"Éditeur\" peut lancer l\'utilitaire de traduction pour écrire, enregistrer et réviser les traductions.

Cependant, seuls les utilisateurs disposant des autorisations \"Administrateur\" peuvent marquer des pages pour traduction. Une page qui n\'est pas marquée pour la traduction n\'utilisera pas l\'extension de traduction et ne sera pas correctement synchronisée avec les informations en anglais.

La barre latérale gauche est également traduisible, mais seuls les administrateurs peuvent modifier cet élément du site. Veuillez suivre les instructions dédiées sur la page [Barre latérale locale](Localisation_Sidebar/fr.md).

La première fois que vous basculez une page vers le nouveau système de traduction, toutes les anciennes traductions \"manuelles\" sont perdues. Pour récupérer une traduction, vous devez enregistrer une copie hors ligne de l\'ancien texte avant le changement. Vous pouvez ensuite utiliser cet ancien texte traduit pour renseigner les unités de traduction du nouveau système. Vous pouvez également ouvrir une version antérieure de l\'historique et récupérer l\'ancien texte de cette manière. Cela doit être fait pour chaque langue ayant une page traduite.



### Traduire la documentation de FreeCAD 

Conformément au consensus général, la page de référence dans le wiki est la page anglaise, qui devrait être créée en premier. Si vous souhaitez modifier ou ajouter du contenu à une page, vous devez d\'abord le faire sur la page anglaise, puis reporter la modification sur la page traduite une fois la mise à jour terminée.



### Anciennes instructions de traduction 

++
| Ces instructions sont pour l\'historique seulement. Les traductions doivent utiliser le nouveau système avec [Traduire le wiki FreeCAD](#Traduire_le_wiki_FreeCAD.md) décrit ci-dessus.                                                                                                                                                                                                                                                                                                      |
++
| La première étape consiste donc à **vérifier si la traduction manuelle a déjà été commencée pour votre langue** (regardez dans la barre latérale gauche, sous \"manuel\").                                                                                                                                                                                                                                                                                                                           |
| Sinon, rendez-vous sur le [forum](http://forum.freecadweb.org/) et dites que vous souhaitez commencer une nouvelle traduction, nous créerons la configuration de base de la langue sur laquelle vous souhaitez travailler.                                                                                                                                                                                                                                                                           |
| Vous devez alors [obtenir l\'autorisation de modification du wiki](Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki.3F.md).                                                                                                                                                                                                                                                                                                                                              |
| Si votre langue est déjà listée, voyez quelles pages n\'ont toujours pas de traduction (elles seront listées en rouge). La technique est simple: **allez dans une page rouge, copiez/collez le contenu de la page anglaise correspondante et commencez à traduire**.                                                                                                                                                                                                                                 |
| N\'oubliez pas d\'inclure tous les tags et modèles de la page anglaise d\'origine. Certains de ces modèles auront un équivalent dans votre langue (par exemple, il existe un modèle Docnav français appelé Docnav/fr). Vous devez utiliser **une barre oblique et votre code de langue** dans presque tous les liens. Consultez d\'autres pages déjà traduites pour voir comment elles l\'ont fait.                                                                                                  |
| Ajoutez une barre oblique et votre code de langue dans les catégories, comme \[\[Category:Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                             |
| Si vous avez des doutes, dirigez-vous vers les forums et demandez aux gens de vérifier ce que vous avez fait et vous dire si c\'est bien fait ou non.                                                                                                                                                                                                                                                                                                                                                |
| Quatre modèles sont couramment utilisés dans les pages de manuel. Ces 4 modèles ont des versions localisées (Modèle: Docnav/fr, Modèle: fr, etc \...)                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -   [Template:GuiCommand/fr](Template:GuiCommand/fr.md) : est le bloc d\'informations de la commande Gui en haut à droite de la documentation de la commande.                                                                                                                                                                                                                                                                                                                                |
| -   [Template:Docnav/fr](Template:Docnav/fr.md) : c\'est la barre de navigation au bas des pages, montrant les pages précédentes et suivantes.                                                                                                                                                                                                                                                                                                                                               |
| -   [Template:Userdocnavi/fr](Template:Userdocnavi/fr.md) : donne des liens directs vers les pages de base principales.                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Page Naming Convention**                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Veuillez noter que, en raison des limitations de l\'implémentation du moteur MediaWiki par Sourceforge, nous exigeons que vos pages conservent toutes le nom de leur homologue anglais d\'origine, en ajoutant une barre oblique et votre code de langue. Par exemple, la page traduite pour À propos de FreeCAD devrait être About FreeCAD/es pour l'espagnol, About FreeCAD/pl pour le polonais, etc. saura à quoi servent ces pages. Cela facilitera la maintenance et évitera les pages perdues. |
| Si vous souhaitez que le modèle Docnav affiche les pages liées dans votre langue, vous pouvez utiliser les **pages de redirection**. Elles sont essentiellement des liens de raccourci vers la page réelle. Voici un exemple avec la page française de About FreeCAD.                                                                                                                                                                                                                                |
| \* La page About_FreeCAD/fr est la page avec le contenu                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -   La page About_FreeCAD contient ce code:                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|  #REDIRECT [[About_FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -   Dans la page About FreeCAD/fr, le code Docnav ressemblera à ceci :                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| {{docnav/fr|[Aide en ligne](Online_Help_Startpage/fr.md)|[Fonctionnalités](Feature_list/fr.md)}}                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| La page \"Aide en ligne\" redirige vers l\'aide en ligne Startpage/fr et la page \"Fonctionnalités\" redirige Feature_list/fr.                                                                                                                                                                                                                                                                                                                                                                       |
++



## Traduire le site web de FreeCAD 

La traduction du site web de FreeCAD est maintenant effectuée par le biais de [Crowdin](https://crowdin.com/translate/freecad/561/en-en). Le fichier est nommé **homepage.po**.



## Développement - Comment ajouter une localisation 

Cette section est destinée aux développeurs qui souhaitent ajouter une localisation dans leur code.



### Préparer vos modules maîtres/Freecad pour la traduction 

Voici les parties du processus de traduction de FreeCAD :

-   extraire les chaînes de texte du code source dans des fichiers \*.ts
-   télécharger les fichiers \*.ts dans le [Crowdin FreeCAD](http://crowdin.net/project/freecad).
-   traduire les chaînes dans Crowdin
-   extraire les nouveau fichiers ou fichiers modifiés \*.ts de Crowdin
-   convertir les fichiers \*.ts en fichiers \*.qm et mettre à jour le fichier \*.qrc de chaque module
-   mettre à jour la branche maître de FreeCAD

Toutes les étapes listées ci-dessus sont exécutées par des \"scripts de traduction\" qui sont lancés périodiquement par un administrateur.

Préparer votre module à la traduction est très facile. Tout d\'abord, créer un répertoire \"translations\" dans **myModule/Gui/Resources**, puis ouvrir un terminal (ou l\'équivalent Windows/OSX) dans votre répertoire \"translations\", et saisir la commande suivante : 
```pythonlupdate -ts myModule.ts```

Ceci crée un fichier de traduction vide. Une fois cette tâche complétée, s\'assurer que les scripts de traduction sont mis à jour comme dans cette [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).

La suite se fait automatiquement, en ce qui concerne le développeur. L\'administrateur fera l\'extraction des chaînes de texte, les traducteurs les traduiront, puis l\'administrateur extraira les traductions et mettra à jour la branche FreeCAD/master.



### Préparer votre module de tierce partie ou macro pour la traduction 

Les modules de tierce partie ou macros sont traduits de façon similaire, mais vous devez vous charger d\'une partie du travail. Cette [discussion sur le forum](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) (en anglais) décrit les détails.

Mise à jour : voir [Traduction d\'un atelier externe](Translating_an_external_workbench/fr.md)



## Automatiser les mises à jour de translations Crowdin 

Actuellement, les mainteneurs de FreeCAD utilisent l'API Crowdin via les [scripts pour Crowdin](Crowdin_Scripts/fr.md) pour extraire et transférer les traductions vers Crowdin, puis vers le dépôt Github. L\'API Crowdin donne aux responsables de FreeCAD la possibilité d\'automatiser certains aspects du flux de traduction du projet. Pour plus d\'informations, reportez-vous à la [documentation de l\'API Crowdin](https://support.crowdin.com/api/api-integration-setup/).



## Pages en relation 

-   [Administration de Crowdin](Crowdin_Administration/fr.md)
-   [Scripts pour Crowdin](Crowdin_Scripts/fr.md)



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour obtenir un dictionnaire des langues prises en charge par l\'interface FreeCAD, utilisez la méthode `supportedLocales` du module `FreeCADGui`.


```python
locales = FreeCADGui.supportedLocales()
```

Après l\'exécution, `locales` contiendra :


```python
{'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'German': 'de', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es-ES', 'Swedish': 'sv-SE', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
```

Pour obtenir la langue de l\'interface en cours, utilisez la méthode `getLocale` du même module :


```python
locale = FreeCADGui.getLocale()
```

Si la langue utilisée est l\'anglais, `locale` contiendra :


```python
'English'
```

Pour obtenir le [code de la langue](https://support.crowdin.com/api/language-codes/) correspondant, vous pouvez utiliser :


```python
locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
```

Si la langue utilisée est l\'anglais, le résultat sera le suivant :


```python
'en'
```

Pour définir la langue de l\'interface utilisée, utilisez la méthode `setLocale` du même module. Vous pouvez spécifier la langue ou le code de la langue :


```python
FreeCADGui.setLocale('Russian')
FreeCADGui.setLocale('ru')
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/fr
