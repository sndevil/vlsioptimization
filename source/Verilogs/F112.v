module F112 (VV110V , VV111V , VV112V); 
input VV110V , VV111V;
output VV112V;
xor f0 (VV112V , VV110V , VV111V);
endmodule