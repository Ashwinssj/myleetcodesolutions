select w.id from Weather w
join weather pre
on datediff(w.recordDate,pre.recordDate)=1
where w.temperature > pre.temperature 