# Пример простого full-serverless API

## Что используется:
- AWS Services: Lambda, DynamoDB, API-Gateway (REST API, HTTP API)
- Serverless framework
- Terraform (для описания таблиц DynamoDB)   

## Зачем:
Простой пример реализации full-serverless API с использованием сервисов AWS. Может быть использован для
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
- [Установить Terrraform: https](//www.terraform.io/downloads.html)

## Как этим всем пользоваться:
#### - Установка зависимостей
1. После того как настроили интерпритатор для проекта, устанавливаем зависимости.   
2. Не забываем про `npm i` нужен для установки serverless framework.

#### - Для начала развернем базу
База разворачивается при помощи Terraform. Но сначала нужно настроить aws провайдер одним из следующих способов:   
1. Прописать креды в темплэйт (уровень безопасности: qwerty123):  
    Переходим в папку `terraform`, открываем  tables.tf и прописываем наши ключи в объявление провайдера (если надо заменить и регион):
    ```hcl-terraform
    provider "aws" {
      region     = "my-region"
      access_key = "my-access-key"
      secret_key = "my-secret-key"
    }
    ```
2. Креды в Environment variables:
данные берем из фала "home directory/.aws/creds"
    ```
    export AWS_ACCESS_KEY_ID="access key"
    export AWS_SECRET_ACCESS_KEY="secret key"
    export AWS_DEFAULT_REGION="region"
    ```   
3. Указание на файл с кредами:   
 Переходим в папку `terraform`, открываем  tables.tf и прописываем путь до ключей.
    ```hcl-terraform
    provider "aws" {
      region                  = "regions"
      shared_credentials_file = "home directory/.aws/creds"
      profile                 = "customprofile"
    }
    ```

Создаем workspace: `terraform workspace new <workspace_name>` (для примера dev)
Переключаемся на него: `terraform workspace select <workspace_name>`

Долгожданный запуск: `terraform apply`

#### - Деплоим основной стэк:
Переходим в корень проекта и запускаем команду: `./deploy.sh <your_stage> <aws_profile>`
`aws_profile` указывался при конфигурации aws-cli, если что можно посмотреть в файле `.aws/creds`
`your_stage` **должен совпадать с именем terraform workspace**

#### - Пора посмотреть что получилось:
При деплое serverless framework показал какие lambda функции у нас есть и эндпоинты на которые можно покидать запрос.   

Для примера создадим нового пользователя:
```curl
curl --request POST \
  --url <берем из консоли после деплоя>/<stage указанный при деплое>/users \
  --header 'content-type: application/json' \
  --data '{
	"username": "test",
	"email": "test@mail.ru"
}
'
```
В ответ придет id пользователя, удостоверимся, что он успешно сохранился в базе:
```
curl --request GET \
  --url <берем из консоли после деплоя>/<stage указанный при деплое>/users/<user_id>
```
