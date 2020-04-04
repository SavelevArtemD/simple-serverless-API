#!/bin/bash

stage=$1
awsProfile=$2
export STAGE=$stage
sls deploy --stage "$stage" --aws-profile "$awsProfile"