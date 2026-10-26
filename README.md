# Instructions

In this challenge, you will create your first commit. Happy branching! 🎋

## 🎯 Data and Context

In the previous exercise, you have created a `feature` branch locally, merged it into the `remote master` branch, and updated your `local master` branch.

In larger scale production apps, it's likely that there will be a `develop` branch that collects a number of individual features, then will periodically merge into `master`.

We'll practice this concept here. Once the cycle of development is over, we will then finally merge `develop` into `master`.

Let’s bring this into practice.

## 📁 Setup

To make challenge completion simpler, we have added terminal instructions to challenges that have test suites.

If you haven't already, **copy the terminal instructions at the top of this page and run them in your terminal**.

This will:

- Create and navigate to a directory (folder) for this challenge in your terminal
- Download all of the files for this challenge
- Set up a new repository locally and on GitHub
- Open the challenge in VS Code
- Run the test suite for this challenge

At this point the tests will fail with a lot of red, that is expected: we haven't started working yet. Keep on reading.

Run the following command in the terminal to check you are in the right directory:

```bash
pwd
```

Your result should look like this:

```bash
~/code/<user.github_nickname>/{{ local_path_to("03-Data-Transformation/08-Intro-To-Git-And-Versioning/04-Developing-In-The-Branch") }}/
```

❌ If it doesn't, consult a TA!

✅ If it does, then you are ready to take on this challenge!

### Data and Context

