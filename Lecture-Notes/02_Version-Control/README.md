Day 02: Basics of Version Control, GitHub, & Social Coding
==========================================================

Today, we introduced the basics of the [GitHub
workflow](https://guides.github.com/introduction/flow/).

<p align="center"
<br>
<img src="fork-and-clone-graphic.png" alt="ForkandClone" height=300> <br>
</p>

## Recapping Today's Activity

#### GitHub Setup: Fork, Clone, and Configuring Remote Repositories
1. We made a GitHub account by using our Georgia Tech credentials
[here](https://github.gatech.edu/).
2. Next, we [forked](https://guides.github.com/activities/forking/#fork) the
central course repository,
[`chem/F19-4803DR-8843DR`](https://github.gatech.edu/chem/F19-4803DR-8843DR),
to your account by clicking the "Fork" button in the top right-hand corner of
the page. Your fork is nicknamed `origin`, since you're starting your own
contribution from there.
3. After we each forked the course repository, everyone [cloned their
fork](https://guides.github.com/activities/forking/#clone) to their own
computer (what we will hereafter call `local`) on the command line by
executing:
    ```
    ~$ git clone https://github.gatech.edu/chem/<username>/F12-4803DR-8843DR.git
    ```
4. Finally, we configured the remote repositories our `local` knows about
by using `git remote`:
    ```
    # Before we do anything to our remotes
    ~/F19-4803DR-8843DR $ git remote -v
    
    origin	https://github.gatech.edu/dsirianni6/F19-4803DR-8843DR.git (fetch)
    origin	https://github.gatech.edu/dsirianni6/F19-4803DR-8843DR.git (push)
    
    # Add the central course repository as a remote, nickname it "upstream"
    ~/F19-4803DR-8843DR $ git remote add upstream https://github.gatech.edu/chem/F19-4803DR-8843DR.git
    
    # Now our local machine knows about upstream!
    ~/F19-4803DR-8843DR $ git remote -v
    origin	https://github.gatech.edu/dsirianni6/F19-4803DR-8843DR.git (fetch)
    origin	https://github.gatech.edu/dsirianni6/F19-4803DR-8843DR.git (push)
    upstream	https://github.gatech.edu/chem/F19-4803DR-8843DR.git (fetch)
    upstream	https://github.gatech.edu/chem/F19-4803DR-8843DR.git (push)
    ```

#### Collaborative Python with Project Euler

As a class, we worked in groups to solve the first [Project
Euler](https://projecteuler.net/problem=1) problem, "Multiples of 3 and 5", in
the Jupyter notebook
[`02_Project-Euler.ipynb`](../../Classroom-Actiities/02_Project-Euler.ipynb),
and then discussed it as a class.  

#### Saving our progress on `local` and `origin`

Even after we had made and saved changes to the `02_Project-Euler.ipynb`
file on our `local` computer, we can still lose our progress in a tragic E-scooter
related incident.  So, we saved the history of our changes with `git` and
synced our progress with our remote fork, `origin`.  To do this, we completed the
following steps:

1. See what we've changed in our `local` repository with `git status`:
    ```
    ~/F19-4803DR-8843DR $ git status
    
    On branch master
    Your branch is up-to-date with 'origin/master'.
    
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)
    
    	modified:   Classroom-Activities/02_Project-Euler.ipynb
    
    no changes added to commit (use "git add" and/or "git commit -a")
    ```
2. We told `git` that we endorse our changes by staging them using `git add`:
    ```
    ~/F19-4803DR-8843DR $ git add Classroom-Activities/02_Project-Euler.ipynb
    ~/F19-4803DR-8843DR $ git status
    On branch master
    Your branch is up-to-date with 'origin/master'.
    
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)
    
    	modified:   Classroom-Activities/02_Project-Euler.ipynb
    ```
3. Next, we commited our changes on `local` to preserve them in the history of
our repository.  We used the additional flag `-m` to add a short message
describing the changes directly on the command line:
    ```
    ~/F19-4803DR-8843DR $ git commit -m "Adds progress from class 02"
    [master 27db453] Adds progress from class 02
     1 file changed, 143 insertions(+), 38 deletions(-)
     rewrite Classroom-Activities/02_Project-Euler.ipynb (17%)
    ```
4. Finally, we pushed our changes from `local` to `origin`, by executing
    ```
    ~/F19-4803DR-8843DR $ git push origin master
    ```

### Additional `git` and GitHub Resources

For additional help using `git` and GitHub, check out the following materials:
- [This page](GitHubFlow.md) has detailed instructions for a number of common
tasks with `git` and GitHub.
- The [Git Handbook](https://guides.github.com/introduction/git-handbook/) (and
all of the [GitHub
Guides](https://guides.github.com/introduction/git-handbook/)) are an excellent
resource for everything version control and social coding.
- If you have a [CodeAcademy](https://www.codecademy.com/learn) account, you
can check out [this interactive
tutorial](https://www.codecademy.com/learn/learn-git) for help.


