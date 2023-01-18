#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHINCREASE=$(echo $DATA | jq '.[0].deathIncrease')
POSINCREASE=$(echo $DATA | jq '.[0].positiveIncrease')

echo "On $TODAY, there were $NEGATIVE negative covid cases, and a death increase of $DEATHINCREASE, with a positive increase of $POSINCREASE."
