# C | S | 5 | 0 | P | y | t | h | o | n
*Repository for CS50: Web Programming with Python and Javascript*
*Course started: October 1, 2020*
**Matthew James Spitzer**

https://github.com/mjs375/CS50Python

### BASIC TERMINAL COMMANDS:
- $ **ls**
    - *short for 'list', it lists all files in the current directory*
- $ **pwd**
    - *prints the current working directory (path/path/folder)*
- $ **cd** *<repository name>*
    – *'change directory'*.
- $ **cd ..**
    - *go back one directory (from child to parent). '$ cd ../..' would go up 2 levels*
- $ **cd ~**
    - *go back to the home directory*
- $ **touch** *<filename>*
    - *create a new file, e.g. 'touch index.html'*
- $ **open** *<filename>*
    - *open a file in the directory*
- $ **cp** *<filename> <newfilename>*
    - *copy a file to another directory, e.g. 'cp ./Desktop/index.html index2.html'*
- $ **mv** *path/<filename>*
    - *move a file to another location, e.g. 'mv ./Desktop/image.jpg ./Documents'*
- $ **mv** *path/<filename> samepath/<filename>*
    - *renames a file*
- $ **mkdir** *path/<directory>*
    - *create a new directory (folder), e.g. 'mkdir ./Desktop/New_Folder'*
- $ **rm -i** *<filename>*
    - *remove a file, with confirmation(!)*
- $ **rmdir** *path/<directory>*
    - *remove an empty directory, e.g. 'rmdir ./Desktop/New_Folder'*
- $ **rm -R** *<directory>*
    - *removes nested directories*
- $ **clear**
    - *clear the terminal of all previous commands*
- $ **help -s** *<command>*
    - *Displays short, helpful information about the <command/pattern>*
- $ **whatis** *<command>*
    - *get a one-line description for a command, e.g. 'whatis rmdir'*
- $ **man** *<command>*
    - *show manual page for a command*



###GIT COMMANDS:
- $ git clone <repository url>
    - *Download the repository to your local computer.*


- $ git add <filename> *-OR-* $ git add.   
    - *adds all files within that directory: 'keep track of these'*
- $ git commit -m "some message"
    - *[save current state]*
- $ git commit -am "some message"
    - *combine the above two git commands*
- ( $ git status )
- $ git push
    - *sends version to github*
- $ git pull
    - *pulls more-updated files from github repository and incorporates them to your local files*
    - *for either pull/push, if the 'other side' has file differences, you will need to reconcile them first*




• MERGE CONFLICT: multiple people have made changes...
   "Conflict (content): merge conflict
   Everything between <<< ... === you made
   Everything between === ... >>> someone else made
   Conflicting commit = "<some number: 5756c5434d89f..."
 How to address the merge conflict: which version do you want to keep? or combine them in some way?
   Make your changes, then commit them... (add/commit/push)


• GIT LOG: keep track of ALL changes (commits) in this particular Repository
  $ git log
    commit(s), author, date
• GIT RESET
   $ git reset --hard <commit_hash> [Go all the way back to one past version/commit]
   $ git reset --hard origin/master [Resets to version on github repository]

• GIT "STRUCTURE": don't save/commit in a linear fashion...
  E.g. you start a new feature, but then need to go back and fix a bug [but keep current work]
     Instead, start a BRANCH when you start something new. Name each BRANCH
     MASTER BRANCH: usually contains up-to-date, stable code [head]
     FEATURE BRANCH: if you start a side branch for a new feature
        'HEAD': current branch you are working on...
    FINALLY: MERGE MASTER and FEATURE BRANCH

• GIT BRANCHING OFF:
$ git branch
   [Will tell you what branch you are currently on, e.g. 'master'. * means your current branch]
$ git checkout            [Switching branches]
$ git checkout -b [name]  [Switching to a NEW branch]
$ git branch
     master
   * [name]
$ git checkout master   [Switch back to master branch]
...
$ git commit -am "change message" [Commit changes in one/current branch]

$ git merge [name]  [currently on master branch, merging to [name] branch]
   "CONFLICT (content): Merge conflict in filename.html" [Usually GIT can merge automatically, but not if the same line(s) of code are changed]
   <!-- -->
$ git commit -am "fixed merge conflicts"


• GIT FORKING REPOSITORIES: making your own copy of the original repository ["save as"/clone]
   E.g. Bootstrap's open-source public code. It would be dangerous if anyway could PUSH their changes to the master/public code.
   Pull Request: request Bootstrap uses your changed code [people fixing bugs, new features, &c.]

• GIHUB PAGES: free way to take a website w/ HTML, Javascript, &c.
   Anyway can make a website for free using GitHub!
   Name convention: "username.github.io"
      Automatically supports GitHub pages:
      $ git clone [url]
         Add index.html, styles.css, &c. [pages of website]
      $ git add index.html
      $ git commit -m "first commit"
      $ git push
      GITHUB PAGES [on github.com]: "Your page is ready to be published!"
