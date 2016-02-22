module F110 (c , e , VV110V); 
input c , e;
output VV110V;
xor f0 (VV110V , c , e);
endmodule