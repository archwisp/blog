# Simplified Git tips for SVN users: log output
### Background

After accepting the fact that Git is likely going to supplant SVN, I decided
to hunker down and figure out how to actually USE the tool rather than fight
with it every time I had to interact with it. Well, my foray into Git has
often reminded me of a very similar experience I had when learning Vim: utter
frustration. Each time I dug into Git's man pages and internals, I felt more
confused than when I started and told myself, "just live with it". Well, as
with Vim, as time has gone by, I've learned things which have made Git
infinitely easier to live with and I want to share them with you.

**DISCLAIMER**: I am by NO means a Git expert. I am still far more comfortable with SVN. My goal here is to provide the information I've found helpful in my transition.

So, I'm going to start posting some very simple tips targeted at seasoned SVN
users. I'm not going to explain the functionality behind each item in order to
keep it simple and make the answers easy to find. So, here we go.

### Log Output

In this post, I'll cover log output. If you're a long-time SVN user who has
recently switched to Git for whatever reason, you may, like I was, be
continually frustrated by the log output. It never gives me the information I
want! Well, here are some tips on how to get that information:

#### _How do I make Git output to STDOUT by default?_

Either execute the following command:
    
    $ git config --unset-all core.pager

Or add the following lines to your ~/.gitconfig file
    
    [core]
       pager =

#### _What is the Git equivalent to `svn log --limit 5`?_
    
    $ git log --name-status -n 5

#### _What is the Git equivalent to `svn info`?_

It's not exact, but most of that information can be shown by executing the
following commands:
    
    $ git config --local --list && git log -n 1

Okay, that's it for now; just some simple tips to help you get by.

Thanks for stopping by!
