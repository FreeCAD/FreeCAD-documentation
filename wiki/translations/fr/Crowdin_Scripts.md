# Crowdin Scripts/fr
{{TOCright}}

## Gérer les traductions de FreeCAD 

FreeCAD utilise un service de traduction tiers appelé [Crowdin](https://crowdin.com/project/freecad) pour gérer les traductions.

Il existe 3 scripts dans FreeCAD/src/Tools utilisés pour gérer les fichiers de traduction:

1.  updatets.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatets.py)
2.  updatecrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatecrowdin.py)
3.  updatefromcrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatefromcrowdin.py)

### Remarques

-   Ces scripts sont exécutés à la racine du répertoire FreeCAD/.
-   Pour que ces scripts fonctionnent, la clé d\'API FreeCAD Crowdin valide doit être placée dans leur fichier ~/.crowdin-freecad. (Pour des raisons de sécurité, disponible uniquement pour les personnes disposant des droits d\'administrateur sur le projet crowdin FreeCAD)
-   Actuellement, ces outils sont compatibles Python2.

### updatets.py

Le script updatets.py créera les fichiers .ts dans votre répertoire local FreeCAD/. Il génère des fichiers .ts (Qt Translation Source File).

Il est appelé avec : python2 updatets.py

### updatecrowdin.py

Le script updatecrowdin.py pousse les modifications vers Crowdin (service de traduction crowdsource de traduction tiers) à partir de votre répertoire local FreeCAD/. Le script prend actuellement en charge 4 arguments:

-   updatecrowdin.py status affiche un statut des traductions
-   updatecrowdin.py update met à jour la version actuelle des fichiers .ts présents dans le code source crowdin
-   updatecrowdin.py build construit un nouveau paquet téléchargeable sur crowdin avec toutes les chaînes traduites
-   updatecrowdin.py download télécharge la dernière version

### updatefromcrowdin.py

Le script updatefromcrowdin.py extrait les modifications de crowdin vers votre répertoire FreeCAD/ local.

## Pour envoyer les dernières modifications à crowdin 

-   Testé uniquement sur Linux
-   Vous avez besoin d'un fichier .credentials dans votre répertoire /home/YourUser. Ce fichier est un simple fichier texte contenant une seule ligne, qui correspond à la clé API que vous obtenez sur <https://crowdin.com/project/freecad/settings#api> (uniquement pour les administrateurs).
-   Assurez-vous que votre dépôt est propre (git pull, git stash si nécessaire)
-   cd /path/to/freecad-source-code/src/Tools
-   python updatets.py (remplira tous les fichiers .ts trouvés dans le source avec les dernières chaînes)
-   python updatecrowdin.py update (enverra les fichiers ts à crowdin. Crowdin ne mettra à jour que les nouvelles chaînes)
-   cd ../.. (retournez au dossier racine du code source)
-   git Checkout. (annulez toutes les modifications apportées aux fichiers .ts, aucune raison de les valider maintenant, car elles ne sont pas traduites)

## Pour fusionner les dernières traductions de crowdin 

-   Testé uniquement sur Linux
-   Vous avez besoin d'un fichier .credentials dans votre répertoire /home/YourUser. Ce fichier est un simple fichier texte contenant une seule ligne, qui correspond à la clé API que vous obtenez sur <https://crowdin.com/project/freecad/settings#api> (uniquement pour les administrateurs).
-   Assurez-vous que votre dépôt est libre (git pull, git stash si nécessaire)
-   cd /path/to/freecad-source-code/src/Tools Outils
-   Python updatecrowdin.py build (créera un zip du côté de crowdin avec tous les fichiers, peut prendre un certain temps .. Cette étape peut également être effectuée sur le site web de crowdin)
-   python updatecrowdin.py télécharger (téléchargera le fichier freecad.zip dans ce répertoire)
-   mv freecad.zip \~ déplace le fichier zip dans votre répertoire personnel, pour éviter de le commettre accidentellement plus tard)
-   (facultatif) éditez le script updatefromcrowdin.py et vérifiez que les default\_languages ​​contiennent tous ceux que vous voulez (essentiellement tous ceux qui sont à plus de 50%)
-   python updatefromcrowdin.py -z /home/YourUser/freecad.zip
-   cd ../.. (retourne au dossier racine du code source)
-   Si quelque chose s\'est mal passé ou si vous avez un doute, nettoyez tout avec Git Checkout.
-   Si tout se passe bien (statut git), validez avec git add. && git commit
-   Créer un PR sur FreeCAD

## Pour générer un fichier de traduction à partir du site Web 

-   Cloner le dépôt de la page d\'accueil
-   cd /path/to/FreeCAD-homepage
-   xgettext \--from-code=UTF-8 -o lang/homepage.pot \*.php
-   Mettre à jour manuellement le \"homepage.po\" sur le site web de crowdin, en utilisant le fichier lang/homepage.pot

## Mettre à jour les traductions du site 

-   Obtenez le fichier freecad.zip en le téléchargeant depuis le site Web de crowdin ou en suivant les instructions ci-dessus (téléchargement de python updatecrowdin.py).
-   cd /path/to/FreeCAD-homepage
-   Assurez-vous que votre dépôt est libre (git pull, git stash si nécessaire)
-   python updatefromcrowdin.py -z /path/to/freecad.zip
-   Si quelque chose s\'est mal passé ou si vous avez un doute, nettoyez tout avec Git Checkout.
-   Si tout se passe bien (statut git), validez avec git add. && git commit
-   Créer un PR sur FreeCAD-Homepage
-   Après la fusion du RP, l'un des administrateurs va s'appuyer sur l'hôte Web

## En relation 

-   [Localisation](Localisation/fr.md)
-   [Administration de Crowdin](Crowdin_Administration/fr.md)
-   [Release process](Release_process.md) (en)




[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Administration](Category_Administration.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Crowdin Scripts/fr
