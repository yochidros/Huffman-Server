var fs = require('fs');
var firebase = require('firebase');

config = {
   apiKey: "AIzaSyAFZxSiZIATrWimOTen-6KMElp8_Kz9vic",
   authDomain: "huffmancode-f137e.firebaseapp.com",
   databaseURL: "https://huffmancode-f137e.firebaseio.com",
   projectId: "huffmancode-f137e",
   storageBucket: "",
   messagingSenderId: "294641754899"
};
firebase.initializeApp(config);
var gcloud = require('gcloud')({ ... });
vat gcs = gcloud.storage();
var bucket = gcs.bucket('');
/*

var storage = firebase.storage();

var storageRef = storage.ref();

var imagesRef = storageRef.child('images/graph.png');

var imageFile = fs.readFile('./graph.png', 'utf8', function (err, text) {
  console.log('read file');
  console.log(text);
});
*/

