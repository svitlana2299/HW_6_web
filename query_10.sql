SELECT s.name AS subject_name, t.name AS teacher_name
FROM students st
JOIN grades g ON st.id = g.student_id
JOIN subjects s ON g.subject_id = s.id
JOIN teachers t ON s.teacher_id = t.id
WHERE st.id = 1 AND t.id = 1;
