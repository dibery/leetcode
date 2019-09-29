tr ' ' \\n < words.txt | grep -v ^$ | sort | uniq -c | sort -nk1r | awk '{print $2, $1}'
