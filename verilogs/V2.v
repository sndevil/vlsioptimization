module V2 (a , b , V1 , V2); 
input a , b , V1;
output V2;
wire W10;

or f0 (W10 , a , b);
and f1 (V2 , W10 , V1);
endmodule