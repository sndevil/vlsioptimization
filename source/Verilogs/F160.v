module F160 (b , e , VV160V); 
input b , e;
output VV160V;
xor f0 (VV160V , b , e);
endmodule