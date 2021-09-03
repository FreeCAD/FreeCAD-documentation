





{{TOCright}}

## Vue d'ensemble {#vue_densemble}

La **localisation** en général, est le processus de fourniture d\'un logiciel avec une interface utilisateur en plusieurs langues. Dans FreeCAD vous pouvez définir la langue d\'interface utilisateur dans le menu {{MenuCommand|Édition → Préférences → Général → Onglet Général → Langue}}. FreeCAD utilise [Qt](wikipedia:fr:Qt.md) pour activer le support de plusieurs langues. Sur les systèmes Unix/Linux, FreeCAD utilise les paramètres régionaux actuels de votre système par défaut.

## Aider à la traduction de FreeCAD {#aider_à_la_traduction_de_freecad}

Une des choses importantes que les utilisateurs peuvent apporter à FreeCAD (s'ils ne possèdent pas de compétences en programmation, par exemple) est d'aider à traduire ses différents aspects (code source, wiki, site Web, documentation, etc.) dans une autre langue. Voici les moyens de le faire.

## Traduire le code source de FreeCAD {#traduire_le_code_source_de_freecad}

FreeCAD utilise un système de traduction en ligne tiers collaboratif appelé [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

Il s\'agit d\'un logiciel propriétaire mais gratuit pour les projets FOSS. Vous trouverez ci-dessous des instructions sur son utilisation :

-   Aller à la page du [projet de traduction de FreeCAD sur Crowdin](http://crowdin.net/project/freecad) ;
-   Connectez-vous en créant un nouveau profil, ou en utilisant un compte tiers, comme votre adresse (GitHub, GitLab, GMail etc\...) ;
-   Cliquez sur la langue que vous souhaitez traduire ;
-   Commencez la traduction en cliquant sur ​​le bouton **Translate** à côté d\'un des fichiers. Par exemple, {{FileName|FreeCAD.ts}} contient les chaînes de texte pour l\'interface principale de FreeCAD ;
-   Vous pouvez voter pour les traductions existantes, ou créer une nouvelle traduction.

{{Message|Si vous prenez une part active dans la traduction de FreeCAD, et que vous voulez être informé avant le lancement de la prochaine version, afin d'avoir le temps de revoir votre traduction, veuillez s'il vous plaît vous inscrire à une des équipes de traduction de FreeCAD sur Crowdin.}}


**Remarque :**

les détails sur l\'utilisation de crowdin peuvent être trouvés sur la page [Administration de Crowdin](Crowdin_Administration/fr.md).

## Traduction des ateliers externes {#traduction_des_ateliers_externes}

Visitez [Traduction d\'un atelier externe](Translating_an_external_workbench/fr.md).

## Traduire le wiki FreeCAD {#traduire_le_wiki_freecad}

Ce wiki héberge un contenu volumineux, dont l\'essentiel sert à produire le manuel. Vous pouvez naviguer dans la documentation à partir de la [Page principale](Main_Page/fr.md), ou consulter la [table des matières](Online_Help_Toc/fr.md) du guide utilisateur.

Pour pouvoir traduire le wiki, vous devez bien sûr [obtenir les droits d\'édition au wiki](Frequently_asked_questions/fr#Comment_puis-je_obtenir_les_droits_pour_modifier_le_wiki_.3F.md).

Il est recommandé d\'avoir des connaissances de base du formatage de style wiki et des directives générales du wiki FreeCAD, car vous devrez ajuster le code de balisage lors des traductions. Vous trouverez cette information sur la page [Les pages Wiki](WikiPages/fr.md).

### Extension de traduction Mediawiki {#extension_de_traduction_mediawiki}

Après le départ du wiki de SourceForge, [Yorik](User:Yorik.md) a installé un [plugin de traduction MediaWiki](http://www.mediawiki.org/wiki/Help:Extension:Translate/fr) qui facilite les traductions de pages. Les avantages de l\'extension de traduction sont que le titre de la page peut maintenant être traduit, qu\'il garde une trace des traductions, qu\'il informe si la page d\'origine a été mise à jour et qu\'il maintient la synchronisation des traductions avec la page anglaise d\'origine.

L\'outil est documenté dans [MediaWiki Traduire](http://www.mediawiki.org/wiki/Help:Extension:Translate/fr), et fait partie du [MediaWiki Language Extension Bundle](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

Pour commencer rapidement la préparation d\'une page pour la traduction et activer le plugin, veuillez lire l\'[Exemple de traduction de page](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr). Essentiellement, une paire de

    &lt;translate&gt; ... &lt;/translate&gt;

balises doit entourer la page entière pour activer le système de traduction, et la page doit être marquée pour traduction.

Pour voir un exemple de comment l\'outil de traduction fonctionne, vous pouvez visiter la [Page principale](Main_Page/fr.md). Vous verrez qu\'une barre de menu de langues est automatiquement générée en haut de page. Cliquez par exemple sur le lien *français* et vous serez redirigé sur [Main\_Page/fr](Main_Page/fr.md). Juste sous le titre, vous pourrez lire  (XX étant le pourcentage de traduction réalisé). Cliquez sur le lien \"Traduire\" pour lancer l\'utilitaire de traduction pour mettre à jour, corriger ou revoir une traduction existante.

Si vous allez sur [WIKI : Page principale](Main_Page/fr.md), vous remarquerez que vous ne pouvez plus \"éditer\" directement une page une fois qu\'elle a été marquée pour \"traduction\". Vous devez passer par l\'outil de traduction.

Lors de l\'ajout de nouveau contenu, la page anglaise devrait être créée en premier, puis traduite dans une autre langue. Si vous désirez changer ou ajouter du contenu dans une page, la modification doit en premier se faire dans la page anglaise.

Si vous ne savez pas comment procéder, n\'hésitez pas à demander de l\'aide dans le sous-forum [Development → Wiki](https://forum.freecadweb.org/viewforum.php?f=21) ou dans le [sous-forum français](https://forum.freecadweb.org/viewforum.php?f=12).

### Remarques importantes {#remarques_importantes}

Chaque utilisateur du wiki disposant des autorisations \"Éditeur\" peut lancer l\'utilitaire de traduction pour écrire, enregistrer et réviser les traductions.

Cependant, seuls les utilisateurs disposant des autorisations \"Administrateur\" peuvent marquer des pages pour traduction. Une page qui n\'est pas marquée pour la traduction n\'utilisera pas l\'extension de traduction et ne sera pas correctement synchronisée avec les informations en anglais.

La barre latérale gauche est également traduisible, mais seuls les administrateurs peuvent modifier cet élément du site. Veuillez suivre les instructions dédiées sur la page [Barre latérale locale](Localisation_Sidebar/fr.md).

La première fois que vous basculez une page vers le nouveau système de traduction, toutes les anciennes traductions \"manuelles\" sont perdues. Pour récupérer une traduction, vous devez enregistrer une copie hors ligne de l\'ancien texte avant le changement. Vous pouvez ensuite utiliser cet ancien texte traduit pour renseigner les unités de traduction du nouveau système. Vous pouvez également ouvrir une version antérieure de l\'historique et récupérer l\'ancien texte de cette manière. Cela doit être fait pour chaque langue ayant une page traduite.

### Traduire la documentation de FreeCAD {#traduire_la_documentation_de_freecad}

Conformément au consensus général, la page de référence dans le wiki est la page anglaise, qui devrait être créée en premier. Si vous souhaitez modifier ou ajouter du contenu à une page, vous devez d\'abord le faire sur la page anglaise, puis reporter la modification sur la page traduite une fois la mise à jour terminée.

### Anciennes instructions de traduction {#anciennes_instructions_de_traduction}

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ces instructions sont pour l\'historique seulement. Les traductions doivent utiliser le nouveau système avec [Mediawiki Extension de traduction](#Mediawiki_Extension_de_traduction.md) décrite ci-dessus.                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
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
| \* La page About\_FreeCAD/fr est la page avec le contenu                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -   La page About\_FreeCAD contient ce code:                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|  #REDIRECT [[About_FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -   Dans la page About FreeCAD/fr, le code Docnav ressemblera à ceci :                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| {{docnav/fr|[Bienvenue dans l'aide en ligne de FreeCAD](Online_Help_Startpage/fr.md)|[Fonctionnalités](Feature_list/fr.md)}}                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| La page \"Bienvenue sur l\'aide en ligne\" redirige vers l\'aide en ligne Startpage/fr et la page \"Fonctionnalités\" redirige Feature\_list/fr.                                                                                                                                                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Traduire le site Web FreeCAD {#traduire_le_site_web_freecad}

La traduction du site Web FreeCAD est maintenant effectuée par le biais de [Crowdin](https://crowdin.com/translate/freecad/561/en-en). Le fichier est nommé {{FileName|homepage.po}}.

## Développement - Comment ajouter une localisation {#développement___comment_ajouter_une_localisation}

Cette section est destinée aux développeurs qui souhaitent ajouter la localisation dans leur code.

### Préparer vos modules maîtres/Freecad pour la traduction {#préparer_vos_modules_maîtresfreecad_pour_la_traduction}

Voici les parties du processus de traduction de FreeCAD :

-   extraire les chaînes de texte du code source dans des fichiers \*.ts
-   télécharger les fichiers \*.ts dans [le Crowdin FreeCAD](http://crowdin.net/project/freecad).
-   traduire les chaînes dans Crowdin
-   extraire les nouveau fichiers ou fichiers modifiés \*.ts de Crowdin
-   convertir les fichiers \*.ts en fichiers \*.qm et mettre à jour le fichier \*.qrc de chaque module
-   mettre à jour la branche master de FreeCAD

Toutes les étapes listées ci-dessus sont exécutées par des \"scripts de traduction\" qui sont lancés périodiquement par un administrateur.

Préparer votre module à la traduction est très facile. D\'abord, assurez-vous de créer un répertoire \"translations\" dans {{FileName|myModule/Gui/Resources}}. Puis ouvrez une fenêtre de terminal (ou l\'équivalent Windows/OSX) dans votre répertoire \"translations\", et saisissez la commande suivante : 
```pythonlupdate -ts myModule.ts```

Ceci crée un fichier de traduction vide. Une fois cette tâche complétée, vous devez vous assurer que les scripts de traduction sont mis à jour comme dans cette [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).

La suite se fait automatiquement, en ce qui concerne le développeur. L\'administrateur fera l\'extraction des chaînes de texte, les traducteurs les traduiront, puis l\'administrateur extraira les traductions et mettra à jour la branche FreeCAD/master.

### Préparer votre module de tierce partie ou macro pour la traduction {#préparer_votre_module_de_tierce_partie_ou_macro_pour_la_traduction}

Les modules de tierce partie ou macros sont traduits de façon similaire, mais vous devez vous charger d\'une partie du travail. Cette [discussion sur le forum](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) (en anglais) décrit les détails.

Mise à jour : voir [Traduction d\'un atelier externe](Translating_an_external_workbench/fr.md)

### Anciennes techniques de traduction des modules {#anciennes_techniques_de_traduction_des_modules}

La page [Ancienne méthode de localisation](Localization_Older_Methods/fr.md) décrit l\'utilisation d\'outils de traduction tels que Qt Linguist, lupdate, lrelease, pylupdate4, etc. en détail. La plupart de ces opérations ne sont plus nécessaires pour les modules FreeCAD/master, mais peuvent s\'avérer utiles pour préparer et mettre à jour des modules tiers.

## Automatiser les mises à jour de translations Crowdin {#automatiser_les_mises_à_jour_de_translations_crowdin}

Actuellement, les mainteneurs de FreeCAD utilisent l'API Crowdin via [Crowdin Scripts](Crowdin_Scripts/fr.md) pour extraire et transférer les traductions vers Crowdin, puis vers le dépôt Github. L\'API Crowdin donne aux responsables de FreeCAD la possibilité d\'automatiser certains aspects du flux de traduction du projet. Pour plus d\'informations, reportez-vous à la [documentation de l\'API Crowdin](https://support.crowdin.com/api/api-integration-setup/).

## Pages en relation {#pages_en_relation}

-   [Administration de Crowdin](Crowdin_Administration/fr.md)
-   [Scripts pour Crowdin](Crowdin_Scripts/fr.md)





 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Wiki{{\#translation:}}](Category:Wiki.md)
