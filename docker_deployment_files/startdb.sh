#!/bin/bash
docker-compose up -d
sleep 45
docker exec mongo1 /scripts/rs-init.sh