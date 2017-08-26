#!/bin/bash

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

git add _includes/feed-entries.html
git commit --message "[travis] #$TRAVIS_BUILD_NUMBER"

git remote add github https://${GITHUB_TOKEN}@github.com/MVSE-outreach/resources.git > /dev/null 2>&1
git push --quiet --set-upstream github master > /dev/null 2>&1

