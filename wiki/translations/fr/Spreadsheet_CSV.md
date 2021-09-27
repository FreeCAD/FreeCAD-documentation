# Spreadsheet CSV/fr
Le[format CSV](https://fr.wikipedia.org/wiki/Comma-separated_values) (comma-separated values) est un format texte brut pour échanger des données de tableur. Il peut généralement être importé et exporté par n\'importe quel tableur tel que LibreOffice ou Microsoft Excel. La lecture et l\'écriture au format csv se fait avec le module csv intégré dans Python [module csv](http://docs.python.org/2/library/csv.html).

## Importation

L\'importation d\'un fichier.csv dans FreeCAD crée un objet <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:16px;"> [feuille de calcul](Spreadsheet_CreateSheet/fr.md) puis le remplit avec les valeurs du fichier.

## Exportation

L\'exportation d\'un objet <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:16px;"> [feuille de calcul](Spreadsheet_CreateSheet/fr.md) vers un fichier.csv écrit simplement toutes les valeurs de l\'objet feuille de calcul. Les fonctions, telles que =A3+B5 sont écrites en tant que fonctions et non en tant que valeurs résultantes.


 

_ _ _

---
[documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [Spreadsheet](Spreadsheet_Workbench.md) > Spreadsheet CSV/fr
