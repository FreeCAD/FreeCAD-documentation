# <img alt="Icône de l\'atelier FEM" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/fr


{{TOCright}}

## Introduction

L\'[atelier FEM](FEM_Workbench/fr.md) fournit un flux de travail moderne d\'[analyse par éléments finis](https://fr.wikipedia.org/wiki/M%C3%A9thode_des_%C3%A9l%C3%A9ments_finis) (FEA) pour FreeCAD. Cela signifie principalement que tous les outils permettant d\'effectuer une analyse sont combinés dans une seule interface utilisateur graphique (GUI).

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Flux de travail 

Les étapes pour effectuer une analyse d'éléments finis sont les suivantes :

1.  Prétraitement : configuration du problème d\'analyse.
    1.  Modélisation de la géométrie : création de la géométrie avec FreeCAD ou importation à partir d\'une autre application.
    2.  Créer une analyse.
        1.  Ajout de contraintes de simulation telles que des charges et supports fixes au modèle géométrique.
        2.  Ajout de matériaux aux pièces du modèle géométrique.
        3.  Ajout d'un matériau au modèle d'analyse.
2.  Résolution : résoudre un système d\'équations en utilisant un solveur externe depuis FreeCAD.
3.  Post-traitement : visualisation des résultats d\'analyse depuis FreeCAD.

L\'atelier FEM peut être utilisé sur les plates-formes Windows, MacOSX et Linux. Étant donné que l\'atelier utilise des solveurs externes, la quantité d'installation manuelle dépend du système d'exploitation utilisé. Voir la page [Installation FEM](FEM_Install/fr.md) pour des instructions sur la configuration des outils externes.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



*Flux de travail de l'atelier FEM ; le plan de travail appelle deux programmes externes pour effectuer le maillage d'un objet solide et pour résoudre le problème des éléments finis*

## Menu : Modèle 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Conteneur d\'analyse](FEM_Analysis/fr.md) : Crée un nouveau conteneur pour une analyse mécanique. Si un solide est sélectionné dans l\'arborescence avant de cliquer dessus, la boîte de dialogue de maillage s\'ouvrira.

### Materiaux

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Matériau pour solide](FEM_MaterialSolid/fr.md) : Vous permet de sélectionner un matériau solide de la base de données.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Matériau pour fluide](FEM_MaterialFluid/fr.md) : Permet de sélectionner un matériau fluide dans la base de données.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Matériau mécanique non linéaire](FEM_MaterialMechanicalNonlinear/fr.md) : Permet d\'ajouter un modèle de matériau mécanique non linéaire.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Matériau renforcé](FEM_MaterialReinforced/fr.md) : Permet de sélectionner dans la base de données des matériaux renforcés composés d\'une matrice et d\'un renfort.

-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Editeur de matériaux](Material_editor/fr.md) : Permet d\'ouvrir l\'éditeur de matériaux pour éditer des matériaux.

### Géométrie d\'élément 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Coupe transversale de poutre](FEM_ElementGeometry1D/fr.md) :Utilisé pour définir les coupes transversales des éléments de poutre.

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Rotation de poutre](FEM_ElementRotation1D/fr.md) : Utilisé pour faire pivoter les coupes transversales des éléments de poutre.

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Epaisseur d\'une coque](FEM_ElementGeometry2D/fr.md) : Utilisé pour définir l\'épaisseur de l\'élément de structure.

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Section fluide pour flux 1D](FEM_ElementFluid1D/fr.md) : crée un élément de section fluide FEM pour les réseaux pneumatiques et hydrauliques.

### Contraintes Electrostatiques 

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Contrainte électrostatique potentielle](FEM_ConstraintElectrostaticPotential/fr.md) :

### Contraintes de fluides 

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Contrainte de la vitesse du flux d\'écoulement](FEM_ConstraintInitialFlowVelocity/fr.md) : Utilisé pour définir une vitesse d\'écoulement initiale pour le domaine.

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Contrainte de vitesse d\'écoulement](FEM_ConstraintFlowVelocity/fr.md) : Utilisé pour définir une vitesse d\'écoulement comme condition aux limites sur une arête (2D) ou une face (3D).

