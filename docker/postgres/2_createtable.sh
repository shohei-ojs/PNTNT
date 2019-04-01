#!/bin/bash
psql -U postgres -d pntnt_db < "/docker-entrypoint-initdb.d/createtable.sql"