# TechDraw Hatching/fr
{{TOCright}}

## Description

L\'atelier TechDraw dispose de deux outils de hachurage:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Hachures à partir de motifs](TechDraw_Hatch/fr.md) (basé sur les tuiles)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Hachures par lignes géométriques](TechDraw_GeometricHatch/fr.md) (basé sur la ligne)

## Utilisation

1.  Sélectionnez une face

    :   <img alt="" src=images/SelectFace.png  style="width:150px;">
2.  En fonction des besoins, appuyez sur les icônes <img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> [TechDraw Hachures par motifs](TechDraw_Hatch/fr.md) ou <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [TechDraw Hachures géométriques](TechDraw_GeometricHatch/fr.md).

**Résultat:** La surface sera hachurée initialement en utilisant les valeurs par défaut. **Remarque**: modifiez les propriétés des hachures pour obtenir le motif souhaité.

### Hachures à l\'aide d\'un fichier image 

<img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> [Hachures à l\'aide d\'un fichier image](TechDraw_Hatch/fr.md) utilise des tuiles de base [SVG](SVG/fr.md) ou [bitmap](bitmap/fr.md) pour couvrir la face sélectionnée.

Les tuiles [SVG](SVG/fr.md) sont typiquement des images de **64x64** pixels. Tous les fichiers de modèles fournis avec FreeCAD sont disponibles sur [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

Tout fichier [bitmap](bitmap/fr.md) peut être utilisé (PNG, JPG, etc\...) comme remplissage. **Remarques:** les résultats sont meilleurs avec beaucoup de petites images répétées plutôt qu\'avec moins d\'images plus grandes.

Le fichier de motif de hachures par défaut peut être spécifié dans les [TechDraw Préférences](TechDraw_Preferences/fr.md).

## Hachures géométriques 

<img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Hachures géométriques](TechDraw_GeometricHatch.md) forme un motif de lignes basé sur une spécification lue dans un fichier. Ce fichier est généralement **compatible avec le format AutoDesk® PAT largement utilisé**. Une petite sélection de modèles est incluse dans le fichier FCPAT.pat:


```python
; standard PAT patterns

*Diamond, 45 diagonals L & R, Solid, 1.0 mm separation
45,0,0,0,1.0
-45,0,0,0,1.0
*Diamond2, 45 diagonals L & R, Solid, 2.0 mm separation
45,0,0,0,2.0
-45,0,0,0,2.0
*Diamond4, 45 diagonals L & R, Solid, 4.0 mm separation
45,0,0,0,4.0
-45,0,0,0,4.0
*Diagonal4, 45 diagonal R, Solid, 4.0 mm separation
45,0,0,0,4.0
*Square, square grid, Solid, 5.0 mm separation 
90,1,1,0,5.0
0,0,0,1,5.0
*Horizontal5, horizontal lines, Solid 5.0 separation
0,0,0,0,5.0
*Vertical5, vertical lines, Solid, 5.0 separation
90,0,0,0,5.0
```

Vous pouvez ajouter vos propres modèles si vous avez l\'autorisation d\'écriture sur FCPAT.pat, ou vous pouvez créer votre propre fichier \*.pat et le pointer dans [TechDraw Préférences](TechDraw_Preferences/fr.md).

### Chemin du fichier PAT 

Le fichier `FCPAT.pat` peut être trouvé à l\'emplacement suivant :

-   **Windows** : `C:\Program Files\FreeCAD\data\Mod\TechDraw\PAT\`
-   **Mac** : `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Linux** : `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA* : `/usr/share/freecad-daily/Mod/TechDraw/PAT/`





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/fr
