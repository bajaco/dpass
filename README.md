# dpass

Quick and dirty password manager.

### Usage

Set the FILES_DIR in pass.py.
Upon running the program you are presented with a blank input screen. 
Enter the name of the site you're logging into. If a password exists it will retrieve it, otherwise it will generate one at random.
Either way it will copy it to the clipboard.

Optionally set the site by command line argument

The strings are encrypted, which serves no purpose as the key is stored in the same directory. However it would be trivial in the future to add a key location and more options. I made this simply because I have a bad habit of reusing passwords which I am trying to break, and this is marginally better than writing them down.

