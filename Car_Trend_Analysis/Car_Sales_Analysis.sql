set autocommit = 0 ;
select database();
USE car_trends_queries;
Show tables;
Describe cleaned_data;

-- Query 1: Most Popular Car Brands
SELECT Brand, COUNT(*) AS Total_Listings
FROM cleaned_data
GROUP BY Brand
ORDER BY Total_Listings DESC
LIMIT 5;

-- Query 2: Average Price By Brand
select Brand , Round(Avg(Price),0) as Average_Price
from cleaned_data
group by Brand
Order By Average_Price DESC;

-- Query 3: Average Price By Fuel Type
select Fuel , Round(Avg(Price),0) as Average_Price
from cleaned_data
group by Fuel
Order By Average_Price DESC;

commit;
-- Query 4: New vs Old Distribution
SELECT `Condition`, COUNT(*) AS Count
FROM cleaned_data
GROUP BY `Condition`;

-- top 5 MOST COMMON REGISTERED CITIES
select `Registered City` , Count(*) as Total_Listings
from cleaned_data
Group by `Registered City`
Order by Total_Listings DESC
limit 5;


-- AVERAGE PRICE BY CITY
SELECT `Registered City`, ROUND(AVG(Price), 0) AS Avg_Price
FROM cleaned_data
GROUP BY `Registered City`
ORDER BY Avg_Price DESC
LIMIT 10;

-- AVERAGE PRICE OVER THE YEARS
select Year, Round(Avg(Price),1) as Avg_Price
from cleaned_data
group by year
order By year;

-- TOP 10 BEST CARS 
select Brand, Model , Count(*) as Count from cleaned_data
Group by Brand , Model
Order By Count DESC
limit 10;

-- Relation of KM to Price
select case
when `KMs Driven` < 20000 then '0 - 20K'
when `KMs Driven` between 20000 and 50000 then '20k - 50k'
when `KMs Driven` between 50001 and 100000 then '50k - 100k'
else '100k+'
end as Mileage_Range,
Round (Avg(Price),0) as Avg_Price,
Count(*) as Cars_Count
from cleaned_data
group by Mileage_Range
Order by Avg_Price DESC;
-- TRANSACTION TYPE BREAKDOWN
select `Transaction Type` , Count(*) as Count from cleaned_data
group by `Transaction Type`
Order by Count DESC;
