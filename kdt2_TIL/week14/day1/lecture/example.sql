-- Article.objects.all().query

SELECT 
  "articles_article"."id", 
  "articles_article"."title", 
  "articles_article"."content", 
  "articles_article"."created_at", 
  "articles_article"."updated_at" 
FROM 
  "articles_article"


-- Article.objects.filter(pk=1).query

SELECT 
  "articles_article"."id", 
  "articles_article"."title", 
  "articles_article"."content", 
  "articles_article"."created_at", 
  "articles_article"."updated_at" 
FROM 
  "articles_article" 
WHERE 
  "articles_article"."id" = 1