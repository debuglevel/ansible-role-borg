#!/bin/sh

echo "Running borgmatic with docker-compose..." 1>&2
# NOTE: "borgmatic" is the container name
docker-compose --file /root/borgmatic/docker-compose.yml run --rm borgmatic "$@"
rc=$?
echo "Ran borgmatic with docker-compose; exit code: $rc" 1>&2
exit $rc
