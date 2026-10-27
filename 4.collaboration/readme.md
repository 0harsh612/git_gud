## Hey FYs! 👋

Thanks for coming to the workshop! Working on code with other people feels scary at first, but don't worry, we're here to help! 
Keep this page open while you practise. Merging, pull requests and conflicts feel normal after a few tries, and a conflict is just Git asking you a question.

## 1. Pulling and Merging

`git pull` fetches the latest changes from the remote repository and merges them into your local branch, which keeps your copy up to date.

Other people merge into `main` too, so always pull their work before you merge yours:

```
git checkout main
git pull origin main
git merge <branch_name>
git push origin main
```

(`git switch main` does the same as `git checkout main` in newer Git.)

If Git can merge cleanly, it creates the merge commit by itself. You only need `git add .` and `git commit` when you had to fix a conflict first. In team repositories you will usually merge through a pull request instead (see section 3).

```
git merge --abort            # stop a merge that went wrong
git branch -d <branch_name>  # delete the branch after merging
```

📖 [Pro Git: Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)


## 2. Collaborators and Contributors

- **Collaborator:** someone the owner or an admin has given direct access to the repository. They can push changes and create branches without forking.
- **Contributor:** anyone who adds to a project. Usually they have no special access, so they fork the repository and send a pull request.

**What if I clone without forking?** You can clone any public repository, run it and pull updates. When you try to push, GitHub refuses because you do not have write access. Your changes stay on your laptop until you push them to your own fork. Fork first, or ask the owner to add you as a collaborator.

**What if I don't clone at all?** You can edit a file on GitHub's website. If you are not a collaborator, GitHub offers to make a fork for you and lets you open a PR from it. This works well for typo fixes.

**To add a collaborator:** open the repository, go to Settings, click Collaborators under Access, choose Add people and search for their username. They get an email and receive access once they accept.

**Becoming a contributor:** start small, like fixing a typo or improving documentation, then take bigger issues as you gain confidence. Look for issues tagged "good first issue" or "help wanted", or visit `github.com/<owner>/<repo>/contribute`.

📖 [About forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)


## 3. Pull Requests (PRs)

A pull request is a proposal to merge changes from one branch into another, and teammates can review and discuss it before it is merged. It is a GitHub feature, not a Git command.

**Why use one:**
1. **Notify:** tell the team a feature is ready.
2. **Discuss:** teammates comment, suggest edits and debate the best approach.
3. **Follow-up commits:** keep pushing improvements to the same branch, and the PR updates until it is ready to merge.

**Team project flow (you are a collaborator):**
1. Create the feature in a separate branch on your computer.
2. Push the branch: `git push origin <branch_name>`
3. Open a pull request on GitHub (use the Compare & pull request button).
4. Teammates review the code and give feedback.
5. After approval, the maintainer merges it into `main`.
6. The PR is closed. Delete the branch and run `git pull` on `main`.

**Open source flow (you are not a collaborator):**
1. Fork the repository to your own GitHub account.
2. Clone your fork to your computer.
3. Create a new branch and make your changes.
4. Push the branch to your fork.
5. Open a PR from your fork's branch to the original repository's branch (usually `main`).
6. Once approved, the maintainer of the original repository merges it.

**Structure of a PR:** a title and a description. Check that the base branch (where the changes go) and the compare branch (your work) are correct.

- Title: `Fix login button not responding on mobile`
- Description: what you changed, why, and how to test it.

**Best practices:** keep PRs small and focused, write titles that say exactly what the PR does, break large changes into several PRs, and avoid force pushing once someone has started reviewing.

**Checks on a PR (CI/CD):** many repositories run automatic tests on every PR. If a check fails, fix the code and push another commit, and the checks run again. GitHub Actions is the built-in tool for this. It automates build, test and deployment, and a workflow can start when something happens in the repository, such as a push or a pull request. Workflow files live in `.github/workflows/`.

**Why PRs matter beyond class:** Google Summer of Code is a mentoring program where new contributors work on real open source projects. Organisations usually like to see a small, clean PR from you before you apply. (Hacktoberfest 2026 no longer counts PRs. It focuses on community events about open source AI.)

📖 [GitHub Docs: About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
📖 [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)
📖 [Workshop demo repo for GitHub workflows](https://github.com/shnavii11/github-workflow-demo)
📖 [Google Summer of Code](https://summerofcode.withgoogle.com/) | [Hacktoberfest](https://hacktoberfest.com)


## 4. Merge Conflicts

Git cannot always combine two branches by itself. This happens when:
1. Two people edit the same line.
2. One person deletes a file while another edits it.
3. The branches have drifted far apart.

**What it looks like in the file:**
```
<<<<<<< HEAD
your version of the line
=======
their version of the line
>>>>>>> feature-login
```
Everything between `<<<<<<<` and `=======` is your current branch. Everything between `=======` and `>>>>>>>` is the incoming branch.

**How to fix it on your computer:**
1. Run `git status` to see which files are in conflict.
2. Open each file and decide: keep yours, keep theirs, or combine both.
3. Delete the three marker lines.
4. Save, then run `git add <file>` and `git commit`.

**In VS Code:** click Accept Current Change, Accept Incoming Change, Accept Both Changes or Compare Changes above the conflict.

**On GitHub:** a PR with a conflict shows "This branch has conflicts that must be resolved" and a Resolve conflicts button. This works only for simple competing line changes. If the button is greyed out, use the command line.

**If you panic:** `git merge --abort` takes you back to before the merge.

**How to avoid them:** pull often, keep branches short-lived, and tell teammates which files you are editing.

📖 [Resolving a merge conflict using the command line](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line)
📖 [Resolving a merge conflict on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github)


## 5. Git Rebase

Rebasing means moving the base of your branch to a new starting point. Think of it as a redo: "I meant to start here."

Merging joins the end points of two branches, while rebasing replays your commits one by one on top of another line of work.

```
git checkout feature-login
git rebase main
```

**When to use it:**
- To keep a **linear history** and avoid the diamond shape that merge commits create, which makes the project history easier to follow.
- To update your feature branch with the latest changes from `main`.

If a conflict appears, fix it, run `git add <file>`, then `git rebase --continue`. To cancel, run `git rebase --abort`.

**Golden rule:** do not rebase commits that already exist outside your own repository and that other people may have based work on. If you rebase a branch you already pushed, you must force push it, so do this only on your own branches.

📖 [Pro Git: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)

---

## 6. Undoing Changes

| Situation | Command |
|---|---|
| Unstage a file | `git restore --staged file.py` |
| Throw away edits to a file (cannot be undone) | `git restore file.py` |
| Fix the last commit message (not pushed yet) | `git commit --amend` |
| Undo last commit, keep changes staged | `git reset --soft HEAD~1` |
| Undo last commit, keep changes unstaged | `git reset HEAD~1` |
| Undo last commit and delete the changes | `git reset --hard HEAD~1` ⚠️ |
| Undo a commit that is already pushed | `git revert <commit-hash>` |
| Find a lost commit | `git reflog` |

**Reset vs revert:** `reset` moves the branch back and rewrites history, so use it only on local commits. `revert` adds a new commit that cancels an old one, so it is safe on shared branches.

📖 [Pro Git: Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things)

## Quick Cheat Sheet

```
git checkout -b new-branch
git push -u origin new-branch
git pull origin main
git merge branch-name
git merge --abort
git rebase main
git status
git log --oneline --graph
```

## Practise and Learn More

- 🎮 [Learn Git Branching](https://learngitbranching.js.org): visual, in-browser practice
- 🎓 [GitHub Skills](https://skills.github.com): short hands-on courses