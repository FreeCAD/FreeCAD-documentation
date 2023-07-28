---
- GuiCommand:
   Name:Path Sanity
   MenuLocation:Path → Check the path job for common errors
   Workbenches:[Path](Path_Workbench.md)
   Shortcut:**P** **S**
   Version:0.19
---

# Path Sanity

## Description

Many Path users are hobbyists and DIYers. As such, they use their CNC machines to run G-code that they configured and generated themselves. That isn\'t the case for most professional/commercial users. In professional shops, different people are responsible for creating the G-code (CNC programmers) from those who run it on the machines (CNC operator).

Hobbyists usually run the G-code just a few minutes after post-processing it and probably only once or twice. In a professional shop, proven G-code may be run many times for months or years after initially generated.

One issue that arises in a professional CNC shop is that there are many assumptions made by the programmer that are NOT communicated in the G-code itself. For example, the G-code can call for a tool \"T3\" but unless its commented, the G-code doesn\'t say what kind of tool \"T3\" refers to. It\'s just assumed that T3 in the CAM system is the same as T3 on the machine. There are many assumptions like this involving machine setup, tooling, material, part orientation, etc. Even if the G-code is perfect, if the operator doesn\'t set up the machine with the same assumptions, it can crash.

Commercial shops will often create a \'setup book\' which documents all these assumptions and gives the operators what they need to configure the machine and produce a part.

<img alt="" src=images/Path_Sanity.svg  style="width:16px;"> [Path Sanity](Path_Sanity.md) is the tool in Path workbench to generate this kind of information. The output of this command is a stand-alone .html file with embedded images.

<img alt="" src=images/Sanity.jpg  style="width:600px;">



*Above: Example of a Path Sanity generated report*

## About the Report 

As much as possible, the content is FreeCAD agnostic. The CNC Operator may never use FreeCAD so FreeCAD/Path specific terminology is confusing. The report has distinct sections and is formatted to make finding things easy and predictable.

### Part Information 

This section gives an overview of what is being made. Ideally the image should show the base objects. If there are multiple base objects, the image should show how they nest.

### Run Summary 

Gives a quick view of minimum and maximum heights and run times.

### Rough Stock 

Details the Stock object from the Job. This is an area where Path would benefit from some improvement. A rudimentary material property for the stock would be useful here and could also be used to help suggest feeds/speeds.

### Tool Data 

Has subsections for each tool number used in the job. It details what the programmer assumes the tool to be and which operations are using it. This section only works with the new Toolbit system. This is another area where Path needs improvement. Specifically, Toolbits need additional attributes about the tool like manufacturer/url/part number.

### Output

Gives details about where and when the G-code was post-processed. It also shows whether the job contains optional/mandatory stops so the operator knows if it\'s safe to walk away from the machine during a run.

### Coolant

What kind of coolant, if any, is required.

### Fixtures and Work-holding 

Shows the parts in the context of the stock envelope and also shows the Part origin.

### Squawks

Warnings and errors detected by [Path Sanity](Path_Sanity.md). These may or may not be problems but they\'re noted for additional attention. For example if the same tool number is used for different toolbits, it will show as an error. If a tool controller has no feed/speed configured, it will appear as a warning. It will also detect and warn about unused tool controllers. Path would benefit here from the ability to add arbitrary notes or warnings.

## Usage

1.  Select a <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Path Job](Path_Job.md) in the [Tree view](Tree_view.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Path_Sanity.svg" width=16px> [Path Sanity](Path_Sanity.md)** button.
    -   Select the **Path → <img src="images/Path_Sanity.svg" width=16px> Check the path job for common errors** option from the menu.
    -   Use the keyboard shortcut: **P** then **S**.
3.  The relevant information is collected into a Python dictionary and then formatted into asciidoc format.
4.  The asciidoc file is written to disk in the same location as the file that will be post-processed.
5.  An external process calls asciidoctor to read the asciidoc and generate the .html.
6.  This will auto-launch the system web browser to view the generated standalone HTML report.

## Notes

-   Asciidoc is a lightweight markup format for authoring notes, articles, books ,etc. It is human-readable and easily translated into other formats.

-   Asciidoctor is a fast open-source text processor for converting asciidoc into HTML, PDF, or other formats. It\'s available for Linux, Windows, and MacOS. Asciidoctor is not installed with FreeCAD. If you use **Path Sanity** without installing Asciidoctor, the asciidoc source file will be generated but the resulting HTML will not be produced. See [Asciidoctor website](https://asciidoctor.org/)




 {{Path_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Sanity
