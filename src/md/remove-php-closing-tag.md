# A Script To Remove PHP Closing Tags

If you are a PHP developer, you may or may not know that it is becoming
popular to omit the closing PHP tag in class files as it's not necessary and
it avoids the possibility of a space at the end of the file causing
frustration in various situations. If you've ever had to remove these tags
from a large number of files, you know how tedious it can be. Well, no more;
here is a script to do just that. Just change into the directory containing
the files to be stripped, and run 'php-remove-closing-tag'.

The script makes use of the awk, pcregrep, sed, and wc utilities to get the
job done. You may need to install some or all of them to make the script work.
If you are a developer, you will probably have all of them installed anyway.

[Download Source](http://bryan.ravensight.org/wp-content/uploads/code/php-remove-closing-tag)

Source Code:
    
    
    #!/bin/bash
    # vim:ft=sh:ts=3:sts=3:sw=3:et:
    
    ###
    # Strips the closing php tag `?>` and any following blank lines from the 
    # end of any PHP file in the current working directory and sub-directories. Files
    # with non-whitespace characters following the closing tag will not be affected.
    #
    # Author: Bryan C. Geraghty 
    # Date: 2009-10-28
    ##
    
    FILES=$(pcregrep -rnM --include='^.*\.php$' '^\?\>(?=([\s\n]+)?$(?!\n))' .);
    
    for MATCH in $FILES;
    do
       FILE=`echo $MATCH | awk -F ':' '{print $1}'`;
       TARGET=`echo $MATCH | awk -F ':' '{print $2}'`;
       LINE_COUNT=`wc -l $FILE | awk -F " " '{print $1}'`;
       echo "Removing lines ${TARGET} through ${LINE_COUNT} from file $FILE...";
       sed -i "${TARGET},${LINE_COUNT}d" $FILE;
    done;
    

UPDATE:

I discovered a bug in the previous version of the script. I was performing a
`head -n 1` on the result of the expression to handle the output of multiple
lines from the pcregrep but this was limiting the entire search to one file...
doh! I fixed this problem by making the extra space search a positive-
lookahead. I have tested the new version thoroughly and assure you that it
will work as intended.
