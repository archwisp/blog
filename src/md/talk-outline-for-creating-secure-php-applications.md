# Talk Outline for Creating "Secure" PHP Applications

This is not a complete article on how to create a secure PHP application
but rather, the outline for a talk I've been planning for some time. Yes,
there have been talks on this topic in the past but they either had flaws
or were missing some essential pieces. My goal was to provide a complete
list of application security concerns and explain how you go about dealing
with them in PHP. Of course, much of the context is missing but it
wouldn't be a very good talk if I wrote it all down, now would it? I've
decided to publish it in hopes that it will force me to give the talk
sometime soon.  This list is very extensive, so it's possible that I
missed something. If you happen to read through it and notice something,
please leave a comment.

* Introduction
** Remember, layers
** Simpler is easier to test
** Don't make assumptions
** Vulnerable browser = game over

* Explicit Coding and Quality Assurance
** Don't rely on the server configuration; Set ini directives in your bootstrap
** Don't use global constants / variables / registries
** Don't use function parameter defaults
** Use === instead of == whenever possible
** Use constants for *possible* values
** Use wrappers for super-gloabals ($_GET, $_REQUEST, $_SESSION, etc.)
** Code should read like a book
** Simulate "Strong/Static" types
** Use Code sniffer and PHPMD
** Unit testing / TDD
** Continuous Integration

* Lock Down the Environment
** Implement ACLs
** Web server user should only be able to read from web root
** Web server user should only be able to write to cache directories and log files
** Cache and log directories should not be publicly accessible; Bonus: store them on a separate sever
** Implement MAC / SELinux
** Don't rely on Safe Mode, Suhosin, or any other "automatic" protection
** Configure web server process/thread limits
** PHPMyAdmin bypasses MySQL host filtering

* Error Handling
** Exceptions are okay in PHP
** Install a custom error handler which can catch any code-level error or exception
** Error handler should be able to easily switch between "production" and "development" mode
** Production systems should not expose error content, including HTTP status codes
** Development systems should display ALL error content
** When calling any method that accepts sensitive information (e.g. PDO instantiation), wrap the call in a try-catch block because any resulting exception stack trace will contain sensitive information; The exception message can be re-thrown from within the catch block
** Install a separate "message" handler for dealing with business-logic errors and converting code-level errors into user-friendly errors

* Input Validation & Sanitizing and Output Sanitizing
** Validation means checking, reporting, and then stopping execution
** Sanitizing means automatically converting data into the expected format
** Validation and sanitizing MUST be done in the server-side code
** Front-end JavaScript is only for improving the user experience
** Don't accept include file names as input
** Don't read or write files identified via input
** Don't accept session or cookie data as input
** Business logic validation should happen first
** Validate every parameter of every method
** Sanitize all data before attempting to store it (e.g. SQL injection)
** Use database connection libraries which support bound parameters and correct encoding (PDO)
** Sanitize all data before it is sent to the output (e.g. Cross-site scripting)
** Use quickly-expiring HMAC signatures to authenticate requests from trusted sources
** Only allow input-controlled redirects to do so locally

* User Authentication
** Use SSL
** Don't set arbitrary password limitations
** Use a key derivation function for password hashing (scrypt, bcrypt, PBKDF2, or S/I S2K; in that order)
** Control how often your key derivation function can be executed
** Pay VERY close attention to how sessions are managed (next section)

* Sessions & Cookies
** Session does not equal authenticated
** Explicitly manage association of session IDs with authentication states
** session_destroy() is not enough; the session probably still exists
** Regenerate the session id immediately after authentication and only associate the new session with the authentication state
** Re-authenticate when the user moves to a higher security zone
** NEVER store logic data in the session (e.g. admin = 1), even if it is encrypted
** Only use session and cookie storage for display purposes

* AJAX, Forms, and API handlers
** Each local action should have a unique nonce associated with it in the session
** Use quickly-expiring HMAC signatures to authenticate requests from trusted sources
** Perform access control checks in every single server-side action

* Data Encryption
** Don't bother, you'll probably do it wrong
** No, seriously, if you need encryption, hire an expert to build it
** Then hire Matasano to show you what a terrible job the "expert" did
** If you're not offended, there's a very slim chance you might be qualified to build your own
** Either way, encryption is WAY beyond the scope of this talk
