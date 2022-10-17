# FEM SolverElmer SolverSettings/fr
Cette page décrit les paramètres possibles pour le [solveur Elmer](FEM_SolverElmer/fr.md).

# Général

Elmer est un solveur multiphysique. Par conséquent, vous pouvez utiliser plusieurs équations principales pour résoudre des problèmes. Les différentes équations sont listées [ici](FEM_SolverElmer/fr#A_propos_des_.C3.A9quations.md).

Il existe des paramètres du solveur, disponibles pour toutes les équations. Ils sont décrits ici. Les paramètres disponibles uniquement pour une équation particulière sont décrits dans les pages de l\'équation correspondante.

Elmer offre les [types de résolution](#Type.md) *régime stationnaire* et *transient* et deux principaux systèmes de résolution, [système linéaire](#Syst.C3.A8me_lin.C3.A9aire.md) et [système non linéaire](#Syst.C3.A8me_non_lin.C3.A9aire.md). Le système non linéaire est utilisé pour les <img alt="" src=images/FEM_EquationFlow.svg  style="width   *24px;"> [Équations d\'écoulement](FEM_EquationFlow/fr.md) et les <img alt="" src=images/FEM_EquationHeat.svg  style="width   *24px;"> [Équations de chaleur](FEM_EquationHeat/fr.md).

# Modification des paramètres 

Les paramètres du solveur se trouvent dans l\'[éditeur de propriétés](Property_editor/fr.md) après avoir cliqué sur une équation dans la [vue en arborescence](Tree_view/fr.md). Vous pouvez les modifier directement à cet endroit comme n\'importe quelle autre propriété.

## Le solveur 

### Pas de temps 

Pour les simulations transitoires, les pas de temps doivent être définis. Ceci est fait par les paramètres suivants    *

-    **BDFOrder**   * ordre pour la méthode *BDF* ([Backward Differentiation Formula](https   *//en.wikipedia.org/wiki/Backward_differentiation_formula)). Elle n\'est actuellement utilisée que pour l\'<img alt="" src=images/FEM_EquationHeat.svg  style="width   *24px;"> [équation de chaleur](FEM_EquationHeat/fr.md). Il est recommandé d\'utiliser la valeur par défaut de 2.

-    **Timestep Intervals**   * tableau de calculs par intervalle de temps. Le solveur effectuera un intervalle de temps après l\'autre. Par exemple, si le solveur doit calculer les 10 premières secondes par pas de 0,1 seconde, puis 50 secondes par pas de 1 seconde et enfin s\'arrêter, vous devez définir les intervalles de temps \[100, 50\] et les intervalles de taille de pas de temps \[0.1, 1.0\].

-    **Timestep Sizes**   * tableau de pas de temps. L\'unité de temps est la seconde. Le tableau correspond aux **Timestep Intervals**.

### Type

-    **Simulation type**   * si la simulation est *Steady state*, *Transient* ou simplement *Scanning*. Transitoire signifie que l\'évolution dans le temps est calculée. Voir la section [Pas de temps](#Pas_de_temps.md) pour les paramètres nécessaires.

-    **Steady State Max Iterations**   * nombre maximum d\'exécutions du solveur en régime stationnaire.

-    **Steady State Min Iterations**   * nombre minimum d\'exécutions du solveur en régime stationnaire.

## Équation

### Base

Toutes les équations ont ces propriétés    *

-    **Label**   * nom de l\'équation dans l\'arborescence.

-    **Priority**   * nombre déterminant la priorité de cette équation par rapport aux autres équations de l\'analyse. L\'équation ayant le numéro le plus élevé dans l\'analyse sera résolue en premier. Si deux équations ont le même numéro de priorité, celle qui est la première dans l\'arborescence sera résolue en premier.

-    **Stabilize**   * si défini à *true*, le solveur utilisera la méthode des éléments finis stabilisés lors de la résolution de l\'équation de la chaleur avec un terme de convection. S\'il est défini sur *false*, la stabilisation par Residual Free Bubble (RFB) est utilisée à la place. Si la convection domine, la stabilisation doit être utilisée afin de résoudre l\'équation avec succès.

### Système linéaire 

Ce système a les propriétés suivantes    *

-    **BiCGstabl Degree**   * degré polynomial pour la méthode de résolution itérative *BiCGStabl*. Ceci n\'a d\'effet que si **Linear Solver Type** est *Iterative* et **Linear Iterative Method** est *BiCGStabl*. Il est recommandé de commencer par la valeur par défaut de 2.

-    **Idrs Parameter**   * paramètre pour la méthode du solveur itératif *Idrs*. Ceci n\'a un effet que si **Linear Solver Type** est *Iterative* et **Linear Iterative Method** est *Idrs*. Il est recommandé de commencer avec la valeur par défaut de 2. Le réglage du paramètre à 3 peut augmenter un peu la vitesse de résolution. Pour les analyses de flux, la méthode *Idrs* est jusqu\'à 30 % plus rapide que la méthode par défaut *BiCGStab*.

-    **Linear Direct Method**   * méthode utilisée pour la résolution directe. Ceci n\'a un effet que si Les méthodes possibles sont *Banded*, *MUMPS* et *Umpfpack*. Notez que *MUMPS* doit généralement être installé avant que vous puissiez l\'utiliser.Remarque    * lorsque vous utilisez plus d\'un noyau CPU pour le solveur ({{Version/fr|1.0}}), seul *MUMPS* peut être utilisé.

-    **Linear Iterations**   * nombre maximal d\'itérations pour une exécution itérative du solveur. Ceci n\'a un effet que si **Linear Solver Type** est *Iterative*.

-    **Linear Iterative Method**   * méthode utilisée pour la résolution itérative. Ceci n\'a d\'effet que si **Linear Solver Type** est *Iterative*.

-    **Linear Preconditioning**   * méthode utilisée pour le préconditionnement. Pour plus d\'informations sur le préconditionnement, voir [cette présentation (en)](http   *//www.nic.funet.fi/index/elmer/slides/ElmerLinearSolvers.pdf) (page 8) d\'Elmer.

-    **Linear Solver Type**   * si la résolution est faite *Direct* ou *Iterative*.

-    **Linear System Solver Disabled**   * désactive le solveur linéaire. N\'utilisez cette option que dans des cas particuliers.Elle peut être utilisée pour désactiver temporairement une équation puisque sa résolution n\'est alors pas effectuée. Il existe cependant des cas où le solveur est envoyé dans une boucle infinie à la place.

-    **Linear Tolerance**   * la tolérance pour que le solveur s\'arrête. Si l\'erreur est inférieure à la tolérance, l\'exécution du solveur est terminée. Sinon, le nombre total d\'itérations linéaires Dans le log du solveur Elmer, vous voyez comment l\'erreur est minimisée pendant l\'exécution du solveur. (Regardez dans le log, à la fin de chaque itération du solveur, la valeur derrière *Relative Change*). Dans le cas où elle ne descend pas en dessous d\'une certaine valeur mais atteint une valeur supérieure à la tolérance actuelle qui est acceptable pour vous, vous pouvez augmenter la tolérance.

### Système non linéaire 

Ce système est itératif et possède les propriétés suivantes    *

-    **Nonlinear Iterations**   * nombre maximal d\'itérations.

-    **Nonlinear Newton After Iterations**   *

-    **Nonlinear Newton After Tolerance**   *

-    **Nonlinear Newton After Tolerance**   * la tolérance pour l\'arrêt du solveur. Si l\'erreur est inférieure à la tolérance, l\'exécution du solveur est terminée. Sinon, le nombre total d\'itérations Dans la réponse d\'Elmer, vous voyez comment l\'erreur est minimisée pendant l\'exécution du solveur. Au cas où elle ne descendrait pas en dessous d\'une certaine valeur acceptable mais supérieure à la tolérance actuelle, vous pouvez augmenter la tolérance.

-    **Relaxation Factor**   * c\'est LE paramètre le plus important dans le cas où le solveur ne converge pas    *

#### Facteur de relaxation 

Si les résultats des itérations du solveur oscillent numériquement, les résultats du solveur ne peuvent pas converger vers une valeur finale et stable. Pour éviter cela, la variable calculée $T_{i}$ de la i-ième itération/exécution du solveur n\'est pas prise comme entrée pour l\'itération suivante, mais $T_{i}^{'}$, une valeur qui est \"amortie\" avec le résultat de l\'itération précédente. Le facteur de relaxation $\lambda$ est donc défini comme suit

$\quad
T_{i}^{'} = \lambda T_{i}+\left(1-\lambda\right)T_{i-1}$

Ainsi, pour la valeur par défaut de 1,0, aucun amortissement n\'est utilisé. Plus $\lambda$ est petit, plus l\'amortissement est important et plus le temps de convergence est long. Par conséquent, si le solveur ne converge pas, commencez à modifier le facteur de relaxation à 0,9, puis à 0,8 et ainsi de suite. Les valeurs inférieures à 0,3 sont inhabituelles et si vous en avez besoin, vous devriez examiner de plus près les mathématiques de votre analyse.Pour les cas, où vous obtenez une convergence correcte, vous pouvez définir $\lambda$ au-dessus de 1,0 pour accélérer la convergence.

### Régime stationnaire 

Cette partie des paramètres n\'a qu\'une seule propriété    *

-    **Steady State Tolerance**   * la tolérance spécifique de convergence du régime stationnaire ou du système couplé. Tous les solveurs d\'équations doivent respecter leurs propres tolérances pour la variable $\omega^2$ qu\'ils calculent, avant que l\'ensemble du système soit considéré comme convergé. Le critère de tolérance est    *

$\quad
\left\Vert u_{i}-u_{i-1}\right\Vert <\epsilon\left\Vert u_{i}\right\Vert$

alors que $\epsilon$ est la tolérance en régime stationnaire et $u_{i}$ est la variable calculée dans la i-ième itération/exécution du résolveur.


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverElmer SolverSettings/fr
