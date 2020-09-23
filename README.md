# dpass

Quick and dirty password manager.

### Usage

1. Set the FILES_DIR in pass.py.
2. Set the KEY_DIR in pass.py.
3. Run the python script with the site name as an argument or without Example: `python pass.py github` or `python pass.py`
4. If run without command line argument enter the site name now.
5. The password will be copied to the system clipboard. If it does not exist it will be generated first.


The strings are encrypted, which serves no purpose as the key is in the same directory, but may be useful if the KEY_DIR is set to an external drive such as `/mnt/usb`.
I made this simply because I have a bad habit of reusing passwords which I am trying to break, and this is marginally better than writing them down.

Use at your own risk!
