SELECT
    DISTINCT p.PRODUCT_CODE,
    p.PRICE * SUM(o.SALES_AMOUNT) SALES
FROM
    PRODUCT p 
    INNER JOIN
    OFFLINE_SALE o
    ON
    p.PRODUCT_ID = o.PRODUCT_ID
GROUP BY
    p.PRODUCT_ID
ORDER BY
    SALES DESC,
    p.PRODUCT_CODE