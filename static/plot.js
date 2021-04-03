//////////////////// CONFIGURAÇÃO DO FIREBASE //////////////////////
var firebaseConfig = {
    apiKey: "AIzaSyCX_eRxj6mFZlOP0YQYMkhM9N9eeBw358Q",
    authDomain: "ultimo-b2b4c.firebaseapp.com",
    databaseURL: "https://ultimo-b2b4c-default-rtdb.firebaseio.com/",
    projectId: "ultimo-b2b4c",
    storageBucket: "ultimo-b2b4c.appspot.com",
    messagingSenderId: "422778348983",
    appId: "1:422778348983:web:9b5ba28990f67b2df23432"
};
firebase.initializeApp(firebaseConfig);
/////////////////////////////////////////////////////////////////////

var variavel1 = document.getElementById("variavel1");
var temperatura = firebase.database().ref().child("Sensor/Canal-1");

/* Função de geração de númericos pseudo-aleatórios */
function getData() {
    return Math.random();
}

/* Recebe do firebase os dados do sensor de temperatura */
var temp;
function getTemperatura(){
    temperatura.on('value', function(datasnapshot) { 
        var arru1 = datasnapshot.val();
        variavel1.innerText = datasnapshot.val();
        arru1 = Number(arru1);
        temp = arru1;    
    });
    return temp;
}

/* Cria o gráfico de temperatura */
Plotly.newPlot('temperatura',[{
    y:[getData()],
    type:'line'
}]);

/* Função de atualização do gráfico de temperatura. Aciona o getTemperatura a cada intervalo de tempo pré-definido */
setInterval(function(){
    count=0;
    Plotly.extendTraces('temperatura',{ y:[[getData()]]}, [0]);
    count++;
    if(count > 1500) {
        Plotly.relayout('temperatura',{
            xaxis: {
                range: [count-1500
        ,count]
            }
        });
    }
},15);

var variavel2 = document.getElementById("variavel2");
var oximetria = firebase.database().ref().child("Sensor/Canal-2");

/* Recebe os dados do sensor de oximetria */
var oxi;
function getOximetria(){
    oximetria.on('value', function(datasnapshot) { 
        var arru2 = datasnapshot.val();
        variavel2.innerText = datasnapshot.val();
        arru2 = Number(arru2);
        oxi = arru2;    
    });
    return oxi;
}

/* Cria o gráfico de oximetria */
Plotly.newPlot('oximetria',[{
    y:[getData()],
    type:'line'
}]);

/* Função de atualização do gráfico de oximetria. Aciona o getOximetria a cada intervalo de tempo pré-definido */
setInterval(function(){
    count=0;
    Plotly.extendTraces('oximetria',{ y:[[getData()]]}, [0]);
    count++;
    if(count > 1500) {
        Plotly.relayout('oximetria',{
            xaxis: {
                range: [count-1500
        ,count]
            }
        });
    }
},15);

var variavel3 = document.getElementById("variavel3");
var pressao = firebase.database().ref().child("Sensor/Canal-3");

/* Recebe os dados do sensor de pressão */
var press;
function getPressao(){
    pressao.on('value', function(datasnapshot) { 
        var arru3 = datasnapshot.val();
        variavel3.innerText = datasnapshot.val();
        arru3 = Number(arru3);
        press = arru3;    
    });
    return press;
}

/* Cria o gráfico com as medições de pressão */
Plotly.newPlot('pressao',[{
    y:[getPressao()],
    type:'line'
}]);

/* Função de atualização do gráfico de pressão. Aciona o getPressao a cada intervalo de tempo pré-definido */
setInterval(function(){
    count=0;
    Plotly.extendTraces('pressao',{ y:[[getPressao()]]}, [0]);
    count++;
    if(count > 1500) {
        Plotly.relayout('pressao',{
            xaxis: {
                range: [count-1500
        ,count]
            }
        });
    }
},15);