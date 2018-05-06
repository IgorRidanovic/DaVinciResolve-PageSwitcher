Davinci Resolve Page Switcher

DaVinci Resolve V15 introduced the scripting API allowing user to automate traditionally manual procedures via Python or Lua.

This proof of concept gives user the ability to switch Resolve pages via a third party UI.

Requirements and Dependencies

You need Resolve V15, of course. You also need to add several system environment variables described in the API documentation. Alternately you can make your Python script aware of the location of the fusionscript.dll (fusionscript.so) and DaVinciResolveScript.py which are installed along with DaVinci Resolve v15.
