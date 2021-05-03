printf "Content-Type: text/plain\r\n\r\n"
i=0
while [ $i != 17 ]
do
	read line
	echo $line
	i=$((i+1))
done

