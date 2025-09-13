select 
    student_id,
    subject,
    min(case when rn_asc = 1 then score end) as first_score,
    min(case when rn_desc = 1 then score end) as latest_score
from (
    select 
        student_id,
        subject,
        score,
        exam_date,
        row_number() over (partition by student_id, subject order by exam_date asc) as rn_asc,
        row_number() over (partition by student_id, subject order by exam_date desc) as rn_desc
    from Scores
) x
group by student_id, subject
having count(*) >= 2  -- at least 2 exams in the subject
   and min(case when rn_desc = 1 then score end) > min(case when rn_asc = 1 then score end)
order by student_id, subject;