### Contraintes géométriques 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Contrainte de rotation du plan](FEM_ConstraintPlaneRotation/fr.md) : Permet de définir une contrainte de rotation plane sur une face plane.

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Constraint section print](FEM_ConstraintSectionPrint/fr.md) : {{Version/fr|0.19}}

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Contrainte de transformation](FEM_ConstraintTransform/fr.md) : Utilisé pour définir une contrainte de transformation sur une face.

### Contraintes mécaniques 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Contrainte fixe](FEM_ConstraintFixed/fr.md) : Utilisé pour définir une contrainte fixe sur le point/bord/face(s).

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Contrainte de déplacement](FEM_ConstraintDisplacement/fr.md) : Utilisé pour définir une contrainte de déplacement sur le point/bord/face(s).

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Contrainte de contact](FEM_ConstraintContact/fr.md) : Utilisé pour définir une contrainte de contact entre deux faces.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Contrainte de liaison](FEM_ConstraintTie/fr.md) : Utilisé pour définir une contrainte de liaison (\"contact lié\") entre deux faces. {{Version/fr|0.19}}

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Contrainte de ressort](FEM_ConstraintSpring/fr.md) : utilisé pour définir un ressort. {{Version/fr|0.20}}

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Contrainte de force](FEM_ConstraintForce/fr.md) : Utilisé pour définir une force dans \[N\] appliquée uniformément à une face sélectionnable dans une direction définissable.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Contrainte de pression](FEM_ConstraintPressure/fr.md) : Permet de définir une contrainte de pression.

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Contrainte de poids](FEM_ConstraintSelfWeight/fr.md) : Permet de définir une accélération de gravité agissant sur un modèle.

### Contraintes thermiques 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Contrainte initiale de température](FEM_ConstraintInitialTemperature/fr.md) : Permet de définir la température initiale d\'un corps.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Contrainte flux thermique](FEM_ConstraintHeatflux/fr.md) : Permet de définir une contrainte de flux thermique sur une ou plusieurs face(s)

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Contrainte de température](FEM_ConstraintTemperature/fr.md) : Permet de définir une contrainte de température sur un point/bord/face(s).

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Contrainte de source de chaleur d\'un corps](FEM_ConstraintBodyHeatSource/fr.md) : Utilisé pour définir une source de chaleur interne d\'un objet.

### Contraintes sans solveur 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Condition aux limites du fluide](FEM_ConstraintFluidBoundary/fr.md) :

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Contrainte de roulement](FEM_ConstraintBearing/fr.md) : Utilisé pour définir une contrainte de roulement.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Contrainte d\'engrenage](FEM_ConstraintGear/fr.md) : Utilisé pour définir une contrainte de vitesse.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Contrainte de poulie](FEM_ConstraintPulley/fr.md) : Utilisée pour définir une contrainte de poulie.

### Écraser des constantes 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Constante de permittivité du vide](FEM_ConstantVacuumPermittivity/fr.md) : {{Version/fr|0.19}}

## Menu : Maillage 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [Maillage MEF à partir d\'une forme avec Netgen](FEM_MeshNetgenFromShape/fr.md) :

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Maillage MEF à partir d\'une forme avec Gmsh](FEM_MeshGmshFromShape/fr.md) :

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [Couche limite de maillage MEF](FEM_MeshBoundaryLayer/fr.md) : crée des maillages anisotropes pour des calculs précis près des frontières.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [Région de maillage MEF](FEM_MeshRegion/fr.md) : crée une ou plusieurs zones localisées à mailler, ce qui optimise considérablement le temps d\'analyse.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [Groupe de type maillage MEF](FEM_MeshGroup/fr.md) : regroupe et étiquette les éléments d\'un maillage (sommet, bord, surface) ensemble, ce qui est utile pour exporter le maillage vers des solveurs externes.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Ensemble de nœuds](FEM_CreateNodesSet/fr.md) : Crée/définit un ensemble de nœuds à partir d\'un maillage FEM.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [Maillage à maillage MEF](FEM_FemMesh2Mesh/fr.md) : convertit la surface d\'un maillage MEF en maillage.

