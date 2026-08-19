#!/bin/bash
# Install, build, test and lint every migrated project.
cd /home/user/pro-vue
PROJECTS="solutions/lab03 solutions/lab04 solutions/lab05 solutions/lab11 solutions/lab12 solutions/lab13 solutions/lab14 solutions/lab15 solutions/lab16 solutions/lab17 solutions/lab18 solutions/lab19 solutions/lab20 solutions/lab21 solutions/lab22 solutions/lab23 solutions/lab24 labs/lab03/conduit setup-test"
fail=0
for p in $PROJECTS; do
  echo "##### $p"
  ( cd "$p" || exit 1
    npm install --no-audit --no-fund >/tmp/i.log 2>&1 || { echo "  INSTALL FAILED"; tail -20 /tmp/i.log; exit 1; }
    npx vite build >/tmp/b.log 2>&1 && echo "  build OK" || { echo "  BUILD FAILED"; tail -25 /tmp/b.log; exit 1; }
    if grep -q '"test"' package.json; then
      npx vitest run >/tmp/t.log 2>&1 && echo "  tests OK ($(grep -oE 'Tests  [0-9]+ passed' /tmp/t.log | head -1))" || { echo "  TESTS FAILED"; tail -30 /tmp/t.log; exit 1; }
    fi
    npx eslint . >/tmp/l.log 2>&1 && echo "  lint OK" || { echo "  LINT FAILED"; tail -25 /tmp/l.log; exit 1; }
  ) || fail=1
done
echo "=========================="
[ $fail -eq 0 ] && echo "ALL PROJECTS PASSED" || echo "SOME PROJECTS FAILED"
