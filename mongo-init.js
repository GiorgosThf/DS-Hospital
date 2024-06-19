db = connect("mongodb://localhost:27017/DigitalHospital");

db.createCollection("admin");
db.createCollection("doctors");
db.createCollection("patients");
db.createCollection("appointments");


db.admin.insertMany(
    [
        {username: "admin", password: "@dm1n"}
    ]
)
