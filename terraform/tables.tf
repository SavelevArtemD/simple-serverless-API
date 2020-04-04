provider "aws" {
  region = "us-east-1"
}

resource "aws_dynamodb_table" "users-table" {
  hash_key = "id"
  read_capacity = 1
  write_capacity = 1
  stream_enabled = false
  name = "${terraform.workspace}-users"
  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_dynamodb_table" "comments-table" {
  hash_key = "user_id"
  range_key = "created_datetime"
  read_capacity = 1
  write_capacity = 1
  stream_enabled = false
  name = "${terraform.workspace}-comments"
  attribute {
    name = "user_id"
    type = "S"
  }
  attribute {
    name = "created_datetime"
    type = "N"
  }
}