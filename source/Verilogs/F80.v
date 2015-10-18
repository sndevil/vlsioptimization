module F80 (b , e , VV80V); 
input b , e;
output VV80V;
xor f0 (VV80V , b , e);
endmodule