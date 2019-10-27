select a.Id
from Weather a
where a.Temperature >
    (select Temperature
     from Weather
     where RecordDate = subdate(a.RecordDate, 1));
