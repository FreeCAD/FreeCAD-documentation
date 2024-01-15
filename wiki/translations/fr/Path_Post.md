---
 GuiCommand:
   Name: Path PostProcess
   Name/fr: Path Post-traitement
   MenuLocation: Path , Post-traitement
   Workbenches: Path_Workbench/fr
   Shortcut: **P** **P**
---

# Path Post/fr



## Description

L\'outil <img alt="" src=images/Path_Post.svg  style="width:16px;"> [Post-traitement](Path_Post/fr.md) exporte la <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Path Tâche](Path_Job/fr.md) sélectionnée vers un fichier G-code.

**Chaque contrôleur CNC parle un dialecte G-code spécifique, nécessitant un post-processeur à correction dialectale pour traduire la sortie finale à partir du dialecte G-code interne agnostique de FreeCAD**.



### Fonctions typiques du post-processeur 

-   L\'utilisation d\'une extension de fichier G-code correcte pour la sortie de la tâche.
-   Sélection des commandes G-code. Les commandes numériques prennent généralement en charge un sous-ensemble de commandes G-code disponibles. Le super-ensemble de commandes G-code contient des commandes puissantes et spécialisées qui doivent être traitées à l\'aide de plusieurs commandes plus simples. Les post-processeurs sont écrits pour sélectionner le meilleur G-code pour une opération, disponible sur la cible.
-   Formatage de la syntaxe du G-code en réordonnant les entrées Feed (avance), X, Y, Z, A et B ainsi que la précision.
-   Insertion d\'un préambule pour définir les unités, le format des unités, le plan de travail, le système de coordonnées, etc\...
-   Insertion d\'un post-amble pour stationner la machine, l\'arrêter, traiter les arguments.
-   Insérer des changements d\'outils, ou les supprimer entre les opérations suivantes utilisant le même outil.
-   Formatage des informations relatives à l\'avance et à la vitesse en tours par minute ou par seconde.
-   Formatage de l\'appellation et de l\'appel des fonctions.



### Personnalisation du post-processeur 

Si vous souhaitez écrire votre propre post-processeur, consultez la page [Path Personnalisation du post-processeur](Path_Postprocessor_Customization/fr.md).

**Remarque :** plusieurs post-processeurs fournis génèrent un code adapté à de nombreux contrôleurs CNC ou peuvent être utilisés comme modèles pour des modifications.

Les post-processeurs contiennent des indicateurs de configuration et sont conçus pour être ajustés en ajoutant des G-codes et M-codes aux définitions fournies pour :

-   Initialisation de la machine
-   Finalisation de la tâche
-   Changements d\'outils
-   Refroidissement activé/désactivé
-   Etc\...

Les post-processeurs utilisent le \[Path_scripting/fr#Le_format_G-code_interne_de_FreeCAD\|dialecte G-code interne de FreeCAD\] en conjonction avec les définitions de configuration du post-processeur, afin de générer un G-code correct du point de vue dialectal pour les machines cibles. Cela permet à l\'atelier Path de générer du G-code correct pour cibler différents contrôleurs de machines CNC en appelant différents post-processeurs.

Les types de contrôleur de machine CNC comprennent :

-   Fraiseuses CNC
-   Tours CNC
-   Imprimantes 3D
-   Couteaux tractés
-   Découpeurs laser
-   Graveurs
-   Découpeurs à torche plasma
-   Cintreuses
-   Usinage par décharge électrique
-   Etc\...

Si une seule machine CNC est utilisée ou si toutes les machines CNC partagent un post-processeur commun, l\'atelier Path ne doit inclure qu\'un seul post-processeur. Si un seul post-processeur est insuffisant pour générer un G-code pour tous les contrôleurs CNC cibles, plusieurs post-processeurs doivent être installés.



## Utilisation

1.  Sélectionnez une <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Path Tâche](Path_Job/fr.md) dans la [vue en arborescence](Tree_view/fr.md).
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_Post.svg" width=16px> [Post-traitement](Path_Post/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Post.svg" width=16px> Post-traitement ** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **P**.
3.  Confirmez le nom et le répertoire de **Fichier de sortie**.



## Options

Les propriétés du fichier de sortie et du post-processeur peuvent être définies dans la [tâche](Path_Job/fr.md) à tout moment, avant d\'appeler le post-processeur.

Les post-processeurs fournis sont écrits avec des commentaires indiquant les zones contenant des balises, des variables de configuration et des sections de G-codes et de M-codes qui doivent être utilisés par le post-processeur pour configurer la sortie.

Les indicateurs True/False de la configuration type incluent :

-   **OUTPUT_COMMENTS** (True=Autoriser, False=Supprimer) : utilisé pour insérer des commentaires texte dans le fichier G-code de sortie.
-   **OUTPUT_HEADER** (True=Autoriser, False=Supprimer) : utilisé pour insérer des en-têtes de texte dans le fichier G-code de sortie.
-   **OUTPUT_LINE_NUMBERS** (True=Autoriser, False=Supprimer) : utilisé pour insérer des numéros de ligne dans le fichier G-code de sortie.
-   **SHOW_EDITOR** (True=Autoriser, False=Supprimer) : utilisé pour afficher le G-code de sortie dans une fenêtre contextuelle lors de l\'appel du Post-processeur.
-   **MODAL** (True=Autoriser, False=Supprimer) : utilisé pour réduire le nombre de lignes G-code en sortie en supprimant les informations dU Mode lorsque le Mode ne change pas.

Les variables de configuration typiques incluent:

-   **LINENR** (numéro de ligne) : utilisé pour définir l\'index du numéro de ligne.
-   **UNITS** (G20 ou G21) : utilisé pour communiquer explicitement au contrôleur CNC cible quelles unités utiliser pour interpréter le fichier de sortie final.
-   **MACHINE_NAME** (nom de la fraiseuse CNC cible) : utilisé pour insérer une étiquette de nom de machine dans le fichier de sortie final.
-   **PRECISION** : utilisé pour définir le nombre de chiffres à inclure après la décimale dans le fichier de sortie final

Les sections de configuration typiques incluent:

-   **PREAMBULE** : configuration du code insérée au début de la tâche.
-   **POSTAMBLE** : configuration du code annexée à la tâche, permettant de stationner la machine, etc\...
-   **TOOL_CHANGE** : code inséré avec chaque changement d\'outil dans la tâche.


**Édition**

→ **Préférences...** → **Path** → **Préférences des tâches** → **Valeurs par défaut** → **Parcours** permet de définir le post-processeur par défaut sélectionné lors de la création de la tâche. Ceci permet à l\'atelier Path d\'être configuré pour n\'afficher que les post-processeurs souhaités et de définir une valeur par défaut.

Les post-processeurs inclus sont enregistrés dans **FreeCAD/Mod/Path/Path/Post/scripts** par défaut :

-   centroid
-   comparams
-   dxf
-   dynapath
-   grbl, y compris la prise en charge des blocs d\'en-tête bCNC à l\'aide de l\'argument de sortie du travail \--bcnc
-   jtech (laser)
-   [linuxcnc](http://linuxcnc.org/docs/html/gcode/g-code.html#gcode:g17-g19.1)
-   mach3_mach4
-   nccad
-   opensbp
-   phillips
-   refactorisé\* (Ces post-processeurs sont en cours d\'élaboration et vont beaucoup évoluer)
-   rml
-   smoothie
-   uccnc

## Limitations

N\'utilisez **pas** le menu **Fichier** → **Exporter** pour exporter vers le G-code, cela produirait un G-code endommagé!





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Post/fr
