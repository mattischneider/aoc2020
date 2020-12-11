with i as (
select unnest(array[1, 2, 3, 6, 7, 8, 9, 10, 13, 16, 17, 18, 21, 22, 25, 28, 29, 30, 33, 34, 35, 36, 37, 40, 43, 44, 45, 46, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 63, 66, 67, 68, 69, 72, 75, 78, 79, 80, 81, 82, 85, 88, 91, 94, 95, 96, 97, 98, 101, 102, 103, 104, 105, 108, 109, 110, 111, 112, 115, 118, 119, 122, 123, 124, 125, 126, 129, 132, 133, 134, 135, 138, 139, 140, 141, 144, 147, 148, 149, 150, 153, 156, 157, 158, 159, 160, 163, 166, 167, 168, 169, 172, 173, 174, 177, 178, 179, 180]) as voltages), 

get_diffs as (
select 
	voltages, 
	voltages - lag(voltages) over(order by voltages asc) as diff
from i
order by 1),

number_of_diffs as (
select
	diff,
	count(*) + 1 as count_diffs -- + + 1 because 0 -> 1 and 180 -> 183 will result in an extra voltage difference for each of the 1-jolt and 3-jolt difference
from get_diffs
where diff is not null
group by 1),

first_part as (
select foo1.count_diffs * foo3.count_diffs
from (select * from number_of_diffs where diff = 1) as foo1
	cross join (select * from number_of_diffs where diff = 3) as foo3
)

select * from first_part;

