#!/bin/bash
docker-compose up -d
sleep 10
docker exec -it mongo mongosh --eval 'db.orders.createIndex({"name": 1}, {unique: true});'
docker exec -it mongo mongosh --eval 'db.orders.insertOne({name: "pizza", status: "ready"});'
docker exec -it mongo mongosh --eval 'db.orders.insertOne({name: "hamburger", status: "being_prepared"});'
docker exec -it mongo mongosh --eval 'db.orders.insertOne({name: "pasta", status: "being_cooked"});'
docker exec -it mongo mongosh --eval 'db.orders.insertOne({name: "grilled_meat", status: "burnt"});'
docker exec -it mongo mongosh --eval 'db.orders.insertOne({name: "test", status: "unknown"});'

