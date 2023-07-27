SELECT st.id AS student_id, st.name AS student_name, g.grade, g.date
FROM students st
JOIN grades g ON st.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE st.group_id = 1 AND g.subject_id = 2
AND g.date = (SELECT MAX(date) FROM grades WHERE student_id = st.id AND subject_id = 2)
ORDER BY g.date DESC;

