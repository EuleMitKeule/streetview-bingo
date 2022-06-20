#!/usr/bin/env bash
service nginx start
uwsgi --ini config/uwsgi.ini --enable-threads