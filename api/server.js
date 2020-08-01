const express = require("express");
const cors = require("cors");
const bodyparser = require("body-parser");

const app = express();

//any middleware
app.use(cors());
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.use(bodyparser.json());
app.use(
  bodyparser.urlencoded({
    extended: true,
  })
);
app.use(express.json());
app.use(
  express.urlencoded({
    extended: true,
  })
);

app.get("/", (req, res) => {
  res.sendFile('C:/Ricky/Drone/ADEL API/ADEL/api/model/drone_detection.h5')
});

const port = 8000;
app.listen(port, "localhost", () => {
  console.log(`Listening at http://localhost:${port}`);
});