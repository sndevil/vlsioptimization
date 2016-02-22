module F29 (VV25V , VV28V , VV29V); 
input VV25V , VV28V;
output VV29V;
xor f0 (VV29V , VV25V , VV28V);
endmodule