---
- GuiCommand:/fr
   Name:Path Job
   Name/fr:Path Tâche
   MenuLocation:Path → Job
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **F**
   SeeAlso:
---


</div>

## Description

L\'outil Travail (Tâche) crée un nouvel objet Travail dans le document actif. L\'objet Travail contient les informations suivantes:

1.  Une liste de définitions des paramètres des outils, spécifiant la géométrie, les paramètres de coupe et les vitesses pour les outils des Opérations de Path.
2.  Une liste séquentielle du flux de travail des Opérations de Path.
3.  Un Corps de base: un clone utilisé pour le décalage.
4.  Un Brut représentant la matière première qui sera usinée dans l\'atelier Path.
5.  Une feuille de calcul, contenant les entrées utilisées par les opérations de Path, y compris les valeurs statiques et les formules.
6.  Les Paramètres de configuration spécifiant le chemin de destination, le nom de fichier et l\'extension du fichier G-Code, ainsi que le post-processeur utilisé pour générer le langage approprié pour le contrôleur CNC cible et personnaliser les unités, les changements d\'outil, le stationnement, etc.

## Usage


<div class="mw-translate-fuzzy">

1.  Appelez la commande Tâche en utilisant plusieurs méthodes:
    -   Appuyez sur le bouton **<img src="images/Path_Job.svg" width=16px> [Tâche](Path_Job/fr.md)** dans la barre d\'outils.
    -   Utilisation du raccourci clavier **P** puis **F**.
    -   Utilisation de l\'entrée **Path → Tâche** dans le menu supérieur.


</div>

La boîte de dialogue GUI de la Tâche comporte cinq onglets alignés horizontalement: **General**, **Output**, **Setup**, **Tools** et **Workplan**. L\'utilisateur peut à tout moment utiliser les options **OK** ou **Cancel** dans la boîte de dialogue.

## Généralités

![](images/Job_1.jpg )

-   **Label**: L\'étiquette du Travail affiché dans l\'arborescence.
-   **Model**: Objet de Base qui définit par sa forme les parcours d\'usinage. S\'il s\'agit d\'un objet Part Design, c\'est généralement le corps que vous sélectionnez ici. Si vous avez sélectionné un élément dans l\'arborescence *avant*, cliquez sur l\'icône \"Ajouter un Travail\". Cet élément est déjà entré ici. Vous pouvez le modifier en sélectionnant un élément différent dans le menu déroulant.
-   **Description**: Vous pouvez ajouter quelques notes au travail ici. Les notes sont seulement pour votre information et n\'ont aucun effet sur le parcours d\'usinage.

## Sortie

![](images/Job_2.jpg )

-   **Fichier de sortie**: Définissez le nom, l\'extension et le chemin du fichier de sortie G-Code. Vous pouvez utiliser les espaces réservés suivants:
    -   **%D** Répertoire du document actif
    -   **%d** nom du document actif (sans extension)
    -   **%M** répertoire macro utilisateur
    -   **%j** nom de l\'emploi

-   **Processor**: Sélectionnez le post-processeur pour votre machine.
-   **Arguments**: Ajoutez des arguments pour le post-processeur si nécessaire.

## Conditions initiales 

![](images/Job_3.jpg )

-   **Brut**: définir la taille et la forme de la matière première.
-   **Orientation**:Le bord ou la face sélectionné est utilisé pour orienter la base ou le support en conséquence.
-   **Alignement**: sélectionnez un sommet pour définir l\'origine ou déplacer une base ou un stock

## Outils

![](images/Job_4.jpg )

Ajoutez le(s) outil(s) de votre [Magasin d\'outils](Path_ToolLibraryEdit/fr.md) dont vous avez besoin pour les opérations de ce travail.

Après avoir ajouté un outil, vous pouvez définir / modifier l\'avance et la vitesse de broche si vous avez besoin d\'une vitesse d\'avance différente dans cette tâche. Une modification ici ne modifie pas les paramètres stockés dans le magasin d\'outils.

L\'outil par défaut que vous pouvez supprimer si vous avez ajouté un outil personnel.

## Plan de travail 

![](images/Job_5.jpg )

Si vous avez une tâche qui implique plus d\'une opération d\'usinage, vous pouvez déterminer dans quel ordre les opérations doivent être effectuées. Pour réorganiser, sélectionnez une opération et appuyez sur le bouton haut ou bas.


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
