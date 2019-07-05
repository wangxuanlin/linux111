// var fun = function (n, a) {
//     if (n > 0){
//         console.log('1');
//     } else {
//         console.log('2');
//     }
//     a = a + n;
//     n = n - 1 ;
//     return fun(n,a);
//
//
// };
//
// console.log(fun(100,0));

var a = 5;
var b = 5;
if (a>b){
    console.log('a>b');
} else if (a===b) {
    console.log('a=b');
}else{
    console.log('a < b')
}
var age = 30;
switch (age) {
    case 18:{
        console.log('水蜜桃');
    }break;
    case 20:{
        console.log('西瓜');
    }break;
    case 30:{
        console.log('菠萝');
    }break;
    default :{console.log('异常')}

};

var s = 1;
do{
    s +=1
}while (s<100);

console.log(('s is'+s));




for(var i=1; i<=9; i++){
    var chart='';
    for (var c =1; c<=i; c++){
        chart += (c+'*'+i+"="+(c*i)+'\t')
    }
    console.log(chart);
}


for (var i =1; i<+9; i++){
    var  chart ='';
    chart=''
    for (var j=0; j<=(2*i-1)+1; j++){
       chart  += '*';
    }
    console.log(chart)

};