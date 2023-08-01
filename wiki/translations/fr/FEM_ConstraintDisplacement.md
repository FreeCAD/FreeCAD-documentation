---
- GuiCommand:/fr
   Name:FEM ConstraintDisplacement
   Name/fr:FEM Contrainte de déplacement
   MenuLocation:Modèle → Contraintes mécaniques → Contrainte de déplacement
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Shortcut:
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM ConstraintDisplacement/fr

## Description

Crée une contrainte FEM pour un déplacement imposé d\'un objet sélectionné pour un degré de liberté spécifié.



## Utilisation

1.  Soit vous appuyez sur le bouton **<img src="images/FEM_ConstraintDisplacement.svg" width=16px> '''Contrainte de déplacement'''**, soit vous sélectionnez le menu **Modèle → Contraintes mécaniques → <img src="images/FEM_ConstraintDisplacement.svg" width=16px> Contrainte de déplacement**.
2.  Dans la [vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la contrainte doit être appliquée, qui peut être un sommet (coin), une arête ou une face.
3.  Appuyez sur le bouton **Ajouter**.
4.  Décochez *Non spécifié* pour activer les champs nécessaires à l\'édition.
5.  Définir les valeurs ou ({{Version/fr|0.21}}) spécifier une formule pour les déplacements.



## Formules


{{Version/fr|0.21}}



### Général

Pour le <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [solveur Elmer](FEM_SolverElmer/fr.md), il est possible de définir le déplacement sous la forme d\'une formule. Dans ce cas, le solveur définit le déplacement en fonction de la variable de la formule rentrée.

Prenons par exemple le cas où nous voulons effectuer une [analyse transitoires](FEM_SolverElmer_SolverSettings/fr#Pas_de_temps_(analyses_transitoires).md). Pour chaque pas de temps, le déplacement $d$ doit être augmenté de 6 mm :

$\quad
d(t)=0.006\cdot t$

entrez ce qui suit dans le champ *Formula* : ` Variable "time"; Real MATC "0.006*tx"`

Ce code a la syntaxe suivante :

-   le préfixe *Variable* spécifie que le déplacement n\'est pas une constante mais une variable
-   la variable est l\'heure en cours
-   les valeurs de déplacement sont renvoyées sous forme de valeurs *Real* (virgule flottante)
-   *MATC* est un préfixe pour le solveur Elmer indiquant que le code suivant est une formule
-   *tx* est toujours le nom de la variable dans les formules *MATC*, peu importe que *tx* dans notre cas soit en fait *t*

### Rotations

Elmer n\'utilise que les champs **Displacement \*** de la contrainte. Pour définir les rotations, nous avons besoin d\'une formule.

Si, par exemple, une face doit être pivotée en fonction de cette condition :

$\quad
\begin{align}
d_{x}(t)= & \left(\cos(\phi)-1\right)x-\sin(\phi)y\\
d_{y}(t)= & \left(\cos(\phi)-1\right)y+\sin(\phi)x
\end{align}$

Il faut alors entrer pour **Displacement x** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(1)-sin(tx(0)*pi)*tx(2)`

et pour **Displacement y** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(2)+sin(tx(0)*pi)*tx(1)`

Ce code a la syntaxe suivante :

-   nous avons 4 variables, le temps et toutes les coordonnées possibles (x, y z)
-   *tx* est un vecteur, *tx(0)* se réfère à la première variable, le temps, tandis que *tx(1)* est la première coordonnée *x*
-   *pi* désigne $\pi$ et a été ajouté pour qu\'après $t=1\rm\, s$ une rotation de 180° soit effectuée



## Remarques

Pour le <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md) :

-   La contrainte utilise la carte \*BOUNDARY.
-   Fixer un degré de liberté est expliqué à l\'adresse <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html>.
-   Imposer un déplacement pour un degré de liberté est expliqué à l\'adresse <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/fr
