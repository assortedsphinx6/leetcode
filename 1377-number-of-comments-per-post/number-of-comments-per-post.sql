# Write your MySQL query statement below

SELECT p.post_id, count(distinct c.sub_id) as number_of_comments from (SELECT distinct sub_id as post_id from Submissions where parent_id is null) p
left join submissions c on p.post_id = c.parent_id
group by p.post_id
order by p.post_id