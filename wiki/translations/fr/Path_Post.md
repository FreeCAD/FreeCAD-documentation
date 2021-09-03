---
- GuiCommand:/fr
   Name:Path PostProcess
   Name/fr:Path Post-traitement
   MenuLocation:Path → Post-traitement
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **P**
   SeeAlso:
---


</div>

## Description


<div class="mw-translate-fuzzy">

Le bouton **<img src="images/Path_PostProcess.svg" width=16px> [Post-traitement](Path_Post/fr.md)** exporte la **<img src="images/Path_Job.svg" width=16px> [Path Tâche](Path_Job/fr.md)** sélectionnée vers un fichier G-Code.


</div>

**Chaque contrôleur CNC utilise un langage G-Code spécifique, nécessitant un Post-processeur correcteur de langage pour traduire la sortie finale du langage G-Code FreeCAD interne agnostique.**

### Typical functions of the Postprocessor include 


<div class="mw-translate-fuzzy">

### Les fonctions typiques du postprocesseur incluent 

Les fonctions typiques du Post-processeur incluent:

-   Utilisation d\'une extension de fichier G-Code de sortie de travail correcte.
-   Sélection des commandes G-Code. Les contrôleurs CNC prennent généralement en charge un sous-ensemble de commandes G-Code disponibles. Le super-ensemble de commandes G-Code contient des commandes puissantes et spécialisées qui, autrement, doivent être traitées en utilisant plusieurs commandes plus simples. Les post-processeurs sont écrits pour sélectionner le meilleur code G pour une opération, disponible sur la cible.
-   Formatage de la syntaxe G-Code en réorganisant les entrées Feed (avance), X, Y, Z, A et B et la précision.
-   Insertion d\'un préambule pour régler les unités, le format des unités, le plan de travail, le système de coordonnées, etc \...
-   Insérer un post-amble pour garer la machine, l\'arrêter, traiter tous les arguments.
-   Insérer des changements d\'outil, ou les supprimer entre les opérations suivantes utilisant le même outil.
-   Formatage des informations d\'avance et de vitesse en tours par minute ou par seconde.
-   Fonction de mise en forme du nom d\'appel et appel.


</div>

### Postprocessor Customization 


<div class="mw-translate-fuzzy">

### Personnalisation du postprocessor 

Si vous souhaitez écrire votre propre postprocesseur, consultez la page [Path Personnalisation du postprocesseur](Path_Postprocessor_Customization/fr.md).


</div>

**Remarque:** plusieurs Post-processeurs fournis génèrent un code approprié pour de nombreux contrôleurs CNC, ou peuvent être utilisés comme modèles pour la modification

Les post-processeurs contiennent des indicateurs de configuration et sont conçus pour être ajustés en ajoutant des G-codes et M-Codes aux définitions fournies pour:

-   Initialisation de la machine
-   Finalisation de l\'emploi
-   Changements d\'outils
-   Refroidissement activé / désactivé
-   Etc\...

