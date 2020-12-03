#!/bin/bash
FILE="01.txt"
IFS=$'\r\n' GLOBIGNORE='*' command eval 'entries=($(cat $FILE))' # https://stackoverflow.com/questions/11393817/read-lines-from-a-file-into-a-bash-array
number_of_entries="${#entries[@]}" # https://www.cyberciti.biz/faq/finding-bash-shell-array-length-elements/
TARGET_NUMBER=2020

for i in "${!entries[@]}"; do # https://stackoverflow.com/questions/6723426/looping-over-arrays-printing-both-index-and-value
    for j in "${entries[@]:$i+1}"; do # https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Parameter-Expansion
        ADD_THEM=$(expr ${entries[$i]} + $j)
        if [ $ADD_THEM -eq $TARGET_NUMBER ]
        then
            echo "TARGET NUMBER FOUND! YAY!"
            echo "num1: " ${entries[$i]}
            echo "num2: " $j
            echo "num1 * num2:" $(expr ${entries[$i]} \* $j)
            exit
        fi
    done
done
