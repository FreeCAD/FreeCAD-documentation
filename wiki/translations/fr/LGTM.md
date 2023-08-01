# LGTM/fr
## Présentation




[LGTM](https://www.lgtm.com) est un outil d\'analyse de code pouvant être intégré à plusieurs systèmes de contrôle de version de logiciel en ligne et prenant en charge plusieurs langues. C\'est un excellent vérificateur de la qualité du code, identifiant les problèmes de code qui sont souvent oubliés par les autres vérificateurs de code et les linters.

LGTM convient parfaitement comme outil d'analyse de code pour le développement d'ateliers en Python de FreeCAD et d'autres projets de petite et moyenne taille. Cette page fournit un aperçu de la mise en route de LGTM avec un atelier Python pour FreeCAD.



## Commencer

La prise en main de LGTM dépend de la plate-forme de contrôle de version en ligne que vous utilisez. La documentation LGTM pour [automated code review](https://lgtm.com/help/lgtm/about-automated-code-review) fournit un bon aperçu de la façon d\'intégrer LGTM à votre projet pour plusieurs plates-formes.

En outre, il est possible d\'effectuer une large gamme d\'analyses approfondies du code sur LGTM, ce qui dépasse le cadre de ce tutoriel. Vous pouvez en savoir plus à ce sujet dans la documentation de LGTM sur [configuring code analysis](https://lgtm.com/help/lgtm/configuring-lgtm-analysis-project).



## Résultats

Une fois que vous avez configuré LGTM et fourni l\'accès à vos référentiels de code, les analyses sont généralement effectuées quotidiennement sur le référentiel. Ainsi, les changements poussés ne produiront pas de résultats immédiats. Il est possible que LGTM analyse les demandes d\'extraction lorsqu\'elles sont soumises, comme décrit dans la documentation LGTM.

Pour visualiser les résultats, vous devez simplement vous connecter à votre tableau de bord LGTM et sélectionner le projet souhaité. À partir de là, les analyses de code fourniront une liste de problèmes (tels que des bugs, de mauvaises pratiques de codage, du code inutile/non pertinent/non utilisé, etc.) pour votre lecture attentive. En outre, LGTM fournit des «cotes» de code globales (A, B, C, D) en fonction du nombre de numéros que vous avez comparés à la taille globale de votre projet.

Probablement, le moyen le plus utile et immédiat de gérer les résultats de votre analyse de code consiste simplement à filtrer les fichiers de votre projet que vous ne souhaitez pas analyser. En d'autres termes, supposons que vous développiez un nouveau code incomplet, conserviez du code hérité qui n'était par ailleurs pas utilisé ou que vous disposiez d'une bonne partie du code de test qui n'a pas besoin d'être analysée. LGTM fournit [file classification](https://lgtm.com/help/lgtm/file-classification) un moyen facile de filtrer ces fichiers afin qu\'ils ne polluent pas les résultats de votre analyse.

### Création d\'un fichier .lgtm.yml 

Pour activer la classification de fichier, commencez par créer un fichier nommé \".lgtm.yml\" dans le répertoire le plus haut de votre projet. Ensuite, dans ce fichier, ajoutez quelques classifications.

Vous trouverez ci-dessous un exemple tiré de l'atelier FreeCAD Trails Python:


```python
path_classifiers:
  template:
    - freecad/trails/resources
    - freecad/trails/project/commands/command_template.py
    - freecad/trails/init_gui.py
 
  test:
    - freecad/trails/project/commands/spiral_test.py
    - freecad/trails/TestFPO.py
 
  legacy:
    - freecad/trails/corridor/loft
    - freecad/trails/alignment/VerticalAlignment.py
    - freecad/trails/alignment/VerticalCurve.py
    - freecad/trails/alignment/GenerateVerticalAlignment.py
    - freecad/trails/alignment/ImportVerticalCurve.py
    - freecad/trails/corridor/template/TemplateLibrary.py
```

Notez que les niveaux d\'indentation sont importants dans LGTM. Un retrait incorrect entraînera un échec de la classification des fichiers.

En outre, certaines classifications (telles que \"modèle\" et \"test\") sont utilisées par LGTM pour les requêtes et autres composants d\'analyse. Vous pouvez également définir vos propres balises personnalisées, qui filtreront le code et fourniront des résultats interrogeables supplémentaires.



## Liens pertinents 

-   [Intégration Continue](Continuous_Integration/fr.md)
-   LGTM [FreeCAD Sujet du forum de discussion](https://www.forum.freecadweb.org/viewtopic.php?f=10&t=40228)
-   Fichier FreeCAD .lgtm.yml sur [Github](https://github.com/FreeCAD/FreeCAD/blob/master/lgtm.yml)
-   freecad.trails .lgtm.yml sur [Github](https://github.com/joelgraff/freecad.trails/blob/dev/.lgtm.yml)



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > LGTM/fr
