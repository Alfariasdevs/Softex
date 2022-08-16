<script>
 function Calculadora(){
  var num1=document.getElementById("num1").value;
  var oper=document.getElementById("oper").value;
  var num2=document.getElementById("num2").value;
  
  if(oper == "somar"){
  	result = parseInt(num1) + parseInt(num2);//parseInt para somar e não concatenar	
 	alert('Resultado da Soma: ' + result);
  }else
  if(oper == "subtrair"){
  	result = parseInt(num1) - parseInt(num2); 
  	alert('Resultado da Subtração: ' + result);
  }else
  if(oper == "multiplicar"){
  	result = parseInt(num1) * parseInt(num2);
  	alert('Resultado da Multiplicação: ' + result);
  }else
  if (oper == "dividir"){
  	result = Math.floor(num1/num2);
  	alert('Resultado da Divisão: ' + result);
  let resto = parseInt(num1) % parseInt(num2);
  	alert('Resto: ' + parseInt(num1) % parseInt(num2));
    }
 }
</script>