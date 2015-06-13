# How to deter authentication denial-of-service attacks
Some hype has been going around the web lately related to the use of Bcrypt
and how it opens you up to denial-of-service attacks. Now, to the seasoned
developer, this is a completely ridiculous notion. As developers, we think
about how and when resources will be consumed on a daily basis.

To be fair, one of the videos I saw was targeting "inexperienced developers"
and didn't offer many solutions to the issue. I wanted to chime in with some
simple measures to implement which will help deter attackers from using your
derivation function against you:

  1. Check for a valid user record before hashing the password
  2. Store the last log-in attempt time-stamp for each user
  3. Store the number of failed log-in attempts for each user
  4. Write the following time delay function into your log-in routine before the password is hashed: 
    * If failed log-in attempts &gt; 1 
      * Wait until (failed log-in attempts ^ 2) seconds after the last failed log-in attempt before allowing the password to be hashed again
  5. Reset the number of failed log-in attempts after each successful log-in

That's it. Simple.

Thanks for stopping by.
