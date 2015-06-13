#!/usr/bin/env python

import os
import MySQLdb
import html2text

build_path = os.path.dirname(os.path.realpath(__file__))
out_path = '%s/../import/' % (build_path) 

conn = MySQLdb.connect(
        host="127.0.0.1",  
        user="", passwd="",
        db='wordpress'
)

cur = conn.cursor()
cur.execute("SELECT post_name, post_title, post_date, post_content FROM posts where post_status = 'publish'")
row = cur.fetchone()

while row:
    title = "# " + row[1]
    date = row[2]

    try:
        content = html2text.html2text(row[3])
    except:
        content = row[3]
        print "WARNING: Could not convert content for post %s. Writing HTML to file." % (row[0])

    outfile = "%s%s.md" % (out_path, row[0])
    print "[*] Writing post to file %s" % (outfile)
    open(outfile, 'w').write("%s\n%s" % (title, content))
    row = cur.fetchone()

conn.close()
