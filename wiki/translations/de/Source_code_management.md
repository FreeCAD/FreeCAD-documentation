# Source code management/de
{{TOCright}}

## Einführung

Das Haupt Quellcode Verwaltungswerkzeug für das FreeCAD Projekt ist [Git](http   *//en.wikipedia.org/wiki/Git_%28software%29), das in den meisten Betriebssystemen einfach über einen Paketmanager oder direkt von der Website von [Git](https   *//git-scm.com/) installiert werden kann. Es wird empfohlen, sich mit Git vertraut zu machen, bevor du direkt mit dem FreeCAD Quellcode arbeitest. Besuche die Seite [Git Dokumentation](https   *//git-scm.com/doc) für das Referenzhandbuch sowie das [Pro Git Buch](https   *//git-scm.com/book/en/v2), um zu lernen, das System allgemein zu nutzen. Das vorliegende Dokument konzentriert sich auf die Verwendung von Git für die FreeCAD Entwicklung. Die Kompilierung von FreeCAD ist unter [Kompilieren](Compiling/de.md) beschrieben.

Während Git in erster Linie eine Terminalanwendung ist, gibt es viele grafische Anwendungen, die die Arbeit mit Zweigen, das Anwenden von Patches und das Senden von Pull Anfragen an einen Master Zweig erleichtern. Beispiele sind [gitk](https   *//git-scm.com/docs/gitk) (die erste entwickelte grafische Benutzeroberfläche),[gitg](https   *//wiki.gnome.org/Apps/Gitg/) (Gnome),[qgit](https   *//github.com/tibirna/qgit) (Qt), [tig](https   *//jonas.github.io/tig/) (Ncurses), [git-cola](http   *//github.com/git-cola/git-cola) und [GitKraken](https   *//www.gitkraken.com/) (proprietär). Eine kurze Einführung in dieses Werkzeug findest Du unter [Entwicklung von FreeCAD mit GitKraken](Developing_FreeCAD_with_GitKraken/de.md).

Hinweis   * Wenn dir davon schwindelig wird, gibt es eine sehr gute nicht-technische Serie über die Verwendung von Git und Github mit dem Titel \'[Git und Github für Dichter](https   *//youtu.be/BCQHnlnPusY)\'.

## Quellcodezugang

Jeder kann auf den FreeCAD Quellcode zugreifen und eine Kopie davon bekommen, aber nur die FreeCAD Projektmanager haben Schreibzugriff darauf. Du kannst eine Kopie des Codes erhalten, ihn studieren und nach Belieben ändern, aber wenn du möchtest, dass deine Änderungen in den offiziellen Quellcode aufgenommen werden, musst du eine \"Pull Anfrage\" gegen das Haupt Repositorium durchführen, damit deine Änderungen von den Verwaltern überprüft werden können. Diese Art der Entwicklung ist bekannt als der [Dictator and Lieutenants Workflow](https   *//git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows), da die Kern Entwickler (Diktatoren) und betrauten Entwickler (Leutnante) den Code filtern, der von unabhängigen Entwicklern und Benutzern eingereicht wird.

Wenn deine Quellcode Änderungen signifikant sind, empfehlen wir dir, sie im Pull Request Abschnitt des [FreeCAD-Forum](http   *//forum.freecadweb.org/viewforum.php?f=17) zu erklären.

<img alt="" src=images/FreeCAD_git_workflow.svg  style="width   *600px;"> 
*Typischer Arbeitsablauf zur Entwicklung von Code für FreeCAD; jeder kann den Code aus dem Haupt Repositorium beziehen, aber die Hauptentwickler haben das exklusive Recht, Eingaben anderer Entwickler zu überprüfen und zusammenzuführen.*


<div class="mw-translate-fuzzy">

### Offizielles GitHub Repositorium 

Der FreeCAD Quellcode wird in Github bereitgestellt, {{URL|https   *//github.com/FreeCAD/FreeCAD}}


</div>

The FreeCAD source code is hosted on Github, {{URL|https   *//github.com/FreeCAD/FreeCAD}}

Um Code beitragen zu können, benötigst Du ein [GitHub Konto](https   *//github.com/join).

In der Vergangenheit wurde der Quellcode in einem SVN Repositorium bereitgestellt, {{URL|https   *//free-cad.svn.sourceforge.net/svnroot/free-cad}}. Dieser wurde am 10. Oktober 2011 mit [commit 120ca87015](https   *//github.com/FreeCAD/FreeCAD/commit/120ca87015) nach GitHub verschoben.

   *   Daher gibt es viele Änderungen, die vor dieser Zeit vorgenommen wurden, die nicht in der modernen Git Commit Geschichte aufgezeichnet sind. Lies mehr dazu auf der Seite [Geschichte](History/de.md).

### Setzen des Git Benutzernamens 

Entwickler sollten Code in ihr persönliches Projektarchiv mit ihrem GitHub Benutzernamen eintragen. Wenn dieser nicht bereits global gesetzt ist, kannst du ihn lokal für das aktuelle Git Projektarchiv wie folgt setzen   *


{{Code|lang=text|code=
git config user.name "YOUR_NAME"
git config user.email GITHUB_USERNAME@users.noreply.github.com
}}

Wobei `"YOUR_NAME"` deinen vollständigen Namen oder Spitznamen darstellt, der zur Identifizierung des Autors eines bestimmten Einsatzes verwendet wird, und `GITHUB_USERNAME` den Namen deines Accounts auf GitHub angibt.

### Remote repositories 


<div class="mw-translate-fuzzy">

### Fernrepositorien

Bitte lies [Was ist der Unterschied zwischen Ursprung und Upstream auf GitHub?](https   *//stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-on-github#9257901) (Stackoverflow) um den Unterschied zwischen `origin` und `upstream` im Kontext von Git zu verstehen. Dieser Abschnitt erklärt, wie man die richtigen Repositorien für die Entwicklung festlegt. Im Wesentlichen   *

-    `origin`ist deine persönliche Abspaltung des offiziellen FreeCAD Repositoriums, also {{URL|https   *//github.com/GITHUB_USERNAME/FreeCAD}}

-    `upstream`ist das offizielle FreeCAD Repositorium, d.h. {{URL|https   *//github.com/FreeCAD/FreeCAD}}


</div>

Diese Unterscheidung ist wichtig, da du zuerst Code in deine eigene Kopie des Repositoriums schreiben solltest, bevor du diese Änderungen in das offizielle Repositorium schreibst.

Basierend auf dem oben genannten, gibt es zwei Möglichkeiten, deine Git Entwicklungsumgebung einzurichten   *

-   1\. Methode   * Verzweigung auf GitHub und klone deine Verzweigung lokal
-   2\. Methode   * Klone FreeCAD direkt auf deinen lokalen Rechner und passe die entfernten Server an

Wir empfehlen die 1. Methode, weil sie einen Schritt schneller ist.


<div class="mw-collapsible mw-collapsed toccolours">

#### 1. Methode   * Verzweigung auf GitHub und klone deine Abspaltung lokal 

=


<div class="mw-collapsible-content">

Zuerst teile das FreeCAD Repositorium in GitHub ab, dann klone diese persönliche Abspaltung auf deinen Computer, und schließlich lege das `upstream` Repositorium fest.

-   [Anmelden](https   *//github.com/join) auf dein GitHub Konto.
-   Gehe zum offiziellen FreeCAD Repositorium   * {{URL|https   *//github.com/FreeCAD/FreeCAD}}
-   Drücke oben rechts auf der Seite die Taste \"Fork\". Dadurch wird eine persönliche Kopie des FreeCAD Repositoriums unter deinem GitHub Benutzernamen erstellt   * {{URLn|https   *//github.com/GITHUB_USERNAME/FreeCAD}}
-   Klone auf deinem Rechner deine neu erstellte FreeCAD Fork. Er wird in einem Verzeichnis `freecad-source` erstellt.


{{Code|lang=text|code=
git clone https   *//github.com/GITHUB_USERNAME/FreeCAD.git freecad-source
}}

-   Sobald der Download abgeschlossen ist, gib das neue Quellverzeichnis ein und lege das `upstream` Repositorium fest.


{{Code|lang=text|code=
cd  freecad-source
git remote add upstream https   *//github.com/FreeCAD/FreeCAD.git
}}

-   Bestätige deine Fernrepositorien mit `git remote -v`; die Ausgabe sollte ähnlich wie diese sein


{{Code|lang=text|code=
origin  https   *//github.com/GITHUB_USERNAME/FreeCAD.git (fetch)
origin  https   *//github.com/GITHUB_USERNAME/FreeCAD.git (push)
upstream    https   *//github.com/FreeCAD/FreeCAD.git (fetch)
upstream    https   *//github.com/FreeCAD/FreeCAD.git (push)
}}

-   Jetzt kann die Entwicklung beginnen.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

#### 2. Methode   * Klone FreeCAD direkt auf deinen lokalen Rechner 


<div class="mw-collapsible-content">

Zuerst wirst du das FreeCAD Repositorium in GitHub abspalten (engl.   *fork ‚Gabel'), jedoch wirst du das ursprüngliche FreeCAD Repositorium auf deinen lokalen Rechner klonen und dann deine Fernbedienungen über das Terminal ändern.

-   [Anmelden](https   *//github.com/join) auf dein GitHub Konto.
-   Gehe zum offiziellen FreeCAD Repositorium   * {{URL|https   *//github.com/FreeCAD/FreeCAD}}
-   Klicke oben rechts auf der Seite auf die \"Fork\" Schaltfläche. Dadurch wird eine persönliche Kopie des FreeCAD Repositoriums unter deinem GitHub Benutzernamen erstellt   * {{URLn|https   *//github.com/GITHUB_USERNAME/FreeCAD}}
-   Klone das ursprüngliche FreeCAD Repositorium. Es wird in einem Verzeichnis `freecad-source` erstellt.


{{Code|lang=text|code=
git clone https   *//github.com/FreeCAD/FreeCAD.git freecad-source
}}

-   Sobald das Herunterladen abgeschlossen ist, gib das neue Quellverzeichnis ein und lege das `Ursprung`s Repositorium fest.


{{Code|lang=text|code=
cd freecad-source
git remote add origin https   *//github.com/GITHUB_USERNAME/FreeCAD.git
}}

-   Richte dann das `upstream` Repositorium ein.


{{Code|lang=text|code=
git remote add upstream https   *//github.com/FreeCAD/FreeCAD.git
}}

-   Bestätige deine Fernrepositorien mit `git remote -v`; die Ausgabe sollte ähnlich wie diese sein


{{Code|lang=text|code=
origin  https   *//github.com/GITHUB_USERNAME/FreeCAD.git (fetch)
origin  https   *//github.com/GITHUB_USERNAME/FreeCAD.git (push)
upstream    https   *//github.com/FreeCAD/FreeCAD.git (fetch)
upstream    https   *//github.com/FreeCAD/FreeCAD.git (push)
}}

-   Jetzt kann die Entwicklung beginnen.


</div>


</div>

Wenn die Fernrepositorien aus irgendeinem Grund zwar existieren, aber auf die falsche Adresse verweisen, kannst du die Situation durch Umbenennen des Namens des entfernten Repositoriums beheben. Beispielsweise sollte `Ursprung` auf deine persönliche Abspaltung zeigen; wenn er auf das ursprüngliche FreeCAD Repositorium zeigt, ändere den Namen dieses Fernrepositoriums in `upstream` und füge das `Ursprung`s Repositorium manuell hinzu.


{{Code|lang=text|code=
git remote rename origin upstream
git remote add origin https   *//github.com/GITHUB_USERNAME/FreeCAD.git
git remote -v
}}

Du kannst auch weitere Informationen mit dem Schlüsselwort `anzeigen` anzeigen.


{{Code|lang=text|code=
git remote show origin
git remote show upstream
}}

## Git development process 


<div class="mw-translate-fuzzy">

## Git Entwicklungsprozess 


**Niemals auf deinem lokalen ''Master' Zweig entwickeln. Erstelle stattdessen einen lokalen Zweig für die Entwicklung, und führe diesen lokalen Zweig dann über eine Pull Anforderung mit dem vorgeschalteten Master Zweig zusammen. Lies bitte [https   *//git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell Git Verzweigung], [https   *//book.git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging Grundlegende Verzweigung und Zusammenführung] und [https   *//git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project GitHub - An einem Projekt mitwirken], um mehr zu erfahren.**


</div>

<img alt="" src=images/FreeCAD_git_branches_workflow.svg  style="width   *800px;"> 
*Generischer Arbeitsablauf zur Entwicklung von Code für FreeCAD unter Verwendung von `git*; das Haupt Repositorium wird online gespalten und auf einen Offline Rechner geklont (0); neue Zweige (1) werden verwendet, um lokale Änderungen und Ergänzungen des Codes zu übergeben (2); die Zweige werden auf den neuesten Online Code zurückgeführt (3), und dann zum entfernten Repositorium geschoben (4); dann wird eine Pull Anfrage erstellt, um den Code in das Haupt Repositorium einzufügen (5). Dann wird der persönliche Klon mit dem neuen Mastercode aktualisiert (a); dieser aktualisierte Mastercode wird ebenfalls an das Fernrepositorium (b) geschickt, um denselben Code sowohl online als auch offline zu haben.`

### Verzweigung

Anstatt an der Masterversion des Codes zu arbeiten, empfiehlt die bewährte Methode mit Git die Erstellung eines neuen Zweiges, wann immer du an einer neuen Funktion arbeiten willst. Zweige sind kostengünstig, sie kopieren nicht den gesamten Quellcode Baum, sondern erzeugen lediglich einen Zeitpunkt, an dem Sie Code schreiben werden; daher helfen Zweige dabei, die laufende Arbeit vom Hauptcode getrennt zu halten.

Die Verwendung eines neuen Zweigs erfolgt in zwei Schritten   * Zuerst erstellest du den Zweig, und dann wechselst du zu ihm   *


{{Code|lang=text|code=
git branch myNewBranch
git checkout myNewBranch
}}

Führe alternativ beide Schritte mit einer einzigen Anweisung aus   *


{{Code|lang=text|code=
git checkout -b myNewBranch
}}

Jetzt kannst du Zweige mit `checkout` ändern, wann immer du daran arbeiten musst. Um die Zweige in deinem Projekt und dem aktuellen Zweig zu sehen, verwende die Operation `branch` allein oder füge `-v` oder `-vv` für weitere Informationen hinzu   *


{{Code|lang=text|code=
git branch
git branch -vv
}}

Nachdem du Änderungen vorgenommen und diese Änderungen übertragen hast, verwende die Operation `log` mit den folgenden Optionen, um die Zweige zu visualisieren


{{Code|lang=text|code=
git log --oneline --decorate --graph --all
}}

### Übergeben

Sobald du dich in einem neuen Zweig befindest, bearbeite die gewünschten Quelldateien mit einem Texteditor. Um zu sehen, welche Dateien geändert wurden, verwende die Operationen `status` und `diff`; wenn du mit den Änderungen zufrieden bist, speichere die Änderungen mit der Operation `commit`   *


{{Code|lang=text|code=
git status
git diff
git commit -a
}}

Unlike SVN, you need to specifically tell which files to commit; use the `-a` option to save changes in all files that were altered. Your text editor, for example, `nano` or `vim`, will open to allow you to write a commit message.

Alternatively add the message in the commit itself   *


{{Code|lang=text|code=
git commit -a -m "Fix the bug in the clone function."
}}

If you create new files or directories, you must use the `add` operation first to add them to the local repository before committing the changes.


{{Code|lang=text|code=
git add path
git commit -a
}}

Where `path` can be any directory or file.

### Writing good commit messages 

You should try to work in small steps, that is, commit often, after a small addition in your code. If you cannot summarize your changes in one sentence, then it has probably been too long since you made a commit.

For big changes, it is important that you have helpful and useful descriptions of your work. FreeCAD has adopted a format mentioned in the [Pro Git](https   *//git-scm.com/book/en/v2) book, which consists of a short message, and then a larger descriptive paragraph.


{{Code|lang=text|code=
Short (50 chars or less) summary of changes
 
 More detailed explanatory text, if necessary.  Wrap it to about 72
 characters or so.  In some contexts, the first line is treated as the
 subject of an email and the rest of the text as the body.  The blank
 line separating the summary from the body is critical (unless you omit
 the body entirely); tools like rebase can get confused if you run the
 two together.
 
 Further paragraphs come after blank lines. 
 
  - Bullet points are okay, too
 
  - Typically a hyphen or asterisk is used for the bullet, preceded by a
    single space, with blank lines in between, but conventions vary here
}}

If you are doing a lot of related work in a branch, you should make many small commits (see a [forum post](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=2062&p=14887#p14886)). When you want to merge those changes into the master branch, you should issue


{{Code|lang=text|code=
git log master..myNewBranch
}}

um die einzelnen Übergabe Meldungen zu sehen. Dann kannst du eine Nachricht von hoher Qualität schreiben, wenn eine Zusammenführung durchgeführt wird.

When you merge to master use the `--squash` option and commit with your quality commit message. This will allow you to be very liberal with your commits and help to provide a good level of detail in commit messages without so many distinct descriptions.

### Squashing commits 

Squashing refers to the process of combining various consecutive commits into one. This may be desirable if you made many small commits that you want to present as a single commit, for example, when changing a single variable, correcting spelling mistakes, and adjusting the spacing of the code. You should squash only small commits to a single file; big changes to the code across multiple files should contain the full commit history.

With `git log --oneline` you can see many commits in sequence, with the newest commit on top. In this example, starting from \"feature A\" many commits are made to implement \"feature B\"; we would like to squash all commits belonging to \"feature B\" into one.


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

Use the `rebase` operation with the `--interactive` or `-i` option to select various commits and squash them. Use the hash of the commit just before the first one that you want to squash, in this case the one corresponding to \"feature A\".


{{Code|lang=text|code=
git rebase -i 6394da
}}

(TIP   * If you know how many commits you want to edit, you can use `git rebase -i HEAD~n` to work on the last `n` commits)

The command line editor, like `nano` or `vim`, will open to show you the commits again, now with the older commit on top. Before each commit, the word `pick` will be shown. Delete the word `pick`, and write the word `squash` or just the letter `s` instead, with the exception of the first entry; this commit is the oldest one, so all future commits will be squashed into it.


{{Code|lang=text|code=
pick d94e78 Prepare the module for feature B
s 4e9baa Good implementation
s af2581 Fix this and that
s 643d0e Code cleanup
s 87871a I'm almost ready!
s 1c3317 Whoops, it is not ready yet...
s 871adb OK, feature B is fully implemented
}}

Save the file and close the editor.

The editor will open up again. Now you can add a longer message that describes all changes as if they were a single commit. Save the file and close the editor once more. This will finish combining those commits into one, with the new commit message that you wrote.

You can use `git log --oneline` again to observe the new commit history. In this case only a single commit for \"feature B\" will appear, on top of the unmodified commit for \"feature A\".


{{Code|lang=text|code=
c83d67 OK, feature B is fully implemented now, with proper module setup, and clean code.
6394da Feature A
}}

When coding for FreeCAD, we ask that you begin each commit message with the module that it affects. For example, a commit message for a change to sketcher might be   *

    Sketcher   * make straight lines curve a bit

    Straight lines are sort of ugly, so this commit adds a little bit of curvature to them, so
    they are more visually pleasing. They also sparkle some, and change colors over time.

    Fixes bug #1234.

Your PR will be easier to review, and faster to be merged, if you are careful to use rebase to structure and describe your commits before submitting.

### Pushing your work to your GitHub repository 

The local branches in your computer aren\'t automatically synchronized with the remote servers that you have specified as `origin` or `upstream` (see [Remote repositories](#Remote_repositories.md)); you have to explicitly push the branches to the remote servers, for which you must have write access. Once you do this, the branches become public, and available for review by other developers.

For FreeCAD, you should push your local branch to the `origin` remote repository, that is, {{URLn|https   *//github.com/GITHUB_USERNAME/FreeCAD}}. You need to enter your username and password every time you push, unless you have set up [Credential caching](https   *//git-scm.com/book/en/v2/Git-Tools-Credential-Storage#_credential_caching). Please read [Pushing commits to a remote repository](https   *//help.github.com/articles/pushing-to-a-remote/) for more information.


{{Code|lang=text|code=
git push origin myNewBranch
}}

When you work with a single branch, you may need to interactively rebase, squash, and fix commits many times. In this case, your branch history will not be simple, and you will not be able to push it to the remote repository. You may get a message like the following, saying that it is not possible to do a \"fast-forward\" push.


{{Code|lang=text|code=
error   * failed to push some refs to 'https   *//github.com/USER/FreeCAD.git'
hint   * Updates were rejected because a pushed branch tip is behind its remote
hint   * counterpart. Check out this branch and integrate the remote changes
hint   * (e.g. 'git pull ...') before pushing again.
hint   * See the 'Note about fast-forwards' in 'git push --help' for details.
}}

In order to finally push your branch to the remote repository you need to \"force push\" it. This will completely overwrite your remote branch with the actual branch that you have offline.


{{Code|lang=text|code=
git push -f origin myNewBranch
}}

The regular developer doesn\'t have write access to the `upstream` repository {{URL|https   *//github.com/FreeCAD/FreeCAD}}, therefore, you should never push code to this remote server.

### Rebasing from upstream 

While you work on your own branch, the official FreeCAD code keeps \"moving forward\" with commits from other developers, and thus starts diverging from the code that you have in your personal fork.

          .A origin/myNewBranch
         / 
    oZ FreeCAD upstream/master

Therefore, when you are ready to merge your branch to the main FreeCAD repository, you must \"rebase\" your own copy of the repository, so that it is as close as possible to the official repository. See [Git Branching - Rebasing](https   *//git-scm.com/book/en/v2/Git-Branching-Rebasing) for more information.


{{Code|lang=text|code=
git checkout myNewBranch
git pull --rebase upstream master
}}

This will download the code from the `master` branch of the `upstream` repository (the official FreeCAD source), and will merge it with your current branch (`myNewBranch`), so that your changes will appear on top of the latest official code. If nobody modified the same files that you did, then the merge will succeed without problems. If some files were changed at the same time by different people, there may be a conflict that needs to be resolved.

                      .A' origin/myNewBranch
                     /
    oZ FreeCAD upstream/master

To summarize, you need to be in the appropriate branch, rebase the upstream code, and then proceed with the push.


{{Code|lang=text|code=
git checkout myNewBranch
git pull --rebase upstream master
git push origin myNewBranch
}}

The `pull` operation is equivalent to a `fetch` followed by a `merge`. When the `--rebase` option is used, instead of doing a simple `merge`, it runs the `rebase` operation.


{{Code|lang=text|code=
git pull upstream

git fetch upstream
git merge FETCH_HEAD
}}


{{Code|lang=text|code=
git pull --rebase upstream master

git fetch upstream
git rebase master
}}

### Merging the branch (pull request) 

Once you have committed your changes locally, rebased your branch from the upstream repository, and pushed your branch online, you can initiate a \"pull request\". A [pull request](https   *//help.github.com/articles/about-pull-requests/) tells the administrators of the official FreeCAD repository that you want to merge the new code in your branch with the official code.

To recap, the development process looks like this   *

1.  Fork FreeCAD and get a local copy of that fork.
2.  Create a branch on your fork and change to that branch.
3.  Code! Commit and much or as little as you like, writing good commit messages to keep track of what you are doing.
4.  When you are satisfied with your work, use `git rebase -i HEAD~n` (where n is the total number of commits you\'ve made) to collapse your commits into a logical set with good commit messages (each message should begin with the name of the module it affects, e.g. \"Sketcher   * make straight lines curve a bit\").
5.  Use GitHub to submit your code as a \"Pull Request (PR)\" as described below.

As soon as you push the code to your `origin` repository {{URLn|https   *//github.com/GITHUB_USERNAME/FreeCAD}}, GitHub will give you the option of comparing and creating a pull request against the `upstream` repository. By pressing **Compare & pull request** you will open an interface that will allow you to pick which repository is the \"base\", target of the merge, and which is the \"head\", your additional code. A quick check will be done by the system telling you if there are no conflicts with the files that you modified; if you worked on files that nobody has touched, your branch will be able to merge cleanly.

GitHub will show you a text editor so you can write a message documenting your changes   * this editor will be pre-filled with a welcome message (that you can delete), a checklist (that you should go through), and a reminder to document your change on the wiki when it\'s accepted. To use the checklist, go through each item in turn and change the `[ ]` to `[X]` to indicate that you\'ve done that step. GitHub will also display the number of commits in your branch, the number of files that were modified, and a view showing you the differences between the \"base\" and the \"head\" so that everybody can immediately see your intended modifications. Double-check these for things like stray blank lines you didn\'t mean to add, or huge formatting changes that your IDE decided to make behind your back.


{{Code|lang=text|code=
base repository   * FreeCAD/FreeCAD    base   * master  <  head repository   * GITHUB_USERNAME/FreeCAD    compare   * myNewBranch

Able to merge. These branches can be automatically merged.
}}

Click **Create pull request** to proceed. A message will appear indicating that some checks need to be done on the code. This is a system that compiles FreeCAD automatically and runs the unit tests. If the tests pass, the pull request will have a better chance of being merged into the main code, otherwise a report will be made indicating the errors encountered. See [FreeCAD pull requests](https   *//travis-ci.org/FreeCAD/FreeCAD/pull_requests).

    Some checks haven’t completed yet

    * continuous-integration/travis-ci/pr Pending — The Travis CI build is in progress  |Required|

If the tests succeed, you will see a message such as the following

All checks have passed

    * continuous-integration/travis-ci/pr — The Travis CI build passed  |Required|

This branch has no conflicts with the base branch Only those with write access to this repository can merge pull requests.

Now you must wait for the administrators to merge your branch; you will be notified when this happens.


{{Code|lang=text|code=
Pull request successfully merged and closed

You’re all set — the GITHUB_USERNAME   *myNewBranch branch can be safely deleted.
If you wish, you can also delete your fork of FreeCAD/FreeCAD.
}}

If you wish, you may delete the branch that was just merged, or even your entire FreeCAD fork, as your own code is already included at the end of the master branch.


{{Code|lang=text|code=
oZA' FreeCAD upstream/master
}}


**Note   ***

you may continue working (`git commit -a`) on the same branch while you wait for merge approval; if you `git push` again, a second merge commit will be queued in the same pull request, and another automated test will be done. That is, while your merges aren\'t yet approved by the administrators, you may keep pushing changes to your `origin` repository, and this will queue those commits in the same pull request to the `upstream` repository. Using a single pull request to queue many individual commits is often desirable for small changes. For big additions to the source code, you should create another branch, develop your features there, and then submit a separate pull request for this branch.

The pull request interface can be used whenever you want to submit code from your own repositories to another repository in GitHub. You can use it to merge code in the opposite direction as well, from other people\'s branches to your own, or even between your own branches. In the last case, since you own the branches, the merges can be approved by yourself immediately.


{{Code|lang=text|code=
base repository   * SomeProject/Some_Software  base   * master       <  head repository   * GITHUB_USERNAME/Some_Software  compare   * add_new_functions
base repository   * GITHUB_USERNAME/FreeCAD    base   * myNewBranch  <  head repository   * FreeCAD/FreeCAD                compare   * master
base repository   * GITHUB_USERNAME/FreeCAD    base   * myNewBranch  <  head repository   * GITHUB_USERNAME/FreeCAD        compare   * fix-many-bugs-branch
}}

### Das GitHub Repositorium auf dem neuesten Stand halten 

Once you\'ve forked FreeCAD, your personal repository exists independently from the original. When the original repository has new commits, GitHub will inform you that your personal repository is behind in number of commits   *


{{Code|lang=text|code=
This branch is 5 commits behind FreeCAD   *master.
}}

In similar way, if you created a development branch with new code, GitHub will inform you that this branch is ahead in number of commits; that is, this branch has changes that haven\'t been merged into the official FreeCAD repository   *


{{Code|lang=text|code=
This branch is 3 commits ahead of FreeCAD   *master.
}}

While developing, both cases are possible, as your own branch may lack commits made by other developers, but include new commits by you   *


{{Code|lang=text|code=
This branch is 2 commits ahead, 14 commits behind FreeCAD   *master. 
}}

When developing code it is recommended that you rebase the branch in which you are currently working, as that will put your branch always ahead of the FreeCAD master code.

As for your original `master` branch, it will never be automatically updated by GitHub; this is something that you must do yourself. Switch to the `master` branch, then `pull` from `upstream` (which performs a `fetch` and `merge`), and then push this updated `master` branch to your remote `origin` repository.


{{Code|lang=text|code=
git checkout master
git pull upstream master
git push origin master
}}

After this is done, GitHub will let you know that your are synchronized with the `upstream` repository.


{{Code|lang=text|code=
This branch is even with FreeCAD   *master. 
}}

Now that your `master` is up to date, you may decide to switch to it, and delete the other branch that you used previously to develop a feature.


{{Code|lang=text|code=
git checkout master
git branch -d myNewBranch
}}

To delete the branch in the `origin` remote repository, you can use the `push` operation. Normally, you push a local branch; this creates a remote branch with the same name as your local branch.


{{Code|lang=text|code=
git push origin myNewBranch
}}

However, if you use the notation `local_name   *remote_name`, the local branch is created in the remote repository under a different name   *


{{Code|lang=text|code=
git push origin myNewBranch   *someRemoteBranch
}}

Daher kannst du den entfernte Fernzweig löschen, indem du einen leeren lokale Zweig schiebst   *


{{Code|lang=text|code=
git push origin    *myNewBranch
git push origin    *someRemoteBranch
}}

Now that you only have an up-to-date `master`, you can create a new branch, and repeat the steps of changing files, committing, pushing, submitting a pull request, merging, and updating.


{{Code|lang=text|code=
git checkout master
git checkout -b anotherBranch
}}

If you don\'t want to delete your already custom branch, you may force updating it to be equal to the updated `master`; then you can do whatever you want with it, including adding more commits and pushing it to the remote `origin` repository.


{{Code|lang=text|code=
git checkout myNewBranch
git reset --hard master
git push -f origin myNewBranch
}}

Hard resetting a branch like this is usually not needed. In most cases, you want to follow the sequence of creating a new branch, committing changes, pushing those changes, merging the branch, and then deleting the branch.

## Erweiterte Git Operationen 

### Suchen

Some handy tools to help you find what you\'re looking for   *

#### Dateinamen suchen 

Use `git ls-files` to search the repository for file that contains a certain string in a filename. The example below will return all instances of the files that contain the \'dxf\' in their filenames.


{{Code|lang=text|code=
git ls-files *dxf*
}}

#### Suche nach einer Zeichenkette 

Use `git grep` to search the repository for file that contains a certain string with the files themselves. The example below will return all instances of the files that contain the \'dxf\' within each and every file.


{{Code|lang=text|code=
git grep dxf
}}

### Auflösen von Zusammenführungskonflikten 

Merging branches with `git merge`, or rebasing your branch with `git rebase`, will occasionally present conflicts, as files may have been modified by another author at the same time. If this happens you should see the changes of both sides, the other author\'s, and your own, and then make a decision on how to include both sets of changes in the best way possible. This is normally a manual process that cannot be automated; the programmer must understand the code, and decide what code to move, re-write, or drop to solve the conflict.

Sobald ein Konflikt auftritt, kann eine Meldung wie diese erscheinen.


{{Code|lang=text|code=
CONFLICT (content)   * Merge conflict in src/Mod/source_code.py
error   * Failed to merge in the changes.
Patch failed at 1234 Some commit message when editing source_code.py
}}

If a specialized diff tool is installed and configured for Git, for example, Gnome\'s [Meld](https   *//wiki.gnome.org/Apps/Meld), the conflict can be examined and solved by using the `mergetool` operation.


{{Code|lang=text|code=
git mergetool
}}

The Meld tool normally displays three columns; the two columns on the sides display the two conflicting files, while the column on the middle displays the new code that will be saved and committed finally. Therefore, this central column should be edited in a way that it integrates the code of both side columns. Once the conflict is solved and the new source code (the central column) is saved, the Meld tool can be closed. Then the `merge` or `rebase` operation can continue.


{{Code|lang=text|code=
git merge --continue
git rebase --continue
}}

For more information on merging and solving conflicts see   *

-   [How merge conflicts are presented](https   *//git-scm.com/docs/git-merge#_how_conflicts_are_presented) with `git merge`.
-   [Basic merge conflicts](https   *//git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts) and [Git Tools - Advanced Merging](https   *//git-scm.com/book/en/v2/Git-Tools-Advanced-Merging).
-   [Resolving a merge conflict using the command line](https   *//help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/).
-   [External merge and diff tools](https   *//git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_external_merge_tools) to use when you encounter a Git conflict.

### Änderungen untersuchen 

Inspect the history of a single file through various commits with the `log` operation   *


{{Code|lang=text|code=
git log --patch path
}}

Where `path` can be any directory or file. Instead of `--patch`, also the shorthands `-p` or `-u` can be used.

### Änderungen zwischen zwei Zweigen untersuchen 

Inspect the changes between two branches with the `log` and `diff` operations with the names of the branches   *


{{Code|lang=text|code=
git log master..myBranch
git diff master..myBranch
}}

The `log` operation shows the commits, while `diff` shows the actual changes in the files.

### Dateien und Verzeichnisse zurücksetzen 

If you accidentally made modifications to a file or directory, you may want to completely revert these changes, to get the previous state of the source code.

This can be done quickly using the `checkout` operation   *


{{Code|lang=text|code=
git checkout path
git checkout .
}}

This will restore the `path` (a file or a directory) to the state it is at the tip of the branch, discarding changes that haven\'t been committed. If `path` is the single dot `.`, it will restore all files in the current directory.

If you have accidentally added files and directories you can use the `clean` operation   *


{{Code|lang=text|code=
git clean -df
}}

This will forcefully delete all files and directories (`-df`) that are not being tracked by the repository, that is, those that have not been included previously with the `add` operation.

To completely reset the repository, losing all uncommitted modifications, use the `reset` operation   *


{{Code|lang=text|code=
git fetch
git reset --hard FETCH_HEAD
}}

Where `FETCH_HEAD` is the the tip of the `upstream` repository. Another commit can also be used.

The `revert` operation also reverts changes. However, this command does this by adding another commit to the history; in many cases this is not desired.

### Beschneiden alter Zweige 

If you have committed many branches to the `upstream` repository, you may wish to remove these branches from your local system as they have already been merged. The branch in the `origin` repository online can be deleted immediately after merging. Then you can remove the local references to that branch, using the `--prune` or `prune` options to the `fetch` and `remote` operations.


{{Code|lang=text|code=
git fetch --prune origin
git remote prune origin
}}

Schließlich kannst du die Zweige lokal löschen


{{Code|lang=text|code=
git branch -D myBranch
}}

It is also a good practice to do garbage collection after a while, by using the `gc` operation. This will cleanup unnecessary files, and compress local file revisions, in order to optimize local disk usage of the repository.


{{Code|lang=text|code=
git gc
}}

### Arbeiten mit Patches 

Obwohl Git Ihnen dir erlaubt, verschiedene Code Zweige mit `git merge` zusammenzuführen (in deinem Computer) oder einer Pull Anfrage (Fernrepositorium) gibt es Zeiten, in denen es wünschenswert sein kann, einen traditionellen \"Patch\" zu erstellen, der als Anhang per Email verschickt werden kann. Der folgende Arbeitsablauf erklärt, wie dies zu tun ist.

#### Patches erstellen 

-   You should be developing your new code in a secondary branch of your repository, and not in the master branch. So the first step is to make sure you are in the correct branch.


{{Code|lang=text|code=
git branch -v
git checkout myBranch
}}

-   Now use `git format-patch` against the master branch, and use the `--stdout` option to redirect the result to standard output; then redirect the standard output to a file, which for convenience is created above the source code directory.


{{Code|lang=text|code=
git format-patch master --stdout > ../myCode.patch
}}

-   Eine andere Methode ist


{{Code|lang=text|code=
git format-patch HEAD^
git format-patch HEAD~1
}}

The number of circumflex carets `^` or the number `1` indicate the number of commits that should be considered, that is, `^^^` or `~3` will create three patches for three commits.


{{Code|lang=text|code=
git format-patch HEAD^
}}

This will create a patch or series of patches with the following naming convention


{{Code|lang=text|code=
XXXX-commit-message.patch
}}

where `XXXX` is a number from `0000` to `9999`, and the commit message forms the majority of the file name, for example,


{{Code|lang=text|code=
0001-fix-ViewProjMatrix-getProjectionMatrix.patch
}}

#### Patches anwenden 

Git can merge patches or diffs. To know more about this process read [Applying patches with Git](https   *//www.drupal.org/node/1399218).

Wenn du die Patch Datei bereits in deinem System hast, wende sie einfach an.


{{Code|lang=text|code=
git apply myCode.patch
}}

You can use `curl` to download a patch from a website, and then apply it through `git`.


{{Code|lang=text|code=
curl -O https   *//some.website.org/code/myCode.patch
git apply myCode.patch
}}

Add `.diff` or `.patch` at the end of the URL of a GitHub commit, pull request, or compare view so that the website shows you the plain text view of that page.

-   Regular commit page   * {{URL|https   *//github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621}}
-   Diff page   * {{URL|https   *//github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.diff}}
-   Patch page   * {{URL|https   *//github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.patch}}

You can point `curl` to a particular commit patch in the repository, and pipe it directly to `git` to apply the patch.

    curl https   *//github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.patch | git apply -

#### Einen Patch rückgängig machen 

When you apply a patch you modify some files. However, these modifications aren\'t permanent until you commit the changes. Therefore, if you want to revert a patch use the following instructions.

This will revert the changes applied, if you still have access to the original patch file.


{{Code|lang=text|code=
git apply -R myCode.patch
}}

Alternatively, this will remove non-committed changes to the branch.


{{Code|lang=text|code=
git checkout -f
}}

### Stashing git commits 

Say that you\'re working on a branch and you find yourself making some modifications to the source that are out of the scope of your current branch; in other words, those changes would be better in another branch instead of the current one. The `git stash` command can be used to temporarily store those uncommitted local changes.


{{Code|lang=text|code=
git stash
}}

If in the future you want to use those commits, you can \"pop\" the commits out of the stash, and into your working branch.


{{Code|lang=text|code=
git stash pop
}}

Or if you decide that you don\'t like those saved commits anymore, you may drop the commits from the stash entirely.


{{Code|lang=text|code=
git stash drop
}}

You can list multiple stash commits with


{{Code|lang=text|code=
git stash list
}}

To learn more, read [Useful tricks you might not know about Git stash](https   *//medium.freecodecamp.org/useful-tricks-you-might-not-know-about-git-stash-e8a9490f0a1a).

### GitHub Anfragen lokal herausfinden 

[Checkout GitHub pull requests locally](https   *//gist.github.com/piscisaureus/3342247)

### Blaming


**Section TBD**

Add content from <https   *//forum.freecadweb.org/viewtopic.php?f=23&t=55943&p=481483#p481287>

### Bisect


`git bisect`

is a method to find the specific commit that introduced a bug.

You need to find 2 commits   *

-   A good commit (for example `abcd`) before the system broke.
-   A bad commit (for example `efgh`) after the system broke.

Then enter this from the terminal   *


{{Code|lang=text|code=
git bisect start
git bisect good abcd
git bisect bad efgh
}}

Result   * `git` will check out the mid point between the two commits.

The next step is to build and test the code. If the system works, continue the process by typing   *


{{Code|lang=text|code=
git bisect good
}}

Repeat the previous step of building the code and testing it.

If the system is broken, type   *


{{Code|lang=text|code=
git bisect bad
}}

Repeat the previous steps applying `good` or `bad` depending on the outcome of your tests.

Eventually, `git` will tell you that `wxyz` is the first bad commit.

Finally, to exit the bisect process, type   *


{{Code|lang=text|code=
git bisect reset
}}

Note   * `git bisect` takes a long time if good and bad are far apart.

## FreeCAD Revisionsnummer 

In contrast to subversion, which uses a consecutive number for its revisions, Git produces [SHA-1 hash values](https   *//en.wikipedia.org/wiki/SHA-1) with every commit. A hash value is a long alphanumeric string that looks like this


{{Code|lang=text|code=
9b3ffef570596e184006287434fba54a4b03ccc3
}}

### Letzte Revisionsnummer 

To find the latest revision number of a particular branch use the `rev-list` operation with the `--count` option. Give the name of the branch, remote repository, tag, or a special pointer like `HEAD`, to indicate the last commit in that particular object.


{{Code|lang=text|code=
git rev-list --count master
git rev-list --count HEAD
git rev-list --count origin
}}

Or browse [the repository on GitHub](https   *//github.com/FreeCAD/FreeCAD), and read the amount of commits reported in the particular branch.

### Revisionsnummer eines bestimmten Commit Hashes 

Since the hash is an alphanumeric string it is not very useful to decide if a certain commit is older or newer than another hash. To find the revision number of a particular hash, again use the `rev-list` operation; the input can be the full hash, or a partial hash that is unique, usually the first 7 digits are enough.


{{Code|lang=text|code=
git rev-list --count ab1520b872821414c6ce4a15fb85d471ac2a2b03
git rev-list --count 9948ee4
}}

### Revisions Hash einer bestimmten Commit Nummer 

If we have the commit number, say, 15000, and we want to find the corresponding hash, we need to calculate the number of commits since this point until the last commit (`HEAD`). First, get the latest commit number.


{{Code|lang=text|code=
git rev-list --count HEAD
17465
}}

Then subtract the commit that we want.


{{Code|lang=text|code=
17465 - 15000 = 2465
}}

Then use the `log` operation to show all commits and hashes. The `--skip` option jumps the difference in commits that we calculated so that we go directly to the hash that we are looking for.


{{Code|lang=text|code=
git log --skip=2465
commit 44c2f19e380e76b567d114a6360519d66f7a9e24
}}

Since the log may show you two close commits, confirm it\'s the right commit number. If it\'s off by one, just pick the next commit in the sequence (before or after) and check again.


{{Code|lang=text|code=
git rev-list --count 44c2f19e38
15000
}}

-   [Show the commits](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=26673) immediately before a particular commit in GitHub   * in the address bar of the browser, change the word `commit` to `commits` to show a list.
-   [Finding the revision number of the commit](https   *//forum.freecadweb.org/viewtopic.php?t=5308)
-   [Finding the revision number of the commit](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=12883&p=103207#p103203)
-   [Finding the corresponding hash value to a particular commit number](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=31118)

### Revisionsnummer in der FreeCAD Oberfläche 

Die Versionsnummer, die mit dem [Std Über](Std_About/de.md) Werkzeug angezeigt wird, ist in `src/Build/Version.h` definiert, was zur Kompilierzeit erstellt wird, wenn das Werkzeug `cmake` ausgeführt wird. Lies [Versionsnummer aus der Git Quelle extrahieren](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=3025) für weitere Informationen.

## Hinzufügen weiterer (Fern) Repositorien 

Mehrere Mitarbeiter des FreeCAD Projekts haben ihre eigenen Git Repositorien, in denen sie ihre Arbeit aufbauen oder neue Ideen ausprobieren, bevor sie bereit sind, in den offiziellen Quellcode aufgenommen zu werden. Vielleicht möchtest du ihre Quellen bekommen, um ihren Code selbst zu testen, wenn sie eine Pull Anfrage stellen.

Verwende den Befehl `git fern` Befehl, um diese anderen Repositorien hinzuzufügen, so dass du deren Code `holen` und `abrufen` kannst.


{{Code|lang=text|code=
git checkout master
git remote add OTHER_USER OTHER_URL
git fetch OTHER_USER
git checkout -b OTHER_BRANCH OTHER_USER/OTHER_BRANCH
}}

Lass uns zum Beispiel Bernds Fernrepositorium hinzufügen   *


{{Code|lang=text|code=
git remote add bernd http   *//github.com/berndhahnebach/FreeCAD_bhb
}}

Der `git holen` Befehl lädt die Referenzen von diesem Fernrepositorium herunter.


{{Code|lang=text|code=
git fetch bernd
}}

Liste alle Zweige in deinem eigenen Repositorium und die von deinen hinzugefügten Fernen auf. Bernds Zweige werden als `Fern/bernd/<Zweigname>` angezeigt.


{{Code|lang=text|code=
git branch -a
}}

Lass uns nun eine zusammenfassende Liste der letzten 10 Commits von bernds `femdev` Zweig ansehen.


{{Code|lang=text|code=
git log -10 --oneline remotes/bernd/femdev
}}

Jetzt können wir den gewünschte Zweig zur Inspektion herausfinden.


{{Code|lang=text|code=
git checkout remotes/bernd/femdev
}}

Dann können wir einen lokalen Zweig erstellen, der auf dem entfernten Zweig basiert. Diesen lokalen Zweig können wir modifizieren und unseren eigenen Code hinzufügen.


{{Code|lang=text|code=
git checkout -b local_branch_name /remotes/bernd/femdev
}}

Du kannst den `git rebase` des neu erhaltenen Zweigs auf den `upstream/master` Zweig umstellen, um sicherzustellen, dass er den neuesten Code verwendet. Wenn es Konflikte gibt, müssen diese an diesem Punkt gelöst werden.


{{Code|lang=text|code=
git pull --rebase upstream master
}}

Der neue Zweig ist bereit, modifiziert und kompiliert zu werden, wie in [Kompilieren](Compiling/de.md) beschrieben.

Besuche die Entwicklungsabteilung des [FreeCAD Forum](https   *//forum.freecadweb.org/viewforum.php?f=6)s, um mehr über die Entwicklung zu erfahren.

## Weiterführende Literatur 

-   [FreeCAD mit GitKraken entwickeln](Developing_FreeCAD_with_GitKraken/de.md), eine Anleitung zur Verwendung einer grafischen Oberfläche mit Git.
-   [Git für die Faulpelze](https   *//wiki.spheredev.org/index.php/Git_for_the_lazy), eine sehr prägnante Anleitung zu den wichtigsten Befehlen von `git`.
-   Das [Pro Git Buch](https   *//git-scm.com/book), ein quelloffenes Buch, das dich über Git lehrt; es ist in elektronischer und gedruckter Version erhältlich.
-   Der [Visual Git Leitfaden](https   *//marklodato.github.io/visual-git-guide), eine Referenz mit Diagrammen, die die häufigsten Operationen mit Git erklären.
-   [Git Tutorium für Anfänger   * Kommandozeilen Grundlagen](https   *//www.youtube.com/watch?v=HVsySz-h9r4), Video von Corey Schafer.
-   [Einführung in Git - Kernkonzepte](https   *//www.youtube.com/watch?v=uR6G2v_WsRA), Video von David Mahler.



[Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source code management/de
