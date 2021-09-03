

## Importation des données des profils aérodynamiques 

FreeCAD peut importer des données de profils comme celles qui se trouvent sur la base de données de coordonnées de profils [UIUC Airfoil Coordinates Database](http://m-selig.ae.illinois.edu/ads/coord_database.html) ou des fichiers produits par un logiciel de création et d\'annalyse de profils comme [XFLR5](http://www.xflr5.com/xflr5.htm).

## Utilisation

Dans le menu Fichier, sélectionnez Ouvrir pour un nouveau document ou Importer pour un document existant. Dans la boîte de dialogue Ouvrir ou Importer \"Fichiers de type: menu déroulant sélectionnez Common airfoil data (\*.dat), sélectionnez votre fichier et cliquez sur Ouvrir.

Lors de l\'ouverture des fichiers de données des profils, FreeCAD lit le fichier et l\'importe ensuite en unités FreeCAD. Les fichiers de données des profils fournissent des coordonnées XY entre 0 et 1, ce qui fait que le profil importé aura une longueur de corde de 1 mm par défaut. Voici un exemple d\'un fichier airfoil.dat typique. Notez que tous les points de données se situent entre 0 et 1. 
```python
AG35
     0.999998    0.002490
     0.994759    0.003346
     0.985091    0.004927
     0.973580    0.006810
     0.961032    0.008862
     0.948054    0.010984
     0.934900    0.013135

~ ~ ~ ~ ~ ~ ~ ~

     0.947640   -0.000001
     0.960660   -0.000001
     0.973282    0.000000
     0.984898    0.000000
     0.994724   -0.000001
     1.000001    0.000000
```

## Importation améliorée 

Il y a une macro disponible qui importera le profil avec une longueur de corde définie par l\'utilisateur. Cette macro permet d\'abord à l\'utilisateur de sélectionner le fichier de données de profil d\'aile à importer, puis de saisir la longueur de l\'accord. Il mesurera ensuite correctement la voilure en vue de son utilisation. La macro peut être trouvée dans la section [Macros](Macros_recipes/fr.md) de ce Wiki sous [Macro Airfoil Import & Scale](Macro_Airfoil_Import_&_Scale/fr.md).




[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md)
