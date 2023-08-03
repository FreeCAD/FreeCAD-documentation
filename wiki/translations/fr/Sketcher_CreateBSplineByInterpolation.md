---
 GuiCommand:
   Name: Sketcher CreateBSplineByInterpolation
   Name/fr: Sketcher B-spline par des nœuds
   MenuLocation: Esquisse , Géometries d'esquisse , Créer une B-spline par des nœuds
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **B** **I**
   Version: 0.21
   SeeAlso: Sketcher_CreatePeriodicBSpline/fr
---

# Sketcher CreateBSplineByInterpolation/fr

## Description

Cet outil crée une courbe B-spline passant par des points donnés. Voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines.



## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Sketcher_CreateBSplineByInterpolation.svg style="width:16px"> [B-spline par des noeuds](Sketcher_CreateBSplineByInterpolation/fr.md)**.
2.  Créez une série de points en cliquant dans la [vue 3D](3D_view/fr.md). Tant que la commande est active, les points créés sont reliés par des lignes droites.
3.  Appuyez sur **M** avant de terminer la saisie pour définir la multiplicité du nœud au dernier point défini (notez que cela n\'est pas toujours respecté, voir [limitations](#Limitations.md) pour plus de détails).
4.  Appuyez sur **Retour arrière** avant de terminer la saisie pour supprimer le dernier point de contrôle créé.
5.  Cliquez avec le bouton droit de la souris pour terminer l\'entrée et générer la courbe.
6.  Selon les préférences, l\'outil peut rester actif pour tracer une nouvelle courbe. Cliquez à nouveau avec le bouton droit de la souris pour quitter la commande.



## Remarques

Voir [Sketcher B-spline simple](Sketcher_CreateBSpline/fr#Remarques.md).

## Limitations

-   La courbe résultante n\'est pas différente d\'une B-spline (non-uniforme) définie par des points de contrôle. Toutes les limitations correspondantes s\'appliquent donc. Voir [Sketcher B-spline simple](Sketcher_CreateBSpline/fr#Limitations.md).
-   Les B-splines créées sont toujours cubiques (c\'est-à-dire de degré 3).
-   La multiplicité définie n\'est pas toujours respectée :
    -   Pour une spline périodique, le premier noeud (coïncidant avec le dernier) a toujours une multiplicité de 2.
    -   Pour une spline non périodique, les premier et dernier noeuds ont toujours une multiplicité de 4.
    -   Si les points juste avant et juste après ont des multiplicités \>=3, le morceau entre ces deux points est entièrement continu, et ce point (du milieu) ne sera contraint que par un point sur l\'objet. Si un nœud est nécessaire, envisagez d\'utiliser l\'outil d\'insertion de nœud.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSplineByInterpolation/fr
