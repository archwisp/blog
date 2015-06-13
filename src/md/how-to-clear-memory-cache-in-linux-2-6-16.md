# How To Clear Memory Cache In Linux (&gt;= 2.6.16)
Without getting into the politics of why you would want to clear your memory
cache in Linux, here is a very small script I wrote to do just that. It makes
use of a feature that was introduced in kernel 2.6.16, so your kernel version
needs to be >= 2.6.16 in order to use this script. If you're running a kernel
older than that, you have bigger problems to worry about than your memory
cache ;) If you don't know how to determine your kernel version, you're
probably better off not messing with your memory cache.

free-cache:
    
    #!/bin/bash
    
    ###
    # This script flushes the file system buffers and clears memory caches.
    # 
    # From the man page:
    #
    # /proc/sys/vm/drop_caches (since Linux 2.6.16)
    #
    #   Writing to this file causes the kernel to drop clean caches, dentries and
    #   inodes from memory, causing that memory to become free.
    #
    #   To free pagecache, use echo 1 > /proc/sys/vm/drop_caches
    #   To free dentries and inodes, use echo 2 > /proc/sys/vm/drop_caches
    #   To free pagecache, dentries and inodes, use echo 3 > /proc/sys/vm/drop_caches
    #
    # @Author Bryan C. Geraghty 
    # @Since 2010-11-01
    ##
    
    sudo sync && sudo bash -c 'echo 3 > /proc/sys/vm/drop_caches';
    
