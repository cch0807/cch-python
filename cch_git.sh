#!/bin/bash
dt=$(date +'%Y%m%d_%s')

git add .
git commit -m $dt
git push origin mac

echo success upload
