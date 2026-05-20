# CS391-2026-Summer
For teaching CS391X1: Modern Compiler Design and Implementation in Python

## Mirroring this repository

Please create a private repository that mirrors this one and update
frequently.

Step 1:

Please clone the class repository:

```
git clone https://github.com/hwxi/CS391-2026-Summer
```

Step 2:

Please create a repository of your own.
For instance, the following one is created
for my own use:

https://github.com/githwxi/CS391-2026-Summer-hwxi

Then please mirror-push the class repo into your own repo:

```
cd CS391-2026-Summer
git push --mirror https://github.com/githwxi/CS391-2026-Summer-hwxi
git clone https://github.com/githwxi/CS391-2026-Summer-hwxi
cd CS391-2026-Summer-hwxi
git remote add upstream https://hwxi@github.com/hwxi/CS391-2026-Summer.git
```

Step 3:

Please remember to sync with the class repo *frequently*:

```
git fetch upstream
git merge upstream/main main
```
