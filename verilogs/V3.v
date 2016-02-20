module V3 (a , V2 , V3); 
input a , V2;
output V3;
wire W20;

not f0 (W20 , a);
and f1 (V3 , V2 , W20);
endmodule