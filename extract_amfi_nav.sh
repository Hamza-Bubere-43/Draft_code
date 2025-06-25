#!/bin/bash

# Download NAVAll.txt
curl -s "https://www.amfiindia.com/spages/NAVAll.txt" -o nav_data.txt

# Extract Scheme Name and Asset Value (assumed columns: 4 and 5)
# Skips header lines and empty lines
awk -F';' 'NF > 5 && $1 ~ /^[0-9]+$/ { print $4 "\t" $5 }' nav_data.txt > scheme_asset.tsv

# Convert to JSON format
awk -F';' 'NF > 5 && $1 ~ /^[0-9]+$/ { print "{\"scheme_name\":\"" $4 "\", \"asset_value\":\"" $5 "\"}," }' nav_data.txt > data.json


echo "Extraction complete: scheme_asset.tsv"
