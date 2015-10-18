module F160 (c , a , VV160V); 
input c , a;
output VV160V;
xor f0 (VV160V , c , a);
endmodule