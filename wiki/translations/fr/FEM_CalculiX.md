# FEM CalculiX/fr
{{TOCright}}

## Introduction

Cette page rassemble des informations sur le solveur d\'éléments finis [CalculiX](http://www.calculix.de/), le solveur par défaut de l\'**<img src="images/Workbench_FEM.svg" width=24px> [atelier FEM](FEM_Workbench/fr.md)** pour l\'analyse structurelle et thermo-mécanique à partir de FreeCAD 0.17. Selon le système d\'exploitation que vous utilisez, vous devrez installer CalculiX avant de lancer votre première simulation. Veuillez voir [Installation des composants requis pour l'atelier FEM](FEM_Install/fr.md).

Le solveur est capable de faire des calculs linéaires et non linéaires pour des problèmes statiques, dynamiques et thermiques. Le solveur opère sur un fichier Abaqus (`.inp`), ce qui signifie qu\'il peut être utilisé avec différents pré-processeurs prenant en charge ce format. Le programme inclut son propre préprocesseur graphique qui, toutefois, n'est pas utilisé par FreeCAD, mais uniquement par le solveur lui-même.

CalculiX est conçu pour fonctionner sur les plates-formes Unix telles que les ordinateurs Linux et Irix mais également sur MS-Windows. CalculiX a été développé par des ingénieurs de MTU Aero Engines, Munich, Allemagne, pour les aider à concevoir des machines telles que des turbines à jet. Le logiciel est actuellement disponible au public selon les termes de la GPL version 2.



## Intégration à FreeCAD 

L\'interaction entre l\'[atelier FEM](FEM_Workbench/fr.md) et CalculiX s\'effectue par l\'écriture et la lecture de fichiers texte. La séquence des opérations est la suivante :

1.  Un fichier d\'entrée CalculiX est créé avec les détails nécessaires à l\'exécution de la simulation.
2.  Le solveur CalculiX est démarré avec ce fichier d\'entrée.
3.  La sortie du solveur est enregistrée.
4.  Les fichiers de sortie du solveur sont lus, s'ils sont disponibles.

L\'outil [FEM Réglage du solveur](FEM_SolverControl/fr.md) gère l\'ensemble du processus. L\'interaction de l\'utilisateur dans le processus est possible.



## L\'interface de post-traitement 

Le fichier d\'entrée utilisé par CalculiX peut être préparé et édité avant le démarrage du solveur. Les unités utilisées dans le fichier d\'entrée sont indépendantes des unités définies dans FreeCAD ; ils seront toujours en millimètres (mm) et en Newton (N).


**(À faire : vérifiez ceci. Que se passe-t-il avec le maillage est si l'unité inch est utilisée dans FreeCAD ? Parce que la densité a été introduite, avec cela nous avons kg et s et non plus N ?! comment ça ?!)**

L\'interface CalculiX prend en charge les objets suivants :



### Eléments MEF 

-   Tet4 et Tet10
-   S3 et S6
-   B31 et B32
-   et ceux décrits dans [FEM Maillage avec Calculix](FEM_Mesh_CalculiX/fr.md)



### Analyses

-   analyse statique linéaire
-   analyse fréquencielle
-   analyse structurale thermique couplée



### Matériaux

-   un matériau élastique linéaire isotrope (uniformité dans toutes les directions)
-   plusieurs matériaux sont en développement



## Interface de post-traitement 

L\'atelier FEM charge les résultats de CalculiX dans l\'[objet résultat](FEM_ResultShow/fr.md) qui contiendra :

-   Déplacements
-   Contraintes
-   Déformations
-   Déformation plastique équivalente (PEEQ) - si un matériau non linéaire a été utilisé.
-   Température - pour l\'analyse thermomécanique.

FreeCAD lit les résultats du fichier \*.frd qui a été créé par CalculiX. Si ces résultats contiennent plusieurs pas de temps, chaque pas de temps est importé dans FreeCAD comme un nouvel objet résultat. Le même comportement s\'applique à l\'analyse fréquentielle ou de flambage avec de multiples valeurs propres.

Les forces de réaction se trouvent dans le fichier ccx_dat_file qui contient les composantes des forces de réaction (fx, fy, fz) pour chaque contrainte fixée et pour chaque déplacement de contrainte qui contraint les degrés de liberté de déplacement.



## En relation 

-   [FEM Maillage avec Calculix](FEM_Mesh_CalculiX/fr.md)
-   [Préférences de CalculiX](FEM_Preferences/fr#CalculiX.md) dans le menu des préférences de l\'atelier FEM.


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [FEM](Category_FEM.md) > FEM CalculiX/fr
