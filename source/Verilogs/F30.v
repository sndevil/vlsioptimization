module F30 (VV22V , VV29V , VV30V); 
input VV22V , VV29V;
output VV30V;
xor f0 (VV30V , VV22V , VV29V);
endmodule