---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintDisplacement
   Name/fr: FEM Condition limite de déplacement
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Condition limite de déplacement
   Workbenches: FEM_Workbench/fr
   Shortcut: 
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintDisplacement/fr

## Description

Crée une condition limite FEM pour un déplacement donné d\'un objet sélectionné pour les degrés de liberté spécifiés.



## Utilisation

1.  Soit vous appuyez sur le bouton **<img src="images/FEM_ConstraintDisplacement.svg" width=16px> [Condition limite de déplacement](FEM_ConstraintDisplacement/fr.md)**, soit vous sélectionnez le menu **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintDisplacement.svg" width=16px> Condition limite de déplacement**.
2.  Appuyez sur le bouton **Ajouter**.
3.  Dans la [vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la condition de limite doit être appliquée, qui peut être un sommet, une arête ou une face (mais tous les objets sélectionnés doivent être du même type). Pour supprimer des objets de la liste, appuyez sur le bouton **Supprimer** et cliquez dessus.
4.  Cochez les cases à côté des degrés de liberté que vous souhaitez utiliser. Par défaut, ils sont fixés à zéro (fixe) mais n\'importe quelle valeur ({{Version/fr|0.21}} : ou une formule pour Elmer) peut être spécifiée.



## Formules


{{Version/fr|0.21}}



### Général

Pour le <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [solveur Elmer](FEM_SolverElmer/fr.md), il est possible de définir le déplacement sous la forme d\'une formule. Dans ce cas, le solveur définit le déplacement en fonction de la variable de la formule rentrée.

Prenons par exemple le cas où nous voulons effectuer une [analyse transitoire](FEM_SolverElmer_SolverSettings/fr#Pas_de_temps_(analyses_transitoires).md). Pour chaque pas de temps, le déplacement $d$ doit être augmenté de 6 mm :

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

Elmer n\'utilise que les champs **Displacement \*** de la condition limite. Pour définir les rotations, nous avons besoin d\'une formule.

Si, par exemple, une face doit être pivotée en fonction de cette condition :

$\quad
\begin{align}
d_{x}(t)= & \left(\cos(\phi)-1\right)x-\sin(\phi)y\\
d_{y}(t)= & \left(\cos(\phi)-1\right)y+\sin(\phi)x
\end{align}$

Il faut alors entrer pour **Déplacement en X** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(1)-sin(tx(0)*pi)*tx(2)`

et pour **Déplacement en Y** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(2)+sin(tx(0)*pi)*tx(1)`

Ce code a la syntaxe suivante :

-   nous avons 4 variables, le temps et toutes les coordonnées possibles (x, y z)
-   *tx* est un vecteur, *tx(0)* se réfère à la première variable, le temps, tandis que *tx(1)* est la première coordonnée *x*
-   *pi* désigne $\pi$ et a été ajouté pour qu\'après $t=1\rm\, s$ une rotation de 180° soit effectuée



## Remarques

Pour le <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md) :

-   Cet outil utilise le jeu de paramètres \*BOUNDARY.
-   Fixer un degré de liberté est expliqué à l\'adresse <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html>.
-   Imposer un déplacement pour un degré de liberté est expliqué à l\'adresse <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/fr
