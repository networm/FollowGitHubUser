#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from github import Github


# usage
def usage():
    print 'Follow GitHub user\'s starred, watching and following.'
    print
    print 'Usage: python follow.py <token> <user>'
    print
    print 'token: Go to https://github.com/settings/tokens and `Generate new token` with scope `public_repo`.'
    print
    print 'user: GitHub user ID you want to follow.'


# args
if len(sys.argv) != 3:
    usage()
    exit(1)

# variable
me = Github(sys.argv[1])

namedUser = Github().get_user(sys.argv[2])

# action
for starred in namedUser.get_starred().reversed:
    me.get_user().add_to_starred(starred)

for subscription in namedUser.get_subscriptions().reversed:
    me.get_user().add_to_subscriptions(subscription)

for watched in namedUser.get_watched().reversed:
    me.get_user().add_to_watched(watched)

for following in namedUser.get_following().reversed:
    me.get_user().add_to_following(following)
