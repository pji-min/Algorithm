-- 코드를 작성해주세요
SELECT C.ID
FROM ECOLI_DATA A
JOIN ECOLI_DATA B ON B.PARENT_ID = A.ID
JOIN ECOLI_DATA C ON C.PARENT_ID = B.ID
WHERE A.PARENT_ID IS NULL
ORDER BY C.ID;