SELECT s.id AS student_id, s.name AS student_name, g.grade, g.date
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 2 AND g.subject_id = 1;