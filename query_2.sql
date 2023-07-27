SELECT s.id, s.name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 1
GROUP BY s.id, s.name
ORDER BY avg_grade DESC
LIMIT 1;
