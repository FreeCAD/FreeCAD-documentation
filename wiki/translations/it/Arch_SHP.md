 FreeCAD è in grado di importare [shapefiles](https://en.wikipedia.org/wiki/Shapefile)

L\'importatore utilizza la libreria shapefile.py da <https://github.com/GeospatialPython/pyshp>, che non si trova nel proprio sistema al primo avvio, ma che l\'importatore proporrà di scaricare e installare.

Gli Shapefile sono composti da 3 file (un file .shp, un .shx e un .dbf), ognuno dei quali può essere utilizzato con questo importatore. Sono composti da oggetti 2D di un tipo di geometria, che possono essere poligoni/facce, polilinee o nuvole di punti (tutti i 3 tipi sono supportati da questo importatore) e campi personalizzati, per i quali ogni faccia, polilinea o punto nel shapefile ha un valore. Questo è il vero gioiello di GIS, per legare un database con la geometria. L\'uso più comune è avere un campo per rappresentare la coordinata di elevazione di ogni forma nel file. All\'apertura del file, l\'importatore chiede da quale campo ottenere l\'elevazione della forma.

In FreeCAD verrà creata una forma da ciascun shapefile.

Notare che al momento non viene trattata tutta la questione delle unità georeferenziate, con centinaia di sistemi di proiezione utilizzati in tutto il mondo. Le coordinate del file vengono utilizzate \"così come sono\".

## Correlazioni

-   Annuncio nel forum di FreeCAD [Shapefile Importer](https://forum.freecadweb.org/viewtopic.php?f=9&t=46150)
-   Forum thread on [OSArch](https://community.osarch.org/discussion/comment/578#Comment_578) discussion
-   [Importazione e Esportazione](Import_Export/it.md)
-   [Come importare e esportare in FreeCAD](FreeCAD_Howto_Import_Export/it.md)
-   [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md)


 

[Category:File Formats{{\#translation:}}](Category:File_Formats.md)
