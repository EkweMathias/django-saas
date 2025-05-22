#!/bin/ash

echo "Applying data migration"
python3 manage.py migrate

# docker run my-image /bin/bash -c "echo hello"
# The exec "$@" replaces the entrypoint script with /bin/bash -c "echo hello", ensuring:
# The shell process becomes the command (/bin/bash), not a parent of it.

exec "$@"