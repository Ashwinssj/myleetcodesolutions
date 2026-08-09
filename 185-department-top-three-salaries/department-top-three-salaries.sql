select d.name as Department, e.name as Employee, e.salary as Salary
from (select name, salary, departmentId,
dense_rank() over (partition by departmentId order by salary desc) as ranking
from Employee) as e
join department d
on e.departmentId=d.id
where e.ranking<=3
