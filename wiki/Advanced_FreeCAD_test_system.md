# Advanced FreeCAD test system
This page is dedicated to the Google Summer of Code project regarding the enhancement of FreeCAD\'s test system.

## Outline

FreeCAD as a CAE application has a high level of complexity, both in its source code and also in its user interaction. To ensure a certain level of quality automatic testing is essential. However, as an open source application with spare time coders only this part of the project has not seen very much attention. One of the major reasons is the low-level handling required to write test cases. All actions to trigger, every result fetching and every single comparison needs to be hand coded. This makes it cumbersome to provide a test for every created functionality and possibly impossible to do so if deep document comparisons are needed. For example the Part and PartDesign workbench: An automated test for document objects require the resulting topology shape to be analysed. This is a tremendous part and cannot be handled on a per test basis.

This project aims at reducing the work required to write meaningful tests. This should be accomplished by providing a infrastructure for result file storage and special \"comparators\" which compare the stored result files with the test result for equality.

## Details

1.  Create a result file infrastructure for the test system. It should allow to save an arbitrary number of files together with the test itself where the expected results are stored. It is intended to have one result file for each comparator used. The infrastructure should make the storage (file structure), loading and handling easy. It furthermore should define a specification for the generic file content, e.g. which comparator to use for it etc.
2.  Create a infrastructure for comparators and provide a few important ones. The comparators should be able to read in a result file and compare the available test output with it. As every workbench requires different types of comparisons the comparators need to be provided by the workbench itself, as well as possible top-level ones. The test infrastructure needs to be adopted to work with such workbench specific types. Furthermore there needs to be a way to generate result files for comparators. this can be done either by themselves or by a different class.
    1.  Implement a global comparator for the document structure: It stores the Document object structure with all properties in a result file and compares the available document after a test run with it
    2.  Implement a Part workbench comparator for shapes: It stores data about a certain TopoShape in a result file suitable for comparison, e.g. number of edges/vertices/faces, properties like area, mass, center of gravity.
    3.  Advanced: Create a global comparator for the 3D output based on picture comparison. This is marked as advanced as this comparator needs to be tolerant to slight changes due to driver differences (see VTK for example) and also needs to somehow ensure the same display settings used for the comparators every time
3.  Create a wizard or GUI for test creation in the Test workbench. This would work like macro recording: the user starts the test recording, and everything plotted in the python console would be the test procedure. When hitting stop the user gets a dialog where he can choose which comparators to apply. The wizard than creates the appropriate test structure with the test itself, all needed result files etc.
4.  Create a Wiki page describing the working of the test system and how to create tests and new comparators

## Expected Outcome 

1.  Mergable code for a result file based comparator system
2.  A GUI for simplified test generation based on macro recording
3.  A Wiki page describing the procedure for the user to create tests and the developer to create new comparators
4.  Tests which utilize the created comparators and show their use

## Future Possibilities 

Future contributions can include new comparators, e.g. for meshes. Also creating tests for existing functionality has a high priority and can be achieved with the new system. Futhermore a GUI based system can be created, where a test is defined by recorded UI events, see [Record and replay events](http://algoholic.eu/recording-and-replaying-qt-input-events/). This could also be a new GSoC project.

## Project Properties 

### Skills

-   Programming language mainly Python, some comparators may need C++ code.
-   Understand and use APIs from FreeCAD and external libraries (OCC for Part comparator)

### Difficulty

Medium

### Additional Information



---
![](images/Right_arrow.png) [documentation index](../README.md) > Advanced FreeCAD test system
