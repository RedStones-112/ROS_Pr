select *, (select * from celeb where name like ("%이%")) from celeb;
