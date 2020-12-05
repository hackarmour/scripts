### Operators
**>**. redirect the output of any command to a file
**>>**. append the output of any command to a file
**&&**. execute a second command after the first one has executed *successfully*
**&**. run commands simultaneously
**$**. environment variable
**export**. set *varname* to *value* `export <varname>=<value>`
**|**. take the output of a command and use it as input for a second command
**;**. like `&&`, but does ++not++ require the first command to execute *successfully*
**ln**. completely duplicates the file, and links the duplicate to the original copy
**ln -s** just a reference to another file (symlink)
**find**. `find / -type {f/d} -user kittycat -size {-2k/+2k} -name "*.xml"`
