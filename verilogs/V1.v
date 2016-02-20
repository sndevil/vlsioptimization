module V1 (b , c , V1); 
input b , c;
output V1;
wire W00;

not f0 (W00 , b);
xor f1 (V1 , c , W00);
endmodule