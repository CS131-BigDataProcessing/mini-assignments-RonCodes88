The shellscript provides commands to process the AB_NYC_2019.csv dataset, containing Airbnb listings. 
Prerequisites:
  - Ensure bash is installed
  - Ensure awk is installed
  - Ensure sort is installed
How to Use Commands:
  - sh a8_preprocess_airbnb.sh
      - Running this script will run all of the following commands listed
  - awk -F'\t' 'NF < 16 { print "Line", NR ":", $0 }' AB_NYC_2019.csv
      - Identify rows with fewer than 16 fields (missing values)
  - awk -F, '$1 != "" { print $0 }' AB_NYC_2019.csv
      - Identify rows where the first column is not empty
  - sort -t $'\t' -k1 AB_NYC_2019.csv | uniq > unique_AB_NYC_2019.csv
      - Sort and keep unique rows by the first column, then store them in a .csv file
  - cut -d$'\t' -f14 AB_NYC_2019.csv > field_values.txt
    mode_value=$(sort field_values.txt | grep -v "^$" | uniq -c | sort -nr | head -n 1 | awk '{ print $2 }')
    awk -F '\t' -v mode="$mode_value" '{ if ($14 == "") $14 = mode; print $0 }' OFS='\t' AB_NYC_2019.csv > Airbnb_inputted.csv
      - Replace null values in reviews_per_month column with the mode and store the result in a .csv file
