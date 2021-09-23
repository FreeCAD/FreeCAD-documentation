# Tracker/fr
{{TOCright}}

![](images/Mantis_logo_262x90.png )

Le [traqueur de bogues FreeCAD](https://www.freecadweb.org/tracker) est un endroit pour rapporter des bogues, soumettre des demandes de fonctionnalités, de correctifs, ou encore faire une demande de fusion de votre branche si vous développez avec Git. Le traqueur est divisé en plusieurs sections de travail, donc s\'il vous plait soyez rigoureux et remplissez votre demande dans la catégorie appropriée. En cas de doutes, laissez le dans la section \"FreeCAD\".

## Flux de travail recommandé 

![](images/Bugreport-workflow.png )

Comme vous pouvez le voir dans l\'organigramme présenté ci-dessus, avant de créer des tickets, prenez le temps de faire des recherches dans les forums et le traqueur de bogues pour vérifier si votre problème n\'est pas déjà référencé. Ceci afin d\'éviter de gaspiller un temps de travail \"au combien précieux\" pour les développeurs et les volontaires qui pourraient le consacrer davantage au développement de l\'application.

## Signaler les bugs 

Si vous pensez que vous pourriez avoir trouvé un bogue (dysfonctionnement ou erreur), vous êtes invité de le signaler si vous avez suivi nos instructions pas à pas.

-   Assurez-vous que vous utilisez la version la plus récente de FreeCAD. **REMARQUE :** votre bug peut être corrigé dans la version de développement (instable). L\'utilisateur lambda exécute la version stable de FC.
-   Assurez-vous que votre bug est vraiment un bug, c'est-à-dire quelque chose qui devrait fonctionner mais ne l'est pas. **Assurez-vous que le même bug n\'a pas été signalé auparavant en effectuant d\'abord une recherche dans le bugtracker et le forum**.
    -   N\'oubliez pas que si vous n\'êtes pas sûr, n\'hésitez pas à expliquer votre problème/bug dans le [forum d\'aide](http://forum.freecadweb.org/viewforum.php?f=3) et à demander ce qu\'il faut faire.
    -   **Remarque**ː avant de poster sur le forum, veuillez lire les [Instructions du forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=2264).
-   Décrivez aussi clairement que possible le problème et comment il peut être reproduit. Si nous ne pouvons pas vérifier le bug, nous ne pourrons peut-être pas le résoudre.
    -   Cela signifie **rendre compte de manière claire, bien formatée et étape par étape** afin que même un utilisateur amateur puisse le reproduire.
    -   Recommandéː **Les captures d\'écran** du bug sont également très utiles à inclure. Utilisateurs Windows : veuillez ne pas joindre de captures d\'écran au format Word ou PDF. Utilisez l'outil Capture de Windows pour enregistrer votre capture en tant qu'image PNG.
    -   Recommandéː encore mieux, un **Animation gif ou Screencast** augmenterait également la probabilité de reproduire le problème.
-   **Ajouter un exemple de fichier FreeCAD** (fichier .FCStd) afin que developpeurs/testeurs puissent reproduire rapidement le bug.
    -   Veuillez ne pas compresser votre fichier \*.FCStd, il est déjà compressé.
    -   La taille des pièces jointes est limitée. Si votre fichier \*.FCStd est trop volumineux pour être joint, vous pouvez utiliser un service de stockage en ligne (beaucoup sont gratuits).
-   Inclure toutes les informations du bouton \"Copier dans le presse-papier\" dans le dialogue **Aide (menu) -\> À propos de FreeCAD**. Assurez-vous que vos données incluent votre version OCC ou OCE.
-   Merci de déposer un rapport séparé pour chaque bug.
-   Si votre bug provoque un crash dans FreeCAD et que vous êtes sur un système qui le supporte, vous pouvez essayer de lancer une **trace de debugage** et joindre cette trace au ticket. Cela peut permettre aux développeurs à gagner beaucoup de temps à identifier la source du crash. Voir [Debugging](Debugging/fr.md) pour plus de détails.

## Demande de fonctionnalités 

Si vous souhaitez que quelque chose apparaisse dans FreeCAD qui ne soit pas encore implémenté,  ce n\'est pas un bug mais une demande de fonctionnalité.

1.  **IMPORTANT ː** Avant de demander une éventuelle demande de fonctionnalité **assurez-vous d\'être le premier à le faire en effectuant une recherche dans les forums et dans le bugtracker**. Si vous avez conclu qu\'il n\'y a pas de tickets/discussions préexistants, la prochaine étape consiste à...
2.  Démarrer un fil de discussion pour discuter de votre demande de fonctionnalité avec la communauté via le [Open Discussion forum](http://forum.freecadweb.org/viewforum.php?f=8).
3.  Une fois que la communauté accepte que cette fonctionnalité est valide, vous pouvez ensuite ouvrir un ticket sur le suivi (enregistrez-la sous *feature request* au lieu de \"bug\").

-   **REMARQUE \#1** Pour que tout reste organisé, rappelez-vous de lier l\'URL du fil de discussion au ticket et le numéro du ticket (sous forme de lien) au fil de discussion.
-   **REMARQUE \#2** Gardez à l\'esprit qu\'il n\'y a aucune garantie que votre souhait soit exaucé.

![Page de rapport de FreeCAD Bugtracker - utilisez le menu déroulant pour désigner correctement le ticket](images/MantisBT-setting-Feature-Request.jpg )

## Soumettre un correctif (**patch**) 

Dans le cas, où vous avez programmé une correction d\'un bug (**patch**), une extension ou autre chose qui peut être d\'utilité publique dans FreeCAD, créer un **patch** à l\'aide de l\'outil **Subversion diff tool** et de le soumettre sur **[mantis bug tracker](http://www.mantisbt.org/)** <img alt="" src=images/Mantis_logo_button.gif  style="width:64px;"> **et envoyez-le comme patch**.

Addendum ː Le développement de FreeCAD a basculé vers le modèle de développement [GitHub](https://github.com/FreeCAD/FreeCAD), de sorte que le flux de travail pour soumettre des correctifs a été grandement amélioré/simplifié par la soumission de Pull Requests (PR).

1.  Ouvrez un fil de discussion dans le forum [Developer subforum](https://forum.freecadweb.org/viewforum.php?f=10) pour annoncer et discuter de votre correctif.
2.  Soumettez votre Pull Request (PR) sur le [dépôt FreeCAD GitHub](http://github.com/FreeCAD/FreeCAD). Veillez à créer un lien vers le fil de discussion du forum dans le résumé du commit git. Si vous n\'avez jamais travaillé avec `git` auparavant ou si vous n\'êtes pas familier avec la soumission d\'une PR à github, veuillez lire notre page wiki d\'introduction à [github](Source_code_management/fr.md).
3.  Collez le lien PR dans le fil de discussion du forum pour que les développeurs/testers puissent le tester.
4.  Soyez présent lors de la discussion afin que votre code puisse potentiellement être fusionné plus efficacement.

**Remarque :** la communauté FreeCAD recommande de discuter au préalable de toute révision importante du code source afin de faire gagner du temps à tous.

## Demande de fusion 

Si vous avez créé une branche git contenant les modifications que vous aimeriez voir fusionné dans le code FreeCAD, vous pouvez y demander que votre branche soit examinée et fusionnée si les développeurs FreeCAD sont OK avec elle. Vous devez d\'abord publier votre branche dans un dépôt git publique (github, bitbucket, sourceforge \...) et donner ensuite l\'URL de votre branche dans votre demande de fusion.

Si vous avez créé une branche git contenant les modifications que vous souhaiteriez voir fusionnées dans le code FreeCAD, vous pouvez demander à ce que votre branche soit revue et fusionnée si les développeurs FreeCAD le souhaitent. Vous devez d\'abord publier votre branche dans un répertoire git public (github, gitlab, bitbucket, sourceforge, etc.), puis donner l\'URL de votre branche dans votre demande de fusion.

## Trucs et astuces sous MantisBT 

### Le balisage de MantisBT 

MantisBT (Mantis Bug Tracker) a son propre balisage.

-   **@**mention - fonctionne comme sur GitHub où si vous ajoutez le nom d\'utilisateur \'@\' au nom d\'utilisateur de celui-ci, celui-ci recevra un e-mail indiquant qu\'il a été \'mentionné\' dans un fil de ticket

<img alt="" src=images/mantisbt-mention-example.jpg  style="width:600px;">

-   **\#**1234 - en ajoutant une balise de hachage devant un numéro, un raccourci pour créer un lien vers un autre ticket dans MantisBT sera présenté.

    :   **Remarque** : si vous survolez un ticket, il vous montrera le récapitulatif + si le ticket est fermé, il sera barré ainsi \#1234.

<img alt="" src=images/mantisbt-ticket-shortcut-example.jpg  style="width:600px;">

-   **\~**5678 - raccourci qui relie à une note de bug dans un ticket. Cela peut être utilisé pour référencer la réponse de quelqu\'un dans le fil. Chaque personne qui publie affiche un numéro \~\#\#\#\# unique à côté de son nom d\'utilisateur. Si vous regardez l\'image dans l\'exemple, vous voyez que le raccourci fait référence au *ticket number:comment number* de ce ticket.

<img alt="" src=images/mantisbt-comment-shortcut-example.jpg  style="width:600px;">

-   **\<del\>\</del\>** - l\'utilisation de ces balises aura pour effet de barrer le texte strikeout text.

<img alt="" src=images/mantisbt-strikeout-text-example.jpg  style="width:600px;">

-   **\<code\>\</code\>** - pour présenter une ligne ou un bloc de code, utilisez cette balise qui la colorisera et le différenciera.

<img alt="" src=images/mantisbt-colorized-code-example.jpg  style="width:600px;">

### Le BBCode de MantisBT 

En plus du [MantisBT Markup](Tracker/fr#MantisBT_Markup.md) ci-dessus, il est également possible d\'utiliser le format BBCode. Pour une liste complète, voir [BBCode plus plugin page](https://github.com/mantisbt-plugins/BBCodePlus#supported-bbcode-tags). Voici une liste des tags BBCode supportés ː 
[img][/img] - Images
[url][/url] - Liens
[email][/email] - Adresses E-mail
[color=red][/color] - Texte colorisé
[highlight=yellow][/highlight] - Texte surligné
[size][/size] - Taille de police
[list][/list] - Listes
[list=1][/list] - Listes numérotées (le numéro est le numéro de départ)
[*] - Liste d'items
[b][/b] - Gras
[u][/u] - Sousligné
[i][/i] - Italique
[s][/s] - Barré
[left][/left] - Aligné à gauche
[center][/center] - Centré
[right][/right] - Aligné à droite
[justify][/justify] - Justifié
[hr] - Règle horizontale
[sub][/sub] - Indice
[sup][/sup] - Exposant
[table][/table] - Tableau
[table=1][/table] - Tableau avec bordure de largeur spécifiée
[tr][/tr] - Rangée du tableau
[td][/td] - Colone du tableau
[code][/code] - Bloc de code
[code=sql][/code] - Bloc de code avec définition de langage
[code start=3][/code] - Bloc de code avec des numéros de ligne commençant par un numéro
[quote][/quote] - Citation de *quelqu'un* (sans nom)
[quote=name][/quote] - Citation de *nom*


=== MantisBT \<=\> GitHub Markup === Vous trouverez ci-dessous des mots-clés spéciaux du plug-in MantisBT Source-Integration qui renverront au référentiel FreeCAD GitHub. Voir [GitHub et MantisBT](Tracker/fr#GitHub_et_MantisBT.md).

-   **c:FreeCAD:git commit hash:** - **c** signifie \'commit\'. FreeCAD est un raccourci pour répértoire FreeCAD GitHub. \'git commit hash\' est le hachage spécifique de git commit à référencer. Remarque: les deux points sont nécessaires. Exempleː cːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **d:FreeCAD:git commit hash:** - de manière similaire à ce qui précède, **d** signifie \'diff\' qui fournira une vue Diff du commit. dːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **p:FreeCAD:pullrequest:** - enfin **p** signifie Pull Request. Exempleː pːFreeCADː498ː

<img alt="" src=images/mantisbt-source-integration-markup.jpg  style="width:600px;"> 

## GitHub et MantisBT 

Le bugtracker de FreeCAD a un plug-in appelé [Source Integration](https://github.com/mantisbt-plugins/source-integration) qui lie essentiellement le référentiel FreeCAD GitHub à notre traqueur MantisBT. Cela facilite le suivi et l'association des commits git avec leurs tickets MantisBT respectifs. **Le plug-in Source Integration recherche dans les messages de git commit des mots-clés spécifiques afin d\'exécuter les actions suivantes :**

**Remarque :**les mots-clés ci-dessous doivent être ajoutés au git commit message et non au sujet du PR.

### Référencement à distance d\'un ticket 

L\'utilisation de ce modèle associera automatiquement un commit git à un ticket (**Remarque:** cela ne fermera pas le ticket.) Le format MantisBT reconnaîtra:

-   bug \#1234
-   bugs \#1234, \#5678
-   issue \#1234
-   issues \#1234, \#5678
-   report \#1234
-   reports \#1234, \#5678

Pour les curieux, voici le regex que MantisBT utilise pour cette opération:


### Résolution à distance d\'un ticket 

-   fix \#1234
-   fixed \#1234
-   fixes \#1234
-   fixed \#1234, \#5678
-   fixes \#1234, \#5678
-   resolve \#1234
-   resolved \#1234
-   resolves \#1234
-   resolved \#1234, \#5678
-   resolves \#1234, \#5678

Pour les curieux, voici le regex que MantisBT utilise pour cette opération:


## En relation 

-   [Tri des bogues](Bug_Triage/fr.md)
-   [Source Code Management](Source_code_management/fr.md)







[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Administration](Category:Administration.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Tracker/fr
