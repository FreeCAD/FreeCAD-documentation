# Common Airfoil Data Import/it
## Importare Dati Airfoil 

FreeCAD può importare i dati di un profilo alare, come quello trovato in [UIUC Airfoil Coordinates Database](http://m-selig.ae.illinois.edu/ads/coord_database.html) o file prodotti con software per la creazione e l\'analisi di un profilo alare come [XFLR5](http://www.xflr5.com/xflr5.htm)

## Come

Dal menu File, selezionare Apri un nuovo documento o Importa per un documento esistente. Dalla finestra di dialogo Apri o Importa, aprire il menu \"Tipi di File\" e selezionare Common airfoil data (\*.dat), poi selezionare il proprio file e cliccare Open.

Quando si apre un file di dati di un profilo alare, FreeCAD legge il file e lo importa usando le unità di FreeCAD. I file di dati Airfoil forniscono le coordinate XY in numeri compresi tra 0 e 1. Come risultato, il profilo alare importato avrà di default una lunghezza di corda di 1 mm. Ecco un esempio di un tipico file di profilo alare .dat. Si noti che tutti i dati dei punti sono compresi tra 0 e 1. 
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

## Importazione avanzata 

È disponibile una macro che consente di importare il profilo aerodinamico con una lunghezza della corda definita dall\'utente. Questa macro consente all\'utente di selezionare prima il file di dati da importare e poi anche di definire la lunghezza della corda. Quindi scala correttamente il profilo. La macro si trova nella sezione [Macros recipes](Macros_recipes/it.md) di questo Wiki sotto il nome di [Macro Airfoil Import & Scale](Macro_Airfoil_Import_&_Scale/it.md).




_

---
[documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Common Airfoil Data Import/it
