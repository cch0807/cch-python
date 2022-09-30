#!/bin/bash
dt=$(date +'%Y%m%d_%s')

git add .
res= git status

$res


# if [ "${res}"==*"modified:"* ]; then
#     echo 'warning'
# else
#     echo 'fiald'
# fi

echo 'Enter the commit message'
read commit_message

git commit -m $commit_message


git push origin mac
git status

echo success upload
