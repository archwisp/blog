# SHA-3 Finalists: PHP Speed Comparison

### Background

As everyone interested in cryptology knows, NIST has been running a
[cryptographic hash algorithm competition](http://csrc.nist.gov/groups/ST/hash/sha-3/) 
to determine the successor of SHA-2. The chosen algorithm will be aptly
named, SHA-3.  

> NIST selected five SHA-3 finalists - BLAKE,
> Gr0stl, JH, Keccak, and Skein to advance to the third (and final) round of
> the competition on December 9, 2010, which ended the second round of the
> competition.

As I've said in other places, the SHA-3 competition is extremely important
because it draws in the entire cryptology industry together to beat on the
submitted algorithms for three years. You can be pretty confident in any
algorithm that advances to the final round. But what the competition
ultimately determines is which function is the "Jack of all trades". For
those of us who do large-scale database operations where hashes are part
of the works, a high security margin and speed are more important than the
number of CPU cycles and bits of memory saved, and how well it can be
implemented in embedded systems. So I set out to test the five finalist
hashes in a typical web application environment.

### Why I created the test My foray

into this test began when I wrote a quick CLI PHP script to download
photos from my cell phone. As part of the copy process, I naturally built
in a checksum routine to verify that each file was copied correctly. I
have been an avid follower of the SHA-3 competition from the beginning,
and I had read good things about the Skein function, so I had decided to
implement it in the script just for fun.  Right around the same time, NIST
[published](http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/Round2_Report_NISTIR_7764.pdf)
its rationale for selecting the five finalists in the competition. After
reading through the rationale, I became really curious to see how each
function would stack up against one-another in a PHP environment. So after
creating PHP extensions for each of the finalists that didn't already have
one, I modified my download script to do some hash benchmarking, and ran
the test.

### The Test
After using the script to download the photos off of my cell phone, I
decided that the amount of data (about 40 MB) just wasn't large enough to
give me a good benchmark. So I decided to run the script against a whole
month of exported JPG photos from my DSLR which ended up being nearly 1 GB
of data (154 files @ 4-6 MB each). Since each file is hashed twice, we're
approaching 2GB of data hashed each time the operation runs. Since we are
only benchmarking the performance of the hash functions, all of the files
were copied once and verified a couple of times before the official timing
began.  Here is basic overview of how the script works:

* List the source directory contents recursively, looking for .jpg files
* Iterate through the list
* Get the file creation date
* Build a destination path based on the file creation date and file name
* If the destination file does not exist, or hashes of the files do not match, copy the file
* If hashes of the files still don't match, report a failure

Click [here](http://bryan.ravensight.org/wp-content/uploads/code/download-photos.phps)
for the source code.  Since the files have already been copied and
verified, as mentioned above, the file copy and the last verify never
happen in the speed comparison test. It essentially loops through all of
the files, builds hashes of the source and destination files, and verifies
that they all match.  For the purposes of this test, I needed to be able
to keep track of the exact number of bytes hashed (for verification
between runs) and the exact amount of time spent actually hashing data so
we wouldn't have to worry about other operations clouding the results. To
that end, I built a class with an internal counter for each. The class
also contains an isolated hash wrapper function which only accepts the raw
data to be hashed, increments the counters, and passes the data on to hash
function configured at the object level.

A new object is created and destroyed for each hash function being tested,
per round. The wrapper function increments the counters for the lifetime
of the object. The number of bytes hashed is an explicit count of the
bytes fed to the wrapper function. The time spent hashing is calculated by
getting the microsecond time stamp immediately before the hash function is
executed, and once again immediately after. The former is subtracted from
the latter, and the internal counter is incremented by the result.

### The Results

To establish a baseline, I ran iterations of MD5 and SHA-512. MD5 has been
the hash of choice for the past few years where speed was a major concern.
Unfortunately, MD5 is now considered to be cryptographically broken but it
served its purpose here in determining a reasonable floor for speed. I
chose SHA as the second baseline because it is the current standard, and I
chose to implement its 512 bit mode because that is what the new
algorithms will be using.  I ran the entire script, which performs the the
verification of the entire dataset for all seven hash functions (MD5,
SHA-512, BLAKE, Gr0stl, JH, Keccak, Skein), five times.  This test was
performed on a 64-bit Ubuntu 10.10 installation running PHP
5.3.3-1ubuntu9.3 in CLI mode. The CPU is an Intel Core2 Duo T9300 @
2.50GHz and the machine has 4 GB of memory installed. During the entire
duration of the test, the load average of the machine peaked at 1.2, CPU
usage peaked at 85%, and memory usage peaked at 25%.

Seconds spent hashing 154 files (1937164902 bytes)

| Function   | Round 1   | Round 2   | Round 3   | Round 4   | Round 5   |
|------------|-----------|-----------|-----------|-----------|-----------|
| MD5        | 5.731552  | 5.729477  | 5.817808  | 5.813912  | 5.740509  |
| SHA-512    | 14.610088 | 14.269413 | 14.222281 | 14.468436 | 14.378429 |
| Skein-512  | 6.952610  | 6.767148  | 6.858372  | 6.877997  | 6.812982  |
| Keccak-512 | 8.023958  | 7.778949  | 7.952572  | 7.887774  | 7.886457  |
| JH-512     | 8.195324  | 7.830080  | 7.916424  | 8.040076  | 7.995283  |
| Gr0stl-512 | 8.192576  | 8.121383  | 8.205048  | 8.063461  | 8.326136  |
| BLAKE-512  | 9.894579  | 9.715329  | 9.627831  | 9.588126  | 9.610026  |

Click [here](http://bryan.ravensight.org/wp-content/uploads/sha3-finalists-comparison.log) for the raw results.
Well, that's it. I'll leave the analysis of what the results mean to the reader.

Oh, and if you're interested in the PHP extensions I wrote, they're
available at: https://github.com/archwisp
