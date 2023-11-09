SELECT machine_id,
       ROUND(SUM(end_time - start_time) / COUNT(DISTINCT process_id), 3) as processing_time
FROM (
    SELECT machine_id,
           process_id,
           MAX(CASE WHEN activity_type = 'start' THEN timestamp END) as start_time,
           MAX(CASE WHEN activity_type = 'end' THEN timestamp END) as end_time
    FROM Activity
    GROUP BY machine_id, process_id
) AS process_times
GROUP BY machine_id;
