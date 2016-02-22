module F128 (b , c , VV128V); 
input b , c;
output VV128V;
xor f0 (VV128V , b , c);
endmodule