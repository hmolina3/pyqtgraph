/*Ejemplo basico para emitir en formato JSON por el puerto serial, 
  en este ejemplo a fin de practica se lee el puerto analogo 0 y 
  se incorpora este valor como
  x: analogo0, y: 40, z: 30 
  los valores y e z son fijos solo para representar la salida pero
  pueden ser otros valores de puertos analogos realizando las lecturas
  previas y asignandole un valor a cada variable*/

double anterior;
double actual;
double dato;
double dif;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  anterior = analogRead(A0);
  delay(1);
}

void loop() {
  // put your main code here, to run repeatedly:
  actual = analogRead(A0);
  dif = abs(actual - anterior);

  if(dif >= 0.05){
    dato = mapf(anterior, 0,1023.0,0.0,255.0);
    //Serial.print(" AJ ");
    anterior=analogRead(A0);
  }else{
  dato = mapf(actual, 0,1023.0,0.0,255.0);
  anterior = actual;
  //Serial.print(" OK ");
  }
  //Serial.println(dato);
  Serial.print("{\"x\": ");
  Serial.print(dato);
  Serial.print(", ");
  Serial.print("\"y\": ");
  Serial.print(40);
  Serial.print(", ");
  Serial.print("\"z\": ");
  Serial.print(30);
  Serial.print("}\n");
  delay(1);
  
}

/*Funcion map pero con flotantes*/
float mapf(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
/*#########################FIN DE MAPF########################*/
