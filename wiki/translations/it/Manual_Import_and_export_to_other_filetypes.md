# Manual:Import and export to other filetypes/it
{{Manual:TOC/it}}

FreeCAD può importare ed esportare molti tipi di file. Ecco un elenco dei più importanti con una breve descrizione delle funzioni disponibili:

  Formato   Importazione   Esportazione   Note
     
  STEP      Si             Si             Questo è il più fedele formato di importazione / esportazione disponibile, dato che supporta la geometria solida e NURBS. Usatelo ogni volta che è possibile.
  IGES      Si             Si             Un vecchio formato per i solidi, anche molto ben supportato. Alcune applicazioni meno recenti non supportano STEP, ma hanno IGES.
  BREP      Si             Si             Il formato nativo di [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), il kernel della geometria di FreeCAD.
  DXF       Si             Si             Un formato aperto gestito da Autodesk. Dato che i dati 3D all\'interno di un file DXF sono codificati in formato proprietario, FreeCAD può solo importare e esportare dati 2D da e verso questo formato.
  DWG       Si             Si             La versione proprietaria di DXF. Richiede l\'installazione dell\'utility [Teigha File Converter](https://www.opendesign.com/guestfiles). Questo formato soffre delle stesse limitazioni di DXF.
  OBJ       Si             Si             Un formato basato su mesh. Può contenere solo maglie triangolari. In fase di esportazione tutti gli oggetti solidi e le superfici basate su NURBS di FreeCAD sono convertiti in mesh. L\'ambiente Arch fornisce un esportatore alternativo, più adatto all\'esportazione di modelli architettonici.
  DAE       Si             Si             Il principale formato di importazione e esportazione di Sketchup. Può contenere solo maglie triangolari. In fase di esportazione tutti gli oggetti solidi e le superfici basate su NURBS di FreeCAD sono convertiti in mesh.
  STL       Si             Si             Un formato basato su mesh, comunemente utilizzato per la stampa 3D. Può contenere solo maglie triangolari. In fase di esportazione tutti gli oggetti solidi e le superfici basate su NURBS di FreeCAD sono convertiti in mesh.
  PLY       Si             Si             Un vecchio formato basato su mesh. Può contenere solo maglie triangolari. In fase di esportazione tutti gli oggetti solidi e le superfici basate su NURBS di FreeCAD sono convertiti in mesh.
  IFC       Si             Si             [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes). Richiede l\'installazione di [IfcOpenShell-python](http://ifcopenshell.org/python). Il formato IFC e la sua compatibilità con altre applicazioni è un affare complesso, utilizzare con cautela.
  SVG       Si             Si             Un eccellente e diffuso formato grafico 2D
  VRML      Si             Si             Un formato web piuttosto vecchio basato su mesh.
  GCODE     Si             Si             FreeCAD può già importare ed esportare da e verso vari dialetti di codice G, ma per il momento supporta solo alcune macchine.
  CSG       Si             No             Formato di OpenSCAD [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (Constructive Solid Geometry).

Alcuni di questi formati di file hanno delle opzioni. Questi formati possono essere configurati nel menu **Modifica → Preferenze → Importa/esporta**:

![](images/Import_preferences.jpg )

**Approfondimenti**

-   [Tutti i formati di file supportati da FreeCAD](Import_Export/it.md)
-   [Lavorare con i file DXF in FreeCAD](Draft_DXF/it.md):
-   [Abilitare il supporto per i file DXF e DWG](Dxf_Importer_Install/it.md)
-   [Lavorare con i file SVG in FreeCAD](Draft_SVG/it.md)
-   [Importare e esportare verso IFC](Arch_IFC/it.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Teigha File Converter](https://www.opendesign.com/guestfiles)
-   [IFC Specifications Database](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/)
-   [IfcOpenShell](http://ifcopenshell.org/)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Import and export to other filetypes/it
