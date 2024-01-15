# Console API

FreeCAD Console module.

The Console module contains functions to manage log entries, messages,
warnings and errors.
There are also functions to get/set the status of the observers used as
logging interfaces.



### Functions

#### <img src="images/Arrow-right.svg" style="width:16px;"> GetObservers

GetObservers() -> list of str

Get the names of the current logging interfaces.



#### <img src="images/Arrow-right.svg" style="width:16px;"> GetStatus

GetStatus(observer, type) -> bool or None

Get the status for either 'Log', 'Msg', 'Wrn' or 'Error' for an observer.
Returns None if the specified observer doesn't exist.

observer : str
    Logging interface name.
type : str
    Message type.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintCritical

PrintCritical(obj) -> None

Print a critical message to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintDeveloperError

PrintDeveloperError(obj) -> None

Print an error message intended only for Developers to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintDeveloperWarning

PrintDeveloperWarning(obj) -> None

Print an warning message intended only for Developers to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintError

PrintError(obj) -> None

Print an error message to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintLog

PrintLog(obj) -> None

Print a log message to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintMessage

PrintMessage(obj) -> None

Print a message to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintNotification

PrintNotification(obj) -> None

Print a user notification to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintTranslatedNotification

PrintTranslatedNotification(obj) -> None

Print an already translated notification to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintTranslatedUserError

PrintTranslatedUserError(obj) -> None

Print an already translated error message intended only for the User to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintTranslatedUserWarning

PrintTranslatedUserWarning(obj) -> None

Print an already translated warning message intended only for the User to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintUserError

PrintUserError(obj) -> None

Print an error message intended only for the User to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintUserWarning

PrintUserWarning(obj) -> None

Print a warning message intended only for the User to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> PrintWarning

PrintWarning(obj) -> None

Print a warning message to the output.

obj : object
    The string representation is printed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> SetStatus

SetStatus(observer, type, status) -> None

Set the status for either 'Log', 'Msg', 'Wrn' or 'Error' for an observer.

observer : str
    Logging interface name.
type : str
    Message type.
status : bool









---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Console API
