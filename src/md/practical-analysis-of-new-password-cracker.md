Just before the holidays, I saw a press release regarding some state-of-the-art hash cracking hardware and the headlines made it sound like it was a big deal:

>“New 25 GPU Monster Devours Passwords In Seconds”
http://securityledger.com/new-25-gpu-monster-devours-passwords-in-seconds/

Well, along with my general interest in hashing and cryptography, we had discussed salted-MD5 password hashing that week with a client. The press release provided an interesting aside to that discussion, so I did some analysis on the benchmarks from which we could draw practical conclusions about its impact. In this article, I’ll provide a high-level overview of why you should be moving from salted hashes to Key Derivation Functions (KDFs), and then plunge into the mathematics and information theory analysis I performed so we can all understand exactly what these benchmarks mean from a practical point of view.

## The High-Level
After all is said and done, hash algorithms like MD5, SHA-1, SHA-256, SHA-512, and SHA-3 are designed to be as fast as they possibly can while not producing collisions or reversible outputs. Speed may sound like a good thing but it’s a problem for password hashing. Speed works in the attacker’s favor because his job is to recompute the hashes one-by-one until he lands on the correct value. And while the complete keyspace of even MD5 is well beyond the realm of plausible brute-force attack, the limited keyspace we tend to use makes brute-force attack extremely plausible. Moving from MD5 to SHA-3 will increase your possible keyspace but if you’re still using 8-character passwords, the only security benefit you get is that SHA-3 is marginally slower than MD5.

Well, custom password cracking machines like the one in the article will keep getting faster and we likely still have 6-12 character passwords. There are strong arguments for coming up with something other than passwords for authentication purposes, and people are working on that, but there is a current solution to the brute-force problem. For those of us who still have passwords, the cryptographic solution is to use a key derivation function like S/I S2K (PGP), PBKDF2 (RSA), BCrypt (OpenBSD), or SCrypt (Tarsnap), in place of a salted hash. All of these functions were designed to be deliberately slow in order to thwart brute-force calculation. The idea is that the authentication system only has to compute the hash once given the correct password, but the attacker has to compute the hash, literally, 6 million billion times.

## Mathematics & Information Theory
The headline of the article refers to LM (Microsoft’s LAN Manager) hashes but as I mentioned above, I was more interested in the MD5 benchmark. If you’re interested in the other benchmarks, I’ve provided all of the formulas and logic you’ll need to perform the same analysis against those. The benchmark that the author provides for MD5 is 180 billion (180x10^9) guesses per second. If the entire keyspace, meaning all possible one-to-one values, of MD5 were used that would present the attacker with 2^128 possible hashes to calculate for every password. To determine the relationship between 180x10^9 and 2^128, we need to do some math which I’ll go over in the next section.

## Practical Speed Analysis
First, we’ll simplify everything greatly by converting the base 2 number (2^128) into a base 10 number because it’s easy for most people to convert other numbers to base 10 notation in their heads for comparison. Here is the formula:

`Let x be the exponent, let a be the starting base, and b the target base, and y be the result`:

`y = x*ln(a)/ln(b)`

To convert `2^128` to base 10, we do: `128*ln(2)/ln(10)` = `38.5`

Therefore, `2^128` = `10^38.5` = `1x10^38.5` = `1e38.5`

So, the password cracker can perform 180x10^9 hashes per second and it has to calculate 1x10^38.5 hashes for every password. The following formula  shows how long that will take:

`1x10^38.5 / 180x10^9` ~= `1.75x10^27` seconds

Given 1 year = 3.15569x10^7 seconds
`1.75x10^27 / 3.15569x10^7` ~= `5.5x10^19` years

So, with state-of-the-art custom hardware, it would take 5.5x10^19 (10 billion billion) years to crack one salted MD5 hash. That seems pretty secure even given the ½ probability that you will guess the correct value at random. It WOULD be if the entire keyspace could legitimately be used. Unfortunately, the passwords that people can effectively type into a prompt are pretty limited.

### Entropy & Other Limitations
A standard ASCII character consumes 1 byte (8 bits) and each byte can theoretically have 2^8 (256) unique values. Because each character consumes 8 bits, 16 possible characters can fit into the keyspace of MD5. To figure out the work needed to guess all of the combinations, we’ll consider the typeable characters: a-z, A-Z, 0-9, and 32 special characters for a total of 94 possible values per byte. 94 possible values is being VERY generous. In practice, I see only 4-6 permitted special characters for a total of 68 possible values per byte but we’ll work with 94 to analyze the best-case scenario. So, in reality, rather than having to try 2^128 possible values, we only have to try 94^16 (~2^105) possible values.

On top of the ASCII entropy limitation, people have a hard time remembering passwords, so most password policies allow between 6 and 12 characters. This further reduces the work from 94^16 to between 94^6 and 94^12.

For comparison, the conversions are:
* 6 Characters: `94^6` = `6*ln(94)/ln(2)` ~= `2^39` ~= `7x10^11`
* 8 Characters: `94^8` = `8*ln(94)/ln(2)` ~= `2^52` ~= `6x10^15`
* 10 Characters: `94^10` = `10*ln(94)/ln(2)` ~= `2^65.5` ~= `5x10^19`
* 12 Characters: `94^12` = `12*ln(94)/ln(2)` ~= `2^79` ~= `5x10^23`

Due to practical limitations, the key space of a 128 bit hash has been reduced from 1x10^38.5 to between 7x10^11 and 5x10^23. If we factor in fewer special characters, it is much lower.

### Final Analysis
Recall that the hash cracker is capable of generating 180x10^9 MD5 hashes per second. Below is the table of time to crack a salted MD5 password with this technology:

* 6 Characters: `7x10^11 / 180x10^9` ~= `3.8` seconds
* 8 Characters: `6x10^15 / 180x10^9` ~= `9` hours
* 10 Characters: `5x10^19 / 180x10^9` ~= `8` years
* 12 Characters: `5x10^23 / 180x10^9` ~= `9` million years

## Conclusion

So, there you have it. If you are using 6 or even 8 character passwords, your salted MD5 hashes are well within the practical realm of being cracked if they were to fall into the hands of an attacker.

As I mentioned above, moving to a different fast hashing algorithm isn’t the answer as all of them will eventually be in the same boat. Consider moving to a key derivation function for your password hashing needs.
