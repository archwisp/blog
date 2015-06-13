# Complie Simple C Programs With Vim
When working on simple C programs, I like vim to produce a compiled output-
file named the same as the source file with the .c extension removed when I
issue the :make command. For instance, if I create a source file named
"helloworld.c", I want the compiled binary to be named "helloworld".

UPDATE:

I discovered this simpler command which does not have any external
dependencies. Add it to your ~/.vim/ftplugin/c.vim file.
    
    set makeprg=gcc\ %\ -g\ -o\ %:r

Here is the old command I came up with which uses Perl for the substring
extraction. I'm leaving this here as a reference for how you might do other
things.

    set makeprg=gcc\ -g\ -o\ $(perl\ -e\ 'print\ substr(%,0,-1)')\ %
