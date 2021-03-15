var variavel1 = document.getElementById("variavel1");
var x = firebaseRef = firebase.database().ref().child("Sensor/Canal-1");

x.on('value',function(datasnapshot){
    variavel1.innerText = datasnapshot.val();
})

var variavel2 = document.getElementById("variavel2");
var x = firebaseRef = firebase.database().ref().child("Sensor/Canal-2");

x.on('value',function(datasnapshot){
    variavel2.innerText = datasnapshot.val();
})

var variavel3 = document.getElementById("variavel3");
var x = firebaseRef = firebase.database().ref().child("Sensor/Canal-3");

x.on('value',function(datasnapshot){
    variavel3.innerText = datasnapshot.val();
})