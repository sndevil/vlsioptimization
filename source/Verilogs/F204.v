module F204 (VV172V , VV203V , VV204V); 
input VV172V , VV203V;
output VV204V;
xor f0 (VV204V , VV172V , VV203V);
endmodule