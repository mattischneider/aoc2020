#!/bin/bash
FILE="01.txt"
IFS=$'\r\n' GLOBIGNORE='*' command eval 'entries=($(cat $FILE))' # https://stackoverflow.com/questions/11393817/read-lines-from-a-file-into-a-bash-array
unset IFS
number_of_entries="${#entries[@]}" # https://www.cyberciti.biz/faq/finding-bash-shell-array-length-elements/
TARGET_NUMBER=2020

IFS=$'\n' sorted_entries=($(sort -n <<<"${entries[*]}")) # https://stackoverflow.com/questions/7442417/how-to-sort-an-array-in-bash
unset IFS
echo ${sorted_entries[*]}

for i in "${!sorted_entries[@]}"; do # https://stackoverflow.com/questions/6723426/looping-over-arrays-printing-both-index-and-value
    echo $i
    for j in "${sorted_entries[@]:$i+1}"; do # https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Parameter-Expansion
        TMP=$(expr ${sorted_entries[$i]} + $j)
        if [ $TMP -gt $TARGET_NUMBER ]
        then
            continue
        fi
        for k in "${sorted_entries[@]:$i+1}"; do
            ADD_THEM=$(expr ${sorted_entries[$i]} + $j + $k)
            if [ $ADD_THEM -gt $TARGET_NUMBER ] 
            then
                continue
            fi
            if [ $ADD_THEM -eq $TARGET_NUMBER ]
            then
                echo "TARGET NUMBER FOUND! YAY!"
                echo "num1: " ${sorted_entries[$i]}
                echo "num2: " $j
                echo "num3: " $k
                echo "num1 * num2 * num3:" $(expr ${sorted_entries[$i]} \* $j \* $k)
                exit
            fi
        done
    done
done