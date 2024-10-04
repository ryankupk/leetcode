-- https://leetcode.com/problems/second-highest-salary

-- Write your PostgreSQL query statement below
-- select 
-- case when count(*) = 1 then null else salary end as SecondHighestSalary from Employee
-- where salary != (select max(salary) from Employee)

-- group by salary
-- order by salary desc
-- limit 1

SELECT 
  NULLIF(
    (SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     OFFSET 1
     LIMIT 1), 
  (SELECT max(salary) 
   FROM Employee
   )) AS SecondHighestSalary;

