var tempo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Dados obtidos pelo medidor de temperatura 
var temperatura = [37, 38, 38, 39, 40, 38, 39, 38, 39, 38, 37];

// Dados obtidos pelo oximetro
var oximetria = [81, 80, 82, 83, 81, 84, 85, 83, 82, 84, 82];

// Gráfico temperatura x tempo
var b1 = JXG.JSXGraph.initBoard('box1', {boundingbox: [-2, 50, 12, -8], axis: true, showCopyright:false, showNavigation:true});
b1.create('curve', [tempo,temperatura],{strokeColor:'black',strokeWidth:2});

// Gráfico oximetria x tempo
var b2 = JXG.JSXGraph.initBoard('box2', {boundingbox: [-2, 90, 12, -12], axis: true, showCopyright:false, showNavigation:true});
b2.create('curve', [tempo,oximetria],{strokeColor:'red',strokeWidth:2});