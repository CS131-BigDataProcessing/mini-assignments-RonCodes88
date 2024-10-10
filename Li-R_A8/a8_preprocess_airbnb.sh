#!/bin/bash

echo "Identifying missing values: printing lines with less than 16 fields"
awk -F'\t' 'NF < 16 { print "Line", NR ":", $0 }' AB_NYC_2019.csv


echo "Rows where the first column is not empty"
awk -F, '$1 != "" { print $0 }' AB_NYC_2019.csv


echo "Sorting and keeping unique rows by the first column:"
sort -t $'\t' -k1 AB_NYC_2019.csv | uniq > unique_AB_NYC_2019.csv
echo "Unique records saved to unique_AB_NYC_2019.csv"

echo "Replacing reviews_per_month null values with mode"
cut -d$'\t' -f14 AB_NYC_2019.csv > field_values.txt
mode_value=$(sort field_values.txt | grep -v "^$" | uniq -c | sort -nr | head -n 1 | awk '{ print $2 }')
awk -F '\t' -v mode="$mode_value" '{ if ($14 == "") $14 = mode; print $0 }' OFS='\t' AB_NYC_2019.csv > Airbnb_inputted.csv
echo "Result outputted to Airbnb_input.csv file"
