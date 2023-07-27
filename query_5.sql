SELECT s.name AS subject_name, t.name AS teacher_name
FROM subjects s
JOIN teachers t ON s.teacher_id = t.id
WHERE t.id = 2;
