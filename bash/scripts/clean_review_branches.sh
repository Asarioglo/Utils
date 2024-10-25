#!/bin/bash
git branch --list 'review*' | xargs -r git branch -D
