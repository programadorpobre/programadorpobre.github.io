#!/bin/bash

echo "./scripts/travis_push.sh started"

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

git checkout master

git add _includes/feed-entries.html
git commit --message "[travis] #$TRAVIS_BUILD_NUMBER"

git remote add github-origin https://${GITHUB_TOKEN}@github.com/programadorpobre/programadorpobre.github.io
git push -u github-origin master

echo "./scripts/travis_push.sh finished"