For this challenge we will be using the [🔗gwz_sales](https://console.cloud.google.com/bigquery?project=data-analytics-bootcamp-363212&ws=!1m5!1m4!4m3!1sdata-analytics-bootcamp-363212!2scourse14!3sgwz_sales) table. We'll write some SQL queries in VS Code then push them to a remote repository on GitHub.

Your mission is to write the queries to be able to create a dashboard for the sales manager. You won't save different versions of your work in BigQuery, but use the power of Git to track changes in your SQL files!

## 🧩 Implementation

1. Run the following code in your terminal to add a sqlite copy of this dataset to this repository for testing:

   ```bash
   mkdir -p data
   curl https://wagon-public-datasets.s3.amazonaws.com/sql_databases/gwz_sales.sqlite --output data/gwz_sales.sqlite
   ```

    The downloaded file is 174 MB — too large to push to GitHub. Before you commit anything, check that your `.gitignore` is keeping it out:

   ```bash
   cat .gitignore
   ```

    You should see `*.sqlite` and `data/` in the output. If either is missing, open `.gitignore` in VS Code and add them:

   ```bash
   code .gitignore
   ```

    Then verify the file is being ignored as expected:

   ```bash
   git status
   ```

    `data/gwz_sales.sqlite` should **not** appear in the output. If it does, your `.gitignore` isn't working — fix it before continuing.

    In your git status, you might see that your `.gitignore` is modified. So, let's commit it:

   ```bash
   git add .gitignore
   git commit -m "Initial commit"
   ```

### 1. Daily Turnover

1. In VS Code, create a new file called `gwz_sales.sql`, stage, commit, and push this file to `master`.

1. Write a query to obtain the daily turnover.

    <details>
    <summary markdown="span">💡 Solution</summary>

    ```sql
    SELECT
      date_date
      ,SUM(turnover) AS turnover
    FROM gwz_sales
    GROUP BY date_date
    ```

    </details>
    <br>

1. Test your code locally with `make run_tests`. At this point you should pass 4 tests.

1. Check your git status: you should see the changes to your SQL file, but also some files in the `tests` folder with `.pkl` extension. These files are the results of the tests we just ran to check your code. You will need to commit them so we can see the results on Kitt later.

   ```bash
   git add gwz_sales.sql tests/*.pkl
   git commit -m "Added daily turnover"
   ```

**DON'T push yet.**

### 2. Git Graph

Git is a very powerful tool but it can be hard to use it.

A very good way to avoid getting lost is to use a tool to **visualise all commits and branches for a project**.

We will use the **VS Code extension “Git Graph”** for this bootcamp.

1. Go to the VS Code extension marketplace at [this link](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) and install Git Graph in your VS Code.

1. In VS Code, click on the **source control sign** in the left side bar and download Git if it’s not yet installed. (A link will guide you to the official page to download it).

    ![Screenshot of VS Codes left extension sidebar with Git Graph selected](https://wagon-public-assets.s3.eu-west-3.amazonaws.com/04-Data-Collection/05-Intro-To-Git-And-Versioning/03-Local-Versus-Remote-asset-1-Untitled.png)

1. Relaunch VS Code and open your `gwz_sales` folder and **click on Git Graph** at the bottom of your screen.

    💡 The first part of the status bar at the bottom of the screen gives you the branch name you are using. When you create a new repository tracked by Git, it always shows the default `main / master` branch.

    ![Screenshot of VS Code bottom status bar. The Git Graph logo and the word main are circled](https://wagon-public-assets.s3.eu-west-3.amazonaws.com/04-Data-Collection/05-Intro-To-Git-And-Versioning/03-Local-Versus-Remote-asset-2-Screenshot_2023-09-21_at_15.53.55.png)

## 3. Test Your Knowledge

We now have Git Graph installed, it's time to try it out and test your knowledge (with visuals!)

1. How many commits do you see? Why? Which commit are you on?

1. Based on your understanding, if your computer stops working, do you think you will lose your project?

1. How do you suggest we solve this problem?

1. Go back to the terminal and push your recent commit to your remote repository.

1. Go back to VS Code and look at the git graph. What is different? Can you understand why? Make sure that “Show Remote Branches” is selected.

At this point you should see 4 tests passing on Kitt.

## 4. First Feature Branch

The sales manager has told us he also wants to see the purchase costs. Let’s add it!

1. Go to your terminal and create a new feature branch called `add_purchase_cost`.

1. Go to VS Code and **modify your query to add the purchase cost** (the sum of the `purchase_cost` columns).

1. Run the tests with `make run_tests`. At this point you should pass 5 tests.

1. Save, Stage, and Commit the update. Don't forget the `.pkl` files like before. **DON'T push yet.**

1. Go back to the VS Code Git Graph, how many branches do you see now?
   Why is there no `origin` next to your feature branch `add_purchase_cost`?

   ❗ Make sure you have "Show Remote Branches" selected.

    <details>
    <summary markdown="span">💡 Explanation</summary>

    If we don’t take into account `origin/head`, we have 3 branches here:
    - `master` branch
    - `origin/master`, the remote version of the local main branch - up on github.
    - `add_purchase_cost`
    We don’t see `origin` next to the feature branch because there is no remote branch yet. We still have to push our feature branch to the remote, `origin`.

    </details><br>

1. Go back to your terminal and checkout to  `master`. Now go back to VS Code and have a look at the SQL file. Can you see the line that added the purchase cost? Why is that?

    <details>
    <summary markdown="span">💡 Explanation</summary>

    You can’t see the line because you added it when you were on your feature branch.  We have not made any changes on `master` locally or remotely.

    Take a few minutes to think about it, it’s hard to understand that you have a single file on your computer `gwz_sales.sql` but that its content changes depending on which branch you are on. This is what we call versioning. You have different versions of the same file.

    </details><br>

1. Go to your terminal and change your current branch to `add_purchase_cost`. Push your branch to the remote repository. Check in Git Graph that an `origin` appears next to your `add_purchase_cost`.

1. On github.com, make a Pull Request to integrate your changes from `add_purchase_cost` into `master`. Not sure how to do that? Have a look at the last part of the previous challenge, and follow the same process.

At this point you should see 5 tests passing on Kitt.

## 5. Create Develop Branch and Rounding Results Branch

Our sales manager was very happy with the result of our work, but he’s a bit confused by all the decimals he sees in `turnover` and `purchase_cost`. Can we round that to whole numbers (zero decimals)? That would be great!

From now on we'll work on multiple feature branches and first merge them into a `develop` branch. Once we finished a couple of feature branches like this, and have tested and are happy with the results, we will merge this `develop` branch into `master`. This is a more advanced, and quite common, "git flow".

1. Update your local master to match your remote:

   ```bash
   git checkout master
   git pull origin master
   ```

1. Go to the terminal, create a new branch called `develop` and push it to `origin`.

    <details>
    <summary markdown="span">💡 Quick refresher on creating new branches</summary>

    You can create the branch and navigate to it in one line of code: `git checkout -b develop`

    When it's time to push the branch: `git push origin develop`

    </details><br>

1. Create another branch called `rounding_results`. You can base it on `develop` or `master`, for now the result will be the same because right now both branches correspond to the same code, the last commit.

    <details>
    <summary markdown="span">💡 Hint</summary>

    While still inside the `develop` branch create the `rounding_results` branch and navigate to it: `git checkout -b rounding_results`

    </details>

## 6. Features

### 6.1. Rounding

1. Working on the `rounding_results` branch, modify `gwz_sales.sql` to round the numbers to zero decimals. Save, `make run_tests`, Stage, and Commit the change in the terminal. Don't forget the `.pkl` files! Use `git status` to check which files are changed or new.

1. Push your `rounding_results` branch to `origin`. What does your Git Graph in VS Code show?

1. We now want to merge the `rounding_results` branch into `develop`. Make a pull request and merge it.

    ❗ **Be careful to select the correct base branch for your pull request, it will be at the top of the page! Be sure to merge into `develop`, not into `master`!**

    ![Screenshot of solution](https://wagon-public-assets.s3.eu-west-3.amazonaws.com/04-Data-Collection/05-Intro-To-Git-And-Versioning/06-Working-With-Branches-asset-7-Screenshot_2023-09-21_at_16.46.30.png)

1. Checkout to your `develop` branch in the terminal. Does your local branch `develop` contain the updated code? Why?

1. Run the following command in the terminal to fetch the changes from the remote (but **not** merge them) `git fetch origin develop`.

    Go to Git Graph in VS Code. Where can you find your local branch `develop` compared to the remote branch `develop`? **Why is that?** Discuss it with your buddy. Try and understand this - it is the source of many Git problems.

    `git fetch` fetches the changes from the remote, but doesn't `merge` them into the local branch. `git pull` automatically runs a `merge` after it runs `fetch`. This is useful information to have, but is a little advanced for your first proper day of git so don't panic if you don't understand it just yet! Here is a [useful explanation on Stack Overflow](https://stackoverflow.com/a/292359). For those of you who are VERY interested here is an [indepth blog post about this topic](https://longair.net/blog/2009/04/16/git-fetch-and-merge/).

1. Go to the terminal, make sure you're on the `develop` branch, and run the command `git pull origin develop`. Go back to VS Code Git Graph. You should now see that `develop` and `origin/develop` are at the same level, both showing the rounding code.

1. Delete the `rounding_results` branch locally. Why can you delete it?

   ```bash
   git branch -d rounding_results
   ```

At this point you will still see only 5 tests passing on Kitt, not 6. Can you think why that is?

### 6.2. Sort Dates

Our sales manager just sent us an email saying that while we are working on the rounding, that it would be nice to see the most recent dates first.

1. Create a new branch `sort_dates` based on develop and repeat the steps from the previous section to implement this new feature. This time it is **very important** that you base the new branch on `develop` otherwise it won't have the changes you just made (the rounding).

    <details>
    <summary markdown="span">💡 Hint</summary>

    Make certain you are checked into `develop` and then run the `git checkout -b` command to your new date sorting branch

    Write your code, `make run_tests`, and don't forget to also commit the `.pkl` files.

    At this point you should be passing all tests locally.

    Create a pull request on `develop` and not `master`

    </details>

    You should get a Git Graph like this one in VS Code:

    ![Screenshot of Git Graph with branch lineage and seperate commits](https://wagon-public-assets.s3.eu-west-3.amazonaws.com/04-Data-Collection/05-Intro-To-Git-And-Versioning/06-Working-With-Branches-asset-13-Screenshot_2023-09-21_at_17.01.49.png)

At this point you will still see only 5 tests passing on Kitt, not all tests. Can you think why that is?

## 7. Merging into `master`

1. We merged two feature branches into `develop`. We now want to merge `develop` into `master` to deploy our code into production. Create a pull request. Have a look at all the changes this will make to main. Do you recognise these? When you're happy, merge the pull request from `develop` into `master`.

1. Go to Git Graph in VS Code. Why are your local and remote `develop` branches behind the `master` branches? How can you bring `develop` to the same level as `master` after the merge? Try it out.

After the final merge, your git graph should look similar graph to this one:

![Screenshot of Git Graph with branch lineage and seperate commits](https://wagon-public-assets.s3.eu-west-3.amazonaws.com/04-Data-Collection/05-Intro-To-Git-And-Versioning/06-Working-With-Branches-asset-22-Screenshot_2023-09-21_at_17.19.57.png)

Local and remote branches, main and develop, are at the top. We can iterate the process and launch a new cycle of features development!

At this point you will finally see all tests passing on Kitt. Do you understand why we only see all tests passing now, and not after the previous step?


## 🎯 Finishing up

Congratulations! You have now covered all the basics of Git and Github 🎉

Wherever you work, small or large companies, you will use the same processes.
