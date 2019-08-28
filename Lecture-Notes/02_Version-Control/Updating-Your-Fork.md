Updating Your Fork
==================

So, something was added to the `upstream` repository, `chem/F19-4803DR-8843DR`,
that you want to have in both your `local` and `origin`.  How can you do this?

<p align="center"
<br>
<img src="fork-and-clone-graphic.png" alt="ForkandClone" height=300> <br>
</p>

Looking at the scheme above for how our remote repositories are organized, we
could seeminly sync our fork with `upstream` if we first pull to `local`, and
then push to `origin`.  Here are the steps to do this:

1. Make sure you're on your `master` branch.  If not, stash your changes and
switch to `master` by checking it out:
    ```
    ~/F19-4803DR-8843DR $ git checkout master
    Already on 'master'
    ```
2. Pull in changes from `upstream`, replaying any new changes of yours on top
of them using the option `--rebase`:
    ```
    ~/F19-4803DR-8843DR $ git pull --rebase upstream master
    ```

3. Now, the changes from `upstream` have been incorporated into `local:master`.
To update your fork, we must push the new history to `origin:master`.  To
ensure the additional history isn't rejected, we must add the `--force` option:
    ```
    ~/F19-4803DR-8843DR $ git push --force origin master
    ```

Now, `origin:master` should be even with `upstream:master`, and all of the
changes introduced in `upstream:master` are synced into your fork! 

