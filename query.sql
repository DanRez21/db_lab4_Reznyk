--1. Вивести середню оцінку вин для кожного дегустатора
SELECT taster_name, AVG(e.points) AS average_evaluation
FROM wine w
JOIN evaluation e ON w.eva_id = e.eva_id
JOIN taster ta ON ta.taster_id = e.taster_id
GROUP BY taster_name;

--2.Вивести розподіл вин за місцем вирощування
SELECT country, COUNT(*) AS wine_count
FROM wine w
JOIN location_ l ON w.wine_id = l.wine_id
GROUP BY country;

--3.Вивести залежність між рейтингами вин і різними параметрами
SELECT AVG(e.points) AS average_evaluation, l.country 
FROM wine w
JOIN evaluation e ON w.eva_id = e.eva_id
JOIN taster ta ON ta.taster_id = e.taster_id
JOIN location_ l ON l.wine_id = w.wine_id
GROUP BY l.country;