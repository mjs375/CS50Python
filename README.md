# CS50Python
Repository for CS50: Web Programming with Python and Javascript
Course started: October 1, 2020
Matthew James Spitzer


https://github.com/mjs375/CS50Python


git clone <repository url>
  Download the repository to your local computer
$ ls
$ cd <repository name>

$ git add <filename> #OR# git add.   [adds all files within that directory: 'keep track of these']
$ git commit -m "some message" [save current state]
$ git status
$ git push [Sends version to github]


• GIT PULL: take changes on github.com, and pull them down to local version
   $ git pull


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
