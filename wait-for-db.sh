#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until nc -z "$host" 5432; do
  echo "Waiting for PostgreSQL at $host:5432..."
  sleep 3
done

>&2 echo "PostgreSQL is up - executing command"
exec $cmd
