# Swept-path Analysis GSoC Project
This page is describes a potential 2018 Google Summer of Code project regarding configuration management for the FreeCAD CAE application.

## Outline

In Transportation Engineering, a common need is a \"swept-path analysis\", which simply analyzes the path a vehicle takes as it turns a corner. Vehicles of differing dimensions and wheel bases, obviously, have different turning capabilities, so it\'s necessary to ensure public facilities are designed to accommodate the least agile vehicles that are expected to use it.

Commercial packages exist which do this. The industry standard in the US is AutoTURN and sells for about \$12,000 per license. Despite the price, the technology and theory behind the software has been known and understood for well over 50 years. Yet, apart from one freeware (closed source) option, no freely available tools to perform this analysis exist.

## Details

1.  Develop a simple database (a CSV file) which contains the key parameters for the design vehicles used in the analysis. This data includes parameters like vehicle height, length, width, axle count, wheel base, and others.
2.  Develop several generic vehicle templates as separate sketches into which the database parameters can be fed to create a template which represents a real-world vehicle.
3.  Create a Part-based geometry from the sketch object representing the design vehicle and generate a mesh
4.  Import a data file (DXF) which contains the roadway gemetry on which to run the analysis.
5.  Choose lines from the imported file which act as boundaries for the analysis collision detection.

## Expected Outcome 

1.  Accomplishing these items would provide the basis for performing swept path analyses in FreeCAD.

## Future Possibilities 

This work will provide exposure to highway design techniques.

## Project Properties 

### Skills

-   Familiarity with
    -   

### Difficulty

Medium

### Additional Information 

[FreeCAD Civil Engineering Thread](https://forum.freecadweb.org/viewtopic.php?f=8&t=22277&start=250)

[<img src="images/Property.png" style="width:16px"> Google Summer of Code](Category_Google_Summer_of_Code.md)

---
[documentation index](../README.md) > Swept-path Analysis GSoC Project
