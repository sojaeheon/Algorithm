-- 프로그래머스: 년, 월, 성별 별 상품 구매 회원 수 구하기
-- 문제: https://school.programmers.co.kr/learn/courses/30/lessons/131532
-- 난이도: Level 4

SELECT
    YEAR(s.SALES_DATE) AS YEAR,
    MONTH(s.SALES_DATE) AS MONTH,
    u.GENDER,
    COUNT(DISTINCT s.USER_ID) AS USERS
FROM ONLINE_SALE AS s
JOIN USER_INFO AS u ON u.USER_ID = s.USER_ID
WHERE u.GENDER IS NOT NULL
GROUP BY YEAR(s.SALES_DATE), MONTH(s.SALES_DATE), u.GENDER
ORDER BY YEAR ASC, MONTH ASC, u.GENDER ASC;
