# 简介

该项目是使用django和celery结合的学习案例

有意见欢迎提出，共同进步~

# 命令

**开启worker** 
> celery -A django_celery_demo worker -l info

**开启beat**
> celery beat -A django_celery_demo -l info

**开启flower**
> celery flower --broker=redis://localhost:6379/0
