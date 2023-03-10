select owner_id,owner_name,count(categoty_id)
from owner join article join category_article_mapping 
where article_id=category_articel_mapping.article_id AND ORDER BY category_id
