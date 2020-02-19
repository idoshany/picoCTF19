#!/usr/bin/python3
for i in {1..256}
do
	printf "\\$(printf "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n%03o" $i)"
done

