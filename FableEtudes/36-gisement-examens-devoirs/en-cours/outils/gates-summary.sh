#!/bin/bash
SP=/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad
F=$SP/gates-$1.txt
head -3 $F | cut -c1-200
sed -n '/content:tranche --fresh (cliquets CI)/,/bilan/p' $F | cut -c1-220 | head -16
sed -n '/bilan content:gates/,$p' $F | cut -c1-160
