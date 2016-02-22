module F7 (VV3V , VV6V , VV7V); 
input VV3V , VV6V;
output VV7V;
xor f0 (VV7V , VV3V , VV6V);
endmodule