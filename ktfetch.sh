for p in $(python3 -c "import json; print(' '.join(json.load(open('kt_pagelist.json'))))"); do
  [ -s kt/$p.json ] && continue
  curl -s -m 30 -A "voynich-comparison-study (academic, cached locally)" "https://rechnitzer-kodex.hu/api/GetPage/$p" -o kt/$p.json
  head -c 2 kt/$p.json | grep -q '\[' || { rm -f kt/$p.json; sleep 10; }
  sleep 1.5
done
echo done > kt/.done
