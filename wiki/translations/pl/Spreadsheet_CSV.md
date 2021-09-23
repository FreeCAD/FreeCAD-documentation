# Spreadsheet CSV/pl
 The [CSV format](http://en.wikipedia.org/wiki/Comma-separated_values) (comma-separated values) is a plain-text format to exchange spreadsheet data. It can usually be imported and exported by any spreadsheet application such as LibreOffice or Microsoft Excel. Reading and writing to csv format is done with python\'s built-in [csv module](http://docs.python.org/2/library/csv.html).

## Importing

Importing a .csv file into FreeCAD creates a <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:16px;"> [spreadsheet](Spreadsheet_CreateSheet.md) object, then fills it with the values from the file.

## Exporting

Exporting a <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:16px;"> [spreadsheet](Spreadsheet_CreateSheet.md) object to a .csv file simply writes all the values of the spreadsheet object. Functions, such as =A3+B5 are written as functions, not resulting values.


 

[Category:User\_Documentation](Category:User_Documentation.md) [Category:Spreadsheet](Category:Spreadsheet.md) [Category:File\_Formats](Category:File_Formats.md)
