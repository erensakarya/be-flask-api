docker exec -it mongo1 mongosh
rs.status()


# INSERT
db.orders.insertOne({name: "pizza", status: "ready"});
db.orders.insertOne({name: "hamburger", status: "being_prepared"});
db.orders.insertOne({name: "pasta", status: "being_cooked"});
db.orders.insertOne({name: "grilled_meat", status: "burnt"});
db.orders.insertOne({name: "test", status: "unknown"});


# SELECT
db.orders.find()
db.orders.find({name: "pizza"})
db.orders.find({name: {$in: ["pizza", "grilled_meat"]}})
db.orders.find({name: "pizza", $or: "status": "ready"})
db.orders.find({
     name: "pizza",
     $or: [{"status": "ready"}]
})


# UPDATE
db.orders.updateOne({name: "pizza"},
{
  $set: {
    name: "iskender"
  }
})

db.orders.updateOne({name: "pizza"},
{
  $set: {
    status: "burnt"
  }
})


# DELETE
db.orders.deleteOne({name: "pizza"})
db.orders.deleteMany({});


# CLEAR
cls