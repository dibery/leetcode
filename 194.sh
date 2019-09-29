line=`head -1 file.txt | awk '{print NF}'`
for i in `seq $line`
do
    tr ' ' \\n < file.txt | sed -n "$i~${line}H;\${x;s/\n/ /g;s/ //p}"
done
#tr ' ' \\n < file.txt | pr -ts\  --columns `wc -l < file.txt`
