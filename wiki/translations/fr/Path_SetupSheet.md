





{{TOCright}}

## Description

L\'utilisation d\'une feuille de configuration permet à l\'utilisateur de personnaliser le mode de calcul des différentes valeurs de propriété pour les opérations. L\'utilisateur a toujours la possibilité de remplacer les valeurs de SetupSheet par une valeur explicite ou de modifier le mode de calcul des valeurs de SetupSheet.

Etant donné que SetupSheets fait partie du travail de chemin, les valeurs ne modifient pas le comportement par défaut de Path. Au contraire, ils ne changent que le comportement dans le contexte du travail en cours.

Les SetupSheets sont particulièrement utiles lorsqu'ils sont enregistrés avec [Exporter comme modèle Path](Path_ExportTemplate/fr.md).

## Propriétés

-    **VertRapid**: définit le taux de rotation rapide vertical dans les nouveaux contrôleurs d\'outil. (Utilisé dans les post-processeurs prenant en charge les taux rapides personnalisables).

-    **HorizRapid**: définit le taux rapide horizontal dans les nouveaux contrôleurs d\'outil. (Utilisé dans les post-processeurs prenant en charge les taux rapides personnalisables).

-    **SafeHeightOffset**: l\'utilisation de ce champ dépend de SafeHeightExpression (voir ci-dessous).

-    **SafeHeightExpression**: le résultat de cette expression sera utilisé pour définir la hauteur de sécurité des opérations.

-    **ClearanceHeightOffset**: l\'utilisation de ce champ dépend de ClearanceHeightExpression (voir ci-dessous).

-    **ClearanceHeightExpression**: le résultat de cette expression sera utilisé pour définir la hauteur de dégagement des opérations.

-    **StartDepthExpression**: le résultat de cette expression sera utilisé pour définir la propriété StartDepth des opérations.

-    **FinalDepthExpression**: le résultat de cette expression sera utilisé pour définir la propriété FinalDepth des opérations.

-    **StepDownExpression**: le résultat de cette expression sera utilisé pour définir la propriété StepDown des opérations.


<div class="mw-translate-fuzzy">

1.  1.  Paramètres d\'opération


</div>


<div class="mw-translate-fuzzy">

Les suivants sont tirés de: OpFinalDepth - La valeur de la propriété FinalDepth. OpStartDepth - La valeur de la propriété FinalDepth. OpToolDiameter - Valeur de la propriété Tool Diameter du contrôleur d\'outil référencé par l\'opération.


</div>


<div class="mw-translate-fuzzy">

Valeurs SetupSheet


</div>

Les autres valeurs de la SetupSheet peuvent être référencées directement:

-   SetupSheet.ClearanceHeightOffset
-   SetupSheet.SafeHeightOffset

-   StartDepth
-   SafeHeightOffset
-   SafeHeightExpression
-   ClearanceHeightOffset
-   ClearanceHeightExpression
-   StartDepthExpression
-   FinalDepthExpression
-   StepDownExpression





{{Path_Tools_navi

}} 
