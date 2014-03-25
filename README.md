# Keyboard Layout Editor

PyGTK program that helps create or edit XKB keyboard layouts.

To run the application, you need the python binding packages for
* Cairo
* Pango
* GObject
* lxml
* ANTLR 3.1.2

You need to process the ANTLR grammars in order to generate the necessary Python code.
All *.g files should be processed with ANTLR:

    sudo apt-get install python-setuptools
    pip install http://www.antlr3.org/download/Python/antlr_python_runtime-3.1.2.tar.gz
    wget http://www.antlr3.org/download/antlr-3.1.2.jar
    java -classpath "antlr-3.1.2.jar" org.antlr.Tool *.g

You finally run this program with:

    ./KeyboardLayoutEditor
