# Пример простого serverless API

## Что используется:
- AWS Services: Lambda, DynamoDB, API-Gateway (REST API, HTTP API)
- Serverless framework
- Terraform (для описания таблиц DynamoDB)   

## Зачем:
Простой пример реализации serverless API с использованием сервисов AWS. Может быть использован для
- обучения.
- знакомства с сервисами AWS.
- тестового стенда или основы нового проекта.


## Описание проекта:
API включает следующие простые функции:
- создание пользователя.
- получения пользователя по id.
- создание комментария определенного пользователя.

Структура проекта:
- `applications` - папка с основной логикой, разделенной по доменам.
- `services` - папка для сервисов или утилит.
- `terraform` - папка с темплэйтами terraform.
- файл `serverless` - файл, содержащий описание инфраструктуры проекта.

В проекте продемонстрировано использование как  API Gateway REST API (создание и получение пользователя) 
так и  API Gateway HTTP API(создание комментария). Обе технологии используется в связке с Lambda functions. 
DynamoDB используется в качестве БД, соответственно.

## Необходимо:
Достаточно сделать один раз (~15 минут), потом можно штамповать облачные проекты хоть каждый день)
- [Создать аккаунт AWS](https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start)
- По best-practices рутовый акк рекомендуется удалять и создавать админский ([как это сделать](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html))
- [Установить aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [Установить Serverless Framework](https://serverless.com/framework/docs/getting-started/)
- [Настроить Serverless Framework](https://serverless.com/framework/docs/providers/aws/cli-reference/config-credentials/)

## Как этим всем пользоваться:
#### - Установка зависимостей
1. После того как настроили интерпритатор для проекта, устанавливаем зависимости.   
2. Не забываем про `npm i` нужен для установки serverless framework.

#### - Деплоим основной стэк:
Переходим в корень проекта и запускаем команду: `./deploy.sh <your_stage> <aws_profile>`    
`aws_profile` указывался при конфигурации aws-cli, если что можно посмотреть в файле `.aws/creds`   
`your_stage` наименование окружения(dev, stage, prod)

#### - Пора посмотреть что получилось:
При деплое serverless framework показал какие lambda функции у нас есть и эндпоинты на которые можно покидать запрос.   

Для примера создадим нового пользователя:
```curl
curl --request POST \
  --url <берем из консоли, например:  https://<индетификатор API>.execute-api.us-east-1.amazonaws.com/dev/users> \
  --header 'content-type: application/json' \
  --data '{"username": "test", "email": "test@mail.ru"}'
```
В ответ придет id пользователя, удостоверимся, что он успешно сохранился в базе:
```
curl --request GET \
  --url <берем из консоли после деплоя>
```
