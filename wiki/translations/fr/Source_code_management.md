# Source code management/fr
## Introduction

Le principal outil de gestion de code source du projet FreeCAD est [Git](http://en.wikipedia.org/wiki/Git_%28software%29), qui peut être facilement installé dans la plupart des systèmes d\'exploitation à partir d\'un gestionnaire de paquets ou directement à partir de [Git\'s website](https://git-scm.com/). Nous vous conseillons de vous familiariser avec Git avant de travailler directement avec le code source FreeCAD. Visitez la page [Git documentation](https://git-scm.com/doc) pour obtenir le manuel de référence, ainsi que le [Pro Git book](https://git-scm.com/book/en/v2) pour apprendre à utiliser le système de manière générale. Le présent document porte sur l\'utilisation de Git pour le développement FreeCAD. La compilation de FreeCAD est décrite dans [Compilation](Compiling/fr.md).

Bien que Git soit principalement une application de terminal, il existe de nombreux clients graphiques qui facilitent le travail avec les branches, l'application de correctifs et la soumission de demandes d\'extraction à une branche main. Les exemples incluent [gitk](https://git-scm.com/docs/gitk) (la première interface graphique développée), [gitg](https://wiki.gnome.org/Apps/Gitg/) (Gnome), [qgit](https://github.com/tibirna/qgit) (Qt), [tig](https://jonas.github.io/tig/) (Ncurses), [git-cola](http://github.com/git-cola/git-cola) et [GitKraken](https://www.gitkraken.com/) (propriétaire). Veuillez consulter [Developing FreeCAD with GitKraken](Developing_FreeCAD_with_GitKraken.md) pour une introduction sommaire à cet outil.

Remarque: si tout cela commence à vous donner le vertige, il existe une très bonne série non technique sur l\'utilisation de git et Github appelée \'[Git et Github pour les poètes](https://youtu.be/BCQHnlnPusY)\'



## Accès au code source 

Tout le monde peut accéder et obtenir une copie du code source de FreeCAD, mais seuls les gestionnaires de projet(s) peuvent en modifier le contenu. Vous pouvez avoir une copie du code, l\'étudier et le modifier comme vous le souhaitez, mais si vous voulez que vos modifications soient prises en compte dans le code source officiel, vous devez effectuer un \"pull request\" sur le dépôt main. Les gestionnaires pourront alors vérifier vos modifications avant de les valider. Cette façon de développer est connue sous le nom de [flux de travail des dictateurs et des lieutenants](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows) où les développeurs principaux (dictateurs) et développeurs de confiance (lieutenants) filtrent le code soumis par les développeurs et les utilisateurs indépendants.

Si votre code source change de manière significative, il vous est conseillé de l\'expliquer dans la section [\"pull requests\"](http://forum.freecadweb.org/viewforum.php?f=17) du forum FreeCAD.

<img alt="" src=images/FreeCAD_git_workflow.svg  style="width:600px;"> 
*Flux de travail générique pour développer du code pour FreeCAD; Tout le monde peut récupérer le code depuis le dépôt principal, mais les développeurs principaux ont les droits exclusifs pour faire une revue et prendre en compte les changements apportés par les autres développeurs.*



### Dépôt officiel Github 

Le code source de FreeCAD est hébergé sur {{URL|https://github.com/FreeCAD/FreeCAD}}

Pour pouvoir contribuer et accéder au code source, vous devez avoir un [compte GitHub](https://github.com/join).

Dans le passé, le code source était hébergé en tant que dépôt SVN, {{URL|https://free-cad.svn.sourceforge.net/svnroot/free-cad}}. Cela a été déplacé vers GitHub le 10 octobre 2011, avec [commit 120ca87015](https://github.com/FreeCAD/FreeCAD/commit/120ca87015).

Par conséquent, de nombreuses modifications ont été apportées avant cette date qui ne sont pas enregistrées dans l\'historique de validation Git moderne. Pour en savoir plus, consultez la page [Histoire](History/fr.md).



### Configurer votre nom d\'utilisateur sous Git 

Les développeurs doivent faire un commit vers le dépôt de leur code, en utilisant leur nom personnel d\'utilisateur GitHub. Si ce n\'est pas déjà fait globalement, vous pouvez le régler au niveau local pour le dépôt Git actuel comme ceci :


{{Code|lang=text|code=
git config user.name "YOUR_NAME"
git config user.email GITHUB_USERNAME@users.noreply.github.com
}}

Où `"YOUR_NAME"` représente votre nom complet ou votre pseudonyme, utilisé pour identifier l\'auteur d\'un commit spécifique, et `GITHUB_USERNAME` indique le nom de votre compte sur GitHub.



### Dépôts distants 

Veuillez lire [what-is-the-difference-between-origin-and-upstream-on-github#9257901 Quelle est la différence entre l\'origine et l\'upstream sur GitHub?](https://stackoverflow.com/questions/9257533/) (Stackoverflow) pour vous aider à comprendre la différence entre `origin` et `upstream` dans Git. Cette section explique comment définir les référentiels appropriés pour le développement. En gros :

-    `origin`est votre branche personnelle du référentiel officiel de FreeCAD, à savoir, {{URL|https://github.com/GITHUB_USERNAME/FreeCAD}}

-    `upstream`est le référentiel officiel de FreeCAD, à savoir, {{URL|https://github.com/FreeCAD/FreeCAD}}.

La distinction est importante, vous devez d\'abord écrire votre code dans votre propre dépôt, avant de \"pousser\" ces changements sur le dépôt officiel.

Sur la base de ce qui précède, il existe deux manières de configurer votre environnement de développement Git:

-   1ère méthode: fork GitHub et clonez votre fork localement
-   2ème méthode: clonez FreeCAD directement sur votre machine locale et ajustez les serveurs distants

Nous recommandons la première méthode car c\'est la plus rapide.


<div class="mw-collapsible mw-collapsed toccolours">



#### 1ère méthode: Créez une branche sur GitHub et clonez votre branche localement 


<div class="mw-collapsible-content">

Vous allez d\'abord créer le référentiel FreeCAD dans GitHub, puis cloner ce fork personnel sur votre ordinateur et enfin définir le référentiel `upstream`.

-   [Log in](https://github.com/join) sur votre compte GitHub.
-   Accédez au référentiel officiel FreeCAD: {{URL|https://github.com/FreeCAD/FreeCAD}}
-   En haut à droite de la page, appuyez sur le bouton \"Fourchette\". Cela créera une copie personnelle du référentiel FreeCAD sous votre nom d\'utilisateur GitHub: {{URL|https://github.com/GITHUB_USERNAME/FreeCAD}}
-   Sur votre machine, clonez votre nouvelle fourche FreeCAD. Il sera créé dans un répertoire `freecad-source`.


{{Code|lang=text|code=
git clone https://github.com/GITHUB_USERNAME/FreeCAD.git freecad-source
}}

-   Une fois le téléchargement terminé, entrez le nouveau répertoire source et définissez le référentiel `upstream`.


{{Code|lang=text|code=
cd  freecad-source
git remote add upstream https://github.com/FreeCAD/FreeCAD.git
}}

-   Confirmez vos référentiels distants avec `git remote -v`; la sortie devrait être semblable à celle-ci


{{Code|lang=text|code=
origin  https://github.com/GITHUB_USERNAME/FreeCAD.git (fetch)
origin  https://github.com/GITHUB_USERNAME/FreeCAD.git (push)
upstream    https://github.com/FreeCAD/FreeCAD.git (fetch)
upstream    https://github.com/FreeCAD/FreeCAD.git (push)
}}

-   Maintenant, le développement peut commencer.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



#### 2ème méthode: clonez le dépôt officiel FreeCAD git sur votre ordinateur local 


<div class="mw-collapsible-content">

Vous allez d\'abord créer le référentiel FreeCAD dans GitHub, mais vous clonerez le référentiel FreeCAD d\'origine sur votre ordinateur local, puis modifierez vos télécommandes via le terminal.

-   [Log in](https://github.com/join) sur votre compte GitHub.
-   Accédez au référentiel officiel FreeCAD: {{URL|https://github.com/FreeCAD/FreeCAD}}
-   En haut à droite de la page, appuyez sur le bouton \"Fourchette\". Cela créera une copie personnelle du référentiel FreeCAD sous votre nom d\'utilisateur GitHub: {{URL|https://github.com/GITHUB_USERNAME/FreeCAD}}
-   Clonez le référentiel FreeCAD d\'origine. Il sera créé dans un répertoire `freecad-source`.


{{Code|lang=text|code=
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
}}

-   Une fois le téléchargement terminé, entrez le nouveau répertoire source et définissez le référentiel `origin`.


{{Code|lang=text|code=
cd freecad-source
git remote add origin https://github.com/GITHUB_USERNAME/FreeCAD.git
}}

-   Ensuite, configurez le référentiel `upstream`.


{{Code|lang=text|code=
git remote add upstream https://github.com/FreeCAD/FreeCAD.git
}}

-   Confirmez vos référentiels distants avec `git remote -v`; la sortie devrait être semblable à celle-ci


{{Code|lang=text|code=
origin  https://github.com/GITHUB_USERNAME/FreeCAD.git (fetch)
origin  https://github.com/GITHUB_USERNAME/FreeCAD.git (push)
upstream    https://github.com/FreeCAD/FreeCAD.git (fetch)
upstream    https://github.com/FreeCAD/FreeCAD.git (push)
}}

-   Maintenant, le développement peut commencer.


</div>


</div>

Si, pour une raison quelconque, les référentiels distants existent mais indiquent une adresse incorrecte, vous pouvez remédier à la situation en renommant le nom du référentiel distant. Par exemple, `origin` doit pointer sur votre branche personnelle; s\'il pointe vers le référentiel FreeCAD d\'origine, remplacez le nom de cette télécommande par `upstream` et ajoutez manuellement le référentiel `origin`.


{{Code|lang=text|code=
git remote rename origin upstream
git remote add origin https://github.com/GITHUB_USERNAME/FreeCAD.git
git remote -v
}}

Vous pouvez également afficher plus d\'informations avec le mot clé `show`.


{{Code|lang=text|code=
git remote show origin
git remote show upstream
}}



## Processus de développement sous Git 


**Ne développez jamais sur votre branche '''main''' locale. Au lieu de cela, créez une branche locale pour le développement, puis fusionnez cette branche locale avec la branche main en amont via une demande d'extraction. Lire [https://git-scm.com/book/fr/v2/Git-Branching-Branches-in-a-Nutshell Git Branching], [https://book.git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Fusion Fusioning], et [https://git-scm.com/book/fr/v2/GitHub-Contributing-to-a-Project GitHub - Contribuer à un projet] pour en savoir plus**

<img alt="" src=images/FreeCAD_git_branches_workflow.svg  style="width:800px;"> 
*Flux de travail générique pour développer du code pour FreeCAD en utilisant `git*; Un "fork" du dépôt principal est créé sur le serveur distant et cloné sur un ordinateur local (0); De nouvelles branches (1) sont utilisées pour appliquer des modifications et des ajouts de code localement (2); Les branches sont "rechargées" avec la version de code la plus récente du serveur (3), et elles sont ensuite "poussées" vers le dépôt distant (4); Puis un "Pull Request" est créé afin de pouvoir fusionner le code dans le dépôt principal (5). Le clone du "fork" sur l'ordinateur local est alors mis à jour avec le nouveau code main du serveur (a). Ce main mis à jour est également "poussé" vers le dépôt distant (b) afin d'obtenir le même code à la fois sur le serveur distant et l'ordinateur local.`



### Ramifications

Au lieu de travailler sur la version main du code, les meilleures pratiques avec Git recommandent de créer une nouvelle branche chaque fois que vous souhaitez travailler sur une nouvelle fonctionnalité. Les branches sont peu coûteuses en ressources, elles ne copient pas l'ensemble de l'arborescence des sources, mais créent simplement un point dans le temps sur lequel vous allez écrire du code; ainsi, les branches aident à garder le travail en cours séparé du code principal.

L\'ajout d\'une nouvelle branche est réalisée en 2 étapes : Tout d\'abord vous créez la branche, puis vous vous commutez sur celle-ci.


{{Code|lang=text|code=
git branch myNewBranch
git checkout myNewBranch
}}

Sinon, effectuez les deux étapes avec une seule instruction:


{{Code|lang=text|code=
git checkout -b myNewBranch
}}

Maintenant, vous pouvez changer de branche avec `checkout` chaque fois que vous avez besoin de travailler dessus. Pour afficher les branches de votre projet et de la branche actuelle, utilisez l\'opération `branch` seule ou ajoutez `-v` ou `-vv` pour plus d\'informations:


{{Code|lang=text|code=
git branch
git branch -vv
}}

Une fois que vous avez effectué les changements et que vous les avez validés (commit), utilisez la ligne de commande `log` avec les options suivantes pour visualiser les branches.


{{Code|lang=text|code=
git log --oneline --decorate --graph --all
}}



### Validation des modifications 

Une fois que vous êtes dans une nouvelle branche, éditez les fichiers sources que vous voulez avec votre éditeur de texte. Pour voir quels fichiers ont été modifiés, utilisez la commande `status` et `diff`; Lorsque que vous êtes satisfait de votre travail, validez le avec la commande `commit` :


{{Code|lang=text|code=
git status
git diff
git commit -a
}}

Contrairement à SVN, vous devez indiquer précisément les fichiers à valider. utilisez l\'option `-a` pour enregistrer les modifications dans tous les fichiers modifiés. Votre éditeur de texte, par exemple, `nano` ou `vim`, s\'ouvrira pour vous permettre d\'écrire un message de validation.

Alternativement, ajoutez le message dans le \"commit\" lui-même:


{{Code|lang=text|code=
git commit -a -m "Fix the bug in the clone function."
}}

Si vous créez de nouveaux fichiers ou répertoires, vous devez d\'abord utiliser l\'opération `add` pour les ajouter au référentiel local avant de valider les modifications.


{{Code|lang=text|code=
git add path
git commit -a
}}

Où `path` peut être n\'importe quel répertoire ou fichier.



### Rédiger de bons messages de validation 

Vous devriez essayer de travailler par petites sections. Si vous ne pouvez pas résumer vos modifications en une phrase, cela fait probablement trop longtemps que vous n\'avez pas effectué de livraison.

Pour les grands changements, il est important que vous disposiez de descriptions utiles et utiles de votre travail. FreeCAD a adopté un format mentionné dans le livre [Pro Git](https://git-scm.com/book/en/v2), qui consiste en un court message, puis en un paragraphe descriptif plus grand.


{{Code|lang=text|code=
Résumé succinct (50 caractères ou moins) des modifications apportées

 Un texte explicatif plus détaillé, si nécessaire. Limitez-le à environ 72
 caractères environ. Dans certains contextes, la première ligne est traitée
 comme le sujet d'un message électronique et le reste du texte comme le corps
 du message. La ligne vierge séparant le résumé du corps est essentielle 
 (à moins que vous n'omettiez entièrement le corps); des outils comme rebase
 peuvent être confondus si vous exécutez les deux ensemble.
 
 Les paragraphes suivants sont placés après les lignes vides. 
 
  - Les puces peuvent également être utilisées.
 
  - En général, on utilise un trait d'union ou un astérisque pour la puce,
    précédé d'un espace simple, avec des lignes vides entre les deux, mais
    les conventions varient selon les cas.
}}

Si vous effectuez de nombreux travaux connexes dans une branche, vous devez effectuer de nombreux petits commits (voir un [forum post](https://forum.freecadweb.org/viewtopic.php?f=10&t=2062&p=14887#p14886)). Lorsque vous souhaitez fusionner ces modifications dans la branche main, vous devez émettre


{{Code|lang=text|code=
git log main..myNewBranch
}}

pour voir les messages individuels de commit. Vous pouvez ensuite écrire un message de haute qualité lors d'une fusion.

Lorsque vous fusionnez à la branche main, utilisez l\'option `--squash` et validez avec votre message de validation de qualité. Cela vous permettra d\'être très libéral avec vos commits et vous aidera à fournir un bon niveau de détail dans les messages de validation sans autant de descriptions distinctes.



### Regroupement des \"commits\" 

Il est possible de regrouper plusieurs \"commits\" consécutifs dans 1 seul \"commit\", on appelle ça le \"squashing\". Ceci peut être utile dans les cas où vous avez effectué beaucoup de \"petits commits\" et que vous souhaitez les regrouper dans un seul \"commit\". Par exemple, lorsque vous changez simplement une variable, que vous corrigez des erreurs d\'orthographe ou que vous ajustez la mise en forme de votre code. Vous devez faire des regroupements uniquement sur des \"petits commits\". Les grandes modifications effectuées sur plusieurs fichiers doivent contenir l\'ensemble de l\'historique des changements du commit.

Avec la commande `git log --oneline`, vous pouvez voir plusieurs \"commits\" consécutifs dont le plus récent est situé en haut de la liste. Dans cet exemple, plusieurs \"commits\" ont été effectués à partir de la \"fonctionnalité A\" pour réaliser l\'implémentation de la \"fonctionnalité B\"; Nous souhaiterions maintenant regrouper tous les \"commits\" effectués pour la \"fonctionnalité B\" en un seul.


{{Code|lang=text|code=
871adb OK, feature B is fully implemented
1c3317 Whoops, it is not ready yet...
87871a I'm almost ready!
643d0e Code cleanup
af2581 Fix this and that
4e9baa Good implementation
d94e78 Prepare the module for feature B
6394da Feature A
}}

Utilisez la commande `rebase` avec l\'option `--interactive` ou `-i` pour sélectionner différents \"commits\" et les regrouper en un seul. Utilisez la valeur de hachage située juste devant le premier commit que vous voulez regrouper. Dans notre cas, il s\'agit de celui qui correspond à la \"fonctionnalité A\".


{{Code|lang=text|code=
git rebase -i 6394da
}}

(ASTUCE : Si vous savez combien de commits vous voulez éditer, vous pouvez utiliser `git rebase -i HEAD~n` pour travailler sur les derniers commits `n`)

un éditeur de ligne de commande comme `nano` ou `vim` s\'ouvrira pour vous montrer les \"commits\", mais cette fois avec le plus ancien en haut de la liste. Avant chaque \"commit\", le mot `pick` sera affiché. Supprimez le mot `pick`, et écrivez le mot `squash` ou juste la lettre `s` à la place, à l\'exception de la première entrée; Ce \"commit\" est le plus ancien, donc tous les futurs \"commits\" seront regroupés dans celui-ci.


{{Code|lang=text|code=
pick d94e78 Prepare the module for feature B
s 4e9baa Good implementation
s af2581 Fix this and that
s 643d0e Code cleanup
s 87871a I'm almost ready!
s 1c3317 Whoops, it is not ready yet...
s 871adb OK, feature B is fully implemented
}}

Sauvegardez le fichier et fermez l\'éditeur.

L\'éditeur s\'ouvrira de nouveau. Vous pouvez maintenant ajouter un long message qui décrira tous les changements effectués comme s\'ils étaient réunis dans un seul \"commit\". Sauvegardez le fichier et fermez l\'éditeur une fois de plus. Ceci finira l\'action de regroupement de ces \"commits\" avec le nouveau message que vous avez saisis.

Vous pouvez encore utiliser `git log --oneline` pour observer le nouvel historique des changements du commit. Dans ce cas, seul un simple \"commit\" pour la \"fonctionnalité B\", apparaitra au dessus du \"commit\" non modifié pour la \"fonctionnalité A\".


{{Code|lang=text|code=
c83d67 OK, feature B is fully implemented now, with proper module setup, and clean code.
6394da Feature A
}}

Lorsque vous codez pour FreeCAD, nous vous demandons de commencer chaque message de validation par le module qu\'il affecte. Par exemple, un message de validation pour une modification de sketcher pourrait être :

    Sketcher: make straight lines curve a bit

    Straight lines are sort of ugly, so this commit adds a little bit of curvature to them, so
    they are more visually pleasing. They also sparkle some, and change colors over time.

    Fixes bug #1234.

Votre PR sera plus facile à réviser et plus rapide à être fusionné, si vous prenez soin d\'utiliser rebase pour structurer et décrire vos commits avant de les soumettre.



### Publication de votre travail sur votre dépôt GitHub 

Les branches locales de votre ordinateur ne sont pas automatiquement synchronisées avec les serveurs distants que vous avez spécifiés comme `origine` ou `en amont` (voir [Référentiels distants](#Référentiels_distants.md)); vous devez explicitement pousser les branches sur les serveurs distants, pour lesquels vous devez avoir un accès en écriture. Une fois que cela est fait, les branches deviennent publiques et disponibles pour être revues par d\'autres développeurs.

Pour FreeCAD, vous devez placer votre branche locale dans le référentiel distant `origin`, à savoir, {{URLn|https://github.com/GITHUB_USERNAME/FreeCAD}}. Vous devez entrer votre nom d\'utilisateur et votre mot de passe chaque fois que vous appuyez, sauf si vous avez configuré [mise en cache](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage#_credential_caching). Veuillez lire [Pushing dans un référentiel distant](https://help.github.com/articles/pushing-to-a-remote/) pour plus d\'informations.


{{Code|lang=text|code=
git push origin myNewBranch
}}

Lorsque vous travaillez avec une seule branche, vous devrez peut-être rebaser, écraser et corriger les commits plusieurs fois de manière interactive. Dans ce cas, votre historique de branche ne sera pas simple et vous ne pourrez pas le pousser vers le référentiel distant. Vous pouvez obtenir un message comme le suivant, indiquant qu\'il n\'est pas possible d\'effectuer un push \"fast-forward\" (avance rapide).


{{Code|lang=text|code=
error: failed to push some refs to 'https://github.com/USER/FreeCAD.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
}}

Pour pousser enfin votre branche vers le dépôt distant, vous devez la \"forcer à la pousser\". Cela remplacera complètement votre branche distante par la branche réelle que vous avez hors ligne.


{{Code|lang=text|code=
git push -f origin myNewBranch
}}

Le développeur standard n\'a pas d\'accès en écriture au référentiel `upstream` {{URL|https://github.com/FreeCAD/FreeCAD}}. Par conséquent, vous ne devez jamais envoyer de code à ce serveur distant.



### Rebasing de l\'amont 

Pendant que vous travaillez sur votre propre branche, le code officiel de FreeCAD continue de s\'améliorer avec les \"commits\" des autres développeurs, ce qui créé une différence de contenu avec votre branche personnelle.

          .A origin/myNewBranch
         / 
    oZ FreeCAD upstream/main

Par conséquent, lorsque vous êtes prêt à fusionner votre branche sur le dépôt principal de FreeCAD, vous devez faire un \"rebase\" (sorte de re-synchronisation) de votre copie du dépôt, afin que son contenu se rapproche le plus possible de celui du dépôt officiel. Voir le document [Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) pour plus d\'informations.


{{Code|lang=text|code=
git checkout myNewBranch
git pull --rebase upstream main
}}

Cette opération va télécharger le code à partir de la branche `main` du dépôt `upstream` (le code source officiel de FreeCAD), et va le fusionner avec celui de votre branche courante (`myNewBranch`), afin que vos modifications apparaissent tout en haut de la liste du dernier code officiel. Si personne n\'a réalisé de modifications dans les fichiers sur lesquels vous avez travaillés, la fusion se fera sans erreurs. Si certains fichiers ont été modifiés en même temps par des personnes différentes, il se peut qu\'il y ait des conflits qui devront être résolus.

                      .A' origin/myNewBranch
                     /
    oZ FreeCAD upstream/main

Pour résumer, vous devez être dans la branche appropriée, faire un \"rebase\" et puis un \"push\".


{{Code|lang=text|code=
git checkout myNewBranch
git pull --rebase upstream main
git push origin myNewBranch
}}

L\'opération `pull` est équivalente à un `fetch` (récupération) suivit d\'un `merge` (fusion). Lorsque l\'option `--rebase` est utilisée, à la place de faire un simple `merge`, c\'est l\'opération `rebase` qui sera exécutée.


{{Code|lang=text|code=
git pull upstream

git fetch upstream
git merge FETCH_HEAD
}}


{{Code|lang=text|code=
git pull --rebase upstream main

git fetch upstream
git rebase main
}}



### Fusion de la branche (pull request) 

Une fois que vous avez validé vos modifications, \"mis à jour\" votre branche à partir du dépôt principal et \"poussé\" votre branche sur le serveur, vous pouvez initier un \"pull request\". Un \"[pull request](https://help.github.com/articles/about-pull-requests/)\" informe les administrateurs du dépôt officiel de FreeCAD que vous souhaitez fusionner le nouveau code de votre branche avec le code officiel.

Pour résumer, le processus de développement ressemble à ceci :

1.  Forkez FreeCAD et faites une copie locale de ce fork.
2.  Créez une branche sur votre fork et passez à cette branche.
3.  Codez ! Commencez à coder autant ou aussi peu que vous le souhaitez, en écrivant de bons messages de validation pour garder une trace de ce que vous faites.
4.  Lorsque vous êtes satisfait de votre travail, utilisez `git rebase -i HEAD~n` (où n est le nombre total de commits que vous avez fait) pour réduire vos commits en un ensemble logique avec de bons messages de commit (chaque message doit commencer par le nom du module qu\'il affecte, par exemple \"Sketcher : make straight lines curve a bit\").
5.  Utilisez GitHub pour soumettre votre code en tant que \"Pull Request (PR)\" comme décrit ci-dessous.

Dès que vous transmettez le code à votre référentiel `origin` {{URLn|https://github.com/GITHUB_USERNAME/FreeCAD}}, GitHub vous offre la possibilité de comparer et de créer une demande d\'extraction par rapport au Référentiel `upstream`. En appuyant sur le bouton **Compare & pull request**, vous ouvrirez une interface qui vous permettra de choisir quel référentiel est la \"base\", cible de la fusion, et quelle est la \"tête\", de votre code supplémentaire. Une vérification rapide sera effectuée par le système vous indiquant s\'il n\'y a pas de conflit avec les fichiers que vous avez modifiés; si vous avez travaillé sur des fichiers que personne n\'a touchés, votre branche pourra fusionner proprement.

GitHub vous montrera un éditeur de texte pour que vous puissiez écrire un message documentant vos modifications : cet éditeur sera pré-rempli avec un message de bienvenue (que vous pouvez supprimer), une liste de contrôle (que vous devez parcourir) et un rappel pour documenter votre modification sur le wiki lorsqu\'elle est acceptée. Pour utiliser la liste de contrôle, passez en revue chaque élément et remplacez `[ ]` par `[X]` pour indiquer que vous avez effectué cette étape. GitHub affichera également le nombre de commits dans votre branche, le nombre de fichiers qui ont été modifiés, ainsi qu\'une vue vous montrant les différences entre la \"base\" et la \"head\" afin que tout le monde puisse immédiatement voir les modifications prévues. Vérifiez que vous n\'avez pas oublié d\'ajouter des lignes vides ou que votre IDE n\'a pas décidé d\'effectuer d\'énormes changements de formatage par devers vous.


{{Code|lang=text|code=
base repository: FreeCAD/FreeCAD    base: main  <  head repository: GITHUB_USERNAME/FreeCAD    compare: myNewBranch

Able to merge. These branches can be automatically merged.
}}

Cliquez sur **Create pull request** pour continuer. Un message apparaîtra indiquant que certaines vérifications doivent être effectuées sur le code. C\'est un système qui compile automatiquement FreeCAD et exécute les tests unitaires. Si les tests réussissent, la demande d\'extraction aura plus de chance d\'être fusionnée dans le code principal, sinon un rapport sera généré indiquant les erreurs rencontrées. Voir [FreeCAD](https://travis-ci.org/FreeCAD/FreeCAD/pull_requests).

    Some checks haven’t completed yet

    * continuous-integration/travis-ci/pr Pending — The Travis CI build is in progress  |Required|

Si les tests réussissent, vous verrez un message tel que le suivant

Tous les tests ont passés

    * continuous-integration/travis-ci/pr — The Travis CI build passed  |Required|

Cette branche n\'a pas de conflits avec la branche de base Seules les personnes ayant un accès en écriture à ce référentiel peuvent fusionner des demandes d\'extraction.

Vous devez maintenant attendre que les administrateurs fusionnent votre branche. vous serez averti lorsque cela se produira.


{{Code|lang=text|code=
Pull request successfully merged and closed

You’re all set — the GITHUB_USERNAME:myNewBranch branch can be safely deleted.
If you wish, you can also delete your fork of FreeCAD/FreeCAD.
}}

Si vous le souhaitez, vous pouvez supprimer la branche qui vient d\'être fusionnée, ou même votre branche entière de FreeCAD, car votre propre code est déjà inclus à la fin de la branche main.


{{Code|lang=text|code=
oZA' FreeCAD upstream/main
}}


**Note:**

vous pouvez continuer à travailler (`git commit -a`) sur la même branche en attendant l\'approbation de la fusion; si vous `git push` à nouveau, une deuxième validation de fusion sera mise en file d\'attente dans la même demande d\'extraction, et un autre test automatisé sera effectué. En d'autres termes, même si vos administrateurs n'approuvent pas encore vos fusions, vous pouvez continuer à appliquer des modifications à votre référentiel `origin`, ce qui mettra ces commits en file d\'attente dans la même demande d\'extraction du référentiel `en amont`. L\'utilisation d\'une seule demande d\'extraction pour mettre en file d\'attente plusieurs commits individuels est souvent souhaitable pour de petites modifications. Pour les ajouts importants au code source, vous devez créer une autre branche, d\'y développer vos fonctionnalités, puis soumettre une demande d\'extraction distincte pour cette branche.

L\'interface de requête d\'extraction peut être utilisée chaque fois que vous souhaitez soumettre du code à partir de vos propres référentiels vers un autre référentiel de GitHub. Vous pouvez également l\'utiliser pour fusionner du code dans la direction opposée, des branches d\'autres personnes à la vôtre, ou même entre vos propres branches. Dans le dernier cas, puisque vous possédez les branches, les fusions peuvent être approuvées par vous-même immédiatement.


{{Code|lang=text|code=
base repository: SomeProject/Some_Software  base: main       <  head repository: GITHUB_USERNAME/Some_Software  compare: add_new_functions
base repository: GITHUB_USERNAME/FreeCAD    base: myNewBranch  <  head repository: FreeCAD/FreeCAD                compare: main
base repository: GITHUB_USERNAME/FreeCAD    base: myNewBranch  <  head repository: GITHUB_USERNAME/FreeCAD        compare: fix-many-bugs-branch
}}



### Maintien du dépôt GitHub à jour 

Une fois que vous avez créé FreeCAD, votre référentiel personnel existe indépendamment de l\'original. Lorsque le référentiel d\'origine comporte de nouveaux commits, GitHub vous informera que votre référentiel personnel est en retard sur le nombre de commits:


{{Code|lang=text|code=
This branch is 5 commits behind FreeCAD:main.
}}

De la même manière, si vous avez créé une branche de développement avec un nouveau code, GitHub vous informera que cette branche est en avance en nombre de validations; c\'est-à-dire que cette branche contient des modifications qui n\'ont pas été fusionnées dans le référentiel officiel de FreeCAD:


{{Code|lang=text|code=
This branch is 3 commits ahead of FreeCAD:main.
}}

Pendant le développement, les deux cas sont possibles, car votre propre branche peut ne pas avoir de commits faits par d'autres développeurs, mais inclure de nouveaux commits de votre part:


{{Code|lang=text|code=
This branch is 2 commits ahead, 14 commits behind FreeCAD:main. 
}}

Lors du développement du code, il est recommandé de rebaser la branche dans laquelle vous travaillez car cela mettra votre branche toujours devant le code main de FreeCAD.

Quant à votre branche originale `main`, elle ne sera jamais automatiquement mise à jour par GitHub. C\'est quelque chose que vous devez faire vous-même. Passez à la branche `main`, puis `pull` à partir de `upstream` (ce qui qui effectue un `fetch` et `merge`), puis poussez cette branche `main` mise à jour vers votre dépôt distant `origin`.


{{Code|lang=text|code=
git checkout main
git pull upstream main
git push origin main
}}

Une fois cela fait, GitHub vous indiquera que vous êtes synchronisé avec le référentiel `upstream`.


{{Code|lang=text|code=
This branch is even with FreeCAD:main. 
}}

Maintenant que votre `main` est à jour, vous pouvez décider de le changer et de supprimer l'autre branche que vous avez utilisée précédemment pour développer une fonctionnalité.


{{Code|lang=text|code=
git checkout main
git branch -d myNewBranch
}}

Pour supprimer la branche du référentiel distant `origin`, vous pouvez utiliser l\'opération `push`. Normalement, vous poussez une branche locale; cela crée une branche distante portant le même nom que votre branche locale.


{{Code|lang=text|code=
git push origin myNewBranch
}}

Toutefois, si vous utilisez la notation `local_name:remote_name`, la branche locale est créée dans le référentiel distant sous un nom différent:


{{Code|lang=text|code=
git push origin myNewBranch:someRemoteBranch
}}

Par conséquent, vous pouvez supprimer la branche distante en poussant une branche locale vide:


{{Code|lang=text|code=
git push origin :myNewBranch
git push origin :someRemoteBranch
}}

Maintenant que vous ne disposez que d\'un `main` à jour, vous pouvez créer une nouvelle branche et répéter les étapes de modification de fichiers, de validation, d\'insertion, de soumission d\'une demande d\'extraction, de fusion et de mise à jour.


{{Code|lang=text|code=
git checkout main
git checkout -b anotherBranch
}}

Si vous ne souhaitez pas supprimer votre branche déjà personnalisée, vous pouvez forcer la mise à jour pour correspondre à la valeur de la mise à jour `main`. Vous pouvez ensuite faire ce que vous voulez, y compris ajouter plus de commits et le pousser dans le dépôt distant `origin`.


{{Code|lang=text|code=
git checkout myNewBranch
git reset --hard main
git push -f origin myNewBranch
}}

Réinitialiser une branche comme ceci n'est généralement pas nécessaire. Dans la plupart des cas, vous souhaitez suivre la séquence de création d\'une nouvelle branche, de validation des modifications, de transmission de ces modifications, de fusion de la branche, puis de suppression de la branche.



## Opérations git avancées 



### Rechercher

Quelques outils pratiques pour vous aider à trouver ce que vous cherchez:



#### Rechercher les noms de fichiers 

Utilisez `git ls-files` pour rechercher dans le dépôt un fichier contenant une certaine chaîne dans un nom de fichier. L\'exemple ci-dessous renverra toutes les instances des fichiers contenant \'dxf\' dans leurs noms de fichiers.


{{Code|lang=text|code=
git ls-files *dxf*
}}



#### Rechercher une chaîne 

Utilisez `git grep` pour rechercher dans le dépôt un fichier contenant une certaine chaîne avec les fichiers eux-mêmes. L\'exemple ci-dessous renverra toutes les instances des fichiers qui contiennent \'dxf\' dans chaque fichier.


{{Code|lang=text|code=
git grep dxf
}}



### Résolution des conflits de fusion 

La fusion de branches avec `git merge` ou la redistribution de votre branche avec `git rebase` présente parfois des conflits de fichiers pouvant avoir été modifiés par un autre auteur en même temps. Si cela se produit, vous devriez voir les modifications des deux côtés, de l\'autre auteur et du vôtre, puis décider de la meilleure façon d\'inclure les deux ensembles de modifications. Ceci est normalement un processus manuel qui ne peut pas être automatisé; le programmeur doit comprendre le code et décider du code à déplacer, réécrire ou abandonner pour résoudre le conflit.

Lorsqu\'un conflit survient, un message comme celui-ci peut apparaître.


{{Code|lang=text|code=
CONFLICT (content): Merge conflict in src/Mod/source_code.py
error: Failed to merge in the changes.
Patch failed at 1234 Some commit message when editing source_code.py
}}

Si un outil de différenciation spécialisé est installé et configuré pour Git, par exemple, celui de Gnome [Meld](https://wiki.gnome.org/Apps/Meld), le conflit peut être examiné et résolu en utilisant l\'opération `mergetool`..


{{Code|lang=text|code=
git mergetool
}}

L\'outil de fusion affiche normalement trois colonnes; les deux colonnes sur les côtés affichent les deux fichiers en conflit, tandis que la colonne du milieu affiche le nouveau code qui sera enregistré et finalement validé. Par conséquent, cette colonne centrale doit être modifiée de manière à intégrer le code des deux colonnes latérales. Une fois le conflit résolu et le nouveau code source (la colonne centrale) enregistré, vous pouvez fermer l'outil de fusion. Ensuite, l\'opération `merge` ou `rebase` peut continuer.


{{Code|lang=text|code=
git merge --continue
git rebase --continue
}}

Pour plus d\'informations sur la fusion et la résolution des conflits, voir:

-   [explications git-scm sur la manière dont les conflits sont présentés](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented) avec `git merge`.
-   [Conflits de fusion élémentaires](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts) et [Outils Git - Fusion avancée](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging)
-   [Article de GitHub sur la résolution des problèmes de fusion par la ligne de commande](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/).
-   [Personnalisez votre outil de fusion préféré](https://git-scm.com/book/fr/v2/Customizing-Git-Git-Configuration#_external_merge_tools) lorsque vous rencontrez un conflit entre plusieurs git.



### Inspecter les changements 

Inspectez l\'historique des modifications apportées à un fichier qui a subit plusieurs \"commits\" avec l\'opération `log`:


{{Code|lang=text|code=
git log --patch path
}}

Où `path` peut être n\'importe quel répertoire ou fichier. Au lieu de `--patch`, vous pouvez également utiliser les raccourcis `-p` ou `-u`.



### Inspecter les changements entre deux branches 

Inspectez les modifications entre deux branches avec les opérations `log` et `diff` avec les noms des branches:


{{Code|lang=text|code=
git log main..myBranch
git diff main..myBranch
}}

L\'opération `log` affiche les validations, tandis que `diff` indique les modifications réelles apportées aux fichiers.



### Réinitialiser les fichiers et les répertoires 

Si vous avez accidentellement apporté des modifications à un fichier ou à un répertoire, vous souhaiterez peut-être annuler complètement ces modifications pour obtenir l\'état précédent du code source.

Cela peut être fait rapidement en utilisant l\'opération `checkout`:


{{Code|lang=text|code=
git checkout path
git checkout .
}}

Cela restaurera le `path` (un fichier ou un répertoire) à l\'état dans lequel il se trouve à l\'extrémité de la branche, en ignorant les modifications qui n\'ont pas été validées. Si `path` est le point unique `.`, Tous les fichiers du répertoire en cours seront restaurés.

Si vous avez accidentellement ajouté des fichiers et des répertoires, vous pouvez utiliser l\'opération `clean`:


{{Code|lang=text|code=
git clean -df
}}

Ceci forcera la suppression de tous les fichiers et répertoires (`-df`) qui ne font pas l\'objet d\'un suivi par le référentiel, c\'est-à-dire ceux qui n\'ont pas été inclus précédemment avec l\'opération `add`.

Pour réinitialiser complètement le référentiel en perdant toutes les modifications non validées, utilisez l\'opération `reset`:


{{Code|lang=text|code=
git fetch
git reset --hard FETCH_HEAD
}}

Où `FETCH_HEAD` est la pointe du référentiel `upstream`. Un autre commit peut également être utilisé.

L\'opération `revert` annule également les modifications. Cependant, cette commande fait cela en ajoutant un autre commit à l\'historique; dans de nombreux cas, cela n\'est pas souhaité.



### Taille des vieilles branches 

Si vous avez engagé de nombreuses branches dans le référentiel `upstream`, vous souhaiterez peut-être supprimer ces branches de votre système local car elles ont déjà été fusionnées. La branche en ligne du référentiel `origin` peut être supprimée immédiatement après la fusion. Ensuite, vous pouvez supprimer les références locales à cette branche en utilisant les options `--prune` ou `prune` pour les opérations `fetch` et `remote`.


{{Code|lang=text|code=
git fetch --prune origin
git remote prune origin
}}

Enfin, vous pouvez supprimer les branches localement


{{Code|lang=text|code=
git branch -D myBranch
}}

Après un certain temps, il est également recommandé de procéder à la récupération d\'espace disque, en utilisant l\'opération `gc`. Cela supprimera les fichiers inutiles et compressera les révisions de fichiers locaux, afin d\'optimiser l\'utilisation du disque local du référentiel.


{{Code|lang=text|code=
git gc
}}



### Travailler avec des patchs 

Bien que Git vous permette de fusionner le code de différentes branches localement sur votre ordinateur via la commande `git merge` ou d\'effectuer un \"pull request\" sur le serveur distant (remote repository), il est parfois préférable de créer un patch qui peut être envoyé en tant que pièce jointe par e-mail au lieu de soumettre un PR. Le flux de travail suivant explique comment procéder:



### Création de correctifs 

-   Il est conseillé de travailler dans une nouvelle branche et non pas directement sur la branche main de votre dépôt. La première étape consiste donc à s\'assurer que vous êtes dans la bonne branche et le cas échéant à s\'y raccorder. Les commandes suivantes permettent de réaliser ces opérations :


{{Code|lang=text|code=
git branch -v
git checkout myBranch
}}

-   Maintenant, utilisez `git format-patch` sur la branche main et utilisez l\'option `--stdout` pour rediriger le résultat vers la sortie standard, puis redirigez la sortie standard vers un fichier, qui pour des raisons de commodité est créé au-dessus du répertoire du code source.


{{Code|lang=text|code=
git format-patch main --stdout > ../myCode.patch
}}

-   Une autre méthode


{{Code|lang=text|code=
git format-patch HEAD^
git format-patch HEAD~1
}}

Le nombre d\'accents circonflexes `^` ou le nombre situé derrière le tilde \~ `1` indique le nombre de \"commits\" qui devront être considérés, à savoir par exemple `^^^` ou `~3` va créer 3 correctifs pour 3 \"commits\".


{{Code|lang=text|code=
git format-patch HEAD^
}}

Cette commande va créer un \"patch\" ou une série de \"patchs\" en respectant la convention de nommage suivante :


{{Code|lang=text|code=
XXXX-commit-message.patch
}}

où `XXXX` est un nombre compris entre `0000` et `9999`, et où le message du \"commit\" forme la majorité du nom du fichier, par exemple :


{{Code|lang=text|code=
0001-fix-ViewProjMatrix-getProjectionMatrix.patch
}}



### Application des correctifs 

Git a la capacité de fusionner des correctifs/diffs. Pour en savoir plus à ce sujet, lisez la référence suivante: [Application des patches avec Git](https://www.drupal.org/node/1399218)

Si vous avez déjà le fichier du correctif dans votre système, il suffit juste de l\'appliquer.


{{Code|lang=text|code=
git apply myCode.patch
}}

Vous pouvez utiliser `curl` pour télécharger un correctif depuis un site web, et ensuite l\'appliquer via la commande `git`.


{{Code|lang=text|code=
curl -O https://some.website.org/code/myCode.patch
git apply myCode.patch
}}

Conseil utile: ajoutez simplement .diff ou .patch à la fin de l\'URL d\'une page de validation GitHub, d\'une demande d\'extraction ou d\'une vue de comparaison et vous obtiendrez une vue de cette page. Exemple:

-   Page GitHub pour un \"commit classique\" : {{URL|https://github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621}}
-   Page GitHub pour un \"Diff\" : {{URL|https://github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.diff}}
-   Page GitHub pour un correctif : {{URL|https://github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.patch}}

Vous pouvez pointer `curl` vers le \"commit\" d\'un correctif particulier dans un dépôt, et le faire suivre directement vers `git` pour appliquer le correctif.

    curl https://github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.patch | git apply -



### Inverser un patch 

Lorsque vous appliquez un correctif, vous modifiez certains fichiers. Cependant, ces modifications ne sont pas permanentes tant que vous n\'avez pas validé les modifications. Par conséquent, si vous souhaitez rétablir un correctif, utilisez les instructions suivantes.

Cette commande annulera les modifications qui ont été appliquées, si vous avez toujours accès au fichier original du correctif:


{{Code|lang=text|code=
git apply -R myCode.patch
}}

Cette commande alternative enlèvera toutes les modifications non validées dans la branche.


{{Code|lang=text|code=
git checkout -f
}}



## Stockage temporaire dans le cache des git commits 

Supposons que vous travaillez sur une branche et que vous apportiez des modifications à la source qui sortent du cadre de votre branche actuelle; autrement dit, ces changements seraient meilleurs dans une autre branche que dans la branche actuelle. La commande `git stash` peut être utilisée pour stocker temporairement ces modifications locales non validées.


{{Code|lang=text|code=
git stash
}}

Si à l\'avenir vous souhaitez utiliser ces commits, vous pouvez les *extraire* de la réserve puis dans votre branche active.


{{Code|lang=text|code=
git stash pop
}}

Ou si vous décidez que vous n\'aimez plus ces commits sauvegardés, vous pouvez les supprimer complètement de la réserve.


{{Code|lang=text|code=
git stash drop
}}

Vous pouvez lister plusieurs commits stash avec


{{Code|lang=text|code=
git stash list
}}

Pour en savoir plus, lisez [Useful tricks you might not know about Git stash](https://medium.freecodecamp.org/useful-tricks-you-might-not-know-about-git-stash-e8a9490f0a1a).



### Vérifier sur GitHub les demandes locales 

[Checkout GitHub pull requests locally](https://gist.github.com/piscisaureus/3342247)



### Blâme


**Section TBD**

Ajouter du contenu depuis <https://forum.freecadweb.org/viewtopic.php?f=23&t=55943&p=481483#p481287>



### Dichotomie


`git bisect`

est une méthode pour trouver la livraison (commit) spécifique qui a introduit un bug.

Vous devez trouver 2 livraisons :

-   Une bonne livraison (par exemple `abcd`) avant que le système ne soit cassé.
-   Une mauvaise livraison (par exemple `efgh`) après la panne du système.

Puis entrez ceci depuis le terminal :


{{Code|lang=text|code=
git bisect start
git bisect good abcd
git bisect bad efgh
}}

Résultat : `git` vérifiera le point médian entre les deux livraisons .

L\'étape suivante consiste à construire et à tester le code. Si le système fonctionne, continuez le processus en tapant :


{{Code|lang=text|code=
git bisect good
}}

Répétez l\'étape précédente qui consiste à builder le code et à le tester.

Si le système est cassé, tapez :


{{Code|lang=text|code=
git bisect bad
}}

Répétez les étapes précédentes en appliquant `good` ou `bad` selon le résultat de vos tests.

Éventuellement, `git` vous dira que `wxyz` est la première mauvaise livraison.

Enfin, pour quitter le processus de dichotomie, tapez :


{{Code|lang=text|code=
git bisect reset
}}

Remarque : `git bisect` prend beaucoup de temps si la bonnne et la mauvaise livraison sont très éloignées.



## Numéro de révision FreeCAD 

Contrairement à Subversion qui incrémente le numéro de révision, Git génère une [valeur de hachage SHA-1](https://en.wikipedia.org/wiki/SHA-1) à chaque \"commit\". Une valeur de hachage est une longue chaîne de caractères alphanumériques qui ressemble à ceci :


{{Code|lang=text|code=
9b3ffef570596e184006287434fba54a4b03ccc3
}}



### Quelle est la dernière révision de FreeCAD Dev ? 

Pour trouver le dernier numéro de révision d\'une branche particulière, utilisez l\'opération `rev-list` avec l\'option `--count`. Donnez le nom de la branche, du référentiel distant, de la balise ou un pointeur spécial tel que `HEAD`, pour indiquer le dernier commit dans cet objet particulier.


{{Code|lang=text|code=
git rev-list --count main
git rev-list --count HEAD
git rev-list --count origin
}}

ou parcourez [le dépôt sur GitHub](https://github.com/FreeCAD/FreeCAD) et lisez le nombre de mises à jour (commits) effectuées dans la branche correspondante.



### Quel est le numéro de révision correspondant à la valeur de hachage d\'un \"commit\" ? 

Comme la valeur de hachage est une chaîne de caractères alphanumériques, il n\'est pas très utile de savoir si un \"commit\" est plus ancien ou plus récent qu\'un autre. Pour trouver le numéro de révision correspond à une valeur de hachage particulière, utilisez à nouveau l\'opération `rev-list`; l\'entrée peut être la valeur de hachage complète ou une valeur de hachage partielle qui est unique, généralement les 7 premiers chiffres sont suffisants.


{{Code|lang=text|code=
git rev-list --count ab1520b872821414c6ce4a15fb85d471ac2a2b03
git rev-list --count 9948ee4
}}



### Quel est la valeur de hachage correspondante au numéro de révision d\'un \"commit\" ? 

Si nous avons un \"commit\" qui porte le numéro 15000 et que nous voulons trouver la valeur de hachage correspondante, nous allons avoir besoin de calculer le nombre de \"commits\" réalisés entre ce \"commit\" et le dernier \"commit\" (`HEAD`). Dans un premier temps, cherchons le numéro du dernier \"commit\".


{{Code|lang=text|code=
git rev-list --count HEAD
17465
}}

Puis, soustrayons à ce résultat le \"commit\" que nous voulons.


{{Code|lang=text|code=
17465 - 15000 = 2465
}}

Puis, utilisez la commande `log` pour afficher la liste des \"commits\" et des valeurs de hachage. L\'option `--skip` permet de sauter la différence dans les \"commits\" que nous avons calculez, ce qui nous permet d\'aller directement à la valeur de hachage que nous recherchons.


{{Code|lang=text|code=
git log --skip=2465
commit 44c2f19e380e76b567d114a6360519d66f7a9e24
}}

Il se peut que le résultat vous affiche 2 \"commits\" assez proches, confirmez que ce soit le bon numéro de \"commit\". Si ce n\'est pas le cas, choisissez simplement le prochain \"commit\" dans la séquence (avant ou après) et vérifiez à nouveau.


{{Code|lang=text|code=
git rev-list --count 44c2f19e38
15000
}}

-   [Show the commits](https://forum.freecadweb.org/viewtopic.php?f=10&t=26673) juste avant un commit particulier dans GitHub: dans la barre d'adresse du navigateur, changez le mot `commit` par `commits` pour afficher la liste.
-   [Trouver le numéro de révision du commit](https://forum.freecadweb.org/viewtopic.php?t=5308)
-   [Trouver le numéro de révision du commit](https://forum.freecadweb.org/viewtopic.php?f=18&t=12883&p=103207#p103203)
-   [Recherche de la valeur de hachage correspondante pour un numéro de validation particulier](https://forum.freecadweb.org/viewtopic.php?f=10&t=31118)



### Comment le numéro de révision dans l\'aide de FreeCAD est-il généré ? 

Le numéro de version qui apparait avec l\'outil [Std About](Std_About/fr.md) est définit dans le fichier `src/Build/Version.h`, qui est créé au moment de la compilation lorsque l\'outil `cmake` est exécuté. Lisez le post [Extract version number from git source](https://forum.freecadweb.org/viewtopic.php?f=4&t=3025) pour plus d\'informations.



## Ajout d\'autres référentiels (distants) 

Plusieurs collaborateurs du projet FreeCAD ont leurs propres référentiels Git où ils développent leur travail où ils expérimentent de nouvelles idées avant d\'être prêts à être inclus dans le code source officiel. Vous voudrez peut-être obtenir leurs sources afin de tester leur code vous-même lorsqu\'ils font une demande d\'extraction.

Utilisez la commande `git remote` pour ajouter ces autres référentiels afin que vous puissiez `fetch` (récupérer) et `pull` (pousser) suivre leurs codes.


{{Code|lang=text|code=
git checkout main
git remote add OTHER_USER OTHER_URL
git fetch OTHER_USER
git checkout -b OTHER_BRANCH OTHER_USER/OTHER_BRANCH
}}

Par exemple, ajoutons le dépôt de Bernd:


{{Code|lang=text|code=
git remote add bernd http://github.com/berndhahnebach/FreeCAD_bhb
}}

La commande `git fetch` télécharge les références à partir de ce dépôt distant.


{{Code|lang=text|code=
git fetch bernd
}}

Répertoriez toutes les branches de votre propre dépôt et celles de vous avez ajoutées. Les branches de Bernd s\'afficheront sous la forme `remotes/bernd/<branchname>`.


{{Code|lang=text|code=
git branch -a
}}

Maintenant, regardons une liste résumée des 10 derniers commits de la branche `femdev` de Bernd.


{{Code|lang=text|code=
git log -10 --oneline remotes/bernd/femdev
}}

Maintenant, nous pouvons vérifier la branche à inspecter.


{{Code|lang=text|code=
git checkout remotes/bernd/femdev
}}

Ensuite, nous pouvons créer une branche locale basée sur la branche distante. Cette branche locale, nous pouvons la modifier et y ajouter notre propre code.


{{Code|lang=text|code=
git checkout -b local_branch_name /remotes/bernd/femdev
}}

Vous pouvez souhaiter `git rebase` la branche nouvellement obtenue sur la branche `upstream/main` pour vous assurer qu\'elle utilise le dernier code. S\'il y a des conflits, ils devront être traités à ce stade.


{{Code|lang=text|code=
git pull --rebase upstream main
}}

La nouvelle branche est prête à être modifiée et compilée comme décrit dans [Compiler](Compiling/fr.md).

Dirigez vous vers la section de développement du [forum FreeCAD](https://forum.freecadweb.org/viewforum.php?f=6) pour discuter du développement.



## Lecture complémentaire 

-   [Développer FreeCAD avec GitKraken](Developing_FreeCAD_with_GitKraken/fr.md), un guide pour utiliser l\'interface graphique avec Git.
-   [Git pour les paresseux](https://wiki.spheredev.org/index.php/Git_for_the_lazy), un guide très concis des principales commandes de `git`.
-   Le [Pro Git book](https://git-scm.com/book) livre open source vous enseignant Git; il est disponible en versions électronique et imprimée.
-   Le [Visual Git guide](https://marklodato.github.io/visual-git-guide), une référence avec des diagrammes expliquant les opérations les plus courantes avec Git.
-   [Git Tutorial for Beginners: Command-Line Fundamentals](https://www.youtube.com/watch?v=HVsySz-h9r4), vidéo de Corey Schafer.
-   [Introduction to Git - Core Concepts](https://www.youtube.com/watch?v=uR6G2v_WsRA), vidéo de David Mahler.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Source code management/fr
