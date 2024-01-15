-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherWithMaxAssignments AS (
    SELECT
        teacher_id,
        COUNT(*) AS total_assignments
    FROM
        assignments
    GROUP BY
        teacher_id
    ORDER BY
        total_assignments DESC
    LIMIT 1
)

SELECT
    COUNT(*) AS grade_a_count
FROM
    TeacherWithMaxAssignments tma
JOIN
    assignments a ON tma.teacher_id = a.teacher_id
WHERE
    a.grade = 'A'
GROUP BY
    tma.teacher_id, tma.total_assignments;
