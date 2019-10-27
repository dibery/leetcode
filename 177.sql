CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare a int;
  set a = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select (
        select Salary
        from Employee
        group by Salary desc
        limit 1 offset a
      )
  );
END
