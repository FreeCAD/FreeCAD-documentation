# Part and PartDesign/fr

 {{TOCright}}

## Présentation

Il y a eu beaucoup de discussions au cours des années sur les différences et les conséquences de l\'utilisation des ateliers <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/fr.md) et <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md).

Il est bon d\'utiliser l\'un ou l\'autre jusqu\'à ce que l\'utilisateur soit à l\'aise avec l\'un, puis d\'apprendre l\'autre. Il est aussi généralement recommandé aux nouveaux utilisateurs de ne pas les mélanger avant d\'avoir compris les tenants et aboutissants.

Parlons de ces implications.

## Concepts de l\'atelier Part 

L\'atelier Part est essentiellement une [modélisation de type CSG](Constructive_solid_geometry/fr.md). L\'opérateur combine différentes primitives pour aboutir à une représentation de la forme souhaitée. (En fait, l\'atelier Part va plus loin que les simples primitives et permet à l\'utilisateur d\'utiliser une opération esquisse+extrusion pour créer également des formes particulières). Lorsque chaque primitive ou forme est créée, elle n\'a aucune relation avec les autres objets créés (à l\'exception des esquisses et de leurs attachements), c\'est un solide unique et solitaire.

![centre\|Solides isolés](images/Part_CSG_Prims.png )

Cette condition demeure jusqu\'à ce que l\'utilisateur utilise une opération pour les combiner (généralement une opération booléenne qui les additionne ou les soustrait). Chaque solide d\'origine reste accessible séparément et l\'opération crée un nouvel objet (solide).

Le point à retenir est la partie solide et solitaire et la partie qui les combine.

## Concepts de l\'atelier PartDesign 

Dans l\'atelier PartDesign, l\'objet Corps (Body) représente un solide unique et cumulatif.

La 1ère étape d\'un corps (body) doit être un bloc de matière, soit à partir d\'une primitive additive, soit d\'une extrusion à partir d\'une esquisse, soit d\'une forme importée (alors appelée fonction de base (Base Feature)).

Ce bloc initial de matière sera modifié séquentiellement jusqu\'à ce que la forme finale souhaitée (solide) soit obtenue.

Elle est cumulative dans le sens où chaque opération ajoute ou enlève de la matière.

Par défaut, la \"pointe\" ou partie résultante du corps - à moins qu\'il n\'y ait un changement volontaire dans la visualisation d\'une fonctionnalité particulière - est la dernière opération effectuée sur le corps. Il s\'agit de l\'état actuel et visible du corps, prêt à être modifié à nouveau par une nouvelle fonctionnalité.

Toute fonction sous le corps représente la forme cumulée du solide depuis la 1ère fonction jusqu\'à la fonction considérée.

Donc **pour avoir le solide complet**, d\'une part la fonction résultante (Tip) doit être la dernière étape de la construction de ce solide, et d\'autre part **c\'est le corps qui doit être sélectionné** et non une étape de sa construction.

Cela permettra, en cas de modification, **d\'avoir toujours la dernière version du solide représenté.**

**Remarque et compléments:** A chaque instant de la construction, la dernière fonction utilisée est la \"Tip\", qui peut être définie aussi comme \"étape active dans la construction de l\'objet\" ou \"étape précédant l\'action suivante dans la construction de l\'objet\". Lorsque le dessin de l\'objet est terminé, Tip est naturellement la dernière étape ou fonctionnalité de la construction. Mais si vous le souhaitez, en cas d\'oubli, toute fonctionnalité de la construction peut être provisoirement déclarée comme Tip: elle devient alors l\'étape précédant l\'action suivante dans la construction de l\'objet, ce qui signifie que de nouvelles fonctionnalités peuvent être insérées n\'importe où dans la construction, **à condition de ne pas créer d\'incompatibilité avec la suite**.

Lorsque tout est terminé, vous devez redéclarer la dernière fonction comme Tip, ce qui correspond à l\'objet fini.

![centre\|Corps solide cumulé](images/Part_Design_Cumulativ.png )

Cette image montre un Corps. Il s\'agit d\'un solide cumulatif composé d\'une esquisse extrudée et d\'une primitive de cône. Il s\'agit d\'un seul solide.

Si Tip est sur **Pad**, le Pad peut exister séparément, mais si Tip est sur **Cone**, le cône ne peut pas exister séparément (Tip sur Cone = Pad + Cone).

