# FollowGitHubUser
Follow GitHub user's starred, watching and following.

## Prerequisite
This tool used https://github.com/PyGithub/PyGithub library.
So you need install it first by `easy_install PyGithub` or `pip install PyGithub`. If you encounter errors, add `sudo` and retry.

## Usage
`python follow.py <token> <user>`

token: Go to https://github.com/settings/tokens and `Generate new token` with scope `public_repo`.

user: GitHub user ID you want to follow.

## Link
There is also another similar tool to do this. It didn't use a GitHub API wrapper library. It just use normal pycurl to do this manually.

https://github.com/ningyu/poorness-githubhelper
