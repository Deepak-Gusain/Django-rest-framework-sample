#!/bin/bash
-e
gunicorn --bind=0.0.0.0 --timeout 6000 --workers=2 --threads=4 FileExtraction.wsgi:application