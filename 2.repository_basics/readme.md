# hey fys! 👋 welcome to git gud

now that you know the difference between git and github (if not, check out the git_fundamentals readme first), let's get into the actual guide and learn how to use them!

---

## 1. local vs. remote repositories

a **local repository** is the version of your project on your computer.
a **remote repository** is a version hosted online, usually on github.

they don't automatically stay in sync. when you upload your commits, you *push* them. when you bring changes from the remote repository into your local one, you can *pull* them.

think of local as your workspace and remote as the online copy you can share with others.

---

## 2. fork vs. clone

found a cool project on github and want to work with it? that's where forking and cloning come in.

- **fork:** creates your own copy of someone else's repository on github.
- **clone:** downloads a repository onto your computer.

### how to fork

1. open a repository on github.
2. click **fork**.
3. choose your account if prompted, then create the fork.

### how to clone

1. open the repository on github.
2. click **code**, select **HTTPS**, and copy the URL.
3. run this command in your terminal, replacing the example URL with the actual one:

```bash
git clone https://github.com/username/first-project.git
```

then enter the downloaded folder:

```bash
cd first-project
```

### fork vs. clone: what's the difference?

| | fork | clone |
|---|---|---|
| **where?** | github | your computer |
| **what does it do?** | creates your own online copy | downloads a repository locally |

you can fork **and** clone: fork a project on github, then clone your fork onto your computer.

**remember:** cloning someone's repository doesn't automatically give you permission to push changes to it.

---

## 3. `git init`

got a project folder you want git to track? open a terminal inside it and run:

```bash
git init
```

git creates a hidden `.git` directory to store the information it needs to track your project.

**remember:** this creates a local repository. it doesn't create a github repository or upload anything.

### try it out

1. create a folder called `git-gud-practice`.
2. open a terminal inside it.
3. run `git init`.

that's it! your folder is now a git repository.

---

## 4. `git status`: your git detective

forgot what you've changed? run:

```bash
git status
```

it shows you which files are new, which have been modified, and which changes are staged.

### try it out

inside your repository, create a file called `hello.cpp`:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "hello, git gud!";
    return 0;
}
```

save it, then run:

```bash
git status
```

your file should appear as **untracked**. git can see it, but you haven't staged it yet.

**pro tip:** when you're confused about what's happening in git, start with `git status`.

---

## 5. staging and `git add`

before changes can be included in a commit, you need to **stage** them. think of staging as selecting which changes you want to include in your next snapshot.

to stage one file:

```bash
git add hello.cpp
```

to stage multiple files:

```bash
git add hello.cpp README.md
```

to stage eligible changes under the current directory:

```bash
git add .
```

check what happened:

```bash
git status
```

your file should now appear under **changes to be committed**.

### try it out

1. run `git status` and find `hello.cpp`.
2. run `git add hello.cpp`.
3. run `git status` again and notice what's changed!

**remember:** staging doesn't create a commit. it just prepares your selected changes for one.

---

## useful resources

- [git documentation](https://git-scm.com/doc)
- [github repository docs](https://docs.github.com/en/repositories)

you don't need to memorize everything today. keep experimenting, and don't hesitate to ask your seniors for help if you're stuck.

**happy coding, fys! 💜**
