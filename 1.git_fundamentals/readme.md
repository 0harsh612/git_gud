# hey fys! 👋 welcome to git gud

welcome to git, where you can break your code, track exactly what you broke, and occasionally blame your past self for it.
ever wondered how developers work on the same project without sending 84 versions of `final_final_REAL_final.cpp` on whatsapp? let's find out.

**no prior git experience needed. just bring your laptop and your curiosity.**

---

## 1. git vs. github

they're not the same thing!

- **git** tracks changes in your code and lets you revisit older versions.
- **github** is a website where you can store repositories online and collaborate with others.

think of git as your save system and github as your online hub.

### what's a repository?

a repository (or *repo*) is a project that git tracks. your website, C++ assignment, or random python script can all have their own repositories.
a repository can live on your laptop, on github, or in both places.

---

## 2. local vs. remote repositories

**local repository:** the version of your project on your computer.
**remote repository:** the version hosted online, usually on github.

they don't automatically sync. when you upload your commits, you *push* them. when you bring changes from the remote repository into your local one, you can *pull* them.
think of local as your workspace and remote as the online copy you can share with others.

---

## 3. fork vs. clone

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

## 4. `git init`

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

## 5. `git status`: your git detective

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

## 6. `git add`: the VIP list

before changes can be included in a commit, you need to **stage** them. think of staging as choosing what goes into your next snapshot.

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
3. run `git status` again. notice what's changed!

---

## 7. `git commit`: save your progress

staging changes doesn't save a snapshot in your repository. for that, you need a **commit**.
think of it like saving a checkpoint in a game. if you make more changes later, you can still look back at earlier commits.

run:

```bash
git commit -m "add hello.cpp"
```

the `-m` lets you add a short message describing what the commit contains.

### try it out

after staging `hello.cpp` with `git add`, run the commit command above.

then check:

```bash
git status
```

if everything is committed, you should see that your working tree is clean.

### remember the difference

| command | what it does |
|---|---|
| editing a file | changes your working copy |
| `git add` | stages selected changes |
| `git commit` | saves a snapshot locally |
| `git push` | uploads commits to a remote repository |

---

## 8. quick cheat sheet

| command/action | what it does |
|---|---|
| `git init` | initializes a local repository |
| `git status` | shows the state of your repository |
| `git add <file>` | stages changes to a file |
| `git add .` | stages eligible changes under the current directory |
| `git commit -m "message"` | saves a snapshot with a message |
| `git clone <url>` | downloads a repository to your computer |
| **fork button on github** | creates your own online copy |
| `git push` | uploads commits to a remote repository |
| `git pull` | brings remote changes into your local repository |
| `cd <folder>` | moves into a folder in the terminal |

---

## 9. useful resources

- [git documentation](https://git-scm.com/doc)
- [github repository docs](https://docs.github.com/en/repositories)

---

every developer has googled a git command at some point. you don't need to memorize everything today. keep experimenting, ask for help when you're stuck, and you'll get the hang of it.

**happy coding, fys! 💜**
