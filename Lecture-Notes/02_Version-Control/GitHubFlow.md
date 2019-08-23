GitHub Flow Instructions
========================

> **Note: After making changes to a file, make sure to add & commit your
> changes (steps 2-3) _before_ attempting to pull with rebase!**

To update your local machine & remote fork (`origin`):
1. Make sure `local` is on your `master` branch and is up-to-date with
`upstream:master`:
    ```
    ~$ git checkout master
    ~ (master)$ git pull --rebase upstream master
    ```
2. Make and switch to a new branch on `local` to perform your development:
    ````
    ~ (master)$ git checkout -b myfeature
    ~ (myfeature)$ 
    ```
2. Make some changes to `file1` locally
3. Add & commit your changes locally
    ```
    ~ (myfeature)$ git add file1
    ~ (myfeature)$ git commit -m "Changes to file1"
    ```
4. Push your commits to your `origin` on the new `myfeature` branch
    ```
    ~ (myfeature)$ git push origin myfeature
    ```

If you're interested in contributing your changes back into the `upstream`
repository:
1. Open a pull request to `upstream:master` from the `myfeature` branch
of your fork (`origin:myfeature`)
2. Wait on PR comments, suggestions, etc. and re-edit your code on `myfeature`
branch (step 2 above)
3. Add, commit, and push your changes to `origin:myfeature` according to steps
3-4 above. GitHub will automatically incorporate these changes into your pull request!



