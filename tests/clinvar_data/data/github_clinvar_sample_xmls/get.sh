#!/usr/bin/bash

set -euo pipefail

FNAMES="
rcv_01.xml
rcv_04-1.xml
rcv_04-2.xml
rcv_07-1.xml
rcv_07-2.xml
rcv_08-1.xml
rcv_08-2.xml
rcv_09-1.xml
rcv_09-2.xml
vcv_01.xml
vcv_04.xml
vcv_07.xml
vcv_08.xml
vcv_09.xml
"

for fname in $FNAMES; do
    rm -f $fname
    wget -O $fname \
        https://raw.githubusercontent.com/ncbi/clinvar/master/sample_xmls/$fname
done
