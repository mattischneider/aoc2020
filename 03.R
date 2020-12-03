dat <- read.csv("03.txt", header = FALSE) 

is_tree_or_not_tree <- function(line_number, steps_right, steps_down) {
  line_content <- dat$V1[1 + (line_number-1)*steps_down]
  #print(line_content)
  n <- ((line_number-1) * steps_right) %% nchar(line_content) + 1
  current_position <- substr(line_content, n, n)
  return(current_position == '#')
}

get_sum_of_trees <- function(steps_right, steps_down) {
  sum(sapply(1:nrow(dat), function(i) { is_tree_or_not_tree(line_number = i, steps_right = steps_right, steps_down = steps_down) }), na.rm = TRUE)
}

# first part
get_sum_of_trees(steps_right = 3, steps_down = 1)

# second part
slopes <- matrix(nrow = 5, ncol = 2, data = c(1,1,3,1,5,1,7,1,1,2), byrow = TRUE)
prod(sapply(1:nrow(slopes), function(i) { get_sum_of_trees(steps_right = slopes[i,1], steps_down = slopes[i,2]) }))