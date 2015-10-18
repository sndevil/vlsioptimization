module F75 (b , c , VV75V); 
input b , c;
output VV75V;
xor f0 (VV75V , b , c);
endmodule