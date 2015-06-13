# Why I Choose PHP
### Background

As mentioned by some of the more well-known PHP talking heads in their
responses, there has been quite a bit of PHP smashing going around lately.
Each of them provided great reasons for using PHP. And while they came
close, they didn't quite cover the reasons I continually choose it over
others. Or at least, they expressed it differently.  The first thing I'll
explain is that my development realm is the web. I develop web
applications for a living. There are infinitely better languages for
developing applications for other platforms but for the purposes of this
article, I'm talking about web applications.  So, I'll just come out and
say what many others won't: I'm a huge PHP advocate.

But wait, it gets worse: 1) I love security 2) I love software craftsmanship

Yeah, I know you're thinking, "Wait, a supposed security guys who loves
PHP? This guy has no idea what he's talking about."

Bear with me.

The reasons I choose PHP boil down to

* It's as secure as any other web platform
* It's fast, reliable, and mature yet continually improving
* It's syntactically pretty
* The community & php.net

So, lets cover these items.

### The security of PHP</strong>

I get a lot of flack from my friends at security events whenever I remind
them that I'm a proud PHP developer. The most common response to the idea
that a PHP application can easily be developed to be as secure as any
other platform is a scoff. But of course, not many of them are
programmers, so it's not even worth going into the details. Lets cover
those details now.  First off, no language does security for you and
application security is difficult regardless of the language you're using.
Every language has frameworks and libraries to help with this problem,
including PHP. But don't forget the essential requirement that developers
understand what these tools are doing for them. I don't mean that they
should be able to build those tools themselves but they should understand
what is being done and why.  You could argue about the "security" of
compilers and interpreters but I have looked and and I have never seen any
definitive research on this. The one bit of research I've seen that
affects the potential security of PHP was a comparison of statically and
dynamically typed code. The research showed that static typing produces
superior code. Luckily, there are libraries available for simulating
static typing in PHP and it's something I advocate. I'll be writing an
article on that next.  So, I'll lump compiler and interpreter "security"
this into the same category as operating system security where the most
unbiased assurance ratings we can get are from Common Criteria. Windows
has consistently scored better than Max OSX for as long as I can remember
but everyone swears that OSX is "more secure". If we're talking about
published vulnerabilities in the interpreter, I can assure you that I've
never had to rush a PHP upgrade on a production system because of a
published vulnerability. The PHP manual is generally very good at
providing best practice guidelines for pretty much everything at the
language level. In most cases of published vulnerabilities, if you were
following best practices, you were safe from them.  Many interpreted
(scripting) languages do have a run-time configuration which alters the
behavior of the language and PHP is one of these. In PHP's past, it had
some default behaviors which caused problems for the uninformed but those
have since been removed. Some of those features have been removed entirely
as PHP has evolved. It's common to see magic quotes cited as a terrible
PHP feature. And while yes, I agree, those of us who had to tolerate it
simply added a run-time check to the database abstraction layer. If it was
enabled, we replaced those back-slashed quotes with regular quotes and
went on to our SQL injection checks. So, while it wasn't a great solution,
it didn't actually cause any security problems.  So, lets just drop the
idea that the "language" is less secure. Lets just agree that all
languages are more-or-less equal where security is concerned. Application
security is hard regardless of the language using.

I have been working on a talk on how to build "secure" PHP applications
for some time (work and family keep me busy) because the existing examples
are lacking in key areas. I'll be publishing the outline shortly which
will hopefully force me to give the talk so we can end this argument.

### PHP is a fast and reliable scripting language

Associated with the security argument is the pervasive idea that PHP
itself is a terribly written interpreter and there is nothing you can do
about that. It's just not true. Sure, it has some pitfalls you need to
watch out for but this is programming, not Lego&copy;s. The PHP
interpreter itself is certainly not made of the most elegant code but it
does what it does very well and it is the fastest scripting language in
nearly every regard except for large arrays.  As the manual says, "An
array in PHP is actually an ordered map". It then goes on to explain a
whole lot about what you can do with them; pretty much any kind of list.
The unfortunate side effect of this flexibility is that they can be really
slow. Some PHP array operations are documented to be as slow as O(n). I've
been told that they can be as slow as O(n&sup2;) but I haven't seen any
proof.  Fortunately, a slow array implementation isn't really a problem
for most web applications because we have database engines on which we can
rely for this sort of functionality.  Overall, I think PHP has struck a
good balance. I like the fact that primitives are not objects. I like the
way error handling works. The inconsistencies in argument orders and
function names have never bothered me. Code written in PHP is very easy to
understand because there are so few variations in syntax for accomplishing
the same thing. And finally, references work in exactly the way you would
want them to work in a web application.  So, yes, PHP is quirky. But
honestly, every language is. The most important thing to consider is what
the language was designed to do. PHP was designed to facilitate building
web applications and it does that job very well.

### PHP is mature

PHP has been in continuous development since 1995 and has evolved into a
language which can truly hold its own against any of the other languages
out there. Did you realize that the list of languages released to the
public around the same time includes ASP "classic", ColdFusion,
Java, Python, and Ruby? (and probably others) Sure, there have been
problems along the way; but it has been the same for all of the languages
I mentioned. The important thing to note is that we have all learned from
these problems.  I think the things that truly set PHP apart from the
others were, cross-platform support, open source/free to use, and php.net.
The first two are significant enough accomplishments but I believe PHP's
true genius was php.net.

### The community and php.net

For as long as I can remember, php.net has been there in pretty much its
present form. I've used a lot of languages over the years but I've never
encountered another with documentation that was as well-organized and
accessible as this. Top top that off, anyone can leave moderated comments
directly on the manual page for any given function or feature. I think the
interactive element of the manual is what really encouraged the growth of
the PHP community and improvement of the language. If you were a PHP user,
you used php.net, and you knew what everyone else knew.  The one major
thing php.net didn't provide was design guidelines. For instance, there
was no common document you could visit which explained a good architecture
for implementing database connections. So, what ended up happening was,
new users would need particular features, access the individual manual
sections for them, copy the remedial examples intended to explain
essential implementation details, and piece them together until they had a
functional application.  Sometime around 2005, a significant movement in
the PHP community aimed at software craftsmanship, quality assurance, and
security, began. Unfortunately, it was not directly associated with
php.net so new users don't know about it. These new users ended up going
through the same old cycle and the same old results are produced. Sadly,
this is something we're still battling.  While the documentation and
comments on php.net are indispensable for learning which functions are
available and how each works, they are certainly not the way to go about
learning how to create entire PHP applications. Fortunately, progress is
being made in this area. People like me are writing articles like this one
and talks are being presented at local user groups. As a result, we are
starting to see sites like http://www.phptherightway.com/ crop up. I'm
not affiliated with that site in any way and I don't completely agree with
the message being delivered, but it's a start.  I'm hoping to see
something similar done in in the spirit of php.net where there is a
pre-defined structure but anyone is allowed to contribute in a moderated
way. I think the only way it will make an impact, though, is if it is
blatantly referenced on php.net. A quick tactic I can think of would be to
add a link to "Database connection implementation recommendations" on any
database related manual pages. That way, when new people visit the site,
they are encouraged to consider their overall implementations.  PHP has an
extensive collection of great frameworks, libraries, and information out
there but there is still a lot of work to be done in making these things
known.

### Conclusion

So hopefully, I've explained all of it in a clear and rational way. I
don't expect the PHP bashing to go away because some people will believe
what they want to believe. In the end, I wrote this article to explain why
*I* choose PHP as a software security and craftsmanship advocate.
Remember to keep an eye out for my outline on how to develop "secure" PHP
applications.  Thanks for stopping by.
