./type_counter.sh 200 syn > temp.syn
cat temp.syn | tr -d " \t\ \r" | tr '-' ',' > total_syn_counts.txt
rm temp.syn

./type_counter.sh 200 hypo > temp.hyp
cat temp.hyp | tr -d " \t\ \r" | tr '-' ',' > total_hypo_counts.txt
rm temp.hyp

./type_counter.sh 200 hyper > temp.hyper
cat temp.hyper | tr -d " \t\ \r" | tr '-' ',' > total_hyper_counts.txt 
rm temp.hyper

./type_counter.sh 200 holo > temp.holo
cat temp.holo | tr -d " \t\ \r" | tr '-' ',' > total_holo_counts.txt 
rm temp.holo

./type_counter.sh 200 mero > temp.mero
cat temp.mero | tr -d " \t\ \r" | tr '-' ',' > total_mero_counts.txt 
rm temp.mero

./total_counter.sh 200 > temp.total
cat temp.total  | tr -d " \t\ \r" | tr '-' ',' > total_counts.txt
rm temp.total