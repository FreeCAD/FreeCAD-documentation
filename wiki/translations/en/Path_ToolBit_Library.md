# Path ToolBit Library/en

 





{{TOCright}}

## Description

Within the [Path Tools](Path_Tools.md) system, Toolbits are organized into libraries. A library is simply a list of toolbits and can be used by the user for whichever purpose is needed. A tool library is nevertheless a great representation for a physical grouping of tools, such as in an automatic tool changer. Or tools might be grouped by intended use, for example all tools for cutting plastic.

A tool library is a (JSON) file with a mapping of tool id to the path of the toolbit file. As a consequence each toolbit can be in multiple libraries.

Due to each tool being stored in its own file and the storage/organization of those files being quite flexible the importance of a tool library for organisational purposes is quite diminished. The user is free to organize their tools in whichever directory hierarchy they see fit and can also name them as best fits their use and organisation.

## Toolbit IDs 

The Toolbit does not have an id of it\'s own. The id is a property of the library. When a toolbit is used to create a toolcontroller, the ID in the current library will become the default tool number in the controller. Of course, the tool number can be changed in the tool controller.

## Usage

## Export

A toolbit library can be exported to create a [LinuxCNC Tool Table](http://wiki.linuxcnc.org/cgi-bin/wiki.pl?ToolTable) (.tbl).

## JSON Structure 


{{Code|
{
  "tools": [
    {
      "nr": 1,
      "path": "t1.fctb"
    },
    {
      "nr": 2,
      "path": "t2.fctb"
    },
    {
      "nr": 3,
      "path": "t3.fctb"
    }
  ],
  "version": 1
}
}}

## Options





{{Path_Tools_navi

}} 
