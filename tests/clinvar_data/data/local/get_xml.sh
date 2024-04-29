#!/usr/bin/bash

set -euo pipefail

FNAME=ClinVarVCVRelease_2024-0407.xml

if [[ ! -e /tmp/$FNAME ]]; then
    wget -O /tmp/$FNAME.gz \
        https://ftp.ncbi.nlm.nih.gov/pub/clinvar/xml/weekly_release/$FNAME.gz
    pigz -cd /tmp/$FNAME.gz /tmp/$FNAME.tmp
    mv /tmp/$FNAME.tmp /tmp/$FNAME
fi
