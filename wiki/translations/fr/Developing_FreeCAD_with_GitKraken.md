# Developing FreeCAD with GitKraken/fr
## Avant-propos 




FreeCAD utilise [Git](https://git-scm.com/) pour gérer son code source. Ce document est une introduction rapide à [GitKraken](https://www.gitkraken.com/), une interface utilisateur graphique de Git. GitKraken est un logiciel propriétaire qui est gratuit lorsqu\'il utilisé à des fins non commerciales; vous n\'avez pas besoin de GitKraken pour développer du code pour FreeCAD, mais de nombreux développeurs l\'apprécient et le trouvent utile pour gérer leur développement. FreeCAD n\'approuve pas GitKraken mais nous espérons qu\'un guide comme celui-ci montrera aux utilisateurs à quel point il est facile de configurer l\'environnement de développement et d\'encourager davantage de personnes à la contribution du projet.

Pour plus d\'informations sur l\'utilisation générale de Git à partir de la ligne de commande, consultez [ Gestion du code source](Source_code_management.md) et le livre en ligne [Pro Git](https://git-scm.com/book/en/v2). Pour compiler FreeCAD, voir [ Compilation](Compiling.md).

## Introduction

Git est un puissant système de contrôle de révision couramment utilisé pour suivre le développement de code informatique. Bien qu\'il s\'agisse d\'un système complexe, vous n\'avez généralement besoin que de connaître le fonctionnement général et quelques fonctions en ligne de commande (CLI). Une interface utilisateur graphique (GUI) facilite la courbe d\'apprentissage. [GitKraken](https://www.gitkraken.com/) est un programme propriétaire gratuit (lorsqu\'il est utilisé à des fins non commerciales) qui fonctionne sur le framework [Electron](https://electronjs.org), ce qui signifie qu\'il est multiplateforme et peut être utilisé de la même manière sous Linux, MacOS et Windows.

## Configuration de l\'outil de développement Git 

Il existe différentes manières de télécharger GitKraken en fonction de votre système d\'exploitation. Dans les distributions Linux, vous pouvez parfois l\'obtenir à partir du gestionnaire de paquets.

1.  Télécharger GitKraken.
2.  Dans votre navigateur, allez à: {{URL|https://github.com/FreeCAD/FreeCAD}}.
    ![](images/Github-Fork-button.png )
3.  Cliquez sur le bouton **Fork**. Ceci va cloner le dépôt `FreeCAD/FreeCAD` sur votre compte Git. En d\'autres termes, l\'URL pour accéder à votre fork sera:
        https://github.com/GITHUBUSERNAME/FreeCAD.git
4.  Ouvrez GitKraken, allez sur **File → Clone Repo**, et saisissez cette adresse.
    ![](images/GitKraken-Clone-Repo-dialogue.png )
5.  GitKraken va maintenant effectuer un `git clone` de votre dépôt personnel.
    Veuillez lire le post \"différence entre le référentiel du dépôt original et celui du dépôt cloné (Fork)\" [origin vs upstream](https://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-on-github#9257901). Pour résumer, le référentiel de votre propre dépôt (fork) de FreeCAD est {{incode | origin}}, tandis que le référentiel du dépôt officiel FreeCAD est {{incode | upstream}}. Par conséquent, vous devez maintenant configurer l\'upstream.
6.  Localiser la barre latérale dans Gitkraken. Il y a les sections **Local** et **Remote**. Local fait référence à vos branches locales. Remote fait référence aux dépôts distants et à leurs branches. Ajoutons le dépôt FreeCAD comme dépôt distant. Dans la section *Remote*, cliquez sur le **+**. (comme illustré dans l\'image ci-dessous).
    ![](images/Gitkraken-remote-sidebar.png )
7.  Une boîte de dialogue **Add Remote** s\'ouvre. Cliquez sur le symbole (1) de Github. Dans le champ (2) **Github repo**, trouvez le `FreeCAD/FreeCAD` et cliquez dessus. Dans le champ **Name**, tapez `upstream`. Cliquez ensuite sur le bouton **Add Button**.
    <img alt="" src=images/Gitkraken-add-remote-dark.png  style="width:400px;">
8.  La boîte de dialogue se ferme et vous revenez à l\'interface principale de GitKraken. Cette fois, trouvez la section *Local* dans la barre latérale ; double-cliquez sur la branche `master` pour y accéder. Dans la ligne de commande, ceci est équivalent à
        git checkout master
9.  Cliquez sur l\'icône *Push* en haut à droite de l\'interface. Ceci va pousser votre **maître local** vers votre **maître d\'origine distant**.

## L\'interface de GitKraken 

Pour plus d\'informations, consultez le [Guide de démarrage](https://support.gitkraken.com/start-here/guide/) de GitKraken.

+++
| Local master                 | Votre branche locale de la branche FreeCAD master, indiqué par la ligne **bleue** sur la capture d\'écran.                                                                                                |
|                              |                                                                                                                                                                                                           |
|                              | L\'élément est surligné en **vert**, signifiant que la branche est actuellement active (`git checkout`).                                                                           |
+++
| Local  | Toutes les autres branches sur votre machine locale. Sur la capture d\'écran, vous pouvez voir les branches appelées `editor_fixes` et `editor_fixes_typos` |
+++

: *Local* signifie qu\'il s\'agit de votre machine locale.

   
  Remote upstream   Le dépôt officiel de FreeCAD {{URL|https://github.com/FreeCAD/FreeCAD}}, indiqué par la ligne **verte** sur la capture d\'écran.
  Remote origin     Votre dépôt personnel (Fork) de FreeCAD, {{URLn|https://github.com/YourGitHubUsername/FreeCAD}}, indiqué par la ligne **rouge** sur la capture d\'écran.
   

  : *Remote* signifie qu\'il s\'agit d\'un dépôt distant, par exemple dans GitHub

![](images/GitKraken-Main-Screen-sm.jpg )


{{Caption | Interface GitKraken montrant trois branches locales (dont le {{Emphasis | master}}), et deux dépôts distants {{incode | origin}} et {{incode | upstream}}. Chacun des 2 dépôts distants ayant un master et plusieurs branches dans un dossier "releases". }}

Sur l\'image, les branches distantes **Local master** et **Remote origin master** sont situées après trois commits derrière le **Remote upstream master**, c\'est-à-dire le code source officiel de FreeCAD. Ceci est indiqué par les icônes illustrant les 3 étapes dans la liste qui représente l\'historique de validation de la branche maître. Voir [Rebasage](Developing_FreeCAD_with_GitKraken/fr#Rebasage.md) pour mettre à jour les branches qui se trouvent derrière.

## Rebasage

-   Sélectionnez la branche **Local master** en double cliquant sur elle (`git checkout master`) pour la rendre active.
-   Positionnez la souris sur le dernier commit de upstream, clic droit, et choisissez **Rebase master onto upstream/master** (`git pull upstream master`)
-   Cliquez maintenant sur le bouton **Push** (`git push origin master`). Ceci pousse votre branche locale **Local master** vers le dépôt distant **Remote origin master**.

![](images/GitKraken-Rebasing.gif )



* Le rebasage de la branche master locale l'a met à jour avec les dernières modifications effectuées sur le dépôt officiel upstream master.*

## Branches

Les branches sont une fonctionnalité qui rend Git puissant par rapport aux autres systèmes de révision. Les branches ne sont pas des \"Fork\" complets, mais définissent plutôt des instantanés où une version du code commence à diverger de la branche principale. Chaque fois que vous souhaitez modifier le code de FreeCAD, créez d\'abord une branche, puis effectuez des modifications, puis fusionnez vos commits dans la branche principale. Avec Git, il est simple de créer, fusionner et supprimer des branches lorsque vous n\'en avez plus besoin. Veuillez lire [Branchement et fusion](https://support.gitkraken.com/working-with-repositories/branching-and-merging) pour en savoir plus sur ce processus dans GitKraken.

1.  Assurez-vous que la branche master est actuellement active (double-cliquez dessus, {{incode | git checkout master}}). Dans GitKraken, la branche **Local master** doit être surlignée en **vert**.
2.  Cliquez sur le bouton **Branch** pour créer une nouvelle branche et saisissez son nouveau nom ({{incode | git checkout -b nouveau-nom-de-votre-branche}}).

## Effectuer des pull requests 

Des [Pull requests](https://help.github.com/articles/about-pull-requests/) (PRs) sont nécessaires pour fusionner le code de votre branche du dépôt local avec le code du dépôt distant {{incode | upstream}}. Pour résumer le processus, une fois que vous avez modifié votre branche, vous devez la pousser vers votre fork GitHub ({{incode | origin}}, {{URLn | https: //github.com/GITHUB_USER_NAME/FreeCAD.git}} ), et à partir de là, faites un Pull Request sur le dépôt officiel {{incode | upstream}}. GitKraken vous fait gagner quelques clics pour créer facilement des pull requests au lieu d\'utiliser l\'interface de GitHub.

Étapes dans GitKraken:

-   Trouvez votre branche locale sur l\'interface et assurez-vous qu\'elle est active (double-cliquez dessus).
-   Faites un clic droit sur le nom de la branche et trouvez l\'option **Push  et effectuez un pull request**.

:   GitKraken ouvrira une boîte de dialogue vous demandant de confirmer le dépôt que votre branche utilisera pour extraire et pousser. Il poussera ensuite votre branche locale vers ce dépôt distant.

![](images/Gitkraken-How_to_PR.png )

-   GitKraken vous demandera comment vous voulez appeler la branche distante. Le nom par défaut est le même que celui de la branche locale sur votre ordinateur.

<img alt="" src=images/Gitkraken-How-to-PR-Prompt-for-Branch-name.png  style="width:1200px;">

-   GitKraken ouvre alors une autre boîte de dialogue demandant aux dépôts et aux branches de fusionner, et la direction (de et vers).

:   Vous souhaitez normalement fusionner à partir du dépôt distant origin **** ({{incode | GITHUB_USER_NAME / FreeCAD}}) vers la branche distante **upstream master** ({{incode | FreeCAD / FreeCAD}}). Assurez-vous de saisir un bon titre pour la demande d\'extraction et rédigez un paragraphe plus descriptif si vos modifications sont importantes. Consultez la documentation officielle de [GitKraken](https://support.gitkraken.com/working-with-repositories/pull-requests) pour plus d\'informations.

![](images/Gitkraken-How-to-PR-Github-Dialog-breakdown.png )

## Résolution des conflits lors d\'une fusion 

GitKraken dispose d\'un outil de gestion des conflits de fusion spécial qui n\'est accessible que dans la version GitKraken Pro. Cependant, il existe des solutions de contournement pour utiliser des outils externes pour la fusion.

-   [Outils de fusion externes compatibles GitKraken](https://support.gitkraken.com/working-with-repositories/branching-and-merging/): Beyond Compare, FileMerge, Kaleidoscope, KDiff, Araxis, P4Merge
-   Si aucune des options ci-dessus ne fonctionne pour vous, il est possible de spécifier [Outils externes de fusion et de comparaison](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_external_merge_tools) dans le fichier de configuration {{incode | ~/.gitconfig}} du dossier utilisateur.

## Regroupement des commits 

En tant que système de contrôle des révisions, Git encourage la réalisation de nombreux \"commits\" pour le suivis de vos modifications; Cependant, si vous avez trop de petits changements, l\'historique des \"commits\" pourrait apparaître un peu désordonné. Le \"Squashing\" consiste à regrouper plusieurs \"commits\" en un seul. Dans le [manuel GitKraken](https://support.gitkraken.com/working-with-commits/squash/), le \"squashing\" est disponible pour les commits qui répondent aux exigences suivantes:

-   Vous devez sélectionner au moins deux commits à regrouper.
-   Le plus récent \"commit\", par date de \"commit\", est également le \"commit\" HEAD actuel.
-   Généalogiquement consécutif.
-   Chronologiquement consécutif.
-   Le \"commit\" le plus ancien de la liste a un parent.

Si toutes ces conditions sont remplies, l\'option **Squash** apparaît lorsque vous cliquez avec le bouton droit sur le nœud \"commit\". Voir [Squash.gif](https://support.gitkraken.com/img/documentation/working-with-files/commits/squash.gif)

## Suivre les autres dépôts FreeCAD 

Vous pouvez utiliser GitKraken pour suivre les \"Fork\" FreeCAD personnels des autres développeurs; de cette façon, vous pouvez voir comment ils écrivent du code et valident des modifications dans leurs propres branches avant de soumettre des pull requests vers le dépôt upstream {{incode | FreeCAD / FreeCAD}}.

1.  Dans le panneau latéral gauche à côté de la catégorie **Remote**, appuyez sur le signe **+**.
2.  Une boîte de dialogue apparaîtra pour saisir le nom du dépôt que vous souhaitez ajouter. Les dépôts distants recommandées proviennent des principaux développeurs de FreeCAD et des contributeurs connus: wmayer, yorikvanhavre, ickby, sliptonic, kkremitzki, etc.
3.  Appuyez sur **Add Remote**.

Désormais, chaque fois que de nouveaux commits sont effectués, ou que des branches sont rebasées, par les auteurs de ces dépôts, vous verrez leur historique de commit de manière graphique. ![](images/Gitkraken-add-remote.gif )

## En relation 

-   [ Gestion du code source](Source_code_management.md)
-   [ Développement de FreeCAD avec KDevelop](Developing_FreeCAD_with_KDevelop.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Developer](Category_Developer.md) > [3rd Party](Category_3rd Party.md) > Developing FreeCAD with GitKraken/fr
