This is the Keyboard Layout Editor (KLE), a pygtk program that helps create 
or edit XKB keyboard layouts. This allows you to type characters from different 
languages or other special Unicode characters on your Linux desktop.

The project page of the Keyboard Layout Editor is
http://code.google.com/p/keyboardlayouteditor/

You are strongly encouraged to use the version that is found at the above URL, 
as it includes several bug fixes.

The project was developed using Eclipse (Ganymede), with the Python (PyDev) 
and Antlr (AntlrIDE) add-ons.

PyDev is found at
http://pydev.sourceforge.net/

AntlrIDE is found at
http://antlrv3ide.sourceforge.net/

If you also have SVN support in Eclipse (hint: Subclipse), 
you can grab the latest source from within Eclipse.
There is also integration with Mylene so that you can get the list of 
issues/bugs/todo items automatically.

To run the application, you need the python binding packages for 
* Cairo
* Pango
* GObject
* lxml

and the Antlr 3.1 Runtime environment for Python. You grab that at 
http://antlr.org/download/Python/
Choose the appropriate *.egg file for the 3.1 version, then type

sudo easy_install antlr_python_runtime-3.1-py2.5.egg

This should do the installation for you.

You run the Keyboard Layout Editor with 

./KeyboardLayoutEditor.py
