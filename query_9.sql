SELECT s.id AS student_id, s.name AS student_name, sub.name AS subject_name
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id;