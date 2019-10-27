select (
    select Salary
    from Employee
    group by Salary desc
    limit 1 offset 1
) as SecondHighestSalary
