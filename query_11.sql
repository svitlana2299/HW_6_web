SELECT t.name AS teacher_name, st.name AS student_name, AVG(g.grade) AS avg_grade
FROM teachers t
JOIN subjects s ON t.id = s.teacher_id
JOIN grades g ON s.id = g.subject_id
JOIN students st ON g.student_id = st.id
WHERE t.id = 2 AND st.id = 2;
