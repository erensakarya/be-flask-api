#!/bin/bash

mongosh <<EOF
var config = {
    "_id": "dbrs",
    "version": 1,
    "members": [
        {
            "_id": 1,
            "host": "mongo1:27017",
            "priority": 3
        },
        {
            "_id": 2,
            "host": "mongo2:27017",
            "priority": 2
        },
        {
            "_id": 3,
            "host": "mongo3:27017",
            "priority": 1
        }
    ]
};
rs.initiate(config, {force: true});
rs.status();
db.orders.createIndex({"name": 1}, {unique: true});
db.orders.insertOne({name: "pizza", status: "ready"});
db.orders.insertOne({name: "hamburger", status: "being_prepared"});
db.orders.insertOne({name: "pasta", status: "being_cooked"});
db.orders.insertOne({name: "grilled_meat", status: "burnt"});
db.orders.insertOne({name: "test", status: "unknown"});
EOF
