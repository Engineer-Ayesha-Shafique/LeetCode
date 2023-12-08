# Write your MySQL query statement below
WITH RankedSalaries AS (
    SELECT
        e.id AS EmployeeId,
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS SalaryRank
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)

SELECT
    Department,
    Employee,
    Salary
FROM RankedSalaries
WHERE SalaryRank <= 3;
