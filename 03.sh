# part 1
cat 03.txt | awk 'BEGIN { steps_right = 3; steps_down = 1; line_number = 0; }
{
    if (line_number % steps_down == 0) {
        split($1,chars,"")
        current_position = (line_number * steps_right) % length($1) + 1
        if (chars[current_position]  == "#")
        {
            trees_found += 1
        }
    }
    line_number += 1
}  
END {print trees_found}'

# part 2
cat 03.txt | awk 'BEGIN { 
    slopes["0,0"] = 1
    slopes["0,1"] = 1
    slopes["1,0"] = 3
    slopes["1,1"] = 1
    slopes["2,0"] = 5
    slopes["2,1"] = 1
    slopes["3,0"] = 7
    slopes["3,1"] = 1
    slopes["4,0"] = 1
    slopes["4,1"] = 2
    line_number = 0
}
{

    for (i = 0; i <= 4; ++i) {
        steps_right = slopes[i",0"]
        steps_down = slopes[i",1"]
        if (line_number % steps_down == 0) {
            split($1,chars,"")
            current_position = (line_number * steps_right) % length($1) + 1
            if (chars[current_position]  == "#")
            {
                trees_found[i] += 1
            }
        }
    }
    line_number += 1
}  
END {
    trees_found_prod = 1
    for (i = 0; i <= 4; ++i) { 
        trees_found_prod *= trees_found[i]
    }
    print trees_found_prod
}'