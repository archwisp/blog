#!/usr/bin/env python

import os
import markdown

build_path = os.path.dirname(os.path.realpath(__file__))
md_path = '%s/../src/md/' % (build_path) 
out_path = '%s/../www/' % (build_path) 

source_files = [ f for f in os.listdir(md_path) if os.path.isfile(os.path.join(md_path,f)) ]

template = open("%s/../src/template.html" % (build_path), 'r').read().strip() 

for source_file in source_files:
    infile = md_path + source_file
    print "[*] Reading markdown from file %s" % (infile)
    
    md = open(infile, 'r').read()
    body = markdown.markdown(md)
    html = template.replace('<!--BODY-->', body)
    
    outfile = out_path + source_file.replace('.md', '.html')
    print "[*] Writing HTML to file %s" % (outfile)
    open(outfile, 'w').write(html)
