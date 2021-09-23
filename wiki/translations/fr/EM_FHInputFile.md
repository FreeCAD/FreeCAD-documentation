---
- GuiCommand:/fr
   Name:EM FHInputFile
   Name/fr:EM FHInputFile
   MenuLocation:EM → FHInputFile
   Workbenches:[EM](EM_Workbench/fr.md) (Addon)
   Shortcut:**E** **I**
   SeeAlso:[EM FHSolver](EM_FHSolver/fr.md)
   Version:0.17
---

# EM FHInputFile/fr

## Description

L\'outil FHInputFile crée le fichier FastHenry d\'entrée basé sur les objets de l\'atelier Document EM.

## Utilisation

Pour créer un fichier d\'entrée FastHenry:

1.  Créez un objet [EM FHSolver](EM_FHSolver/fr.md) et d\'autres objets d\'atelier EM représentant la géométrie 3D requise pour votre modèle.
2.  Appuyez sur le bouton **<img src="images/EM_FHInputFile.svg" width=16px> [EM FHInputFile](EM_FHInputFile/fr.md)** ou appuyez sur les touches **E** puis **I**.

### Remarques

-   Dans le cas où un fichier avec le même nom dans le dossier donné comme spécifié dans l\'objet [EM FHSolver](EM_FHSolver/fr.md) existe déjà, vous serez invité à remplacer ou non.

-   Le document peut également contenir des objets non EM Workbench. Ils seront ignorés lors de la création du fichier d\'entrée FastHenry. Vous pouvez donc utiliser tout autre type d\'objet FreeCAD comme guide pour vos modèles EM Workbench.

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil FHInputFile peut-être utilisé dans des [macros](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
node = createFHInputFile(doc=None,filename=None,folder=None)
```

-   Génère un fichier d\'entrée FastHenry basé sur la géométrie du document actif.

-    `doc`est l\'objet Document qui doit contenir au moins un objet EM\_FHSolver et la géométrie appropriée. Si aucun `doc` n\'est donné, le document actif est utilisé, le cas échéant.

-    `filename`est le nom de fichier à utiliser. Si elle n\'est pas passée en argument, la propriété {{PropertyData/fr|Filename}} de l\'objet FHSolver contenu dans le document sera utilisée. Si la chaîne {{PropertyData/fr|Folder}} dans l\'objet FHSolver est vide, la fonction crée un nom de fichier concaténant le nom du document avec l\'extension par défaut {{incode/fr|EMFHSOLVER_DEF_FILENAME}}.

-    `folder`est le dossier où le fichier sera stocké. Si elle n\'est pas passée en argument, la propriété {{PropertyData | Folder}} de l\'objet FHSolver contenu dans le document sera utilisée. Si la chaîne {{PropertyData/fr|Folder}} dans l\'objet FHSolver est vide, la fonction utilise par défaut le chemin d\'accès de l\'utilisateur (par exemple sous Windows \"C:\\Documents and Settings\\username\\My Documents\", sous Linux \"/home/username\")

Example: 
```python
import FreeCAD, EM

fhsolver = EM.createFHInputFile()
```


{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHInputFile/fr
