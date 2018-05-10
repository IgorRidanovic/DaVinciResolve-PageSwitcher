Davinci Resolve Page Switcher

DaVinci Resolve V15 introduced the scripting API allowing user to automate traditionally manual procedures via Python or Lua.

This proof of concept gives user the ability to switch Resolve pages via a third party UI. The switching application can run on the same host as the Resolve, or it can control Resolve page switching remotely via TCP/IP.


Remote Operation Setup

Enter Resolve host IP address in server = 'IP address' in each of the .py files. You may enter another port number than the one provided. 

Run the PageSwicthServer.py on the Resolve machine. Run the PageSwitchServer.py on the remote control host. There is additional reporting available if you execute the scripts inside a command line.

Check "TCP/IP remote" to control a remote Resolve. Uncheck if running the ResolvePageSwitcher.py on the same local machine as the Resolve. The server script is not necessary for local operation.


Requirements and Dependencies

You need Resolve V15, of course, as well as Python 2.x and PyQt4. You also need to add several system environment variables described in the API documentation. Alternately you can make your Python script aware of the location of the fusionscript.dll (fusionscript.so) and DaVinciResolveScript.py which are installed along with DaVinci Resolve v15.