Les post-processeurs utilisent le [langage G-Code des opérations de travail Path de FreeCAD](https://www.freecadweb.org/wiki/Path_scripting/fr#Format_G-Code_interne_de_FreeCAD), en conjonction avec les définitions de configuration du Post-processeur, pour générer le G-Code corrigé pour les machines cibles. Cela permet à l\'atelier Path de générer un G-code correct pour cibler divers contrôleurs de machine CNC en appelant différents Post-processeurs.

Les types de contrôleur de machine CNC comprennent:

-   Fraiseuses CNC
-   Tours CNC
-   Imprimantes 3D
-   Couteaux tractés
-   Découpeurs laser
-   Graveurs
-   Découpeurs à torche plasma
-   Cintreuses
-   Coupeurs EDM
-   Etc\...

Si une seule machine CNC est utilisée ou si toutes les machines CNC partagent un Post-processeur commun, l\'atelier Path ne doit inclure qu\'un seul Post-processeur. Si un seul Post-processeur est insuffisant pour générer un G-code pour tous les contrôleurs CNC cibles, plusieurs Post-processeurs doivent être installés.

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionnez le **<img src="images/Path_Job.svg" width=16px> [Path Tâche](Path_Job/fr.md)** que vous souhaitez exporter
2.  Appelez la commande en utilisant plusieurs méthodes:
    -   En appuyant sur le bouton **<img src="images/Path_PostProcess.svg" width=24px>** dans la barre d\'outils.
    -   Utilisation du raccourci clavier **P** puis **P**.
    -   Utilisation de l\'entrée **Path** → **<img src="images/Path_PostProcess.svg" width=24px> [Post-traitement](Path_Post/fr.md)** dans le menu supérieur.
3.  Confirmez le nom et le répertoire **Fichier de sortie**


</div>

## Options

Les propriétés du fichier de sortie et du post-processeur peuvent être définies dans le [Travail](Path_Job/fr.md) à tout moment, avant d\'appeler le Post-processeur.

Les post-processeurs fournis sont écrits avec des commentaires indiquant les zones contenant des Balises, des Variables de configuration et des Sections de G-codes et de M-codes qui doivent être utilisés par le post-processeur pour configurer la sortie.

Les indicateurs True/False de la configuration type incluent:

-   OUTPUT\_COMMENTS (True=Autoriser, False=Supprimer), Utilisé pour insérer des commentaires texte dans le fichier G-Code de sortie.
-   OUTPUT\_HEADER (True=Autoriser, False=Supprimer), Utilisé pour insérer des en-têtes de texte dans le fichier G-Code de sortie.
-   OUTPUT\_LINE\_NUMBERS (True=Autoriser, False=Supprimer), Utilisé pour insérer des numéros de ligne dans le fichier G-Code de sortie.
-   SHOW\_EDITOR (True=Autoriser, False=Supprimer), Utilisé pour afficher le G-code de sortie dans une fenêtre contextuelle lors de l\'appel du Post-processeur.
-   MODAL (True=Autoriser, False=Supprimer), Utilisé pour réduire le nombre de lignes G-Code en sortie en supprimant les informations de Mode lorsque le Mode ne change pas.

Les variables de configuration typiques incluent:

-   LINENR (numéro de ligne), utilisé pour définir l\'index du numéro de ligne.
-   UNITS (G20 ou G21), Utilisé pour communiquer explicitement au contrôleur CNC cible quelles unités utiliser pour interpréter le fichier de sortie final.
-   MACHINE\_NAME (nom de la fraiseuse CNC cible), utilisé pour insérer une étiquette de nom de machine dans le fichier de sortie final.
-   PRECISION, Utilisé pour définir le nombre de chiffres à inclure après la décimale dans le fichier de sortie final

Les sections de configuration typiques incluent:

-   PREAMBULE (Configuration du code insérée au début du Travail)
-   POSTAMBLE (Configuration du code annexée au Travail, permettant de stationner la machine, etc \...)
-   TOOL\_CHANGE (code inséré avec chaque changement d\'outil dans le Travail)

L\'onglet **Edit** → **Preferences...** → **Path** → **Job Preferences tab** → **Defaults** → **Path** est utilisé pour définir le Post-processeur par défaut sélectionné lors de la création du Travail. Ceci permet à l\'atelier Path d\'être configuré pour n\'afficher que les Post-processeurs souhaités et de définir une valeur par défaut.

Les post-processeurs inclus sont enregistrés dans le fichier **FreeCAD.Mod.Path.Pathscripts.Post** par défaut:

-   centroïde
-   comparams
-   Dynapath
-   grbl, y compris la prise en charge des blocs d\'en-tête bCNC à l\'aide de l\'argument de sortie du travail \--bcnc
-   [linuxcnc](http://linuxcnc.org/docs/html/gcode/g-code.html#gcode:g17-g19.1)
-   opensbp
-   phillips
-   rml
-   smoothie

## Limitations


<div class="mw-translate-fuzzy">

## Limitations 

N\'utilisez **pas** le menu **File** → **Export**\'\'\' pour exporter vers le G-code, cela produirait un G-code endommagé!


</div>


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
