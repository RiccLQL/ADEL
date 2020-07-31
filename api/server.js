const express = require('express');
const tf = require('@tensorflow/tfjs');
//const multer = require('multer');
const Canvas = require('canvas');
const cors = require('cors');
const bodyparser = require('body-parser');
const Busboy = require('busboy');
const path = require('path');
const fs = require('fs');

const app = express();
const model = tf.loadLayersModel('../model/model.json');

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


//const upload = multer({ dest: './temp'});

//busboy

app.post('/process/img', (req, res) => {

    var busboy = new Busboy({ headers: req.headers });
    busboy.on('file', function(fieldname, file, filename, encoding, mimetype) {

      var saveTo = path.join(__dirname, 'temp/' + filename);
      file.pipe(fs.createWriteStream(saveTo));
    });

    busboy.on('finish', function() {
        fs.readFile(`./temp/DJI_0641.JPG`, (err, data) => {
            if (err) throw err;
            const img = new Canvas.Image();
            img.src = data;
            console.log(img);

            var canvas = Canvas.createCanvas(img.width, img.height);
            var ctx = canvas.getContext('2d');

            const imgdata = ctx.getImageData(0, 0, img.width, img.height);

            const tfimg = tf.browser.fromPixels(imgdata);
            console.log(tfimg);
            const number = model.predict(tfimg);
            console.log(number);

            res.send(number);
        })

        res.writeHead(200, { 'Connection': 'close' });
        res.end("That's all folks!");
    });

    return req.pipe(busboy);  

    /*console.log(req.body)
    const rawimg = new Image;
    rawimg.src = "./temp/uploads/"
    const img = tf.browser.fromPixels(ImageData());
    console.log(img);
    const number = model.predict(img);
    console.log(number);

    res.send(number);*/
})

const port = 8000;
app.listen(port, 'localhost', () => {console.log(`Listening at http://localhost:${port}`)});