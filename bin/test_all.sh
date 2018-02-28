#!/bin/bash

cd `dirname $0`
for file in `\find *_test.sh -maxdepth 1 -type f`; do
  sh $file
done