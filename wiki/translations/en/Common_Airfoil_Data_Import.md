

## Importing Airfoil Data {#importing_airfoil_data}

FreeCAD can import airfoil data such as that found on the [UIUC Airfoil Coordinates Database](http://m-selig.ae.illinois.edu/ads/coord_database.html) or files produced by airfoil creation and annalizing software like [XFLR5](http://www.xflr5.com/xflr5.htm)

## How To {#how_to}

From the File menu, select either Open for a new document or Import for existing document. From the Open or Import dialog \"Files of type: pull down menu select Common airfoil data (\*.dat), select your file and click Open.

When opening airfoil data files, FreeCAD reads the file and imports then in FreeCAD units. Airfoil data files provide XY coordinates in numbers between 0 and 1. As a result, the imported airfoil will have a chord length of 1 mm by default. Here is a tunicated sample of a typical airfoil .dat file. Notice that all data points fall between 0 and 1. 
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

## Enhanced Import {#enhanced_import}

There is a macro available that will import the airfoil with a user defined chord length. This macro will first allow the user to select the airfoil data file to import and then take an input for the chord length. It will then properly scale the airfoil for use. The macro can be found in the [Macros recipes](Macros_recipes.md) section of this Wiki under [Macro Airfoil Import & Scale](Macro_Airfoil_Import_&_Scale.md).




[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md)
