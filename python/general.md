# import

1. To import file from another directory, you need to add the directory to the system path.

    ```
    import sys
    sys.path.append("/path/to/dir")
    ```

2. If you have revised a file and want to import it again. Using "import" won't do it,
 because by default, the interpreter won't import anything with the same name that already exists. 

    Use reload.

    ```
    import importlib
    importlib.reload(test_rich)
    ```

3. import will run everything in the file unless the code chunk is under `if __name__=='main':`


# debugging

ctrl+d: duplicate

break point is inserted and removed dynamically during run time

attach to process: use debugger on external python program, eg, kivy app

# tricks

	1. Reformat Code (``Ctrl-Alt-L``)

	2. add line
	 	- Start New Line (Shift-Enter Win/Linux/macOS)

		- Start New Line Before Current
	 	 (Ctrl-Alt-Enter Win/Linux, Alt-Cmd-Enter macOS)

	3. import/install package Alt-Enter
	4. Optimize Imports (``Ctrl-Alt-O`` Win/Linux/macOS)
	5. View documentation ``Ctrl-Q``
	6. Navigate | Back is Alt+Shift+Left Arrow
	7. Put cursor in ``choices()`` and do Cmd-P to see parameter list