## Menu : Résoudre 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solveur Calculix standard](FEM_SolverCalculixCxxtools/fr.md) : Crée un nouveau solveur pour cette analyse. Dans la plupart des cas, le solveur est créé avec l\'analyse.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solveur CalculiX (experimental)](FEM_SolverCalculiX/fr.md) :

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solveur Elmer](FEM_SolverElmer/fr.md) : Crée le contrôleur de solveur pour Elmer. Il est indépendant des autres objets du solveur.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solveur Mystran](FEM_SolverMystran/fr.md):

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solveur Z88](FEM_SolverZ88/fr.md) :

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Équation d\'élasticité](FEM_EquationElasticity/fr.md) :

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Équation force électrique](FEM_EquationElectricforce/fr.md) : {{Version/fr|0.19}}

-   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Équation électrostatique](FEM_EquationElectrostatic/fr.md) :

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Équation d\'écoulement](FEM_EquationFlow/fr.md) :

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Équation de flux](FEM_EquationFlux/fr.md) :

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Équation de chaleur](FEM_EquationHeat/fr.md) :

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Contrôle du travail du solveur](FEM_SolverControl/fr.md) : Ouvre le menu pour ajuster et démarrer le solveur sélectionné.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Résolution](FEM_SolverRun/fr.md) : Lance le solveur sélectionné de l\'analyse active.

## Menu : Résultats 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Purge les résultats](FEM_ResultsPurge/fr.md) : Supprime les résultats de l\'analyse active.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Affiche le résultat](FEM_ResultShow/fr.md) : Utilisé pour afficher le résultat d\'une analyse.

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Appliquer les modifications](FEM_PostApplyChanges/fr.md) :

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Post traitement affichage des résultats](FEM_PostPipelineFromResult/fr.md) :

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Filtre de distorsion](FEM_PostFilterWarp/fr.md) :

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Filtre découpe scalaire](FEM_PostFilterClipScalar/fr.md) :

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Filtre de fonction coupe](FEM_PostFilterCutFunction/fr.md) :

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Filtre rattaché à une région](FEM_PostFilterClipRegion/fr.md) :

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Filtre de données le long d\'une ligne](FEM_PostFilterDataAlongLine/fr.md) :

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Filtre de contraintes linéarisées](FEM_PostFilterLinearizedStresses/fr.md) :

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Filtre de données au point](FEM_PostFilterDataAtPoint/fr.md) :

-   [Fonctions filtres](FEM_PostCreateFunctions/fr.md) :
    -   <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;">
    -   <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;">

## Menu : Utilitaires 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Plan de coupe sur la face](FEM_ClippingPlaneAdd/fr.md) :

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Supprimer tous les plans de coupe](FEM_ClippingPlaneRemoveAll/fr.md) :

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [FEM Exemples](FEM_Examples/fr.md) : Ouvrez l\'interface graphique pour accéder aux exemples FEM.

## Menu contextuel 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Supprimer maillage MEF](FEM_MeshClear/fr.md) : supprime le fichier de maillage du fichier FreeCAD. Utile pour alléger un fichier FreeCAD.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Affichage des informations du maillage MEF](FEM_MeshDisplayInfo/fr.md) : Affiche les statistiques de base du maillage existant - nombre de nœuds et d\'éléments de chaque type.

## Préférences

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Préférences\...](FEM_Preferences/fr.md) : Préférences disponibles dans les outils FEM.

## Informations

Les pages suivantes décrivent différents sujets de l\'atelier FEM.

[FEM Install](FEM_Install/fr.md) pour plus d\'informations sur la méthode de configuration et d\'utilisation de l\'atelier FEM.

[FEM Mesh](FEM_Mesh/fr.md) pour plus d\'informations à propos de FEM Mesh dans l\'atelier FEM.

[ FEM Solver](FEM_Solver/fr.md) des informations supplémentaires sur les différents solveurs disponibles dans l'atelier et sur ceux qui pourraient être utilisés à l'avenir.

[FEM CalculiX](FEM_CalculiX/fr.md) pour plus d'informations sur CalculiX, le solveur par défaut utilisé dans l\'atelier pour l\'analyse des structures.

[FEM Concrete](FEM_Concrete/fr.md) pour des informations sur l\'analyse des structures en béton.

[FEM Project](FEM_project/fr.md) pour plus de détails et d\'informations sur les unités, limitations et développement sur l\'atelier FEM.

