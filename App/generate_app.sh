#! /usr/bash

OS=$1

if [$OS == "macosx"]
	then
		python setup.py py2app
else
	C:/Python35/python.exe setup_win.py intsall 
fi

echo "Python App Created!"
exit 0
