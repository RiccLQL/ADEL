const express = require('express');
import * as tf from '@tensorflow/tfjs';
import { add } from '@tensorflow/tfjs';
const cors = require('cors');
const bodyparser = require('body-parser');

const upload = multer({ dest: './temp'});
const app = express();
const model = await tf.loadLayersModel('./beep/model.json');

//any middleware
app.use(cors());
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
})

app.use(bodyparser.json());
app.use(bodyparser.urlencoded({
    extended: true
}))
app.use(express.json());
app.use(
    express.urlencoded({
        extended: true
    })
)

app.post('/process/img', upload.single('temp'), (req, res) => {
    const img = tf.FromPixels(req.file);
    console.log(img);
    const number = model.predict(img);
    console.log(number);

    res.send(number);
})

const port = 8000;
app.listen(port, () => {console.log(`Listening at http://localhost:${port}`)});