## Tutoriels

Tutoriel 1 : [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/fr.md) ; analyse de base sur une poutre.

Tutoriel 2 : [FEM Tutoriel](FEM_tutorial/fr.md) ; analyse de la tension dans une structure.

Tutoriel 3 : [FEM Tutoriel Python](FEM_Tutorial_Python/fr.md) ; exemple de configuration en porte-à-faux entièrement fait par scripts Python, y compris le maillage.

Tutoriel 4 : [FEM Cisaillement d\'un bloc composite](FEM_Shear_of_a_Composite_Block/fr.md) ; voir la déformation d\'un bloc composé de deux matériaux.

Tutoriel 5 : [Analyse FEM transitoire](Transient_FEM_analysis/fr.md)

Tutoriel 6 : [Post-Processing\_of\_FEM\_Results\_with\_Paraview](Post-Processing_of_FEM_Results_with_Paraview.md)

Tutoriel 7 : [Exemple FEM Capacité Deux Balles](FEM_Example_Capacitance_Two_Balls/fr.md) ; Tutoriel 6 GUI d\'Elmer \"Capacitance électrostatique deux boules\" utilisant des exemples FEM.

Tutoriel analyse de couple thermique [openSIM](https://opensimsa.github.io/training.html)

Tutoriel vidéo 1 : [Article du Forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (avec lien sur YouTube)

Tutoriel vidéo 2 : [Article du Forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (avec lien sur YouTube)

Recherche de tutoriels vidéo : [Article du Forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162640) (avec lien sur YouTube en Allemand)

## Extension de l\'atelier FEM 

L\'atelier FEM est constante évolution. Un des objectifs du projet est de trouver des moyens d'interagir facilement avec divers solveurs FEM, afin que l'utilisateur final puisse rationaliser le processus de création, de maillage, de simulation et d'optimisation d'un problème de conception technique, le tout avec FreeCAD.

Les informations suivantes sont destinées aux utilisateurs expérimentés et aux développeurs qui souhaitent étendre l\'atelier FEM de différentes manières. Une connaissance des langages C ++ et Python est préconisée. Une certaine connaissance du système \"document objet\" utilisé dans FreeCAD est également nécessaire. Ces informations sont disponibles dans la [documentation des utilisateurs](Power_users_hub/fr.md) et le [documentation des développeurs](Developer_hub/fr.md). Veuillez noter que FreeCAD étant toujours en cours de développement, certains articles peuvent être anciens et donc obsolètes. Les informations les plus récentes sont traitées dans les [forums FreeCAD](https://forum.freecadweb.org/index.php), dans la section Développement. Pour les discussions sur l\'atelier FEM, les conseils ou l'aide pour l'extension de l'atelier reférez vous dans le [subforum FEM](https://forum.freecadweb.org/viewforum.php?f=18).

Les articles suivants expliquent comment étendre l\'atelier, par exemple en ajoutant de nouveaux types de conditions aux limites (contraintes) ou équations.

-   [Extension module FEM ](Extend_FEM_Module/fr.md)
-   [Embarquer les développeurs FEM](Onboarding_FEM_Devs/fr.md) Tente d\'orienter les nouveaux développeurs sur la façon de contribuer à l\'atelier FEM.
-   [Tutoriel FEM Ajouter une équation](Add_FEM_Equation_Tutorial/fr.md)
-   [Tutoriel FEM Ajouter une contrainte](Add_FEM_Constraint_Tutorial/fr.md)

Un guide du développeur a été rédigé pour aider les utilisateurs expérimentés à comprendre les bases complexes du code de FreeCAD et les interactions entre les éléments centraux et les ateliers individuels. Le livre est hébergé sur github afin que plusieurs utilisateurs puissent y contribuer et le mettre à jour.

-   [Aperçu préliminaire du ebook : Guide du développeur de modules pour FreeCAD](https://forum.freecadweb.org/viewtopic.php?t=17581) (Discussion sur le forum).
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) (dépôt github)

## Extension de la documentation de l\'atelier FEM 

-   Plus d\'informations concernant l\'extension ou l\'absence de documentation FEM peuvent être trouvées dans le forum : [documentation FEM manquante sur le Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > FEM Workbench/fr