(Une autre chose souvent mentionnée est qu\'un Corps ***DOIT*** être un solide unique et contigu. Cela signifie que toute géométrie créée par une fonction dans le Corps *doit* toucher son prédécesseur).

## Les implications 

Bien que non recommandé pour les nouveaux arrivants, il est possible de combiner les outils de Part WB et PartDesign WB, à condition de savoir ce que vous faites. Par example :

Les gens se font prendre lorsqu\'ils tentent d\'utiliser une fonction sous le corps (plutôt que le corps lui-même) comme sélection d\'une opération booléenne Part Workbench. Ceci pose un problème, car la fonction sélectionnée ne représente pas «LE» solide complet.

En un sens, du point de vue de l\'atelier Part, le Corps représente une autre primitive. Aussi, l\'utilisation d\'un Corps (Body) (rappelez-vous qu\'il s\'agit d\'un proxy pour la fonction résultante) et d\'un objet de l\'atelier Part pour faire un booléen est valide. L\'objet résultant est un objet de l\'atelier Part, et par conséquent, les outils de l\'atelier PartDesign ne peuvent plus être utilisés sur cet objet.

Et, cela peut devenir encore plus compliqué. Si vous créez un nouveau Corps et que vous y faites glisser le résultat du paragraphe précédent, un BaseObject est créé. Vous pouvez alors utiliser les outils de l\'atelier PartDesign.

## Les avertissements 

Il y a un problème avec la fonction résultante (Tip) et sa représentation du solide unique dans le Corps. *Si* la fonction résultante est une fonction soustractive et est utilisée dans une opération de transformation, par exemple une symétrie, la symétrie opère sur la fonction sous-jacente (une cavité par exemple). Ainsi, le solide cumulé n\'est pas symétrisé, mais la fonction soustractive l\'est. Le résultat de cette opération doit créer un solide unique.

Dans cet exemple, une symétrie de la fonction résultante (ici la cavité de la fente) autour de l\'un des plans de base, ou même d\'une face du solide, ne produira pas un solide symétrique du modèle entier. (En fait, cela produira une fonction Symétrie dans l\'arborescence qui est essentiellement vide).

![centre\|Solides isolés](images/PhantomMirror.png )

Dans cet exemple, une symétrie de la fonction résultante (ici la cavité de la fente) est effectuée autour du plan de référence et produit une fente symétrique :

![centre\|Solides isolés](images/MirroredSlot.png )

Voir la page wiki de l\'outil <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [PartDesign Symétrie](PartDesign_Mirrored/fr.md) pour plus d\'informations.

## Comparaison

Vous pouvez voir ci-dessous le même exemple construit avec chacun des deux ateliers. Bien sûr, il existe toujours plusieurs chronologies de construction possibles avec chaque atelier. ![Comparaison des constructions avec Part WB et PartDesign WB](images/PartWBvsPartDesignWBexample.jpg )

  Dans <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> PartDesign WB                                                                                    Dans <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> Part WB
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  01- <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> Corps (Body) + <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Esquisse dans plan XZ   01- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher WB \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Esquisse dans plan XZ
  ![](images/01sketchXZ_PartWBvsPartDesignWBn.jpg )                                                                                               ![](images/01Psketch_PartWBvsPartDesignWBn.jpg )
                                                                                                                                                                                 

  ----------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------
  02- <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> Révolution / Z   02- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Révolution / Z
  ![](images/02revolutionZ_PartWBvsPartDesignWBn.jpg )          ![](images/02revolveZ_PartWBvsPartDesignWBn.jpg )
                                                                                                  
  ----------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  03- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Esquisse dans plan XY   03- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher WB \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Esquisse dans plan XY
  ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                 ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )
                                                                                                   
  ------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------
  04- <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> Poche   04a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Extrusion
  ![](images/04pocket_PartWBvsPartDesignWBn.jpg )   ![](images/04aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ ------------------------------------------------------------------------
                                                                                 04b- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Soustraction
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/04bCut_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ ------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  05- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Esquisse dans plan XZ   05- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher WB \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Esquisse dans plan XZ
  ![](images/05sketchXZ_PartWBvsPartDesignWB.jpg )                   ![](images/05PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                   
  ------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------- --------------------------------------------------------------------------------
  06- <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> Extrusion sym/XZ   06a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Extrusion sym/XZ
  ![](images/06padSymXZ_PartWBvsPartDesignWB.jpg )      ![](images/06aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                      
  ----------------------------------------------------------------------------------- --------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                 06b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> Draft WB <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Répétition circulaire
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ ------------------------------------------------------------------------------
                                                                                 06c- <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> Fusion
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06cFusion_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ ------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  07- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Esquisse sur face plane de la base   07- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher WB \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Esquisse dans plan XZ
  ![](images/07sketchBaseSupFace_PartWBvsPartDesignWB.jpg )              ![](images/07PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                                
  ------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------
  08- <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> Trou lamé                     08a- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Révolution
  ![](images/08hole-counterbore_PartWBvsPartDesignWB.jpg )   ![](images/08aRevolve_PartWBvsPartDesignWB.jpg )
                                                                                                   
  ------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                 08b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> Draft WB <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Répétition circulaire
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/08bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------
  09- <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> Répétition circulaire de Perçage + Extrusion   09- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Soustraction
  ![](images/09polarPatternHoleAndPad_PartWBvsPartDesignWB.jpg )                        ![](images/09Cut_PartWBvsPartDesignWB.jpg )
                                                                                                                                    
  --------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------

Comparez les arbres de construction dans les deux ateliers ainsi que leur organisation et leur chronologie de lecture :

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------
  10- Arbre de construction dans l\'atelier PartDesign                                 10- Arbre de construction dans l\'atelier Part
  ![](images/PartvsPartDesign_TreePartDesignWB.jpg )   ![](images/PartvsPartDesign_TreePartWB.jpg )
                                                                                       
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------

## Conclusion

Les ateliers Part et PartDesign peuvent être utilisés ensemble, avec un peu de précaution, pour créer des modèles assez complexes.

[Haut](#Top/fr.md)


{{Tutorials navi

}}  {{PartDesign Tools navi}} {{Sketcher Tools navi}} 
