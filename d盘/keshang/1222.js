var a = 10;
var b = 'hello world';
a = null;// none
a = undefined
alert(b);
console.log(a)
document.write('aaabbxxx')
var  a = '全局变量';
function print() {
    console.log(a);

}
var  islog = true;
islog ? console.log('执行') : console.log('不执行')
var  a = 5 + (5 * 2)
alert(a)
var func = function () {
    var a = 100;


};
var hano =  function (n, a, b, c) {
  if (n === 1){
      console.log('from' + a+'to'+ c);
  } else {
      console.log(hano(n-1,a,c,b))
      console.log(hano())
  }

};